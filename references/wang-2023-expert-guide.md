# Wang, Sankaran, Wang, Perdikaris (2023): An expert's guide to training PINNs

## Source

- Title: An Expert's Guide to Training Physics-informed Neural Networks
- Authors: Sifan Wang, Shyam Sankaran, Hanwen Wang, Paris Perdikaris
- Year and publication or preprint version: 2023 preprint, arXiv:2308.08468v1 (2023-08-16); no journal reference on the arXiv record at check date
- DOI or source URL: https://arxiv.org/abs/2308.08468
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted full-text read); not yet independently read by a human member
- Access: full text; Sections 3 to 6 and Algorithm 1 read closely, Section 7 results skimmed
- Local file: `downloads/wang-2023-expert-guide/wang-2023-expert-guide.pdf`, SHA-256 afae5ab4ddf2a59b5fdf00516d0145ab1d0b09491e8d03e32be77610efbe0348

## Question and setting

A practical training recipe for PINNs from the group behind the gradient-pathology and NTK papers. It collects defaults for scaling, architecture, loss weighting, sampling, optimizer, and boundary handling, then tests them on time-dependent and flow benchmarks. It does not study parametric families or cost against a classical solver.

## Claims we may use

- Algorithm 1 (p. 4) is a full training pipeline: non-dimensionalize, MLP with tanh and Glorot init, weighted loss, random sampling each step, global weights from gradient norms every f steps with a moving average. Stated defaults: f = 1,000, alpha = 0.9, epsilon = 1.0. Weights are not back-propagated.
- Section 3: scale inputs and outputs to order one, because standard initialization assumes moderate input ranges and unbalanced scales slow training.
- Section 4.1: recommended width 128 to 512 and depth 3 to 6; tanh; "ReLU is not suitable since its second-order derivative is zero".
- Section 5.2: gradient-norm loss balancing (Eqs. 2.12-2.15); extra cost is small when updates are infrequent.
- Section 6.1: Adam with initial learning rate 1e-3 and exponential decay; weight decay is not recommended for forward problems.
- Section 6.2: random resampling of collocation points; full-batch training "may result in over-fitting the PDE residuals".
- Sections 4.2 and 4.3: Fourier features (scale sigma in [1, 10]) and random weight factorization (mu = 1.0, sigma = 0.1) as optional upgrades.

## Relevance to this project

This is the most complete published recipe for the PINN side. We use it for the default Adam settings, input scaling, resampling, and the loss-balancing fallback. Its width range is aimed at harder problems than our smooth steady diffusion; it is an upper bracket, not our choice. Every extra feature (Fourier features, weight factorization, adaptive weights) adds tuning runs, which the study ledger must hold.

## Check status and gaps

Identifier and title confirmed via the arXiv API. Unrefereed preprint at check date; re-check for a published version before the final report. Section 7 per-problem errors were not transcribed.
