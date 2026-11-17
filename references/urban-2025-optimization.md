# Urbán, Stefanou, Pons (2025): How accurate and competitive can PINNs be?

## Source

- Title: Unveiling the optimization process of Physics Informed Neural Networks: How accurate and competitive can PINNs be?
- Authors: Jorge F. Urbán, Petros Stefanou, José A. Pons
- Year and publication or preprint version: 2025, Journal of Computational Physics 523:113656; preprint arXiv:2405.04230v3
- DOI or source URL: https://doi.org/10.1016/j.jcp.2024.113656 ; preprint https://arxiv.org/abs/2405.04230
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted full-text read); not yet independently read by a human member
- Access: full text; abstract, Section 3, and Section 4 setup and tables read; Section 5 skimmed
- Local file: `downloads/urban-2025-optimization/urban-2025-optimization.pdf`, SHA-256 021cf5fd6850a13eddaa91a9785392f545d93f36ce2f4d2ef255402a4e7642a2

## Question and setting

How far PINN accuracy can be pushed by better quasi-Newton optimizers and a small change to the loss. Compares Adam, BFGS, self-scaled BFGS, and self-scaled Broyden on several physics problems, using small tanh networks and a finite-difference reference.

## Claims we may use

- Abstract: compact networks, "typically comprising 2 or 3 layers of 20-30 neurons", reach accuracies comparable to finite-difference schemes with thousands of grid points once the optimizer is improved.
- Section 3.1: Adam for the first iterations, then a quasi-Newton method. Section 4 and Table 1: the random training points are refreshed every 500 iterations.
- Section 3.3: training on a monotone function of the loss (for example its square root) changes the Hessian scaling near the minimum and can improve precision; a one-line change.
- Section 4: with standard BFGS the PINN error is about 1e-3 on one test; the self-scaled variants reach about 1e-5. Error tables report mean plus or minus spread across runs.

## Relevance to this project

Evidence that a small network can reach our 1e-3 and possibly 1e-4 targets if the optimizer is good enough, which matters for query energy (smaller network, cheaper inference). It is single-solve work, not a parametric family, so the network size it needs is a lower bound for ours. Self-scaled Broyden is not in standard PyTorch; adopting it would be new code and a protocol decision.

## Check status and gaps

Journal, volume, article number, and DOI from the arXiv record (journal reference field). Floating-point precision used was not stated in the passages read; check before citing any precision claim from this paper.
