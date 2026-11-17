# Sukumar and Srivastava (2022): Exact boundary conditions with distance functions

## Source

- Title: Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks
- Authors: N. Sukumar, Ankit Srivastava
- Year and publication or preprint version: 2022, Computer Methods in Applied Mechanics and Engineering 389:114333; preprint arXiv:2104.08426v2
- DOI or source URL: https://doi.org/10.1016/j.cma.2021.114333 ; preprint https://arxiv.org/abs/2104.08426
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted read); not yet independently read by a human member
- Access: abstract and contribution list read in full text; constructions and examples not read in detail
- Local file: `downloads/sukumar-2022-exact-bc/sukumar-2022-exact-bc.pdf`, SHA-256 de6dcaead2eb08e773494ccc777878f34199fcd550c0d69af6da1c507a5a3a65

Crossref cited-by count 478 (checked 2026-11-17).

## Question and setting

How to satisfy boundary conditions exactly in a PINN by building them into the trial function, so no boundary loss term is needed.

## Claims we may use

- Abstract: for homogeneous Dirichlet conditions, the trial function is an approximate distance function phi(x) times the network output; transfinite interpolation extends this to inhomogeneous Dirichlet, Neumann, and Robin conditions.
- Abstract: doing so removes the modeling error from soft boundary penalties.

## Relevance to this project

Our square domain with fixed Dirichlet data is the simplest case for this idea: u = g + d(x, y) N(x, y, theta) with d = x(1-x)y(1-y) or a normalized version, and g a smooth lift of the boundary data. This removes the boundary term and the loss weight, which the gradient-pathology and NTK papers name as a main cause of failure. The choice of d changes the residual scale and so the training; we keep it fixed and recorded.

## Check status and gaps

DOI, journal, and volume confirmed via Crossref. The detailed distance-function constructions and their accuracy results were not read; do not quote them yet.
