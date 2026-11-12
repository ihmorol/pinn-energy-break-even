"""Check shared files, proposal hashes, local Markdown targets, and project skills.

Uses only the standard library and makes no writes or network requests. The link
check covers inline links/images and reference definitions, not full CommonMark,
HTML links, or heading anchors. It ignores code examples and generated folders.
"""

import argparse
import hashlib
import json
import os
import re
from pathlib import Path, PureWindowsPath
from urllib.parse import unquote, urlsplit


PROPOSAL_FILES = {
    "docs/proposal/ENERGY_CROSSOVER_PROPOSAL.pdf",
    "docs/proposal/ENERGY_CROSSOVER_PROPOSAL.docx",
}
REQUIRED_FILES = (
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "CLAUDE.md", "GEMINI.md",
    ".gitignore", ".gitattributes", ".editorconfig",
    "docs/research-plan.md", "docs/writing-style.md",
    "docs/proposal/manifest.json", *sorted(PROPOSAL_FILES),
    "references/README.md", "references/paper-note-template.md",
    "experiments/README.md", "experiments/run-template.json", "experiments/study-energy.csv",
    ".agents/skills/README.md",
    ".agents/skills/research-writing/SKILL.md",
    ".agents/skills/literature-check/SKILL.md",
    ".agents/skills/experiment-run/SKILL.md",
    ".agents/skills/research-review/SKILL.md",
    ".github/copilot-instructions.md",
    ".github/ISSUE_TEMPLATE/research-task.md",
    ".github/ISSUE_TEMPLATE/problem-report.md",
    ".github/pull_request_template.md",
    ".github/workflows/workspace-checks.yml",
    "scripts/check_workspace.py", "tests/test_check_workspace.py",
)
IGNORED_DIRS = {
    ".git", ".zcode", ".gstack", ".venv", "venv", "node_modules", "__pycache__",
    ".pytest_cache", ".ruff_cache", ".ipynb_checkpoints", "outputs", "downloads",
}
MACHINE_PATH = re.compile(r"(?<![\w])[A-Za-z]:[/\\]|/(?:Users|home)/[^\s/]+|~[/\\]")


def inside_workspace(path, root):
    try:
        return path.resolve().is_relative_to(root)
    except (OSError, RuntimeError):
        return False


def check_manifest(root):
    relative = "docs/proposal/manifest.json"
    path = root / relative
    if not inside_workspace(path, root):
        return [f"{relative}: outside the workspace"]
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [f"{relative}: invalid JSON: {error}"]
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data.get("schema_version") != 1:
        return [f"{relative}: expected manifest schema_version 1"]
    entries = data.get("files")
    if not isinstance(entries, list):
        return [f"{relative}: files must be a list"]
    problems = []
    names = []
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            problems.append(f"{relative}: each file needs a path")
            continue
        name = entry["path"]
        names.append(name)
        target = root / name
        if PureWindowsPath(name).is_absolute() or not inside_workspace(target, root):
            problems.append(f"{relative}: {name} is outside the workspace")
            continue
        digest, size = entry.get("sha256"), entry.get("size_bytes")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest) or type(size) is not int or size < 0:
            problems.append(f"{relative}: invalid hash or size for {name}")
            continue
        if not target.is_file():
            problems.append(f"{name}: submitted file is missing")
            continue
        try:
            content = target.read_bytes()
        except OSError as error:
            problems.append(f"{name}: cannot read submitted file: {error}")
            continue
        if len(content) != size:
            problems.append(f"{name}: size mismatch")
        if hashlib.sha256(content).hexdigest() != digest:
            problems.append(f"{name}: SHA-256 mismatch")
    if len(names) != len(PROPOSAL_FILES) or set(names) != PROPOSAL_FILES:
        problems.append(f"{relative}: must list each submitted file exactly once")
    return problems


def without_code(text):
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence is not None:
            lines.append("\n" if line.endswith("\n") else "")
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not line[marker.end():].strip():
                fence = None
        elif marker:
            fence = marker[1]
            lines.append("\n" if line.endswith("\n") else "")
        else:
            lines.append(line)
    return re.sub(r"(`+)(.+?)\1", lambda match: "\n" * match[0].count("\n"), "".join(lines), flags=re.S)


def link_targets(text):
    clean = without_code(text)
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*", clean):
        start = match.end()
        if start >= len(clean):
            continue
        if clean[start] == "<":
            end = clean.find(">", start + 1)
            if end != -1:
                yield clean[start + 1:end], clean.count("\n", 0, match.start()) + 1
            continue
        end, depth = start, 0
        while end < len(clean):
            char = clean[end]
            if char == "\\" and end + 1 < len(clean):
                end += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            end += 1
        if end > start:
            target = re.sub(r"\\([()])", r"\1", clean[start:end])
            yield target, clean.count("\n", 0, match.start()) + 1
    for match in re.finditer(r"(?m)^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|(\S+))", clean):
        yield match[1] or match[2], clean.count("\n", 0, match.start()) + 1


def check_links(path, text, root):
    problems = []
    relative = path.relative_to(root).as_posix()
    for target, line in link_targets(text):
        if target.startswith("#"):
            continue
        try:
            url = urlsplit(target)
        except ValueError:
            problems.append(f"{relative}:{line}: invalid link target: {target}")
            continue
        if url.scheme in {"http", "https", "mailto", "ftp"} or url.netloc:
            continue
        local = unquote(url.path)
        if url.scheme or PureWindowsPath(local).is_absolute():
            problems.append(f"{relative}:{line}: nonportable local target: {target}")
            continue
        resolved = path.parent / local
        if not inside_workspace(resolved, root):
            problems.append(f"{relative}:{line}: local target is outside the workspace: {target}")
        elif not resolved.exists():
            problems.append(f"{relative}:{line}: missing local target: {target}")
    return problems


def check_skill(path, text, root):
    relative = path.relative_to(root).as_posix()
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return [f"{relative}: skill needs YAML frontmatter"]
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if separator:
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            fields[key.strip()] = value
    problems = []
    name = fields.get("name", "")
    if name != path.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        problems.append(f"{relative}: skill name must match its directory and use lowercase kebab-case")
    description = fields.get("description", "")
    if not description or description in {"|", ">", "null", "~"}:
        problems.append(f"{relative}: skill needs a single-line description")
    return problems


def markdown_files(root):
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(name for name in dirs if name not in IGNORED_DIRS and not (Path(directory) / name).is_symlink())
        for name in sorted(files):
            if name.lower().endswith(".md"):
                yield Path(directory) / name


def check_workspace(root):
    root = Path(root).resolve()
    problems = []
    if not root.is_dir():
        return [f"{root}: workspace directory does not exist"]
    for relative in REQUIRED_FILES:
        target = root / relative
        if not inside_workspace(target, root):
            problems.append(f"{relative}: outside the workspace")
        elif not target.is_file():
            problems.append(f"{relative}: missing required file")
    problems.extend(check_manifest(root))
    for path in markdown_files(root):
        relative = path.relative_to(root).as_posix()
        if not inside_workspace(path, root):
            problems.append(f"{relative}: outside the workspace")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            problems.append(f"{relative}: cannot read UTF-8 text: {error}")
            continue
        for match in MACHINE_PATH.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            problems.append(f"{relative}:{line}: machine-specific path; use a repository-relative path")
        problems.extend(check_links(path, text, root))
        if path.name == "SKILL.md" and path.relative_to(root).parts[:2] == (".agents", "skills"):
            problems.extend(check_skill(path, text, root))
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    problems = check_workspace(args.root)
    if problems:
        for problem in problems:
            print(f"FAIL {problem}")
        print(f"Workspace checks failed: {len(problems)} problem(s).")
        return 1
    print("Workspace checks passed. No research results, remote links, or writing authorship were checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
