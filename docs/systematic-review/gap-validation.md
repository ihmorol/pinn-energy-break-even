# Gap validation (provisional)

**Status:** provisional, updated 2026-11-26 after full-text reads. Twelve full texts were read; the gap-deciding ones have notes in `references/`. Five open-access papers are still unread because of publisher human-verification checks (see [verification.md](verification.md)). Statements marked "pending" still rest on abstracts only.
**Basis:** the scoping review in this folder ([review-protocol.md](review-protocol.md), [search-log.md](search-log.md)). The gap claims and their falsification conditions are in review-protocol Section 3. Study IDs (R0xxxx) refer to [screening-decisions.csv](screening-decisions.csv).

## 1. Verdict for each claim

| Claim | Provisional verdict | Deciding studies (abstract level) |
|---|---|---|
| GC1 No metered-energy comparison of a PINN against a classical solver at matched accuracy | **Holds as worded ("metered"), full text for R01555 and R01457.** Without the word "metered" it would be falsified by R01555. | R01555 (Jediný 2025, bachelor's thesis, [note](../../references/jediny-2025-pinn-fdm-plasma-thesis.md)) compares PINN and FDM energy, but estimates it from utilization times TDP, with no metering (p25), on a GPU against one CPU core. R01457 (Tandale and Stoffel 2024, [note](../../references/tandale-2024-spiking-fem.md)) models per-forward-pass energy with KerasSpiking and compares network variants across hardware, not against FEM (p27); its FEM comparison is runtime only. R03662 (ISSCC 2024) and R01955 (2026) are hardware units for PINN and FEM or FDM, still at abstract level (closed access). |
| GC2 No break-even count for a parametric PINN against a classical solver | **Falsified in its broad form (full text). Holds only in a narrower form.** | Li, Jiang, Song 2026 (R00383, preprint, [note](../../references/li-2026-parametric-pinn-microfluidic.md)) trains a physics-only parametric PINN and reports break-even "after approximately 108 design evaluations" by wall-clock against COMSOL FEM, including training (p17, Fig. 8). The comparison is not at matched accuracy (PINN error 5.6-8.1% against the FEM reference), uses a GPU against a 56-core CPU, has no energy and no seeds. Other parametric physics-trained models report training-inclusive runtime without a query count: R02880, R01189, R03609 (abstracts). Sun et al. 2026 (R00643, full text, [note](../../references/sun-2026-fevessel.md)) gives training time and an AMG-CG baseline at 1e-3, from which we compute about 4.6 × 10^4 queries. Break-even counts for supervised or hybrid surrogates: R00627 ([note](../../references/zhang-2026-breakeven-complexity.md)), R00670, R00504 ([note](../../references/winkler-stoll-2026-flow-surrogates.md); Journal of Computational Science), R00637 (Journal of Computational Physics), R00649, R02483. |
| GC3 Energy and runtime break-even never reported separately | **Falsified in its broad form (full text). Holds only in a narrower form.** | R01555 reports both separately: "N = 1253 in terms of simulation time and N = 1303 in terms of energy use" (p38). But energy is estimated from TDP, the axis is grid points per dimension for one problem (not parameter queries), and the values are extrapolated from FDM runs up to N = 300. No study reports separate energy and runtime break-even counts over repeated queries with metered energy. |
| GC4 Tuning, failed runs and uncertainty not carried into a break-even estimate | **Holds (full text for R00383, R00504, R00627).** | Li et al. 2026 reports no seeds or failed runs. Winkler and Stoll charge training but state the configuration search is "not charged" (p11). Zhang et al. 2026 counts tuning but tests no PINN. R00649 is a negative result for a hybrid surrogate. R00670 uses three seeds for an FNO. |
| GC5 No PINN evidence on how the accuracy target moves the break-even point | **Holds at abstract level.** | The accuracy effect is shown for neural operators (R00657, R00670), and R00643 reports one tolerance (1e-3). No physics-informed break-even at two or more targets was found. |

Arithmetic from R01189's abstract numbers (our calculation, not the authors'): 8.72 h / 1.30 h is about 6.7. So the parametric PINN would pay back its training after about 7 parameter values, on different hardware (GPU against CPU) and in runtime only. A reviewer could call this an implied break-even, which is why GC2 needs the narrower wording below.

## 2. Proposed narrowed gap statement

To be confirmed after the full-text checks:

> Within a documented search of OpenAlex, Semantic Scholar and arXiv (2017 to November 2026), no study was found that reports, for a parametric physics-informed network trained without solver data, the number of new parameter queries at which its full training cost (including tuning and failed runs) is recovered against an efficient classical solver at matched accuracy on the same machine, with energy measured by hardware counters over one declared boundary for both methods and reported separately from runtime.

The closest work falls into five groups:

- separate time and energy break-even for a single-problem PINN against FDM, over grid resolution, with energy estimated from TDP and different hardware: Jediný 2025 (R01555, bachelor's thesis, N = 1253 for time and N = 1303 for energy);
- an explicit runtime break-even for a physics-only parametric PINN against FEM, without matched accuracy, the same hardware, energy or seeds: Li et al. 2026 (R00383, 108 evaluations);
- break-even counts for supervised surrogates, in runtime units: R00627 (error-matched, same hardware, tuning counted), R00670, R00504;
- training-inclusive runtime comparisons for parametric physics-informed models: R02880, R01189, R03609 (abstracts) and R00643 (full text);
- energy or carbon figures for neural solvers without a matched classical comparison: R00177, R00810, R02174, R00220 (modeled).

What changes from [gap-analysis.md](../gap-analysis.md):

- **Main contribution.** "First break-even for a PINN" is not true. Li et al. 2026 already reports one, and the report must cite it. "First energy break-even for a PINN" is not safe either: Jediný 2025 gives one, estimated from TDP over grid resolution. The contribution is the measured energy break-even under the stated protocol: matched accuracy, an efficient baseline, one machine and boundary, and seeds and failures counted. A useful framing: Li et al. compare against a high-fidelity FEM reference, while we error-match the classical solver, as Zhang et al. 2026 recommend.
- **Section 4 of [gap-evidence.md](../gap-evidence.md).** It said no row reports whether parametric training makes S_P larger or smaller than a single-problem PINN. R00692 (Engineering Applications of Computational Fluid Mechanics 2025) reports parametric training at "approximately 40 times the computational cost of solving a single flow". This is confirmed on p1 of the arXiv copy. That sentence in gap-evidence should be updated.
- **Scope.** The narrowing stays inside the fixed project scope. No new benchmark family is added.

## 3. Full-text checks

| Priority | ID | What to check | Status (2026-11-26) |
|---|---|---|---|
| 1 | R01555 | Is energy measured or estimated? Is it for both PINN and FDM, on what hardware, at what accuracy? Is the break-even reported for energy and for time separately? | **Done.** Estimated from utilization times TDP; GPU against one CPU core; accuracy is agreement with FDM; separate break-even for time (N = 1253) and energy (N = 1303) over grid resolution, extrapolated. |
| 1 | R01457 | What is the energy reduction compared against (classical FEM, or the same network on CPU/GPU)? How was it measured? | **Done.** Against the same network on other hardware; modelled with KerasSpiking, which the authors call conjectural. FEM comparison is runtime only. |
| 1 | R03662 | Does the chip report energy per solve for PINN and FEM at matched accuracy, or per operation? | **Closed access** (IEEE ISSCC) |
| 2 | R01955 | Same question as R03662. | **Closed access** (IEEE) |
| 2 | R02880, R01189, R03609 | Is a break-even or query count stated? Is training counted in full? Is the classical baseline efficient, and is the hardware the same? | R02880 and R01189 **blocked** (ScienceDirect); R03609 **closed** |
| 3 | R00383, R00643, R00692 | Training cost against per-query cost; R00692's "about 40 times a single solve" figure | **Done.** R00383: break-even at 108 evaluations. R00643: training 29.4 h against 2.30 s FEM per case. R00692: confirmed on p1. |

With R01555 and R01457 read, GC1 holds only because of the word "metered", and GC3 holds only in its narrowed form. The report must cite R01555 as the nearest prior energy break-even for a PINN, and say how ours differs: metered energy on one machine, an error-matched classical solver, and a break-even over parameter queries. The narrowed statement in Section 2 still holds. Five other open-access papers (R02880, R01189, R02939, R01850, R00895) are still unread because their publishers showed a human-verification check.
