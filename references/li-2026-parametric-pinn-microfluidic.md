# Li, Jiang and Song (2026): parameterized PINN for embedded microfluidic chip cooling

## Source

- Title: Parameterized Physics-Informed Neural Networks for Efficient Simulation of Embedded Microfluidic Chip Cooling
- Authors: Weiheng Li, Zhiyao Jiang, Bai Song (Peking University)
- Year and publication or preprint version: 2026 preprint, arXiv:2611.10666. No published version found in Crossref on 2026-11-26.
- DOI or source URL: https://doi.org/10.48550/arxiv.2611.10666
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown. Not yet read by a human member. Check each number on the PDF page before the report uses it.
- Access: full text (arXiv PDF)
- Local file: `downloads/li-2026-parametric-pinn-microfluidic/li-2026-parametric-pinn-microfluidic.pdf`, SHA-256 d1a50e56a2bd6c66d06db099e2a243cf194e6ceba727cf6d18305971ea304f43

## Question and setting

A parametric PINN for 3D conjugate heat transfer in embedded manifold microchannels:

- **Inputs:** four geometric dimensions and three spatial coordinates.
- **Training:** physics only. The loss is PDE residuals, boundary and interface constraints, and regularization (p21, figure caption), optimized with SOAP.
- **Reference:** COMSOL Multiphysics 6.3 FEM, one-way coupled, about 2.3 × 10^6 elements (p13).
- **Hardware differs:** the PINN trains on one RTX 4090D GPU; FEM runs on 56 cores of a dual Xeon 8570 node (p17).
- **Cost measure:** wall-clock time and hardware rental price. No energy is measured.

## Claims we may use

- FEM needs 122.53 s per design point. The PINN trains for 3 h 40 min, then needs 9.3 ms per new design, a per-design speedup of about 1.32 × 10^4 (p17).
- "Based on wall-clock time, the training cost is amortized after approximately 108 design evaluations" (p17; Fig. 8, p25).
- Using rental prices of about 9 CNY/h (CPU node) and 2 CNY/h (GPU), the monetary break-even is about 24 design evaluations (p17).
- The authors state the two methods run on different hardware and that the FEM baseline is the efficient one-way coupled form (p17).
- Accuracy against the FEM reference: relative L2 errors of 8.1% (velocity) and 5.6% (temperature) over 625 FEM cases (abstract; p17-18).

## Relevance to this project

This is the closest prior found for our design: a physics-only parametric PINN with an explicit break-even count against a classical solver, training included. It falsifies the broad form of gap claim GC2.

It leaves our narrowed gap open, for five reasons:

1. The comparison is not at matched accuracy. FEM is the reference, and the PINN error is 5-8%; a coarser FEM run at that error would be cheaper, so the break-even would move.
2. Hardware differs, and runtime is not energy.
3. No energy is measured.
4. No seeds or failed runs are reported (the cached text has no mention of seeds).
5. There is one accuracy level.

## Check status and gaps

- Confirmed in the cached text: the break-even numbers, the hardware, the training time and the loss terms.
- Not checked: the figure values on the PDF page.
- Earlier listed in [shortlist.md](shortlist.md) as "not a benchmark"; that description is now out of date.
