# Huang and Stuart (2026): Cost-accuracy trade-offs, neural operator vs classical solver

## Source

- Title: Cost-Accuracy Trade-offs: Neural Operator vs Classical Numerical Solver
- Authors: Daniel Zhengyu Huang, Andrew M. Stuart
- Year and publication or preprint version: 2026 preprint, arXiv:2609.24021v1 (submitted 2026-09-21)
- DOI or source URL: https://arxiv.org/abs/2609.24021
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/huang-stuart-2026-cost-accuracy/huang-stuart-2026-cost-accuracy.pdf`, SHA-256 f9d8c715616a53f9fe325d9ace826b33409431b4875fd964b82ffab4b217024e

OpenAlex: 1 citing work (recent preprint; checked 2026-11-12). Same first author as the Huang et al. 2026 review; the two form one research line.

## Question and setting

Reproducible benchmark comparing neural operator surrogates with problem-matched classical solvers in the post-training, many-query limit, where data acquisition and training costs are treated as fixed and fully amortized. Cost measures: prediction error, per-query floating-point cost, and wall-clock runtime. No electricity measurement.

## Claims we may use

- Even in the deliberately favorable amortized regime, there are regimes where classical solvers outperform the surrogates. Abstract.
- Neural operators are most competitive at low-to-moderate accuracy requirements; as the target accuracy tightens, classical solvers outperform them. Abstract.
- The floating-point cost advantage depends strongly on problem structure: it arises when surrogates avoid temporal or nonlinear iterations or predict a reduced quantity of interest rather than a full field. Abstract.
- Classical solvers will remain important for verification and high-accuracy computation. Abstract.

## Relevance to this project

This is the closest published design analog to our experiment: parameterized PDE, many-query setting, problem-matched classical solver, matched-accuracy comparison. It differs in three ways our study covers: it amortizes training cost away entirely (we measure it), it uses operator networks (we use a PINN trained across the parameter family), and it measures runtime and FLOPs but not electricity. Its finding that the accuracy target decides the winner is a direct hypothesis for our 1 percent versus 0.1 percent targets.

## Check status and gaps

Preprint verified via the arXiv API (title, authors, date). Gaps: abstract-level access only; the benchmark problems and measured regimes were not transcribed. Treat as unrefereed work.
