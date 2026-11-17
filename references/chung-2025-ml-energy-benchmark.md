# Chung et al. (2025): the ML.ENERGY Benchmark

## Source

- Title: The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization
- Authors: Jae-Won Chung, Jeff J. Ma, Ruofan Wu, Jiachen Liu, Oh Jun Kweon, Yuxuan Xia, Zhiyu Wu, Mosharaf Chowdhury
- Year and publication or preprint version: 2025, Advances in Neural Information Processing Systems 38 (NeurIPS 2025, Datasets and Benchmarks Track), pp. 121191-121219; preprint arXiv:2505.06371
- DOI or source URL: https://doi.org/10.52202/085713-3652
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 85 (checked 2026-11-17).

## Question and setting

A benchmark suite and open tool for measuring inference energy of ML models in realistic serving conditions. The early 2025 results cover 40 model architectures across 6 tasks, mostly generative AI. Not about PDE solvers.

## Claims we may use

- Energy "remains a metric that is often overlooked, under-explored, or poorly understood" in building ML systems. Abstract.
- The paper states "four key design principles for benchmarking ML energy" and how the benchmark implements them. Abstract (the principles themselves were not read).
- Automated optimization recommendations can give "significant (sometimes more than 40%) energy savings without changing what is being computed by the model". Abstract.

## Relevance to this project

The newest peer-reviewed reference on how to measure inference energy, which is our per-query cost e_P. Its result that settings alone can change energy by more than 40% without changing the computation is a direct reason to freeze and record batch size, precision, and device settings for both methods before the energy trials. The open tool may be usable for GPU readings in the pilot; check it against the sampling caveats in Yang et al. 2024.

## Check status and gaps

Venue, pages, and DOI confirmed in Crossref. The four design principles, the measurement tool it uses, and how it handles GPU sensor sampling were not read. Read Sections 2 and 3 before citing any principle or adopting the tool.
