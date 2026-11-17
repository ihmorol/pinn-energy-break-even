# McGreivy and Hakim (2024): weak baselines in ML for PDEs

## Source

- Title: Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations
- Authors: Nick McGreivy, Ammar Hakim
- Year and publication or preprint version: 2024, Nature Machine Intelligence 6(10):1256-1269 (online 2024-09-25); preprint arXiv:2407.07218v1
- DOI or source URL: https://doi.org/10.1038/s42256-024-00897-5 ; preprint https://arxiv.org/abs/2407.07218
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata; arXiv abstract; arXiv v1 HTML read in part (first half of the page). The published Nature version was not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 268 (checked 2026-11-17).

## Question and setting

A systematic review of ML-for-PDE papers in fluid mechanics that claim to beat a standard numerical method. It asks whether those comparisons are fair and whether negative results get reported. It is a review; it runs no solver comparison of its own for our problem type.

## Claims we may use

- 79% (60/76) of the reviewed articles that claim to outperform a standard numerical method compare to a weak baseline. Abstract.
- Outcome-reporting bias and publication bias are widespread, so negative results are under-reported. Abstract.
- "Thus, rule 1 is to make comparisons at either equal accuracy or equal runtime." arXiv v1 HTML.
- "Thus, rule 2 is to compare to an efficient numerical method." arXiv v1 HTML.
- PINN papers were left out of the 76 because "standard numerical methods are known to outperform PINNs for solving forward problems". arXiv v1 HTML.

## Relevance to this project

This is the primary, peer-reviewed source for the 79% figure, which our docs previously cited only through Huang et al. 2026. Its two rules match our design: matched accuracy targets, and a classical baseline that must be efficient. Rule 2 is a direct check on our baseline choice (SciPy `spsolve` or preconditioned CG); the pilot must show it is efficient at our grid sizes. Its finding on reporting bias supports reporting "no crossover" as a result.

## Check status and gaps

Venue, volume, issue, pages, and DOI confirmed in Crossref. The rule quotations come from the arXiv v1 HTML, not the published text; check the wording and add section numbers from the Nature version before quoting in the report. The second half of the arXiv HTML was not read.
