# Chatain et al. (2025): Numerical PDE solvers outperform neural PDE solvers

## Source

- Title: Numerical PDE solvers outperform neural PDE solvers
- Authors: Patrick Chatain, Michael Rizvi-Martel, Guillaume Rabusseau, Adam Oberman
- Year and publication or preprint version: 2025 preprint, arXiv:2507.21269v1 (submitted 2025-07-28)
- DOI or source URL: https://arxiv.org/abs/2507.21269
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/chatain-2025-numeric-outperform/chatain-2025-numeric-outperform.pdf`, SHA-256 df5693b2aa200d0dc39349bca8d0a779772d79fc6d9d3b45c2b380c7cab97ab4

OpenAlex: 4 citing works (checked 2026-11-12). arXiv-only at check date.

## Question and setting

DeepFDM: a differentiable finite-difference framework that embeds a classical forward-Euler discretization in a convolutional architecture, with CFL-compliant coefficient parameterizations, evaluated on advection, diffusion, advection-diffusion, reaction-diffusion, and inhomogeneous Burgers equations in 1D to 3D against Fourier neural operators, U-Nets, and ResNets.

## Claims we may use

- DeepFDM reaches normalized mean-squared errors one to two orders of magnitude smaller than the tested neural solvers, with 10 to 20 times fewer training epochs and 5 to 50 times fewer parameters, in and out of distribution. Abstract.
- Embedding classical discretization structure into learning reduces training cost substantially relative to generic neural solvers. Authors' interpretation of their results.

## Relevance to this project

Recent evidence that classical structure lowers the cost of learned solvers. It supports our framing that the interesting question is not learned versus classical as a binary, but where the cost lines cross under controlled conditions. It is a training-cost-side (epochs, parameters) comparison, not an energy measurement.

## Check status and gaps

Preprint verified via the arXiv API. Gaps: abstract-level access only; arXiv-only at check date, so re-check for a published venue before the final report cites it.
