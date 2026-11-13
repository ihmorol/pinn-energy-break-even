# Wang, Yu, Perdikaris (2022): When and why PINNs fail to train

## Source

- Title: When and why PINNs fail to train: A neural tangent kernel perspective
- Authors: Sifan Wang, Xinling Yu, Paris Perdikaris
- Year and publication or preprint version: 2022, Journal of Computational Physics 449:110768 (January 2022); preprint arXiv:2007.14527v1 (2020-07-28)
- DOI or source URL: https://doi.org/10.1016/j.jcp.2021.110768 ; preprint https://arxiv.org/abs/2007.14527
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/wang-2022-pinn-ntk-failure/wang-2022-pinn-ntk-failure.pdf`, SHA-256 d705ee59d92d888ee0f017e30c7b10ae538f2273408597bfbe8c0ba2f670c398

OpenAlex cited_by_count 1,839 (checked 2026-11-12). Do not confuse with arXiv:2001.04536, the different gradient-pathologies paper by overlapping authors.

## Question and setting

Training-dynamics analysis of PINNs through the neural tangent kernel: derivation of the PINN NTK, its infinite-width limit, the convergence-rate discrepancy between loss components, and an adaptive gradient descent algorithm that uses NTK eigenvalues to calibrate convergence.

## Claims we may use

- PINN training can fail to converge because the PDE residual and data loss components converge at very different rates; the NTK analysis explains this as a property of the kernel spectrum. Abstract.
- The authors propose an adaptive algorithm that uses NTK eigenvalues to balance convergence across loss terms. Abstract.
- Direct consequence for cost accounting: PINN training cost and seed-to-seed variance are not incidental; they reflect known optimization pathologies. Our protocol must log failed attempts and keep at least three seeds.

## Relevance to this project

Justifies the failure-logging and seed rules in our plan and explains why the PINN side of the break-even model carries setup and training cost with high variance. Supports framing training cost S_P as a measured quantity, not a constant.

## Check status and gaps

Journal, volume, article number, DOI, and preprint verified via Crossref and the arXiv API. Gaps: abstract-level access only; read the full text before quoting the specific pathologies (ill-conditioned NTK, imbalanced eigenspectrum) or the fix details in the report.
