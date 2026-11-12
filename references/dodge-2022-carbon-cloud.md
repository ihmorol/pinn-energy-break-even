# Dodge et al. (2022): Measuring the carbon intensity of AI in cloud instances

## Source

- Title: Measuring the Carbon Intensity of AI in Cloud Instances
- Authors: Jesse Dodge, Sebastian Prollo, Nicole Mitchell, Austin Waters, Will Buchanan, (full author list to confirm from the PDF)
- Year and publication or preprint version: 2022, ACM Conference on Fairness, Accountability, and Transparency (FAccT 2022); preprint arXiv:2206.05229v1
- DOI or source URL: https://doi.org/10.1145/3531146.3533234 (confirm from the PDF); preprint https://arxiv.org/abs/2206.05229
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/dodge-2022-carbon-cloud/dodge-2022-carbon-cloud.pdf`, SHA-256 f5ffcb4accc8b7b35def3cc110fb432bd1d36ec6552f42a29dc4c907e2e53264

OpenAlex cited_by_count 358 (checked 2026-11-12).

## Question and setting

Framework for measuring operational software carbon intensity, using location-based and time-specific marginal emissions per energy unit. Measures a set of NLP and vision models on Microsoft Azure, including pretraining a 6.1 billion parameter model, and evaluates region choice, time of day, and pause-on-high-intensity scheduling.

## Claims we may use

- Geographic region has a significant effect on carbon intensity for the same compute; choosing an appropriate region can have the largest operational emissions reduction impact. Abstract.
- Time of day also has a notable impact. Abstract.
- Carbon claims require location- and time-specific emissions data, not a single static factor. Abstract framing.

## Relevance to this project

Supports two protocol points: (1) any carbon number we derive from measured joules must state the grid factor, its region, and its time basis; (2) our single-machine study reports electricity in joules as the primary measured quantity, with carbon as a clearly labeled conversion. It also justifies recording operating conditions in run records.

## Check status and gaps

Preprint verified via the arXiv API; venue via OpenAlex. Gaps: abstract-level access only; confirm the full author list and the FAccT DOI from the PDF before the final report. This is a cloud-study paper; do not cite its kilogram figures for our single-machine measurements.
