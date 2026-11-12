# Wilson et al. (2025): Performance-carbon trade-offs in shear flow forecasting

## Source

- Title: Performance-Carbon Trade-Offs across Architectural Biases in Shear Flow Forecasting
- Authors: Sophia N. Wilson, Jens Hesselbjerg Christensen, Raghavendra Selvan
- Year and publication or preprint version: 2025 preprint, arXiv:2509.24517v3 (submitted 2025-09-29)
- DOI or source URL: https://arxiv.org/abs/2509.24517
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/wilson-2025-carbon-forecasting/wilson-2025-carbon-forecasting.pdf`, SHA-256 cded76c3ee4a52639c4b9473472f60e04e4328f915db015f5f77b5ac843810d0

OpenAlex: 0 citing works (checked 2026-11-12). arXiv-only at check date; same Copenhagen group as the EcoL2 paper, which it cites.

## Question and setting

Evaluates seven spatio-temporal forecasting models for incompressible shear flow, differing in receptive field and periodicity bias, on pointwise accuracy, physics fidelity, and carbon cost across both training and inference.

## Claims we may use

- No single model dominated on both predictive performance and carbon cost. Abstract.
- A lower training cost did not straightforwardly extend to inference. Abstract.
- Runtime alone is an unreliable proxy for carbon cost, particularly during training. Abstract.

## Relevance to this project

The third finding is a direct methodological warning for us: our plan measures energy and runtime separately and reports both break-even points, and this paper gives a recent PDE-context reason why. Its second finding supports our choice to measure per-query inference cost independently of training cost rather than infer one from the other.

## Check status and gaps

Preprint verified via the arXiv API. Gaps: abstract-level access only; whether its carbon numbers are counter-measured or modeled was not read. Re-check for a published venue before the final report.
