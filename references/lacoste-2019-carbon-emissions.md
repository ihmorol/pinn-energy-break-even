# Lacoste et al. (2019): Quantifying the carbon emissions of machine learning

## Source

- Title: Quantifying the Carbon Emissions of Machine Learning
- Authors: Alexandre Lacoste, Alexandra Luccioni, Victor Schmidt, Thomas Dandres
- Year and publication or preprint version: 2019 preprint, arXiv:1910.09700v2 (October 2019); presented at the Tackling Climate Change with Machine Learning workshop, NeurIPS 2019 (non-archival)
- DOI or source URL: https://arxiv.org/abs/1910.09700
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/lacoste-2019-carbon-emissions/lacoste-2019-carbon-emissions.pdf`, SHA-256 696e4d3c6a14bfbcc568dd1ca91da678ac604180d7b424d8de75c53672326e73

OpenAlex cited_by_count 1,241 (checked 2026-11-12). Do not confuse with arXiv:1911.08354 (Lottick et al., "Energy Usage Reports") or arXiv:2007.03051 (Anthony et al., Carbontracker), which are different works.

## Question and setting

The Machine Learning Emissions Calculator (the ancestor of CodeCarbon): approximates training emissions as a function of hardware, training duration, and the location's electricity grid, and recommends mitigation actions for practitioners and organizations.

## Claims we may use

- Emissions estimates of this tool are modeled: training time times hardware power times regional grid intensity. Abstract and framing.
- The three dominant factors it identifies are server location and grid, training duration, and hardware make and model. Abstract.

## Relevance to this project

This is the reference for the "modeled estimate" category in our accounting. Our research plan already notes that CodeCarbon may log readings or estimates; this paper is the citation for what those estimates are and why they must be labeled separately from counter measurements.

## Check status and gaps

Preprint verified via the arXiv API; workshop venue confirmed via the climatechange.ai listing. Gaps: abstract-level access only; the exact formula and its coefficients were not transcribed. Note the venue is a non-archival workshop; cite the arXiv version as a preprint.
