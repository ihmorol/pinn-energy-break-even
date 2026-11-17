# Mishra and Molinaro (2022): Generalization error estimates for PINNs

## Source

- Title: Estimates on the generalization error of Physics Informed Neural Networks (PINNs) for approximating PDEs
- Authors: Siddhartha Mishra, Roberto Molinaro
- Year and publication or preprint version: IMA Journal of Numerical Analysis 43(1):1-43 (2023 volume; first published online 2022-01-14); preprint arXiv:2006.16144v3 (2020-06-29)
- DOI or source URL: https://doi.org/10.1093/imanum/drab093 ; preprint https://arxiv.org/abs/2006.16144
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/mishra-molinaro-2022-generalization/mishra-molinaro-2022-generalization.pdf`, SHA-256 84da9984f824c52b3e3eb73b0ff925a7d501d938d58ceb87cd0f5874e9a791a9

OpenAlex cited_by_count 359 (checked 2026-11-12). Companion paper on inverse problems: IMA JNA 42(3):981-1022, 2022, DOI 10.1093/imanum/drab032, arXiv:2007.01138 (verified, not downloaded).

## Question and setting

Theory paper: rigorous upper bounds on the generalization error of PINNs for forward problems, built on an abstract framework that uses stability properties of the underlying PDE. The bound relates generalization error to training error and the number of training (collocation) samples, illustrated on nonlinear PDEs with supporting numerical experiments.

## Claims we may use

- Generalization error of a PINN can be bounded in terms of its training error and the number of training samples, with the PDE's stability constants entering the bound. Abstract.
- Consequence for our design: the held-out relative L2 error we measure depends on the collocation budget; the bound gives a principled reason to fix and report the collocation count as part of the frozen protocol rather than tune it silently.

## Relevance to this project

Provides the theoretical anchor for the accuracy gate: it tells us what knobs (training error via optimization, sample count) the held-out error depends on, and why they must be fixed before comparing costs. It also guards our wording: our measured relative L2 errors are empirical, and this paper is the right citation when we note that such errors can be bounded a priori for stable PDEs.

## Check status and gaps

Journal, volume, pages, DOI, and preprint verified via Crossref and the arXiv API. Gaps: abstract-level access only. The bound's constants and assumptions were not read; do not state the bound's form in the report without a full-text read.

## Full-text methods check, 2026-11-17

Reader: Claude Code AI agent; targeted read of the methods and training sections of the locally stored PDF (hash above matched on re-download). Not yet independently read by a human member.

- Section 2: training points can be grid, random, or low-discrepancy (Sobol) points; low-discrepancy points are suggested for moderate dimensions (roughly 4 to 20). Our (x, y, theta_1, theta_2) input space is four-dimensional.
- Numerical experiments: ensemble training over a hyperparameter grid (layers, width, regularization exponent and size; Table 1), 360 configurations, each retrained five times from different initial weights, keeping the run with the smallest training loss. Optimizer: L-BFGS; light or no L2 regularization worked best.
- Consequence for us: selection by lowest training loss over many retrains is a real cost. If we select among seeds or settings, every discarded run belongs in the study ledger, and the deployment retry policy must say which of them a user would also pay for.
- The bound's exact form and constants were still not transcribed; do not state it in the report from this note.
