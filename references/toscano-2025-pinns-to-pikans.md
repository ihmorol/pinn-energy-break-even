# Toscano et al. (2025): From PINNs to PIKANs

## Source

- Title: From PINNs to PIKANs: recent advances in physics-informed machine learning
- Authors: Juan Diego Toscano, Vivek Oommen, Alan John Varghese, Zongren Zou, Nazanin Ahmadi Daryakenari, Chenxi Wu, George Em Karniadakis
- Year and publication or preprint version: 2025, Machine Learning for Computational Science and Engineering 1(1), article 15 (online 2025-03-11)
- DOI or source URL: https://doi.org/10.1007/s44379-025-00015-1 ; open copy https://pmc.ncbi.nlm.nih.gov/articles/PMC13290273/
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata; PMC full text read in part (first 100k of about 372k characters) through a page reader.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 403 (checked 2026-11-17).

## Question and setting

A review of recent PINN advances: training methods, architectures, physics-informed Kolmogorov-Arnold networks (PIKANs), applications, and software. From the same group as Karniadakis et al. 2021.

## Claims we may use

- Automatic differentiation "significantly increases computational cost due to the need for calculating and multiplying gradients at each layer". Section 3.2.1.
- Finite-difference derivatives inside PINNs speed up computation but rely "on a predefined grid, limiting its broader applicability". Section 3.2.1.
- In the part read, the review gives no head-to-head runtime comparison of PINNs with FEM or finite differences, and no discussion of energy use.

## Relevance to this project

The most cited recent PINN review, and the up-to-date companion to Karniadakis et al. 2021 for the introduction. Its Section 3.2.1 point about autodiff cost supports measuring PINN training energy rather than assuming it is small. Within the part read, it also supports our gap: a leading 2025 review does not compare PINN cost against classical solvers.

## Check status and gaps

Venue, volume, article number, and DOI confirmed in Crossref. About 70% of the full text was not read, so the "no head-to-head comparison" and "no energy" observations hold only for the part read; check the rest before stating them in the report.
