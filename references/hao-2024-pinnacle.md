# Hao et al. (2024): PINNacle benchmark

## Source

- Title: PINNacle: A Comprehensive Benchmark of Physics-Informed Neural Networks for Solving PDEs
- Authors: Zhongkai Hao, Jiachen Yao, Chang Su, Hang Su, Ziao Wang, Fanzhi Lu, Zeyu Xia, Yichi Zhang, Songming Liu, Lu Lu, Jun Zhu
- Year and publication or preprint version: 2024, Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Datasets and Benchmarks Track, pp. 76721-76774; preprint arXiv:2306.08827v2
- DOI or source URL: https://doi.org/10.52202/079017-2442 ; proceedings PDF at https://proceedings.neurips.cc/paper_files/paper/2024/ (D&B track); preprint https://arxiv.org/abs/2306.08827
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/hao-2024-pinnacle/hao-2024-pinnacle.pdf`, SHA-256 69de485e67c6e85b12057300a06004edfd7b0b0ed3bc05550a0bf266af99cf6b

OpenAlex cited_by_count 132; Crossref 43 (checked 2026-11-12). Correction recorded: an earlier attribution of this benchmark to Marin, Errica, Barla, and Bacci and to NeurIPS 2023 was wrong; the verified authors are Hao et al. and the venue is NeurIPS 2024 D&B. A similarly named work, "PINNACLE" by Lau et al. (arXiv:2404.07662), is a different paper.

## Question and setting

Benchmarking tool with more than 20 PDE problem families (including heat conduction, fluid dynamics, biology, electromagnetics) and about 10 state-of-the-art PINN variants, run under matched conditions with a shared evaluation protocol.

## Claims we may use

- Cross-method PINN comparisons under a single benchmark report variable strengths and weaknesses per problem family. Abstract.
- Design lessons for matched-condition comparisons: fixed problem suites, shared error metrics, and consistent training budgets are the basis for any fair cost statement. Framing from the abstract's purpose statement.

## Relevance to this project

Not a template to extend (our scope is fixed at one 2D problem), but a design reference for how we hold conditions fixed between our two methods: same parameters, same output grid, same accuracy metric, recorded budgets. It also supports our claim that systematic matched-condition comparisons are recent and scarce.

## Check status and gaps

DOI, venue, pages, and preprint verified via Crossref and the arXiv API. Gaps: abstract-level access only; read the heat-conduction results before quoting any per-problem PINN performance from PINNacle.
