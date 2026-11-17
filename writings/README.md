# Writings

Two versions of the paper. Both are study-design papers: no solver, PINN, or energy run exists yet, so neither reports measured results.

| Path | Contents |
|---|---|
| `conference/main.tex`, `conference/main.pdf` | IEEE conference version, 6 pages or less |
| `journal/main.tex`, `journal/main.pdf` | Longer IEEE two-column journal version, 10 to 12 pages |
| `shared/references.bib` | Bibliography, built from the notes in [references](../references/README.md) |
| `shared/figures/` | Figures made by `scripts/make_figures.py` (sketches and definitions only, no data) |
| `*/IEEEtran.cls`, `*/IEEEtran.bst` | Official IEEE class (V1.8b) and BibTeX style, unchanged |
| `template/` | The official IEEE conference template source (version 6/27/2024), kept for reference |
| `reviews/` | Review records for each draft |
| `scripts/` | Figure and build scripts |

The template and style files come from the IEEE page [Manuscript Templates for Conference Proceedings](https://www.ieee.org/conferences/publishing/templates). Do not change margins, fonts, or column settings. IEEE asks authors to keep the template layout and to remove all guidance text before submission.

Both versions follow the docs merged to `main`, including the [training pipeline plan](../docs/training-pipeline.md) and the [gap evidence matrix](../docs/gap-evidence.md). When those docs change, update both papers.

## Build

Install a LaTeX distribution with `pdflatex` and `bibtex` (MiKTeX on Windows, TeX Live on Linux), then run from the repository root:

```bash
python -B -X utf8 writings/scripts/make_figures.py
python -B -X utf8 writings/scripts/build_paper.py
```

`build_paper.py conference` or `build_paper.py journal` builds one version.

## Before submission

- Fill Table "Reporting format" and the Reporting Plan section with measured values once the trials run, and rename that section to Results.
- Fill in the author block. It says "Anonymous Author(s)" for now.
- Recheck the preprints (Huang et al. 2026, Huang and Stuart 2026, Zhang et al. 2026, Wilson et al. 2025, Yoo et al. 2026, Kapoor et al. 2025) for published versions.
- Confirm the acknowledgment follows the teacher's AI-use and disclosure rules.
- Members must read and check the drafts. They were written with AI assistance from the project notes.
