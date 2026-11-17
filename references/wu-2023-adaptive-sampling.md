# Wu et al. (2023): Non-adaptive and residual-based adaptive sampling for PINNs

## Source

- Title: A comprehensive study of non-adaptive and residual-based adaptive sampling for physics-informed neural networks
- Authors: Chenxi Wu, Min Zhu, Qinyang Tan, Yadhu Kartha, Lu Lu
- Year and publication or preprint version: 2023, Computer Methods in Applied Mechanics and Engineering 403:115671; preprint arXiv:2207.10289v1
- DOI or source URL: https://doi.org/10.1016/j.cma.2022.115671 ; preprint https://arxiv.org/abs/2207.10289
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted full-text read); not yet independently read by a human member
- Access: full text; abstract, method list, default settings, and main findings read
- Local file: `downloads/wu-2023-adaptive-sampling/wu-2023-adaptive-sampling.pdf`, SHA-256 d09a85ce0b317dde5911b185b2703d7dfbfe6a7f995ff8d8fbc99d0196f3801a

Crossref cited-by count 762 (checked 2026-11-17).

## Question and setting

Compares ten ways to place PINN residual points: six fixed uniform schemes (grid, random, Latin hypercube, Halton, Hammersley, Sobol), random resampling, and adaptive schemes (RAR, RAD, RAR-D), on forward and inverse problems including diffusion and diffusion-reaction.

## Claims we may use

- Main-findings list after the forward-problem results: RAD was best across their problems; for smooth solutions such as the diffusion equation, uniform methods like Hammersley and random resampling "also produce sufficiently low errors".
- Among fixed point sets, low-discrepancy sequences beat random and Latin hypercube, and all beat the equispaced grid.
- Default adaptive settings: RAD with k = 1, c = 1; RAR-D with k = 2, c = 0.

## Relevance to this project

Our main problem has smooth solutions for each parameter setting, so random resampling or a low-discrepancy set is the expected default, and adaptive sampling stays a contingency. Grid-placed collocation points are a weak choice and should be avoided. Adaptive sampling adds residual evaluations on a candidate pool, which is training energy we would have to count.

## Check status and gaps

DOI, journal, volume, and article number confirmed via Crossref. Per-problem error tables were not transcribed.
