# Winkler and Stoll (2026): no free lunch in flow surrogates, with break-even accounting

## Source

- Title: No Free Lunch in Flow Surrogates under Time-Varying Boundary Conditions: A Two-Regime Study
- Authors: Georg Winkler, Martin Stoll (Chemnitz University of Technology)
- Year and publication or preprint version: arXiv:2607.23667 (2026). A journal version with the same title is in Crossref: Journal of Computational Science, DOI 10.1016/j.jocs.2026.103075, issue date 2027-01. Only the arXiv version was read.
- DOI or source URL: https://doi.org/10.48550/arxiv.2607.23667 (published: https://doi.org/10.1016/j.jocs.2026.103075)
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown. Not yet read by a human member.
- Access: full text of the arXiv version
- Local file: `downloads/flow-surrogates-2026-no-free-lunch/flow-surrogates-2026-no-free-lunch.pdf`, SHA-256 4159e9df895d3b3fd8d4b9825da0d9757021e6c1fb7e63439ea55b576100a677

## Question and setting

The paper benchmarks eight data-driven surrogates on two transient flows under time-varying boundary conditions: the 3D slurry film and the 2D Karman vortex street.

- **Classical solver:** a finite-element solver. One case takes about 11 h (film) and 0.77 h (wake) of solver wall-clock (p5-6).
- **Hardware differs:** the solver runs on CPU and the surrogates on GPU (p11).
- **Cost measure:** wall-clock time; no energy.
- **Seeds:** results are means over three seeds (p8, p11).

## Claims we may use

- The break-even query count is defined as Q* = (N_train t_FEM + t_train) / (t_FEM - t_infer), counting the training simulations and the training itself (Sec. 5.4, Eqs. 26-27, p11). This is the same form as our cost model, with S_P = N_train t_FEM + t_train and S_C = 0.
- "The search that selected each configuration is not charged" (Sec. 5.4, p11). Tuning cost is excluded.
- Surrogates answer queries 10^3 to 10^4 times faster than the FE solver, and pay off from the first query beyond the training set on the film and from the third on the wake (abstract).
- The solver is run at its production core count, so that "the reference is not artificially slow" (p11).

## Relevance to this project

This is a peer-reviewed break-even accounting against a classical solver, following the McGreivy and Hakim reporting recommendation. It does not test a PINN: the models are trained on solver data. It does not measure energy, and it leaves tuning cost out. It supports our design choice of counting the full setup, and our plan to charge tuning and failures, which this paper does not.

## Check status and gaps

- The published version was not read. Check that the Journal of Computational Science text matches before citing numbers.
