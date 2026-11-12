# Wang, Teng, Perdikaris (2021): Understanding and mitigating gradient pathologies

## Source

- Title: Understanding and mitigating gradient pathologies in physics-informed neural networks (SIAM title: Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks)
- Authors: Sifan Wang, Yujun Teng, Paris Perdikaris
- Year and publication or preprint version: 2021, SIAM Journal on Scientific Computing 43(5):A3055-A3081; preprint arXiv:2001.04536v1 (2020-01-13)
- DOI or source URL: https://doi.org/10.1137/20M1318043 ; preprint https://arxiv.org/abs/2001.04536
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/wang-2021-gradient-pathologies/wang-2021-gradient-pathologies.pdf`, SHA-256 937e4f3610d52f283e124492ec836740dba6cdb0390ff3919a583d25be2b3881

OpenAlex cited_by_count 2,719 (checked 2026-11-12). Note: Crossref and OpenAlex give pages A3055-A3081; an earlier draft of our shortlist said A3053, corrected here.

## Question and setting

Identifies numerical stiffness as a failure mode of PINN training: unbalanced back-propagated gradients across loss terms. Proposes a learning-rate annealing algorithm driven by gradient statistics and a modified MLP architecture more resilient to gradient pathologies.

## Claims we may use

- A fundamental PINN failure mode comes from numerical stiffness that makes the composite loss terms compete during training. Abstract.
- The proposed learning-rate annealing and architecture changes improve predictive accuracy by a factor of 50 to 100x across a range of computational physics problems. Abstract.
- Relevance to budgeting: mitigation methods change how long training takes; if we adopt any such mitigation in the pilot, the tuning and retraining cost belongs in the study ledger and the deployment estimate.

## Relevance to this project

A second, independent account of why PINN training cost is unstable and method-sensitive. It supports our decision to freeze the training recipe before energy trials and to record every retraining as study electricity. If the pilot hits stiffness-type failures, this paper suggests the mitigation options that stay inside our fixed scope.

## Check status and gaps

Journal, volume, pages, DOI, and preprint verified via Crossref and the arXiv API. Gaps: abstract-level access only; the 50-100x accuracy figure is the authors' own claim, to be quoted with attribution and not generalized to our problem without our own measurements.
