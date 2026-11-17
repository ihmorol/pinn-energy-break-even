# Markidis (2021): PINNs as Poisson solvers against PETSc

## Source

- Title: The Old and the New: Can Physics-Informed Deep-Learning Replace Traditional Linear Solvers?
- Authors: Stefano Markidis
- Year and publication or preprint version: 2021, Frontiers in Big Data 4:669097 (online 2021-11-19); preprint arXiv:2103.09655
- DOI or source URL: https://doi.org/10.3389/fdata.2021.669097
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text (open access) not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 344 (checked 2026-11-17).

## Question and setting

Evaluates PINNs as linear solvers for the Poisson equation, varying network depth, activation, and input distribution, and studies transfer learning. Then proposes hybrids of PINNs and traditional linear solvers, compared with PETSc conjugate gradient. Single solves; cost is performance (time); no energy.

## Claims we may use

- Low-frequency components converge quickly (attributed to the F-principle), but "an accurate solution of the high frequencies requires an exceedingly long time". Abstract.
- Hybrid PINN-plus-traditional solvers perform "on par with other high-performance solvers, such as PETSc conjugate gradient linear solvers, in terms of performance and accuracy". Abstract.
- Accuracy and computational performance remain a limiting factor for direct use of PINN linear solvers. Abstract.

## Relevance to this project

Poisson is the constant-coefficient case of our steady-diffusion problem, so this is the closest peer-reviewed evidence on PINN accuracy cost for our equation type. The slow high-frequency convergence is a concrete risk for the 1e-3 target and supports keeping accuracy failures as results. It also shows conjugate gradient (PETSc) as the natural strong baseline for this equation.

## Check status and gaps

Venue and DOI confirmed in Crossref. Grid sizes, timings, hardware, and error levels were not read; read the open-access full text before quoting any number. The hybrid solvers are outside our fixed scope and are cited as context only.

## Full-text methods check, 2026-11-17

Reader: Claude Code AI agent; targeted read of the methods, setup, and cost passages through the Markdown cache (`scripts/to_markdown.py`). Not yet read by a human member. Source: arXiv:2103.09655 PDF, stored at `downloads/markidis-2021-pinn-linear-solvers/markidis-2021-pinn-linear-solvers.pdf`, SHA-256 35e1c4b012e48acbbd96b53c5d379c83aacfe8691f39f4e0716fcb4333e9204c. Not compared with the published version.

- Section 2: typical PINNs use 4 to 6 hidden layers of 50 to 100 units, Xavier init, Sobol collocation points by default, and Adam followed by L-BFGS-B. The author found L-BFGS-B "by far the highest accuracy and faster convergence" among the optimizers tried. ReLU-like activations are avoided.
- Section 2.1 (2D Poisson): 128 x 128 Sobol points plus 4,000 boundary points; 10,000 Adam epochs at learning rate 0.001, then 13,000 L-BFGS-B epochs (DeepXDE). The Adam training error levels off at about 5e-3 to 1e-2 after 2,000 epochs; L-BFGS-B takes it to 2.79e-5. This is the training (residual) error, not the relative L2 error against the solution.
- Same section: training took 6,380 s (about 1.5 h) on a dual-core Intel i5 CPU; petsc4py CG on a 128 x 128 grid took 92.28 s on the same machine, run to double-precision machine epsilon. The two runs were not matched in accuracy.
- Section 3: networks with four or more hidden layers performed about the same in early training; the activation function mattered.
- Section 4: transfer learning (warm-starting from a network trained for another source term) cut training a lot; with it, only about 10 Adam epochs were needed before L-BFGS-B.

Use for us: Adam alone plateaued in this Poisson case, so the L-BFGS phase is likely needed for the 1e-3 target. Transfer learning per query is not our design; we train once.
