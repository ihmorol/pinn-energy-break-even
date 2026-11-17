# Wang, Wang, Perdikaris (2021): physics-informed DeepONets for parametric PDEs

## Source

- Title: Learning the solution operator of parametric partial differential equations with physics-informed DeepONets
- Authors: Sifan Wang, Hanwen Wang, Paris Perdikaris
- Year and publication or preprint version: 2021, Science Advances 7(40):eabi8605; preprint arXiv:2103.10974
- DOI or source URL: https://doi.org/10.1126/sciadv.abi8605
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text (open access) not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 1436 (checked 2026-11-17).

## Question and setting

Trains a DeepONet with a PDE-residual loss so it learns the solution operator of a parametric PDE without paired input-output data from a solver. Tested on "various types of parametric PDEs". Cost is reported as prediction speed against conventional solvers; no energy.

## Claims we may use

- The framework learns solution operators "even in the absence of any paired input-output training data". Abstract.
- Trained models predict solutions of parametric PDEs "up to three orders of magnitude faster compared to conventional PDE solvers". Abstract. This is per-query speed after training.

## Relevance to this project

Peer-reviewed precedent for the setup our PINN uses: physics-only training across a parameter family, with no solver-generated data. So the parametric PINN is not our contribution; the measured break-even is. The paper's speed claim is the per-query side (e_P against e_C) of our model. Whether its training cost is paid back is not stated in the abstract, which is the question our study measures.

## Check status and gaps

Venue, issue, and DOI confirmed in Crossref. The PDEs, hardware, baseline solvers, training times, and whether the "three orders" figure includes training were not read; read the full text before quoting. This is an operator network, not the plain MLP PINN in our plan.
