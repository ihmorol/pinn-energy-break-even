# Yoo et al. (2026): Energy-efficient operation of neural operators for virtual sensing

## Source

- Title: Energy-efficient operation of neural operators for virtual sensing
- Authors: Jason Yoo, Samrendra Roy, Souvik Chakraborty, Syed Bahauddin Alam
- Year and publication or preprint version: 2026 preprint, arXiv:2609.30580v1 (submitted 2026-09-24)
- DOI or source URL: https://arxiv.org/abs/2609.30580
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/yoo-2026-energy-inference/yoo-2026-energy-inference.pdf`, SHA-256 29f1e7f0008af1142b9bcd990a1692e903458f4ed182d373fa542696fbadb34

OpenAlex: 1 citing work (checked 2026-11-12). arXiv-only at check date.

## Question and setting

Measures operating energy of DeepONet and Fourier neural operator virtual-sensing updates on a power-constrained device (15 W mode with fixed clocks), comparing eager execution, compiler freezing, trunk reuse, and graph replay, with preparation and artifact-construction costs kept outside the repeated-inference accounting.

## Claims we may use

- With fixed clocks at 15 W, reuse with graph replay completed the same request sequence with 22.0 to 22.5 percent less energy than eager execution, including preparation and waiting. Abstract.
- At one request per second the saving was about 1 percent; at forty requests per second about 20 percent. Abstract.
- The repeated-query setting (fixed geometry, changing observations) mirrors a deployment-cost model where only per-query work repeats and setup is separate. Abstract framing.

## Relevance to this project

One of very few papers reporting metered joules rather than modeled carbon for neural PDE-model inference. Its fixed-clock protocol is a reusable idea for our energy trials: pinning clocks removes a variance source from per-query energy. Its separation of preparation costs from repeated queries matches our setup-versus-query accounting.

## Check status and gaps

Preprint verified via the arXiv API. Gaps: abstract-level access only; the exact counter used for energy was not transcribed. Re-check for a published venue before the final report.
