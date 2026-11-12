# Sources and paper notes

Record what each source actually supports. A citation copied from the proposal is a starting point, not a completed literature check. Keep the original title, authors, year, and identifier when recording it.

## Sources in the submitted proposal

| Source | Identifier | Check status |
|---|---|---|
| Grossmann, T. G., Komorowska, U. J., Latz, J., & Schönlieb, C.-B. (2024). *Can physics-informed neural networks beat the finite element method?* IMA Journal of Applied Mathematics. | https://doi.org/10.1093/imamat/hxae011 | Supplied in the proposal; not independently checked in this workspace setup. |
| Huang, Y., Wang, X., Yao, S., Zeng, F., & Peng, W. (2026). *Classical, machine learning, and hybrid solvers for partial differential equations: An evidence-weighted review and decision framework* [Preprint]. arXiv. | https://arxiv.org/abs/2610.32911 | Supplied in the proposal; not independently checked in this workspace setup. |

Before using either source to support a new claim, resolve its identifier, confirm the bibliographic details, and read the relevant passage. If a reference does not match or cannot be accessed, record the problem. Do not silently fix the already-submitted PDF or Word file.

## Add a paper note

Copy the [paper-note template](paper-note-template.md) to a descriptive filename in this directory when there is a real paper to record. Separate the source's findings from our interpretation. Include a page, section, table, figure, or short exact quotation for each claim used in our report.

Record whether you read the full text, only the abstract, or a secondary account. Record the date and version you actually checked. Do not claim a paper is verified because a search result or another AI system supplied its citation.

Use the [literature-check skill](../.agents/skills/literature-check/SKILL.md) for this task. Avoid claims such as "nobody has measured this" unless a recorded search supports that statement within a stated scope. A paper about runtime does not automatically support an energy claim.

Keep paper PDFs and other downloads out of Git unless sharing rights and project approval are clear. Store each download in its own new directory under the ignored `downloads/` path, with source and hash recorded in the note. Keep scripts elsewhere and use isolated Python if processing downloaded files.
