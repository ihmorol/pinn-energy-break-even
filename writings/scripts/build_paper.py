"""Build the conference and journal PDFs with pdflatex and BibTeX.

Run from the repository root:
    python -B -X utf8 writings/scripts/build_paper.py            # both
    python -B -X utf8 writings/scripts/build_paper.py journal    # one
Needs pdflatex and bibtex on PATH (MiKTeX or TeX Live).
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

WRITINGS = Path(__file__).resolve().parents[1]
VERSIONS = ("conference", "journal")
LATEX = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]


def build(folder):
    for cmd in (LATEX, ["bibtex", "main"], LATEX, LATEX):
        result = subprocess.run(cmd, cwd=folder, capture_output=True, text=True, errors="replace")
        if result.returncode != 0:
            print(result.stdout[-3000:])
            sys.exit(f"{folder.name}: failed at {' '.join(cmd)}")
    log = (folder / "main.log").read_text(encoding="utf-8", errors="replace")
    pages = re.search(r"Output written on main\.pdf \((\d+) pages", log)
    problems = [line for line in log.splitlines() if line.startswith(("Overfull", "LaTeX Warning"))]
    print(f"{folder.name}: {pages.group(1) if pages else '?'} pages")
    print(*problems, sep="\n")


def main():
    for tool in ("pdflatex", "bibtex"):
        if shutil.which(tool) is None:
            sys.exit(f"{tool} not found on PATH; install MiKTeX or TeX Live first.")
    names = sys.argv[1:] or VERSIONS
    for name in names:
        if name not in VERSIONS:
            sys.exit(f"unknown version {name!r}; use one of {VERSIONS}")
        build(WRITINGS / name)


if __name__ == "__main__":
    main()
