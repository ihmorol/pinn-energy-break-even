# de Hoop, Huang, Qian, Stuart (2022): Cost-accuracy trade-off in operator learning

## Source

- Title: The Cost-Accuracy Trade-Off In Operator Learning With Neural Networks
- Authors: Maarten V. de Hoop, Daniel Zhengyu Huang, Elizabeth Qian, Andrew M. Stuart
- Year and publication or preprint version: 2022, Journal of Machine Learning 1(1):299-341; preprint arXiv:2203.13181v3
- DOI or source URL: https://doi.org/10.4208/jml.220509 ; preprint https://arxiv.org/abs/2203.13181
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/dehoop-2022-cost-accuracy/dehoop-2022-cost-accuracy.pdf`, SHA-256 4641ee8e7d1172274f5d5ee2c4b3cad45562c5c3d8bea85264c8bfefdf089a50

OpenAlex cited_by_count 107 (merged record; Crossref 44; checked 2026-11-12).

## Question and setting

Formal framework for judging parametric PDE surrogates by the cost needed to reach a given accuracy, aimed at many-query computations (optimization, uncertainty quantification). Establishes a structure for comparing neural-operator and classical approaches on cost versus accuracy rather than accuracy alone.

## Claims we may use

- The relative merit of surrogate approaches should be evaluated by the cost required to achieve a given accuracy level; the paper states the field lacked a rigorous framework for this before its analysis. Abstract.
- Cost-accuracy analysis is the accepted frame for many-query surrogate evaluation. Framing of the abstract.

## Relevance to this project

Supplies the general frame that our break-even study fills in with metered electricity: our E_P(N) and E_C(N) curves are a cost-accuracy trade-off evaluated at fixed accuracy targets, with energy and runtime as the cost axes. Cite it when we define why matched accuracy is the fair comparison basis.

## Check status and gaps

Journal, volume, pages, DOI, and preprint verified via Crossref and the arXiv API. Gaps: abstract-level access only. Its theoretical results were not read; cite it for the framing, not for specific quantitative claims.
