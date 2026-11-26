# Sun et al. (2026): FEVessel, label-free pretrained FE operator for pressure vessels

## Source

- Title: FEVessel: Mesh-Independent Analysis of 3D Pressure Vessels with the Label-Free Pretrained Finite Element Method
- Authors: Yipin Sun, Yizheng Wang, Yuzhou Lin, Baiyang Zheng, Xiaoying Zhuang, Timon Rabczuk (arXiv order; the PDF lists Baiyang Zheng first)
- Year and publication or preprint version: 2026 preprint, arXiv:2607.17318. The PDF uses the International Journal for Numerical Methods in Engineering template with blank received and accepted dates, so treat it as a submitted manuscript. No published version found in Crossref on 2026-11-26.
- DOI or source URL: https://doi.org/10.48550/arxiv.2607.17318
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown. Not yet read by a human member.
- Access: full text (arXiv PDF)
- Local file: `downloads/sun-2026-fevessel/sun-2026-fevessel.pdf`, SHA-256 ee7e3addb4e5629784d469076123341bafd791a496182452f3fd23c9312cf7ef

## Question and setting

3D linear elasticity of pressure vessels across materials, geometries and loads:

- **Methods compared:** a physics-informed (label-free) Transolver trained on the total potential energy, a supervised Transolver, and an FNO (p8-9, Table 2).
- **Classical solver:** AMG-preconditioned CG at a 1e-3 engineering tolerance (Table 2 caption, p9).
- **Hardware:** training on an RTX 5090 GPU; FEM label generation on 8 workers of an AMD Ryzen 9 9950X CPU (p5).
- **Cost measure:** wall-clock time. No energy is measured.

## Claims we may use

- The physics-informed Transolver trains in 29.4 h with no labels, against 25.6 h plus 6.6 h of FEM label generation for the supervised Transolver (p8-9, Table 2).
- Inference takes 0.0130 s per case, against 2.30 s for the AMG-CG FEM solve at 1e-3 (Table 2).
- Using the prediction as a warm start cuts AMG iterations from 195 to 18, a 9.2 times end-to-end wall-clock speedup at 1e-3 (abstract; p2).
- Relative L2 displacement error of the label-free model: 1.35% (Table 2).

## Relevance to this project

A physics-trained parametric model is compared with an efficient classical solver (AMG-preconditioned CG) at a stated tolerance, with training time reported. The paper states no break-even count.

Our arithmetic from Table 2 (not the authors'): 29.4 h / (2.30 s - 0.013 s) is about 4.6 × 10^4 queries before the label-free model pays back its training as a replacement solver. That assumes the 1.35% error is acceptable, and it compares GPU with CPU. This figure is of the same order as Huang et al. 2026 (3.1 × 10^4 for FNO).

## Check status and gaps

- Confirmed in the cached text: the Table 2 values, the hardware and the baseline.
- Unresolved: the publication status (likely under review), and whether any break-even discussion appears outside the sections read.
