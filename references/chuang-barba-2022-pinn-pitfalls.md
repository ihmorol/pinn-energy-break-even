# Chuang and Barba (2022): PINN pitfalls against a finite-difference solver

## Source

- Title: Experience report of physics-informed neural networks in fluid simulations: pitfalls and frustration
- Authors: Pi-Yueh Chuang, Lorena A. Barba
- Year and publication or preprint version: 2022, Proceedings of the 21st Python in Science Conference (SciPy 2022), pp. 28-36; preprint arXiv:2205.14249
- DOI or source URL: https://doi.org/10.25080/majora-212e5952-005 ; open copy http://conference.scipy.org/proceedings/scipy2022/pdfs/PiYueh_Chuang.pdf
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 67 (checked 2026-11-17).

## Question and setting

Data-free PINNs used as a replacement for a traditional CFD solver on the 2D Navier-Stokes equations: Taylor-Green vortex at Re = 100 and cylinder flow at Re = 200. The abstract compares against a finite-difference simulation; the specific solver code was not confirmed from the paper. Single solves, not a parameter family. Cost is training and run time; no energy.

## Claims we may use

- "About 32 hours of training were required for the PINN method's accuracy to match the accuracy of a 16 × 16 finite-difference simulation, which took less than 20 seconds." Abstract.
- For the cylinder flow, the PINN "did not produce a physical solution" and "behaved like a steady-flow solver". Abstract.
- The authors call the PINN method "still a work-in-progress", especially without given data. Abstract.

## Relevance to this project

A peer-reviewed PINN versus finite-difference comparison at matched accuracy, which is the same pairing as ours. It supports two points: training cost at matched accuracy can be several orders of magnitude above a classical solve, and PINN training can fail outright. Both feed the accuracy gate, the failure log, and the S_P term of our break-even model. It does not test a parameter family, so it says nothing about amortization.

## Check status and gaps

Venue, pages, and DOI confirmed in Crossref. Hardware, network size, and the exact accuracy metric were not read; get them from the full text before quoting the 32 hours against our setting. The problem is time-dependent Navier-Stokes, not steady diffusion.

## Full-text methods check, 2026-11-17

Reader: Claude Code AI agent; targeted read of the methods, setup, and cost passages through the Markdown cache (`scripts/to_markdown.py`). Not yet read by a human member. Source: arXiv:2205.14249 PDF, stored at `downloads/chuang-barba-2022-pinn-pitfalls/chuang-barba-2022-pinn-pitfalls.pdf`, SHA-256 cf4080c2a83f542b4a9ca9d76bb179dfeb8bdf202e310334f6673b6ddb4d74c1. The proceedings PDF was not compared line by line.

- Section 3 (Taylor-Green setup): PINN built with NVIDIA Modulus; 6 hidden layers of 256 neurons, SiLU activation, Adam with PyTorch defaults and an exponential learning-rate decay; trained up to 1 million iterations on A100 GPUs. The authors "did not conduct hyperparameter optimization, given the computational cost".
- Same section: 18,432 random residual points per iteration, drawn from 18,432,000 pre-generated points. Using more GPUs (more points per iteration) "did not accelerate the convergence".
- Same section: the PINN used single precision, the finite-difference code (PetIBM) double precision; the authors say this does not change their conclusions.
- Same section: training was stopped when they "considered that further training would not improve the accuracy", "without a quantitative criterion".
- Errors were measured on a 512 x 512 mesh against the analytical solution; the PINN matched the 16 x 16 finite-difference run.

Use for us: a stop rule must be quantitative and frozen; more points per step can cost energy without helping; state the floating-point type of both methods.
