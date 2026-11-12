# Reference solution approach

This document describes how we plan to build and run the comparison so the break-even question in the [problem definition](problem-definition.md) gets an answer that survives review. It is a design record, not a result: nothing here has been measured. Where the [research plan](research-plan.md) defers a decision, this document proposes a candidate and marks it for the pilot. Each design element points to the checked source that motivates it.

## 1. Overview

The study needs three deliverable groups, matching the twelve-week plan (research plan, Section 6):

1. **Two solvers**: a small parametric PINN in PyTorch, trained once across the parameter family, and a finite-difference classical solver in SciPy, with valid reuse retained.
2. **One measurement harness**: synchronized timing plus energy counters inside a declared boundary, recording into the run-record template and the study-energy ledger.
3. **One analysis pipeline**: accuracy gates, linear cost models, crossover estimates with uncertainty, and the outcome classification.

The build order runs pilot first (telemetry check, 1D pilot, protocol freeze), then both solvers in parallel, then the accuracy gate, then energy trials.

## 2. Classical solver design (baseline)

- **Discretization**: uniform grid on the unit square, five-point finite differences for -div(k grad u), with conductivity averaged at cell faces so the stencil stays consistent for variable k. Candidate detail: harmonic or arithmetic face averaging is chosen during the pilot by checking convergence order on the 1D pilot.
- **Solve**: the assembled matrix is sparse and symmetric positive definite under the uniform-ellipticity condition. Candidates to benchmark: a direct sparse factorization (SciPy `spsolve` on CSC) and conjugate gradient with a simple preconditioner (Jacobi or ILU). The pilot picks the faster one on the pilot problem; this choice is recorded, frozen, and not changed afterwards.
- **Reuse policy** (plan, Section 2): the sparsity pattern is reused across parameters. A factorization is reused only when it remains mathematically valid for the new conductivity; since k changes with theta, the default assumption is no factorization reuse, and any preconditioner reuse must be re-validated for the new matrix. This is where an under-tuned baseline would manufacture a false crossover, so the reuse rules are reviewed before energy trials (the weak-baseline warning in [Huang et al. 2026](../references/huang-2026-solver-review.md), Section 4.8).
- **Per-query cost split**: assembly, solve, and output-grid sampling are timed and measured separately, so the setup and query terms of the cost model have honest content.
- **Reference construction**: grid refinement with a Richardson check against the fine grid; for the 1D pilot, a manufactured solution. The reference-error allowance is declared before the accuracy gate (plan, Section 3).

## 3. Parametric PINN design

- **Inputs and output**: the network takes (x, y, theta_1, theta_2), normalized, and returns u. One network covers the parameter family, per plan Section 2; no per-query retraining.
- **Architecture**: small fully connected MLP, width and depth in the small range the plan commits to (candidate: 4 to 6 hidden layers of 40 to 80 units, tanh). Exact size is frozen at the pilot with the training budget.
- **Boundary conditions**: two candidates, decided on the pilot. (a) Hard enforcement: write u = g + d(x) * N(x, y, theta) with d zero on the boundary, which removes the boundary loss term. (b) Soft penalties with loss weights. The choice is recorded because it changes the loss landscape and therefore the training cost ([Krishnapriyan et al. 2021](../references/krishnapriyan-2021-failure-modes.md)).
- **Loss**: PDE residual mean squared error at collocation points (resampled or fixed, per pilot), plus boundary terms if soft constraints are used.
- **Optimizer**: Adam with a fixed step schedule, optional short L-BFGS polish; the recipe is frozen before the gate.
- **Training set**: parameter vectors sampled from Theta with a fixed seed; a separate validation set monitors held-out-style error during training; the held-out test parameters are touched only at the gate.
- **Seeds and failures**: at least three training seeds under the frozen budget (plan, Section 4). Failed or diverged runs are logged with their cost; they are part of the deployment estimate under the declared retry policy, not hidden ([Wang, Yu, and Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md)).
- **Contingency mitigations**, adopted only if the pilot shows the known pathologies, and logged with their tuning cost: adaptive loss weighting from gradient statistics ([Wang, Teng, and Perdikaris 2021](../references/wang-2021-gradient-pathologies.md)), NTK-eigenvalue-based balancing ([Wang, Yu, and Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md)), or curriculum regularization ([Krishnapriyan et al. 2021](../references/krishnapriyan-2021-failure-modes.md)). Any mitigation changes S_P, which is fine as long as the full cost lands in the ledger.

## 4. Measurement harness

- **Counters**: CPU package and DRAM via the Intel RAPL powercap interface; GPU via the NVIDIA management interface (nvidia-smi or its library). Availability is confirmed on the pilot machine first; if a required counter is missing, the fallback estimate is approved with the supervisor before the main trials and labeled `modeled` (plan, Section 4; tooling anchored in [Henderson et al. 2020](../references/henderson-2020-energy-reporting.md), Section 4.3.1).
- **Energy values**: integrated over the measured interval from counter deltas (joules), not single instantaneous samples. Units and counter coverage are recorded per value in the run record.
- **Timing**: monotonic clock around each block, with device synchronization before the stop for GPU work.
- **Block protocol** (per method, per target): warm-up block excluded from accounting; K queries per block; R repetitions; K chosen long enough that the block energy sits clearly above counter noise (checked on the pilot). Query order, batching, thread counts, and device placement are fixed and recorded. Clocks are pinned where the hardware allows, following the fixed-clock protocol of [Yoo et al. 2026](../references/yoo-2026-energy-inference.md).
- **Boundary rule**: both methods are measured inside the same declared component set. If the PINN runs on GPU and the classical solver on CPU, the report gives per-component energies side by side and never presents one component's reading as the whole machine ([Henderson et al. 2020](../references/henderson-2020-energy-reporting.md)).
- **Idle and background**: background load is minimized and its treatment is declared; idle power is recorded once per session as context, not silently added to either method.
- **Records**: each trial writes `experiments/records/<run-id>.json` from the run template; study-level windows go to `experiments/study-energy.csv`. Carbon, if reported, is a labeled conversion with a declared grid factor ([Dodge et al. 2022](../references/dodge-2022-carbon-cloud.md)); CodeCarbon-style readings are labeled estimates ([Lacoste et al. 2019](../references/lacoste-2019-carbon-emissions.md)).

## 5. Accuracy gate and trial sequence

1. Validate the classical solver on the 1D pilot against the known solution; check convergence order and the reference allowance.
2. Validate the PINN on the 1D pilot under the frozen recipe and budget; log all attempts.
3. Freeze the protocol checklist (plan, Section 7): machine and counters, exact equations and bounds, parameter sets and grid, network and budget, query workload, logging formats.
4. Build the 2D implementations on the frozen protocol.
5. Gate: evaluate both methods on held-out parameters at 1e-2, then 1e-3 (and optionally 1e-4). Only qualified methods proceed to energy trials for that target ([Mishra and Molinaro 2022](../references/mishra-molinaro-2022-generalization.md) grounds why the budget knobs are frozen first).
6. Energy trials per qualified target: setup, training (PINN), and query blocks measured with at least three seeds and R repetitions each.

## 6. Analysis pipeline

- **Per method and target**: estimate S and e (joules and seconds) from block totals, with confidence intervals from seeds and repetitions. Nothing is extrapolated beyond the measured N range without a labeled statement.
- **Linear-model adequacy**: check the per-query slope for stability across block positions and sizes; if the slope drifts, the report says the linear model is inadequate on that range instead of quoting N* (plan, Section 5).
- **Crossover estimate**: N* with a bootstrap or delta-method interval over seed and trial variability; then classification: no crossing, one method cheaper throughout, uncertain crossing, or extrapolated crossing.
- **Two separate answers**: the energy crossover and the runtime crossover are reported independently, since a faster method need not use less energy ([Wilson et al. 2025](../references/wilson-2025-carbon-forecasting.md)).
- **Comparison to priors**: the measured N* is discussed against the amortization-law prediction ([Huang et al. 2026](../references/huang-2026-solver-review.md), Section 4.5) and the accuracy-tightening finding ([Huang and Stuart 2026](../references/huang-stuart-2026-cost-accuracy.md)), with the preprint caveat stated.
- **Outputs**: crossover plots with uncertainty bands, a comparison table per target separating qualified measurements from accuracy failures, the study-energy ledger, and the final report statement of when the lower-energy method can be selected for this workload (plan, Section 8).

## 7. Traceability: design choice to source

| Design choice | Motivating source |
|---|---|
| Matched accuracy as the comparison basis | [de Hoop et al. 2022](../references/dehoop-2022-cost-accuracy.md); [Grossmann et al. 2024](../references/grossmann-2024-pinn-vs-fem.md) |
| Break-even model and N* | Research plan Section 5; [Huang et al. 2026](../references/huang-2026-solver-review.md) Section 4.5 |
| Evidence standard for the cost claim (P3) | [Huang et al. 2026](../references/huang-2026-solver-review.md) Section 4.8 |
| Baseline tuning and reuse fairness | [Huang et al. 2026](../references/huang-2026-solver-review.md) baseline audit; research plan Section 2 |
| Counter-based measurement and boundary statement | [Henderson et al. 2020](../references/henderson-2020-energy-reporting.md); [MLPerf Power 2024](../references/mlperf-power-2024.md) |
| Modeled values labeled, carbon as conversion | [Lacoste et al. 2019](../references/lacoste-2019-carbon-emissions.md); [Dodge et al. 2022](../references/dodge-2022-carbon-cloud.md) |
| Fixed clocks, block protocol | [Yoo et al. 2026](../references/yoo-2026-energy-inference.md); [MLPerf Power 2024](../references/mlperf-power-2024.md) |
| Energy and runtime reported separately | [Wilson et al. 2025](../references/wilson-2025-carbon-forecasting.md); research plan Section 5 |
| Seeds, failure logging, training-cost variance | [Wang, Yu, and Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md); [Wang, Teng, and Perdikaris 2021](../references/wang-2021-gradient-pathologies.md); [Krishnapriyan et al. 2021](../references/krishnapriyan-2021-failure-modes.md) |
| Frozen collocation and network budget before the gate | [Mishra and Molinaro 2022](../references/mishra-molinaro-2022-generalization.md) |
| Introduction framing (why energy matters in ML research) | [Strubell et al. 2019](../references/strubell-2019-energy-policy.md); [Schwartz et al. 2020](../references/schwartz-2020-green-ai.md); [Patterson et al. 2022](../references/patterson-2022-carbon-plateau.md); [Luccioni et al. 2024](../references/luccioni-2024-power-hungry.md) |
| Method origin and field context | [Raissi et al. 2019](../references/raissi-2019-pinn.md); [Karniadakis et al. 2021](../references/karniadakis-2021-physics-informed-ml.md); [Cuomo et al. 2022](../references/cuomo-2022-pinn-survey.md) |

## 8. First concrete steps (weeks 1-2 of the plan)

1. On the pilot machine, confirm RAPL and GPU counter access and record a short idle-versus-load check; this decides whether measurements are counter-based or need the approved fallback.
2. Implement the 1D pilot: manufactured solution, classical solve, and a first small PINN, with the error check against the known solution.
3. Run the first timed-and-measured block on both methods to size K, R, and the noise floor; freeze the budget.
4. Write the pilot run record and the first ledger rows; from then on, every run has a record, including failures.

Nothing in this document authorizes a training or energy run; runs follow the [experiment-run skill](../.agents/skills/experiment-run/SKILL.md) and need an approved machine, purpose, protocol, and budget first.
