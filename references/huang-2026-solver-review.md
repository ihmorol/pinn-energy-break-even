# Huang et al. (2026): Classical, machine learning, and hybrid solvers for PDEs

## Source

- Title: Classical, Machine Learning, and Hybrid Solvers for Partial Differential Equations: An Evidence-Weighted Review and Decision Framework
- Authors: Y. Huang, X. Wang, S. Yao, F. Zeng, W. Peng (as listed in the submitted proposal; the arXiv v1 record matches this work)
- Year and publication or preprint version: 2026 preprint, arXiv:2610.32911v1 (submitted 2026-10-23)
- DOI or source URL: https://arxiv.org/abs/2610.32911
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: full text read via arXiv HTML v1
- Local file: `downloads/huang-2026-solver-review/huang-2026-solver-review.pdf`, SHA-256 9462ae52b5e606d69ac690f571c333a5acc7d52a15595648f5a78606f12e0e2f

OpenAlex: 1 citing work (about one month old at check date). Supplied as reference 2 of the submitted proposal; independently checked here.

## Question and setting

Survey and decision framework for choosing among classical, learned, and hybrid PDE solvers, organized by query volume, data availability, and certification needs. The amortization analysis (Sections 4.4-4.6) compares an FNO surrogate against a cell-centered finite volume solver with AMG-preconditioned conjugate gradients on thresholded parametric Darcy flow, resolutions 64^2 to 512^2, training sets of 100 to 2000 samples, three seeds, GPU training versus single-core CPU classical solves.

## Claims we may use

- Amortization law (Section 4.5, Eq. 1): N* = (gamma N_tr + tau) / (1 - 1/S) for S > 1, with gamma the data-generation cost ratio, tau the training cost in classical-solve units, and S the per-query speedup. Surrogates never break even when S <= 1. Consequence F1: N* always exceeds the training-set size N_tr when training data costs at least one classical solve each. Consequence F2: beyond about 10x, higher per-query speedup barely moves N* because speed acts through training cost.
- Break-even claim: "surrogates trained on solver-generated data break even only after many queries, beyond thirty thousand for errors below one percent" (Abstract); "no FNO model with an error below 1% breaks even before 3.1x10^4 queries" (Section 4.6). Higher resolution raises break-even further (about 3x10^4 at 64^2 to about 9x10^5 at 512^2 with 1000 samples).
- Evidence ladder (Section 4.8): P0 training loss, P1 in-distribution error versus independent reference, P2 error under deployment-matched shift, P3 equal-accuracy cost-matched comparison against a tuned classical or ROM workflow, P4 workflow-level evidence inside the deployment loop. Non-transferability principle: evidence for one rung does not establish a higher rung.
- Baseline-quality audit cited there: about 79 percent of 76 ML surrogate papers compared against a weak baseline (McGreivy and Hakim); FNO's 440x per-query speedup becomes about 1.5x end-to-end in its own showcase.
- Decision regimes (Tables 3 and 4): classical solvers stay the default for one-off solves, certification needs, and missing paired data; learned surrogates are justified mainly for many-query regimes with existing data.

## Relevance to this project

The amortization law is the same break-even structure as our E(N) = S + N e model, expressed in cost units rather than measured electricity. Our study instantiates that law with metered energy and runtime on a small parametric diffusion family, so this paper supplies the conceptual model and the honest reporting standard. Its evidence ladder places our planned comparison at rung P3. Its Darcy result (break-even above 30,000 queries at 1 percent error) is the closest quantitative prior for N* and a direct hypothesis for our much smaller 2D steady-diffusion setting, where N* may differ in either direction.

## Check status and gaps

Identifier resolved via arXiv API (title and version confirmed 2026-11-12). Full text read in HTML form. Gaps: author list must be transcribed exactly from the PDF before it goes into the final report reference list; the paper is a one-month-old preprint, so treat every number as unrefereed and re-check for a published version before submission.
