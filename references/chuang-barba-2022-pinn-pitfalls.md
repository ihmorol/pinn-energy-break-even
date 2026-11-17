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
