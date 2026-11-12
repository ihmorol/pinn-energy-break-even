# Kapoor et al. (2025): EcoL2 metric for sustainable neural PDE solvers

## Source

- Title: Beyond Accuracy: EcoL2 Metric for Sustainable Neural PDE Solvers
- Authors: Taniya Kapoor, Abhishek Chandra, Anastasios Stamou, Stephen J. Roberts
- Year and publication or preprint version: 2025 preprint, arXiv:2505.12556v1 (submitted 2025-05-18)
- DOI or source URL: https://arxiv.org/abs/2505.12556
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/kapoor-2025-ecol2/kapoor-2025-ecol2.pdf`, SHA-256 f868de2fd519b7c0b25d0c12264885d10a0cfa5e1231ccc0ad2c82360c31b7a0

OpenAlex: 3 citing works (checked 2026-11-12). No journal or conference record found at check date; arXiv-only.

## Question and setting

Proposes EcoL2, a metric that balances solution accuracy (relative L2 error) against carbon emissions across the solver lifecycle: data collection, model training, and deployment. Evaluated on physics-informed ML and operator-learning architectures.

## Claims we may use

- A combined accuracy-plus-emissions metric for neural PDE solvers exists and has been applied across both PINN-style and operator-learning models. Abstract.
- The paper treats data collection, training, and deployment as the three lifecycle stages that carry emission cost, matching the cost separation our plan requires. Abstract framing.

## Relevance to this project

The nearest published attempt at exactly our scoring idea for PDE solvers: accuracy and environmental cost together. Our study differs by measuring electricity per phase and reporting a break-even query count instead of collapsing the trade into one scalar metric. If the final report discusses how to weigh accuracy against energy, this is the prior to cite.

## Check status and gaps

Preprint verified via the arXiv API. Gaps: abstract-level access only. The exact EcoL2 formula and the measurement approach behind its emission numbers were not read; before using this metric as a comparison point, read the full text and check whether its emissions are measured or modeled.
