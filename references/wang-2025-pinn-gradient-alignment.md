# Wang, Bhartari, Li, Perdikaris (2025): gradient alignment and second-order training for PINNs

## Source

- Title: Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective
- Authors: Sifan Wang, Ananyae Bhartari, Bowen Li, Paris Perdikaris
- Year and publication or preprint version: 2025, Advances in Neural Information Processing Systems 38 (NeurIPS 2025), pp. 186682-186732; preprint arXiv:2502.00604
- DOI or source URL: https://doi.org/10.52202/085713-5615
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 159 (checked 2026-11-17).

## Question and setting

Why composite PINN losses (residual plus boundary terms) train poorly with first-order optimizers, and whether second-order optimization fixes it. Tested on 10 PDE benchmarks, including turbulent flow. Cost is not the focus; no energy and no classical-solver comparison in the abstract.

## Claims we may use

- Directional conflicts between loss terms limit first-order methods; second-order optimization "naturally resolves them through implicit gradient alignment". Abstract.
- SOAP, a quasi-Newton method, gives "state-of-the-art results on 10 challenging PDE benchmarks" with "2-10x accuracy improvements over existing methods". Abstract.

## Relevance to this project

This is the most recent peer-reviewed state of the art for PINN training. It matters for fairness in both directions: McGreivy and Hakim ask for an efficient classical baseline, and a reviewer can equally ask whether our PINN was trained with a current method. If the pilot PINN misses the 1e-3 target with Adam or L-BFGS, this paper is the reason to try a second-order optimizer such as SOAP before recording the miss as a result, inside the frozen training budget. Optimizer choice changes training time and energy, so it is part of S_P and must be frozen and logged.

## Check status and gaps

Venue, pages, and DOI confirmed in Crossref. Training cost, wall-clock time per step, hardware, and the benchmark list were not read. Whether SOAP's extra per-step cost is reported was not checked; read the full text before choosing it for the pilot.
