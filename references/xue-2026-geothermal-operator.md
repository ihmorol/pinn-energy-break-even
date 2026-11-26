# Xue et al. (2026): physics-constrained neural operator for geothermal evaluation

## Source

- Title: A robust physics-constrained neural operator framework for efficient geothermal resource development
- Authors: Zhenqian Xue, Jianfei Bi, Haoming Ma, Zhe Sun, Zhangxing Chen
- Year and publication: 2026, Nature Communications. Received 5 August 2025, accepted 3 May 2026.
- DOI: https://doi.org/10.1038/s41467-026-73183-0
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown (abstract, data section, timing paragraph). Not yet read by a human member.
- Access: full text (Nature open-access PDF, fetched through the app's built-in browser)
- Local file: `downloads/xue-2026-geothermal-operator/xue-2026-geothermal-operator.pdf`, SHA-256 4f9fb7e208198109802fd68c5da496724b217e300cca4fd00c9d84fcbd11a384

## Question and setting

A physics-constrained neural operator (PCNO) predicts subsurface fields and surface energy production for geothermal reservoirs. It is trained on simulator data: 9450 samples from CMG-STARS, of which 7350 are used for training (p2-3). It is not a physics-only model.

## Claims we may use

- On an NVIDIA A100 GPU the PCNO completes 1050 cases in about 310 s including data loading, against about 7380 min for CMG-STARS on an AMD Ryzen 9 5950X CPU (p9).
- The authors state that "these time costs exclude" pre- and post-processing and "the effort to construct the model" (p9). The abstract reports about 1,400-fold acceleration.

## Relevance to this project

A top-tier example (JUFO 3) of a speedup reported without training or data-generation cost, on different hardware. It supports GC4 and the motivation for a break-even count. It does not falsify GC2, because the model is trained on solver data and no break-even is given.

## Check status and gaps

- Confirmed in the cached text: the timing paragraph and dataset size.
- Not read: the supplementary methods; training time and GPU hours were not found in the main text.
