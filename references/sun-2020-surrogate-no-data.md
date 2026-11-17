# Sun, Gao, Pan, Wang (2020): Parametric surrogate without simulation data

## Source

- Title: Surrogate Modeling for Fluid Flows Based on Physics-Constrained Deep Learning Without Simulation Data
- Authors: Luning Sun, Han Gao, Shaowu Pan, Jian-Xun Wang
- Year and publication or preprint version: 2020, Computer Methods in Applied Mechanics and Engineering 361:112732; preprint arXiv:1906.02382v2
- DOI or source URL: https://doi.org/10.1016/j.cma.2019.112732 ; preprint https://arxiv.org/abs/1906.02382
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted read); not yet independently read by a human member
- Access: full text; Sections 1 to 3 (setup, boundary handling, training settings) read; results not read in detail
- Local file: `downloads/sun-2020-surrogate-no-data/sun-2020-surrogate-no-data.pdf`, SHA-256 fe779a5dc470f9578a72416f08a15c601175c0dc8c0f7be98ce4227d4f3fd685

## Question and setting

A physics-constrained network trained over a parameter space with no solver data. The input layer holds time, space, and the varying parameters (Section 2), which is the same structure as our planned parametric PINN.

## Claims we may use

- Section 2.1: inputs are (t, x, theta); one network covers the parameter range without simulation data.
- Section 2.3: soft boundary penalties need weights that are hard to choose; Dirichlet and initial conditions are imposed in a hard way by construction, and Neumann conditions stay in the loss.
- Section 3 (opening): three sub-networks with 3 hidden layers of 20 neurons each, Swish activation, Adam with learning rate 1e-3 and mini-batch size 50.
- Section 4.1 is titled "Pitfall on Using Soft Boundary Enforcement" (heading read; body not read in detail).

## Relevance to this project

An early, peer-reviewed example of the exact design we plan: parameters as network inputs, no labeled data, hard Dirichlet conditions. With no solver data, the data-generation term in the Huang et al. amortization law is zero for the PINN, so N* is not tied to a training-set size. Any validation data we use does cost classical solves, and those belong in S_P.

## Check status and gaps

Journal, volume, article number, and DOI from the arXiv journal reference field. Results and accuracy levels not transcribed.
