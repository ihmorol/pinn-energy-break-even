# Patterson et al. (2022): The carbon footprint of ML training will plateau, then shrink

## Source

- Title: The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink
- Authors: David Patterson, Joseph Gonzalez, Urs Hölzle, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel Rothchild, David So, Maud Texier, Jeff Dean
- Year and publication or preprint version: 2022, Computer (IEEE) 55(7):18-28 (July 2022); preprint arXiv:2204.05149v1
- DOI or source URL: https://doi.org/10.1109/MC.2022.3148714 ; preprint https://arxiv.org/abs/2204.05149
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/patterson-2022-carbon-plateau/patterson-2022-carbon-plateau.pdf`, SHA-256 99baa6948df14609dcbbc078cbef024bebb2fd62e842c027cb8859e5f5814701

OpenAlex cited_by_count 584 (checked 2026-11-12).

## Question and setting

Industry analysis of ML training energy and carbon at Google: four best practices (efficient models, processors, compute, and datacenter) reduce training energy by up to 100x and CO2 by up to 1000x; total ML energy stayed under 15 percent of Google's energy for three years.

## Claims we may use

- Published estimates for papers that omitted measurements have been off by 100x to 100,000x, so publishing emissions is presented as a way to ensure accurate accounting. Abstract.
- The source of the "about 60 percent of ML energy is inference, 40 percent training" split (a Google study, 2022). Abstract and its citation in Luccioni et al. 2024.

## Relevance to this project

Two uses: (1) motivates measured, published energy accounting in research papers (our comparison table and study ledger follow that recommendation); (2) provides the deployment-side context that repeated inference dominates long-run energy in practice, which is the regime our N-query break-even question addresses.

## Check status and gaps

DOI verified via Crossref (55(7):18-28); preprint verified via the arXiv API. Gaps: abstract-level access only; the 60/40 split needs the exact page reference from the published version before it goes in the report.
