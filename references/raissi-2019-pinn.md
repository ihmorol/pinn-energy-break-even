# Raissi, Perdikaris, Karniadakis (2019): Physics-informed neural networks (foundational)

## Source

- Title: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations
- Authors: M. Raissi, P. Perdikaris, G.E. Karniadakis
- Year and publication or preprint version: 2019, Journal of Computational Physics 378:686-707 (online 2018-11-03)
- DOI or source URL: https://doi.org/10.1016/j.jcp.2018.10.045
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and metadata of the published paper; the locally stored PDF is the 2017 preprint pair part "Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations" (arXiv:1711.10561v1), not the published JCP text
- Local file: `downloads/raissi-2019-pinn/raissi-2019-pinn.pdf`, SHA-256 2a8db6776a110a4f36bd1e36af79cf31a2e74baa5af8f7ee3d9286a75fdc400d (this is the Part I preprint)

OpenAlex cited_by_count 22,929; Crossref 20,966 (checked 2026-11-12). The published JCP text has no arXiv version of its own; arXiv:1711.10561 and 1711.10566 are the ancestor preprint pair.

## Question and setting

The foundational PINN paper: neural networks trained to fit data while their outputs satisfy a PDE residual through automatic differentiation, covering forward and inverse problems for nonlinear PDEs in continuous- and discrete-time forms.

## Claims we may use

- PINNs encode PDEs as soft constraints in the training loss and serve as data-efficient function approximators that can solve forward and inverse problems. Abstract of the published paper and Part I preprint.
- Citation level: this is the standard foundational reference for the PINN method we implement in the pilot.

## Relevance to this project

Defines the method under test in our parametric PINN. When we cite the method's origin, this is the reference. No measurement or cost claim is taken from this paper.

## Check status and gaps

Verified against Crossref (DOI, journal, volume, pages) and OpenAlex. Gaps: we have read the abstract only, and the local PDF is the preprint pair part, not the published text. If a specific equation or architecture detail from the published version is needed, obtain library access or read the accepted manuscript before citing that detail.
