# Problem definition

This document sharpens the question the submitted proposal set. It adds the structure, definitions, and decision rules the literature says a fair comparison needs. It does not reopen the scope, and it does not fix the pilot decisions that the [research plan](research-plan.md) leaves open; exact equations and bounds are still frozen during the pilot. Each design element cites the checked source that motivates it (see the [literature shortlist](../references/shortlist.md)).

## 1. The question, stated precisely

For a fixed parametric partial differential equation family, a fixed accuracy target, and one controlled machine: how many new parameter queries N* does a parametric PINN need before its measured cumulative electricity equals that of a classical finite-difference solver that is re-solved per query? The same question is asked separately for wall-clock runtime. A crossover may not exist, may sit beyond practical use, or may be statistically unresolvable. Any of these is a valid answer.

The cost model (research plan, Section 5) is:

$$
E_P(N) = S_P + N e_P, \qquad E_C(N) = S_C + N e_C,
$$

with setup-plus-training energy S and mean per-query energy e for the PINN (P) and classical (C) methods, measured in joules over a declared measurement boundary. The runtime model replaces E with t. The candidate intersection is N* = (S_P - S_C) / (e_C - e_P), with the outcome classified as no crossing, one method already cheaper throughout, an uncertain crossing, or an extrapolated crossing (plan, Section 5).

## 2. What the literature establishes, and the gap

Three checked findings define where our question sits:

1. At matched accuracy, a tuned classical method beat a PINN on wall-clock time for single solves on Poisson, Allen-Cahn, and Schrödinger problems, by roughly one to six orders of magnitude depending on the problem ([Grossmann et al. 2024](../references/grossmann-2024-pinn-vs-fem.md)). That study measured time only, and its limitations section names parameterized PDEs with amortized training as not covered.
2. In the many-query amortized regime, cost-accuracy analyses find that neural surrogates are most competitive at low-to-moderate accuracy and that classical solvers win as the accuracy target tightens ([Huang and Stuart 2026](../references/huang-stuart-2026-cost-accuracy.md); [de Hoop et al. 2022](../references/dehoop-2022-cost-accuracy.md)). The amortization law of [Huang et al. 2026](../references/huang-2026-solver-review.md) predicts break-even only after many queries (beyond 30,000 for errors below 1 percent on parametric Darcy flow), with break-even always exceeding the training-set size.
3. Runtime is not a reliable proxy for energy in PDE-model workloads, particularly during training ([Wilson et al. 2025](../references/wilson-2025-carbon-forecasting.md)), and extrapolated energy estimates can be wrong by orders of magnitude ([Henderson et al. 2020](../references/henderson-2020-energy-reporting.md); [Patterson et al. 2022](../references/patterson-2022-carbon-plateau.md)).

The gap, within the search scope recorded in the shortlist: no published study reports counter-measured electricity for a parametric PINN trained across a parameter family, compared against a classical solver at matched accuracy, with the break-even query count estimated separately for energy and runtime. Grossmann et al. stop at time and single solves; the Huang line works in modeled cost units, not metered joules; the metered-energy works stop at inference or use modeled carbon ([Yoo et al. 2026](../references/yoo-2026-energy-inference.md); [Kapoor et al. 2025](../references/kapoor-2025-ecol2.md)). Our study answers the question inside that gap at pilot scale, on one 2D steady-diffusion family.

## 3. Parametric problem structure

Let the main problem (exact form frozen during the pilot, per plan Section 2) be a steady diffusion boundary value problem on the unit square:

$$
-\nabla \cdot \left( k(\mathbf{x}; \theta) \, \nabla u(\mathbf{x}; \theta) \right) = f(\mathbf{x})
\quad \text{in } \Omega = (0,1)^2,
$$

with fixed Dirichlet boundary data and a fixed source f. The conductivity k carries the entire parameter dependence:

- Two bounded scalar parameters theta = (theta_1, theta_2) in a closed box Theta in R^2 control the spatial shape and contrast of k.
- k stays uniformly elliptic on Theta: a lower bound k_min > 0 holds everywhere, so the operator stays coercive and the classical solve well-posed for every allowed theta.
- Geometry, boundary conditions, and the source do not depend on theta. This is what makes the workload a parametric family rather than a set of unrelated problems.

A concrete candidate (an example to freeze or replace during the pilot, not a decision): k(x; theta) = k_min + (k_max - k_min) * (theta_1 * s_1(x) + theta_2 * s_2(x)) normalized to the unit box, with s_1, s_2 fixed smooth shapes such as s_1 = sin(pi x) sin(pi y) and s_2 = x(1-x)y(1-y). The bounds of Theta are chosen so k stays strictly positive.

**Query.** A query is: given one previously unseen theta* drawn from a fixed, recorded distribution over Theta, produce u on the shared fixed output grid G. The query cost includes everything needed to produce that output: assembly, solve, and sampling for the classical method; a network forward pass and sampling for the PINN. Cached identical answers are not charged again, and repeated-query blocks represent new parameter settings, not an artificial cache advantage (plan, Section 2).

**Workload fairness.** Both methods face the same held-out parameter set and output grid. Held-out parameters are excluded from training and tuning. The classical baseline keeps every valid reuse: sparsity patterns, preconditioners, and factorizations where they remain mathematically valid for the new k. The PINN keeps the trained network and its inference setup. This is the baseline-quality standard the weak-baseline audit in Huang et al. 2026 (Section 4.8) demands.

## 4. Accuracy qualification

The comparison basis is matched accuracy, because cost-accuracy analysis says the winner can change with the target ([de Hoop et al. 2022](../references/dehoop-2022-cost-accuracy.md); [Huang and Stuart 2026](../references/huang-stuart-2026-cost-accuracy.md)):

- Error: relative L2 error against a reference on the shared grid G, per held-out parameter, as defined in plan Section 3.
- Targets: 1e-2 and 1e-3 primary; 1e-4 optional within the frozen budget.
- Qualification rule: a method qualifies for a target when it passes the error check on the declared set of held-out parameters. Full energy trials for that target run only when both methods qualify. Runs that miss the target are recorded and kept out of qualified cost comparisons.
- Reference: the 1D pilot uses a known solution. The main study uses an exact or independently checked reference (fine-grid solution with a refinement check), with a declared reference-error allowance, because the classical baseline is not automatically its own ground truth (plan, Section 3).
- The collocation budget, network size, and stopping rule for the PINN are fixed before the gate, following the generalization-error logic that held-out error depends on training error and sample counts ([Mishra and Molinaro 2022](../references/mishra-molinaro-2022-generalization.md)).

## 5. Measurement definition

The primary quantity is electricity in joules over a declared measurement boundary on one controlled machine; runtime in seconds is the separate computational cost axis (plan, Sections 4 and 5).

- Boundary: the components covered (CPU package, DRAM, GPU, or subsets) are stated for every number, and device readings are never presented as whole-machine electricity without that coverage ([Henderson et al. 2020](../references/henderson-2020-energy-reporting.md)).
- Sources: hardware counters where available (Intel RAPL for CPU/DRAM, the NVIDIA management interface for GPU), integrated over the measured interval. Modeled values (for example from CodeCarbon-style tools) are labeled as estimates ([Lacoste et al. 2019](../references/lacoste-2019-carbon-emissions.md)). Carbon is a labeled conversion of measured energy using a declared region and time basis, never a primary measurement ([Dodge et al. 2022](../references/dodge-2022-carbon-cloud.md)).
- Protocol: warm-up, synchronized timing, long enough query blocks to resolve energy above noise, fixed batching and thread settings, fixed query order, and repeated trials ([MLPerf Power, Reddi et al. 2024](../references/mlperf-power-2024.md)); fixed clocks where the hardware allows, which removes a known variance source ([Yoo et al. 2026](../references/yoo-2026-energy-inference.md)).
- Accounting: setup, training, and per-query costs are separate; training failures, tuning, and retries stay in the study ledger ([Henderson et al. 2020](../references/henderson-2020-energy-reporting.md); plan, Section 4). At least three training seeds; seed-to-seed variance enters the uncertainty on S_P and e_P, which matters because PINN training pathologies make training cost and variance method properties, not accidents ([Wang, Yu, and Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md)).

## 6. Hypotheses the study tests (none assumed true)

- Q1. Existence: does an energy crossover N* exist within a practically usable query count for this workload?
- Q2. Coincidence: do the energy and runtime crossovers land at the same N, or differ? The two need not coincide ([Wilson et al. 2025](../references/wilson-2025-carbon-forecasting.md); plan, Section 5).
- Q3. Accuracy effect: how does N* move when the target tightens from 1e-2 to 1e-3 (and optionally 1e-4)? The literature predicts higher targets push the break-even further out or remove it ([Huang and Stuart 2026](../references/huang-stuart-2026-cost-accuracy.md); [Huang et al. 2026](../references/huang-2026-solver-review.md)).
- Q4. Variance: how wide is the seed-to-seed uncertainty on N*, and can a crossover claim survive it ([Wang, Yu, and Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md))?

A claim of "the PINN reaches break-even after N* queries" is published only with an uncertainty interval from seeds and repeated trials, a statement of the usable N range, and the linear-model adequacy check from plan Section 5. Claims follow the P3 standard (equal-accuracy, cost-matched comparison against a tuned classical workflow) of the evidence ladder in [Huang et al. 2026](../references/huang-2026-solver-review.md), Section 4.8.

## 7. Known threats to validity

- Weak-baseline risk: an under-tuned classical solver manufactures a crossover. Mitigation: baseline tuning and reuse rules are frozen and reviewed ([Huang et al. 2026](../references/huang-2026-solver-review.md), baseline audit; [research-review skill](../.agents/skills/research-review/SKILL.md)).
- Coverage mismatch: GPU-side PINN readings versus CPU-side classical readings are not the same system total. Mitigation: one declared boundary for both methods, or a per-component split reported side by side ([Henderson et al. 2020](../references/henderson-2020-energy-reporting.md)).
- Runtime proxy risk: a faster method can use more energy and vice versa. Mitigation: both axes measured and reported separately ([Wilson et al. 2025](../references/wilson-2025-carbon-forecasting.md)).
- Unrefereed priors: the two closest quantitative priors (Huang et al. 2026; Huang and Stuart 2026) are preprints. Mitigation: their numbers are cited as unrefereed and re-checked against published versions.
- Single-hardware scope: conclusions hold for the tested machine and budget. The report says so (plan, Section 8).

## 8. Out of scope, unchanged

Geometry changes, boundary-condition variation, extra parameter dimensions, additional PDE families, and broad solver or model surveys stay outside this study (plan, Section 2). This document only makes the existing scope precise; it does not extend it.
