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
