# Gap evidence matrix

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.
**Written:** 2026-11-17 (AI-assisted; needs team review)
**Companion to:** [gap-analysis.md](gap-analysis.md). That file explains the gaps; this one shows the evidence cell by cell, with the page or section each cell comes from.

Nothing here is our measurement. Every number below is a value reported by the cited paper, or simple arithmetic on those values, labeled as such.

## 1. How the evidence was read

| Source | How it was read | Location code |
|---|---|---|
| Grossmann et al. 2024; de Hoop et al. 2022; Huang et al. 2026; Kapoor et al. 2025; Henderson et al. 2020; Krishnapriyan et al. 2021; Wang, Yu, Perdikaris 2022 | Keyword search of the cached full text in `outputs/markdown-cache/`, reading the matched lines | `pN` = PDF page (preprint pagination) |
| Markidis 2021 | Publisher full text (Frontiers), first 100k characters | `Sec` = section |
| Chuang and Barba 2022 | arXiv v3 HTML full text | `Sec` |
| Wang, Wang, Perdikaris 2021 | PMC full text (supplement not read) | Section or figure |
| McGreivy and Hakim 2024 | arXiv v1 HTML, first 100k characters | `Sec` |
| Zhang et al. 2026 | arXiv v2 HTML, first 100k characters | `Sec` |

The full-text reads for the web sources were done through a page-reading tool that returns quotes. Check each quote against the original before putting it in the report.

## 2. The matrix

Columns are the parts of our question. "Not stated" means we looked and the read text does not say it.

| Paper (status) | PINN-type model | Classical solver as cost competitor | Parameter family or repeated queries | Training cost in the comparison | Cost measured | Energy | Same hardware for both sides | Seeds or repeats | Break-even count |
|---|---|---|---|---|---|---|---|---|---|
| Grossmann et al. 2024 (peer-reviewed) | Yes | Yes, FEM | No; parameterised PDEs named as not considered (p23) | Yes, PINN training is its solution time | Wall-clock; codes "run 10 times" (p8) | None found | Same machine, but PINN on Quadro P6000 GPU and FEM on 12 CPU cores (p7-8) | 10 timing repeats (p8) | No |
| Chuang and Barba 2022 (peer-reviewed) | Yes | Yes, PetIBM finite differences | No | Yes | Wall-clock | Not stated | No: PINN on 8 A100 GPUs; PetIBM on 1 K40 GPU and 6 i7-5930K cores (Sec 3.2) | Not stated | No |
| Markidis 2021 (peer-reviewed) | Yes | Yes, PETSc CG | No; pre-training for transfer learning is "not included in the reported timings" (Sec 5) | Yes | Wall-clock | Not stated | Yes, one dual-core Intel i5 CPU; "GPUs (not used in this work)" (Sec 2.1) | Not stated | No |
| Wang, Wang, Perdikaris 2021 (peer-reviewed) | Yes (physics-informed DeepONet) | Yes, spectral solver for Burgers | Yes | No; speed-up is for inference with a trained model (Fig. 4 caption) | Wall-clock; inference about 10 ms | Not stated | DeepONet on one V100 GPU; solver hardware not stated in main text | Not stated | No |
| de Hoop et al. 2022 (peer-reviewed) | No (supervised operators) | No; FE used only to make data | Yes | As data volume | FLOPs ("Evaluation cost is measured in terms of FLOPs", p14) | None | Not applicable | Not checked | No |
| Huang et al. 2026 (preprint) | No (FNO) | Yes, finite volume with AMG-preconditioned CG | Yes | Yes | Solve units and time | None found | Not checked in full text | "three seeds with confidence intervals" (p15) | Yes: no FNO under 1% error breaks even before 3.1×10⁴ queries (p18) |
| Kapoor et al. 2025 (preprint) | Yes (PINN, PINNsFormer, SPINN) and operators | No; numerical solvers only as "embodied" data cost (p3) | Yes, for operators | Yes (embodied, developmental, operational carbon) | Carbon | CodeCarbon estimate (p5) | Not applicable | Not checked | No; cumulative footprint Ce + Cd + C0 + Ci·n_infer for each neural model (p3, Eq. 2), no classical line |
| Zhang et al. 2026 (preprint) | No | Yes, coarsened Exponax and PyFR (Sec 4.3, 5) | Yes | Yes, data and training; tuning excluded (Sec 3.3, App. B) | Wall-clock on L40S GPUs (Sec 4.1) | None; power named as future option (Sec 4.1) | Stated as same hardware (Sec 4.1) | No intervals in the part read | Yes (defined; budget in Sec 3.3) |

Supporting rows used for single cells:

- McGreivy and Hakim 2024: rule 1 "equal accuracy or equal runtime" and rule 2 "efficient numerical method" (Sec 2, restated Sec 6.1.4). PINN papers excluded from their review (Sec 6.1.2).
- Henderson et al. 2020: floating-point operations "not strongly correlated with energy consumption (R2 = 0.083, Pearson 0.289)" (p14); without detailed accounting "it is easy to severely over- or underestimate" energy (p15).
- Krishnapriyan et al. 2021: PINNs "can easily fail to learn relevant physical phenomena", tested on convection, reaction, and diffusion operators (p1).
- Wang, Yu, Perdikaris 2022: asks why PINNs "sometimes fail to train at all" (p1) and links it to stiffness in the gradient flow (p2).

## 3. Gaps read off the matrix

### G1. No row measures energy with counters

The Energy column has no counter-measured value. Kapoor et al. is the only PDE row with an energy-type number, and it is a CodeCarbon estimate (p5). Henderson et al. show why an estimate or FLOP count cannot stand in for it (p14, p15).

### G2. No row gives a break-even count for a PINN-type model against a classical solver

Only two rows report a break-even count, and neither uses a PINN: Huang et al. (FNO) and Zhang et al. (supervised operators). The four rows that compare a PINN-type model with a classical solver either test single solves (Grossmann, Chuang and Barba, Markidis) or leave training out of the speed-up (Wang, Wang, Perdikaris, Fig. 4). Kapoor et al. model cumulative carbon over inferences, but with no classical line to cross.

### G3. No row reports energy and runtime break-even separately

Follows from G1 and G2. Henderson et al. give the reason it matters: FLOPs explain little of the energy variation (R² = 0.083, p14).

### G4. Uncertainty from seeds and failed runs is missing in the PINN rows

None of the three single-solve PINN rows reports seed variance (Grossmann repeats timing 10 times, which is run-to-run timing, not training seeds). Only Huang et al. report seeds with confidence intervals, for an FNO (p15). PINN training failure is documented (Krishnapriyan p1, p5; Wang, Yu, Perdikaris p1-2; Chuang and Barba's cylinder case), so a break-even without seed and failure costs would be incomplete.

### G5. Matched accuracy is not always matched in practice

- Markidis: CG ran "to double-precision machine epsilon" in 92.28 s, while the PINN's maximum pointwise error was about 5E-3 (Sec 2.1). The section 5 text gives about 1E-3 for the same basic PINN; the paper does not reconcile the two.
- Chuang and Barba matched accuracy explicitly (16 × 16 grid in the abstract; 10⁻³ at t = 2 in Sec 3.3).

So "same accuracy" has to be enforced by the protocol, as McGreivy and Hakim's rule 1 asks. Our accuracy gate does this.

### G6. No row uses one declared measurement boundary for both methods

Two of the three single-solve PINN rows run the two methods on different devices (Grossmann: GPU against CPU; Chuang and Barba: 8 A100 against 1 K40 plus 6 cores). Markidis used one CPU for both, but measured time only. No row states a common energy boundary covering both methods, which our plan requires.

## 4. What the published numbers say about the size of N*

For runtime, with our model N* = (S_P − S_C)/(e_C − e_P): if the PINN's per-query cost e_P is near zero and the classical setup S_C is small, N* is close to S_P / e_C, the ratio of PINN training time to one classical solve. The single-solve papers report that ratio directly. This is arithmetic on their numbers, not a prediction for our study.

| Source | PINN training | Classical solve | Ratio | Conditions |
|---|---|---|---|---|
| Markidis 2021 (Sec 2.1) | 6,380 s | 92.28 s (PETSc CG) | about 69 | 2D Poisson, 128 × 128, same CPU. CG ran to machine precision, so a CG run stopped at the PINN's accuracy would take no longer, and the ratio at matched accuracy would be at least 69. |
| Chuang and Barba 2022 (abstract) | about 32 h | under 20 s | over 5,700 | 2D Taylor-Green, matched to a 16 × 16 grid, different hardware |
| Chuang and Barba 2022 (Sec 3.3) | more than 8 h | under 1 s | over 28,000 | Same case, 10⁻³ at t = 2, different hardware |
| Huang et al. 2026 (p18, preprint) | n/a | n/a | N* of at least 3.1×10⁴ | FNO, parametric Darcy, error below 1% |

What this means for us:

- These ratios are for PINNs retrained for one problem. Our PINN is trained once for the whole parameter family. Whether that makes S_P larger or smaller than a single-problem PINN is not reported in any row, and it is one of the things our study measures.
- The published values span roughly 69 to over 28,000 in runtime terms. None is in joules. That spread, and the missing energy column, is the space our measurement fills.
- Where a paper reports about 1e-3 accuracy, the PINN cost is high: more than 8 h in Chuang and Barba (Sec 3.3), and "after extensive training" in Markidis (Sec 5). This supports keeping 1e-3 as a target where the PINN may fail the gate.

## 5. Check against 2025-2026 published work

A second search on 2026-11-17 looked only at papers published in 2025-2026 in journals or archival conferences (Crossref and OpenAlex queries, then each paper's abstract or full text). None fills a gap above:

| Paper | What it adds | Effect on the gaps |
|---|---|---|
| Wang, Bhartari, Li, Perdikaris 2025 (NeurIPS 38) | Second-order (SOAP) PINN training, "2-10x accuracy improvements" on 10 benchmarks (abstract) | No classical comparison, no energy. Raises the bar for our PINN side; relevant to G5. |
| Chung et al. 2025, ML.ENERGY Benchmark (NeurIPS 38) | Inference energy measurement; settings alone gave "sometimes more than 40%" savings (abstract) | Generative AI, not PDE solvers. Supports G1 protocol; does not fill it. |
| Toscano et al. 2025 (Mach. Learn. Comput. Sci. Eng. 1) | Leading PINN review; autodiff "significantly increases computational cost" (Sec 3.2.1) | No PINN-versus-FEM cost comparison and no energy in the part read. Consistent with G1 and G2. |
| Wang et al. 2026, FD-Bench (KDD 2026) | Fair-comparison framework against numerical solvers for data-driven fluid models (abstract) | Not PINNs, not energy. |

The closest 2026 work on break-even (Zhang et al., arXiv:2605.15399) is still a preprint as of this check.

## 6. Limits of this matrix

- Eight papers, chosen because they are the PDE comparison papers in our final citation list. Measurement papers (Khan, Yang) and motivation papers (Strubell, Schwartz, Luccioni) are not rows because they do not compare solvers.
- Cells marked "Not checked" were not looked up, to save time; they do not change any gap above.
- Web full texts were read through a summarizing page reader that returned quotes. Confirm each quote on the original page before citing it.
- Huang et al. 2026, Kapoor et al. 2025, and Zhang et al. 2026 are preprints.
