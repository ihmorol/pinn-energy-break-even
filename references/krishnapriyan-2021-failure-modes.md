# Krishnapriyan et al. (2021): Characterizing possible failure modes in PINNs

## Source

- Title: Characterizing possible failure modes in physics-informed neural networks
- Authors: Aditi Krishnapriyan, Amir Gholami, Shandian Zhe, Robert Kirby, Michael W. Mahoney
- Year and publication or preprint version: 2021, Advances in Neural Information Processing Systems 34 (NeurIPS 2021); preprint arXiv:2109.01050v2
- DOI or source URL: NeurIPS 2021 proceedings entry (main track, proceedings.neurips.cc); preprint https://arxiv.org/abs/2109.01050
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/krishnapriyan-2021-failure-modes/krishnapriyan-2021-failure-modes.pdf`, SHA-256 677417a271d24f3927090dfc3a1f5430baeb8d9d2943652d06639cd4db7fc30a

OpenAlex cited_by_count 574 (arXiv-merged record; checked 2026-11-12). The NeurIPS 2021 proceedings entry exists (proceedings.neurips.cc, paper 2021).

## Question and setting

Shows that PINNs can learn trivial problems but easily fail on slightly more complex ones, including convection, reaction, and diffusion equations. Attributes failures to the soft PDE constraint making the loss landscape hard to optimize and the problem more ill-conditioned, not to limited network expressivity. Proposes curriculum regularization and a sequence-to-sequence reformulation.

## Claims we may use

- PINN failures on diffusion-type problems come from the optimization structure of the soft-constraint loss, not from network capacity. Abstract.
- Curriculum regularization and sequence-to-sequence reformulation reach up to one to two orders of magnitude lower error than regular PINN training in their tests. Abstract.
- Consequence for our gate: before any energy trial, both methods must pass the accuracy check on held-out parameters; this paper is the warning that the PINN may fail that gate for some parameter ranges, which the plan already treats as a reportable outcome.

## Relevance to this project

Our main problem is steady diffusion, a close cousin of the diffusion operators where they document failures. This paper motivates the accuracy gate in Section 3 of the research plan and gives us concrete, in-scope mitigation candidates if the parametric PINN struggles at the 1 percent target.

## Check status and gaps

Venue confirmed through the NeurIPS 2021 proceedings location (OpenAlex). Gaps: abstract-level access only; do not quote the exact operator families or error tables until the full text is read. The proceedings DOI was not recorded; add it when the note is next updated.
