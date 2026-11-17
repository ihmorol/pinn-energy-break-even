# De Ryck et al. (2024): An operator preconditioning perspective on PINN training

## Source

- Title: An operator preconditioning perspective on training in physics-informed machine learning
- Authors: Tim De Ryck, Florent Bonnet, Siddhartha Mishra, Emmanuel de Bézenac
- Year and publication or preprint version: 2024, ICLR 2024 conference paper (stated on the PDF); preprint arXiv:2310.05801v2
- DOI or source URL: https://arxiv.org/abs/2310.05801
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted full-text read); not yet independently read by a human member
- Access: full text; abstract, Section 2 theorems, and the discussion of the loss weight and optimizers read; proofs not checked
- Local file: `downloads/deryck-2024-operator-preconditioning/deryck-2024-operator-preconditioning.pdf`, SHA-256 86315edbdf52795f00efa0873febda206cf4118c511ec58a75ca4967bffec102

## Question and setting

Theory and experiments on why gradient descent is slow for physics-informed losses. The main object is the condition number of an operator built from the Hermitian square of the PDE operator.

## Claims we may use

- Abstract: training difficulty "is closely related to the conditioning of a specific differential operator"; if it is ill-conditioned, training is slow or infeasible.
- Theorem 2.3: in the simplified (linearized) setting, the iterations to reach tolerance epsilon grow as O(kappa(A) ln(1/epsilon)).
- Paragraph "Choice of lambda": the boundary-versus-residual loss weight changes the conditioning.
- Same discussion: (quasi-)Newton methods act as automatic preconditioners in this setting.

## Relevance to this project

Gives a reason to expect training cost to grow as the accuracy target tightens (the ln(1/epsilon) factor) and as the conductivity contrast grows (larger condition number). That is a direct hypothesis for how S_P should move between the 1e-2 and 1e-3 targets and across the parameter box. The result is for a linearized model; we treat it as a prediction to check, not a law.

## Check status and gaps

Identifier, title, and authors confirmed via the arXiv API; venue from the PDF. Proofs and the numerical sections were not checked in detail.
