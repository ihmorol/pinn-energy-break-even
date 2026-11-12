# Luccioni, Jernite, Strubell (2024): Power hungry processing

## Source

- Title: Power Hungry Processing: Watts Driving the Cost of AI Deployment?
- Authors: Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell
- Year and publication or preprint version: 2024, ACM Conference on Fairness, Accountability, and Transparency (FAccT 2024); preprint arXiv:2311.16863v3
- DOI or source URL: https://doi.org/10.1145/3630106.3658542 ; preprint https://arxiv.org/abs/2311.16863
- Date checked: 2026-11-12
- Reader: ZCode AI agent (full text read via the arXiv version during the automated literature check); not yet independently read by a human member
- Access: full text read
- Local file: `downloads/luccioni-2024-power-hungry/luccioni-2024-power-hungry.pdf`, SHA-256 997025051680fd262e80da571ddb74d2af4e8f023baea9b6d4bd7539d163ab33

OpenAlex cited_by_count 679 (checked 2026-11-12).

## Question and setting

First systematic comparison of inference-phase energy and carbon across ML systems: deployment cost is measured as the energy and carbon of 1,000 inferences per task, covering task-specific and multi-purpose generative models.

## Claims we may use

- "Multi-purpose, generative architectures are orders of magnitude more expensive than task-specific systems for a variety of tasks, even when controlling for the number of model parameters." Abstract.
- Measured per-1,000-inference energy spans from about 0.002 kWh (most efficient task) to 11.49 kWh (least efficient image-generation model) in the full text.
- The often-quoted claim that about 60 percent of ML energy is inference comes from this paper only as a citation of Patterson et al. 2022 (a Google study), not as this paper's own result. Important when attributing the split.

## Relevance to this project

Supports our decision to account deployment (per-query) cost separately from training cost: inference is a first-class energy consumer, so the per-query energy e_P and e_C in our break-even model deserve the same measurement care as setup S_P and S_C. Also supplies context for the separate study-electricity versus deployment-cost distinction in our plan.

## Check status and gaps

DOI verified via Crossref; full text read via arXiv. Gaps: the ACM version's pagination was not recorded; add it if the final report cites the published version. Its numbers are for language and vision models, not PDE solvers; do not transfer magnitudes to our setting.
