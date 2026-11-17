"""Convert documents to cached Markdown so agents read text, not binary files.

Agents waste tokens when they open PDFs, Word files, slides, or spreadsheets
directly, or when they reread the same paper in every session. This script turns
those files into compact Markdown once, stores the result under the ignored
`outputs/markdown-cache/` folder, and keeps an index with an approximate token
count for each file. Later runs skip files whose bytes have not changed.

Usage (run with the project virtual environment's Python):

    python -I scripts/to_markdown.py downloads docs/proposal   # convert folders
    python -I scripts/to_markdown.py --overview .              # map a folder, no conversion
    python -I scripts/to_markdown.py --stdout file.docx        # print one file, no cache

PDF text comes from pdfminer, split into pages with `<!-- page N -->` markers
so notes can cite pages. MarkItDown's own PDF converter can turn two-column
prose into padded fake tables, so it is used for PDFs only with
`--pdf-engine markitdown`. All other formats use MarkItDown.

Only local files are read. Nothing is sent over the network. The overview mode
and the helper functions use only the standard library, so the tests run
without MarkItDown installed.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "outputs" / "markdown-cache"
INDEX_JSON = "index.json"
INDEX_MD = "INDEX.md"
INDEX_VERSION = 3  # bump when converted output changes, so old caches are rebuilt

# Formats worth converting. CSV, JSON, and XML are left out on purpose: they
# are already text, and a Markdown table version is usually longer.
CONVERT_EXTS = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".html", ".htm",
    ".ipynb", ".epub", ".msg",
}
TEXT_EXTS = {
    ".md", ".txt", ".py", ".json", ".csv", ".tsv", ".yml", ".yaml", ".toml",
    ".cfg", ".ini", ".xml", ".tex", ".bib", ".rst", ".sh", ".ps1", ".js",
    ".ts", ".css", ".gitignore", ".gitattributes", ".editorconfig",
}
SKIP_DIRS = {
    ".git", ".zcode", ".gstack", ".venv", "venv", "node_modules", "__pycache__",
    ".pytest_cache", ".ruff_cache", ".ipynb_checkpoints", "outputs",
}
CHARS_PER_TOKEN = 4  # rough rule of thumb for English text


def approx_tokens(text):
    """Rough token count: about 4 ASCII characters per token.

    Other scripts, such as Bangla, use far more tokens per character, so each
    non-ASCII character counts as one token. This is an estimate, not a tokenizer.
    """
    other = sum(1 for char in text if ord(char) > 127)
    return (len(text) - other + CHARS_PER_TOKEN - 1) // CHARS_PER_TOKEN + other


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def compact_markdown(text):
    """Remove token waste without changing words, numbers, or symbols."""
    lines = []
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = line.rstrip()
        stripped = line.lstrip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if re.fullmatch(r"\|(?:\s*:?-+:?\s*\|)+", stripped):
                cells = stripped.strip("|").split("|")
                line = "|" + "|".join(" --- " for _ in cells) + "|"
            else:
                line = re.sub(r" {2,}", " ", stripped)
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


LIGATURES = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"})


def clean_pdf_page(text):
    """Fix PDF text quirks that break searching.

    Ligatures such as the single "ﬀ" character make `grep differential` miss
    "diﬀerential". Rotated margin text (the arXiv stamp) comes out as one
    character per line, often with blank lines between. Runs of six or more such
    lines are joined into one line with spaces, so a column of numbers never
    merges into a different number. Shorter runs are left exactly as they were.
    """
    lines = text.translate(LIGATURES).split("\n")
    result, raw, short = [], [], []
    for line in lines + [None]:
        stripped = "" if line is None else line.strip()
        if line is not None and len(stripped) <= 2 and (stripped or short):
            raw.append(line)
            if stripped:
                short.append(stripped)
            continue
        if len(short) >= 6:
            result.append(" ".join(short))
            if raw and not raw[-1].strip():
                result.append("")
        else:
            result.extend(raw)
        raw, short = [], []
        if line is not None:
            result.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(result))


def pages_to_markdown(pages):
    """Join page texts with page markers that survive later grep searches."""
    parts = []
    for number, page in enumerate(pages, start=1):
        parts.append(f"<!-- page {number} -->\n\n{clean_pdf_page(page).strip()}\n")
    return "\n".join(parts)


def pdf_pages_pdfminer(path):
    import logging

    from pdfminer.high_level import extract_text

    logging.getLogger("pdfminer").setLevel(logging.ERROR)
    text = extract_text(str(path))
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return pages


def markitdown_convert(path):
    from markitdown import MarkItDown

    result = MarkItDown(enable_plugins=False).convert_local(str(path))
    return result.text_content or ""


def convert_one(path, pdf_engine="pdfminer", converters=None):
    """Return (markdown, engine, page_count) for one local file."""
    converters = converters or {}
    pdf_pages = converters.get("pdf_pages", pdf_pages_pdfminer)
    generic = converters.get("generic", markitdown_convert)
    if path.suffix.lower() == ".pdf" and pdf_engine == "pdfminer":
        pages = pdf_pages(path)
        return compact_markdown(pages_to_markdown(pages)), "pdfminer", len(pages)
    return compact_markdown(generic(path)), "markitdown", None


def display_path(path, root):
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def cache_name(source, root):
    """Mirror the source path under the cache, keeping the extension."""
    try:
        relative = source.resolve().relative_to(root)
        return Path(*relative.parts[:-1], relative.name + ".md")
    except ValueError:
        tag = hashlib.sha256(str(source.resolve()).encode()).hexdigest()[:8]
        return Path("_external", f"{tag}-{source.name}.md")


def walk_files(paths):
    for start in paths:
        start = Path(start)
        if start.is_file():
            yield start
            continue
        for directory, dirs, files in os.walk(start):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            for name in sorted(files):
                yield Path(directory) / name


def load_index(out):
    path = out / INDEX_JSON
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    if data.get("version") != INDEX_VERSION:
        return {}
    return data.get("files", {})


def write_index(out, entries):
    out.mkdir(parents=True, exist_ok=True)
    payload = {"version": INDEX_VERSION, "files": dict(sorted(entries.items()))}
    (out / INDEX_JSON).write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
    total = sum(entry["approx_tokens"] for entry in entries.values())
    lines = [
        "# Markdown cache index",
        "",
        "Generated by `scripts/to_markdown.py`. Token counts are rough estimates "
        "(4 English characters per token, 1 per non-ASCII character). Read the cached file, not the original. Search it "
        "with grep and read only the lines you need.",
        "",
        f"{len(entries)} file(s), about {total:,} tokens in total.",
        "",
        "| Source | Engine | Pages | ~Tokens | Cached Markdown |",
        "| --- | --- | --- | --- | --- |",
    ]
    for source, entry in sorted(entries.items()):
        pages = entry.get("pages") or ""
        lines.append(
            f"| {source} | {entry['engine']} | {pages} | {entry['approx_tokens']:,} "
            f"| [{entry['markdown']}](<{entry['markdown']}>) |"
        )
    (out / INDEX_MD).write_text("\n".join(lines) + "\n", encoding="utf-8")


def convert_paths(paths, out, root=ROOT, force=False, pdf_engine="pdfminer", converters=None, log=print):
    """Convert supported files under `paths`. Returns (converted, skipped, failed)."""
    out = Path(out)
    root = Path(root).resolve()
    entries = load_index(out)
    converted = skipped = failed = 0
    for source in walk_files(paths):
        if source.suffix.lower() not in CONVERT_EXTS:
            continue
        key = display_path(source, root)
        digest = sha256_file(source)
        old = entries.get(key)
        target = out / cache_name(source, root)
        if (not force and old and old.get("sha256") == digest
                and old.get("engine_option") == pdf_engine and target.is_file()):
            skipped += 1
            continue
        try:
            text, engine, pages = convert_one(source, pdf_engine, converters)
        except Exception as error:  # one bad file must not stop the batch
            failed += 1
            log(f"FAIL {key}: {type(error).__name__}: {error}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        entries[key] = {
            "sha256": digest,
            "source_bytes": source.stat().st_size,
            "engine": engine,
            "engine_option": pdf_engine,
            "pages": pages,
            "chars": len(text),
            "approx_tokens": approx_tokens(text),
            "markdown": cache_name(source, root).as_posix(),
        }
        converted += 1
        log(f"OK   {key} -> {entries[key]['markdown']} (~{entries[key]['approx_tokens']:,} tokens)")
    # Drop entries whose source file is gone, so the index stays truthful.
    for key in [k for k in entries if not (root / k).is_file() and not Path(k).is_file()]:
        stale = out / entries.pop(key)["markdown"]
        if stale.is_file() and stale.resolve().is_relative_to(out.resolve()):
            stale.unlink()
    write_index(out, entries)
    return converted, skipped, failed


def overview(paths, out=DEFAULT_OUT, root=ROOT):
    """Return a compact folder map: what each file is and what reading it costs."""
    root = Path(root).resolve()
    entries = load_index(Path(out))
    rows, by_type = [], {}
    for source in walk_files(paths):
        ext = source.suffix.lower() or source.name.lower()
        key = display_path(source, root)
        size = source.stat().st_size
        if key in entries:
            note = f"~{entries[key]['approx_tokens']:,} tok cached: {entries[key]['markdown']}"
        elif ext in CONVERT_EXTS:
            note = "convert first (binary)"
        elif ext in TEXT_EXTS or source.name.lower() in TEXT_EXTS:
            try:
                note = f"~{approx_tokens(source.read_text(encoding='utf-8')):,} tok text"
            except (OSError, UnicodeError):
                note = "unreadable as UTF-8"
        else:
            note = "binary, not converted"
        rows.append(f"{key}  [{size:,} B]  {note}")
        count, total = by_type.get(ext, (0, 0))
        by_type[ext] = (count + 1, total + size)
    summary = ", ".join(f"{ext} x{count}" for ext, (count, _) in sorted(by_type.items(), key=lambda kv: -kv[1][0]))
    return "\n".join([f"{len(rows)} file(s): {summary}", *rows])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Convert documents to cached Markdown for agents.")
    parser.add_argument("paths", nargs="+", type=Path, help="files or folders")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="cache folder (default: outputs/markdown-cache)")
    parser.add_argument("--force", action="store_true", help="reconvert even if the file is unchanged")
    parser.add_argument("--pdf-engine", choices=("pdfminer", "markitdown"), default="pdfminer")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--overview", action="store_true", help="list files and token costs; convert nothing")
    mode.add_argument("--stdout", action="store_true", help="print one converted file; do not cache")
    args = parser.parse_args(argv)

    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    missing = [str(p) for p in args.paths if not p.exists()]
    if missing:
        parser.error(f"not found: {', '.join(missing)}")
    if args.overview:
        print(overview(args.paths, args.out))
        return 0
    try:
        import markitdown  # noqa: F401
    except ImportError:
        print(
            "MarkItDown is not installed for this Python. Set it up once with:\n"
            "  python -m venv .venv\n"
            "  .venv/Scripts/python -m pip install -r scripts/requirements-markitdown.txt   (Windows)\n"
            "  .venv/bin/python -m pip install -r scripts/requirements-markitdown.txt       (Linux/macOS)\n"
            "then run this script with that Python.",
            file=sys.stderr,
        )
        return 2
    if args.stdout:
        if len(args.paths) != 1 or not args.paths[0].is_file():
            parser.error("--stdout takes exactly one file")
        text, _, _ = convert_one(args.paths[0], args.pdf_engine)
        sys.stdout.write(text)
        return 0
    converted, skipped, failed = convert_paths(args.paths, args.out, force=args.force, pdf_engine=args.pdf_engine)
    print(f"Converted {converted}, unchanged {skipped}, failed {failed}. Index: {display_path(args.out / INDEX_MD, ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
