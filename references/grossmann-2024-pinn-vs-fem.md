# Grossmann et al. (2024): Can physics-informed neural networks beat the finite element method?

## Source

- Title: Can Physics-Informed Neural Networks beat the Finite Element Method?
- Authors: Tamara G. Grossmann, Urszula Julia Komorowska, Jonas Latz, Carola-Bibiane Schönlieb
- Year and publication or preprint version: 2024, IMA Journal of Applied Mathematics 89(1), 143-174 (online 2024-05-23); preprint arXiv:2302.04107v1 (2023-02-08)
- DOI or source URL: https://doi.org/10.1093/imamat/hxae011 ; preprint https://arxiv.org/abs/2302.04107
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: full text read via PMC open-access copy (PMC11197852); arXiv PDF stored locally
- Local file: `downloads/grossmann-2024-pinn-vs-fem/grossmann-2024-pinn-vs-fem.pdf`, SHA-256 cb123e7936e5ae55bb63702d1cff30d69e940972450822afbea659ef28234a9a

OpenAlex cited_by_count 320; Crossref 220 (checked 2026-11-12). Supplied as reference 1 of the submitted proposal; independently checked here.

## Question and setting

Head-to-head computational comparison of PINNs (JAX, GPU) and finite elements (FEniCS, CPU) on single solves. Problems: Poisson in 1D, 2D, 3D; Allen-Cahn in 1D; semilinear Schrödinger in 1D and 2D. Hardware: Intel Xeon E5-2643 v3 (12 cores) and one NVIDIA Quadro P6000. Cost measure: wall-clock solution and evaluation time, averaged over 10 runs. No parametric family, no repeated queries, and no energy measurement appear anywhere in the text.

## Claims we may use

- FEM was faster than PINNs at equal or better accuracy in nearly every test: PINN training about two to three orders of magnitude slower for 1D Poisson; FEM faster by one to three orders for 2D and 3D Poisson; five to six orders for Allen-Cahn; about two orders for 1D Schrödinger; two to three orders (solution) for 2D Schrödinger. Sections 4-6 and 7.
- The one exception: for 3D Poisson, trained-PINN evaluation was two to three orders of magnitude faster than FEM interpolation. Section 6.
- Measured cost is time only. Energy or electricity was not measured. Confirmed by full-text check, 2026-11-12.
- On parameterized problems: "An aspect of the evaluation time that we have not considered throughout this work is the possibility of solving parameterized PDEs with neural networks, the so-called operator approximators." Section 7. The paper therefore does not study amortization over parameter queries.
- General conclusion: "for certain classes of PDEs for which classical methods are applicable, PINNs are not able to outperform those". Section 7.
- Stated limits: vanilla PINNs only; no multigrid used; better FEM interpolation could erode the PINN evaluation advantage.

## Relevance to this project

This is the direct predecessor of our study. It supplies the comparison structure (matched problem, matched accuracy, wall-clock cost) and two named gaps our fixed scope fills: it does not measure energy, and it does not consider parametric PDEs with amortized training cost. Our break-even question (how many new parameter queries recover setup and training cost) starts where this paper stops. Its "FEM wins on single solves" result is a prior we must report honestly, not a result to assume for our parametric workload.

## Check status and gaps

Verified against Crossref (DOI, volume 89, issue 1, pages 143-174, note: an earlier draft of our shortlist said 143-164, corrected here) and PMC (title, authors, DOI match). Full text read. Gaps: the exact per-problem timings were not transcribed into this note; read the tables again before quoting specific numbers in the report. GPU (PINN) versus CPU (FEM) placement is a comparability limit to discuss, not copy silently.
