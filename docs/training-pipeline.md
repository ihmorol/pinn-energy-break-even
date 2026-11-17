# PINN training pipeline plan

This is a design record for how we will train, check, and cost the parametric PINN. It turns the training methods in the literature into a pipeline for our one workload: steady diffusion on the unit square with two conductivity parameters, after the 1D heat pilot. Nothing here has been run or measured. It adds detail to Section 3 of the [reference solution](reference-solution.md) and does not change the scope in the [research plan](research-plan.md). Values marked "candidate" are proposals for the pilot to confirm or replace; they are not frozen.

**Notation.** This plan follows [model-equations.md](model-equations.md): inputs (x, y, μ₁, μ₂), network output v, prediction û. [problem-definition.md](problem-definition.md) writes the parameters as θ; the meaning is the same. Network weights are w.

**Evidence rule.** As in the [gap analysis](gap-analysis.md), each design rule rests on at least one peer-reviewed source. Preprints are marked and only add detail or contingency ideas.

The sources were read on 2026-11-17, focusing on methods, training settings, and failure reports. Notes are listed in the [shortlist](../references/shortlist.md) (Tiers B, D, and E); Section 9 lists what this pass added.

## 1. How the literature trains PINNs

| Source | Network | Optimizer and budget | Points | Boundary | Runs | What we take |
|---|---|---|---|---|---|---|
| [Wang, Teng, Perdikaris 2021](../references/wang-2021-gradient-pathologies.md) | tanh, 30 to 100 wide, 3 to 7 deep | Adam, lr 1e-3 with decay, 40,000 steps | mini-batch 128 | soft, adaptive weights | not stated in passages read | soft boundary terms cause gradient imbalance; stiffness limits the learning rate |
| [Wang, Yu, Perdikaris 2022](../references/wang-2022-pinn-ntk-failure.md) | wide MLP (theory) | gradient descent with NTK weights | fixed | soft | n/a | boundary and residual terms converge at different rates |
| [Krishnapriyan et al. 2021](../references/krishnapriyan-2021-failure-modes.md) | 4 x 50 tanh | L-BFGS, lr swept 1e-4 to 2.0 | random | soft | at least 10 seeds | failure grows with the PDE coefficient; curriculum helps |
| [Markidis 2021](../references/markidis-2021-pinn-linear-solvers.md) | 4 to 6 x 50 to 100 | Adam 10,000 epochs at 1e-3, then L-BFGS-B 13,000 | 128 x 128 Sobol + 4,000 boundary | soft | n/a | 2D Poisson: Adam plateaus near 5e-3 to 1e-2 training error; L-BFGS-B takes it to 2.79e-5 |
| [Chuang and Barba 2022](../references/chuang-barba-2022-pinn-pitfalls.md) | 6 x 256, SiLU | Adam with exponential decay, up to 1,000,000 iterations, FP32 | 18,432 random per step | periodic by construction | GPU counts 1 to 8 | no tuning was affordable; stopped by judgment; more points per step did not help |
| [Grossmann et al. 2024](../references/grossmann-2024-pinn-vs-fem.md) | tanh, up to 3 x 40 | Adam 15,000 epochs at 1e-4, then L-BFGS | 256 per epoch, Latin hypercube, resampled each Adam epoch | soft | 10 timing runs | Adam then L-BFGS; L-BFGS uses one fixed point set |
| [Hao et al. 2024, PINNacle](../references/hao-2024-pinnacle.md) | 5 x 100 | Adam lr 1e-3, 20,000 epochs | 8,192 interior, 2,048 boundary | soft | 3 | lr 1e-2 spikes; gains saturate; its "parametric" runs retrain per parameter |
| [Rathore et al. 2024](../references/rathore-2024-loss-landscape.md) | 3 hidden, 50 to 400 wide | Adam then L-BFGS (memory 100, strong Wolfe), 41,000 total | fixed | soft | 5 seeds | Adam+L-BFGS beats each alone; L-BFGS stops early |
| [Urbán et al. 2025](../references/urban-2025-optimization.md) | 2 to 3 x 20 to 30 | Adam then BFGS-family quasi-Newton | refreshed every 500 steps | varies | spread reported | small networks reach high accuracy with a better optimizer |
| [Xu et al. 2025](../references/xu-2025-fp64.md) | standard benchmarks | L-BFGS, FP32 versus FP64 | 101 x 101 | soft | not checked | FP32 makes PyTorch L-BFGS stop early |
| [Sun et al. 2020](../references/sun-2020-surrogate-no-data.md) | 3 x 20, Swish | Adam lr 1e-3, batch 50 | random | hard Dirichlet | not checked | parameters as inputs, no solver data: our design |
| [Wang, Wang, Perdikaris 2021](../references/wang-wang-perdikaris-2021-pi-deeponet.md) | DeepONet, tanh | Adam, batch 10,000, decay 0.9 per 1,000 steps, 40,000 to 300,000 steps | random | soft | n/a | physics-only parametric training took 0.03 to 9.25 GPU-hours; the "1000x faster" claim is inference only |
| [Mishra and Molinaro 2022](../references/mishra-molinaro-2022-generalization.md) | grid of sizes | L-BFGS; 360 settings x 5 retrains, keep lowest training loss | Sobol or random | soft | 5 per setting | held-out error depends on training error and point count; selection has a cost |
| [Wang et al. 2023, expert guide](../references/wang-2023-expert-guide.md) (preprint) | tanh, 128 to 512 wide, 3 to 6 deep | Adam lr 1e-3, exponential decay, no weight decay | random each step | hard where possible | n/a | scale inputs to order one; gradient-norm weights as fallback |

Two patterns hold across the peer-reviewed sources: smooth activations (tanh in most) with Glorot-type initialization, and Adam followed by L-BFGS. Network size, point counts, and budgets vary by more than ten times between sources, so none of them can be copied as our setting.

## 2. Failure modes and catches

Each row is a way the PINN side can fail or the comparison can become unfair. "Handling" is what the pipeline does about it. "Inference" marks where we apply a finding to steady diffusion without direct evidence for it.

### Training the network

| ID | Catch | Evidence | Effect on the study | Handling |
|---|---|---|---|---|
| C1 | Soft boundary penalties make the loss terms compete; weights are hard to choose | Wang 2021, Sec. 2.2 to 2.5; Wang 2022, Sec. 3 to 6; Sun 2020, Sec. 2.3 | extra weight tuning, slower training, higher S_P | Candidate A in model-equations.md: û = x(1 − x)y(1 − y) v, one loss term (Sukumar 2022). Derivatives go through the multiplier |
| C2 | FP32 makes PyTorch L-BFGS stop on rounding noise (`tolerance_change` 1e-7 below FP32 epsilon 1.19e-7) | Xu 2025, Sec. 5.2 | a "converged" run that is not converged; false failures at 1e-3 | train in FP64, or set stop tolerances above the dtype epsilon; record dtype per run |
| C3 | FP64 cost depends on hardware; the reported 1.1 to 1.3x overhead was on an H100 | Xu 2025, Sec. 5.5 | on a consumer GPU, FP64 can cost far more per step, so S_P depends on this choice (inference) | measure FP32 and FP64 time and energy per step on the pilot machine before freezing |
| C4 | L-BFGS stops when the line search fails, with gradient norm still near 1e-2 to 1e-3 | Rathore 2024, Sec. 6 and Fig. 9 | early stop looks like convergence | log stop reason, final gradient norm, and iteration count; a stop is not a pass |
| C5 | Adam alone plateaus; the second-order phase does most of the accuracy work | Markidis 2021, Sec. 2.1; Rathore 2024, Sec. 6 | an Adam-only recipe may never reach 1e-3 | Adam then L-BFGS by default; the Adam phase is short and its length frozen |
| C6 | L-BFGS needs a fixed point set; full-batch training can over-fit the residual at those points | Grossmann 2024, Sec. 3.1; expert guide (preprint), Sec. 6.2 | low training loss, higher held-out error | large fixed Sobol set for the L-BFGS phase; validation on fresh points and parameters |
| C7 | Good error needs near-zero loss; loss alone does not certify error | Rathore 2024, Sec. 4; model-equations.md, Sec. 7 | stopping on loss can miss the target | gate on relative L2 error against a reference, never on loss |
| C8 | Training gets harder with operator conditioning and tighter tolerance (iterations of order κ ln(1/ε) in a linear model); failure grows with the PDE coefficient | De Ryck 2024, Thm. 2.3; Rathore 2024, Sec. 5; Krishnapriyan 2021, Sec. 3 | S_P rises from 1e-2 to 1e-3; the hardest corner of the parameter box fails first (inference) | report error over the whole box; held-out set includes the corners; gate on the worst case. With the model-equations candidate k = 1 + μ₁x + μ₂y, μ in [−¼, ¼]², k stays in [0.5, 1.5], so this risk is mild; it grows if the conductivity choice changes |
| C9 | Large learning rates cause spikes; stiffness bounds the stable step | PINNacle, Sec. 4.3; Wang 2021, Sec. 2.4 | diverged or wasted runs | lr 1e-3 with decay; NaN and infinity checks stop the run and mark it failed |
| C10 | Inputs far from order one slow training | model-equations.md, Sec. 4; expert guide (preprint), Sec. 3 | slower training | normalize inside the model (x̃ = 2x − 1, μ̃ = 4μ for the candidate bounds) so autograd keeps the chain rule |
| C11 | More points per step stop helping after a point | Chuang and Barba 2022, Sec. 3; PINNacle, Sec. 4.3 | energy spent on points that do not improve accuracy | pilot checks two batch sizes and keeps the smaller one if errors match |
| C12 | Point placement | Wu 2023 (grid worst; low-discrepancy and resampling good for smooth solutions); Markidis 2021 | wasted points or worse accuracy | random resampling in the Adam phase; Sobol set for fixed sets; adaptive sampling only as contingency |
| C13 | Network size sets query cost | Urbán 2025 (small networks can be enough); Markidis 2021 (four or more layers perform alike early on) | a larger network than needed raises e_P | pick the smallest candidate that passes the gate within budget; record size per run |
| C14 | How the parameters enter the network | Lazareva and Tarakanov 2026 (preprint, [background list](../references/background-papers.md)): FiLM conditioning gave about 10x lower error than input concatenation for operator-changing parameters | our plain four-input MLP may need more training than a conditioned design | keep the four-input MLP the plan fixes; if it fails the gate, raise FiLM as a design change for owner approval, with its cost logged |

### Stopping, selection, and cost

| ID | Catch | Evidence | Effect on the study | Handling |
|---|---|---|---|---|
| C15 | Stopping "by judgment" | Chuang and Barba 2022, Sec. 3 (stopped "without a quantitative criterion") | S_P depends on who decided to stop | a frozen, quantitative stop rule (Section 5) |
| C16 | Picking the best of many runs hides cost | Mishra and Molinaro 2022 (5 retrains per setting); McGreivy and Hakim 2024 (reporting bias) | S_P understated if only the winning seed is charged | all attempts go in the study ledger; the deployment retry policy states which attempts a user pays for |
| C17 | Untuned or lightly tuned setups, and tuning left out of the cost | Chuang and Barba 2022 (no tuning affordable); Wang, Wang, Perdikaris 2021 (λ tuned over six values) | both a weak PINN and a hidden tuning bill distort N* | a fixed, logged pilot tuning budget; tuning runs count as study electricity and are reported next to S_P |
| C18 | Checking the stop rule needs reference solutions, which are classical solves | Sun 2020 (no-data design); Huang 2026 (preprint), Sec. 4.5 | validation solves are a hidden setup cost (inference) | count validation reference solves in S_P, and count the classical grid study in S_C by the same rule (Section 5) |
| C19 | Monitoring has a cost: validation passes, logging, adaptive weights, NTK traces | Wang 2022, Sec. 6; expert guide (preprint), Sec. 5.2 | S_P includes or hides overhead | monitoring runs inside the training window and is counted; its interval is frozen |
| C20 | Per-query speedups quoted without training cost | Wang, Wang, Perdikaris 2021, App. C (inference up to 1000x faster; training up to 9.25 h) | a fast query is not a break-even | S_P and e_P stay separate in every table (research plan, Sec. 5) |
| C21 | Benchmark success is not our success | PINNacle uses a 10% error threshold and per-parameter retraining | borrowed success rates would overstate PINN accuracy | cite PINNacle for protocol only |
| C22 | Mixed precision between methods | Chuang and Barba 2022 (FP32 PINN, FP64 classical) | an accuracy or cost gap partly due to dtype | record the dtype of both methods; prefer FP64 for both unless C3 rules it out |
| C23 | Too few seeds to judge failure rate | 3 (PINNacle), 5 (Rathore), at least 10 (Krishnapriyan) | a failure rate from 3 seeds is weak | report failure counts per setting, not rates; three seeds is the minimum |

### Measuring and comparing

| ID | Catch | Evidence | Effect on the study | Handling |
|---|---|---|---|---|
| C24 | nvidia-smi samples only part of the runtime; updates every ~20 ms (V100) to ~100 ms (A100) | Yang et al. 2024 (SC24; details from the arXiv v3 preprint), Sec. 4 and 5 | short GPU blocks give wrong joules for S_P and e_P | GPU query blocks last at least 5 s, repeated in four trials with random gaps, rise-time samples dropped; measure training as one long window rather than per short phase |
| C25 | Weak classical baseline | McGreivy and Hakim 2024, rules 1 and 2, rec. 2 | false crossover | classical side uses the coarsest grid that passes each target; CPU versus GPU placement is justified |
| C26 | Classical cost per query may change with μ (for example, CG iterations depend on k) | Zhang et al. 2026 (preprint, background list), Sec. 3.3, state this limit of a constant per-query cost | a constant e_C can be wrong (inference) | record per-query classical cost across held-out μ; the linear-model check in the plan (Sec. 5) covers both methods |

## 3. Pipeline stages

Each stage lists what it produces and which cost bucket its energy and time go to. S_P is PINN setup including training, e_P is per-query cost, and "study" is the research ledger only (research plan, Section 4).

| Stage | What it does | Output | Cost bucket |
|---|---|---|---|
| 0. Config | load one TOML file, hash it, set all seeds, dtype, device, thread counts | run record header | study (negligible) |
| 1. Problem | define k(x, y; μ) and its gradient, source f, boundary multiplier, input normalization (model-equations.md, Sec. 3 to 5) | problem object | S_P (negligible) |
| 2. Parameter sets | training distribution over Θ, a small fixed validation set, a sealed held-out test set from a separate seed that includes the box corners; check the sets do not overlap | three parameter arrays with hashes | validation references: S_P; held-out references: study |
| 3. Model | MLP, tanh, Glorot init, four normalized inputs, output v; û = x(1 − x)y(1 − y) v | initialized model | S_P |
| 4. Loss | L_PDE: mean squared residual over a batch of (x, y, μ) points (model-equations.md, Sec. 6) | scalar loss | S_P |
| 5. Phase A, Adam | fixed step count, lr with exponential decay, points resampled every step, optional gradient clipping | checkpoint A | S_P |
| 6. Phase B, L-BFGS | fixed large Sobol point set, strong Wolfe line search, dtype-aware tolerances, iteration cap, keep the best checkpoint by validation error | checkpoint B, stop reason | S_P |
| 7. Monitoring | every M steps: loss, gradient norm, NaN check, validation relative L2 through the shared `evaluate.py` | training log | S_P |
| 8. Stop rule | frozen rule from Section 5 | final checkpoint and hash | S_P |
| 9. Gate | shared evaluation on the held-out set and fixed output grid G | per-parameter errors, pass or fail per target | study |
| 10. Query | load model once (setup), then per query: fill μ* into the prebuilt G input, forward pass under `torch.inference_mode`, synchronize, return û on G | solution on G | load: S_P; per query: e_P |

The query stage needs no derivatives. Since G is fixed and only μ changes, the coordinate part of the input is built once at setup; one query is filling in μ* and one batched forward pass (model-equations.md, Sec. 4). Energy is read over blocks of queries that last at least 5 s on GPU (C24), and per-query cost is the block total divided by the query count.

### Residual computation

For the candidate conductivity, model-equations.md Section 6 gives the expanded form r = −(1 + μ₁x + μ₂y)(ûₓₓ + ûᵧᵧ) − μ₁ûₓ − μ₂ûᵧ − 1, with k and its gradient known in closed form and autograd used only for û. A unit test with a manufactured solution must confirm the expanded form matches the divergence form −∇·(k∇û) − f, and that derivatives pass through the boundary multiplier.

## 4. Candidate defaults for the pilot

Starting values with the source range they come from. The pilot confirms or replaces each one, and every tuning run is logged.

| Setting | Candidate | Source range |
|---|---|---|
| Activation and init | tanh, Glorot (Xavier) normal, zero biases | Wang 2021, Rathore 2024, Markidis 2021; ReLU-like activations unsuitable (Markidis 2021, Sec. 2) |
| Network | 3 or 4 hidden layers; try widths 32 and 64 | 2 to 3 x 20 to 30 (Urbán), 3 x 20 (Sun), up to 6 x 256 (Chuang and Barba) |
| Boundary | Candidate A, û = x(1 − x)y(1 − y) v, for zero Dirichlet data | Sukumar 2022; Sun 2020; model-equations.md, Sec. 5 |
| Precision | FP64 for training and evaluation, unless the pilot shows its cost is unacceptable and FP32 passes the targets | Xu 2025; coding rules (float64 for references) |
| Adam phase | lr 1e-3, exponential decay, no weight decay, a few thousand steps (count fixed by the pilot) | PINNacle, Sec. 4.3; Markidis 2021 (plateau near 2,000 epochs) |
| L-BFGS phase | memory 50 to 100, strong Wolfe, tolerances above dtype epsilon, iteration cap from the pilot | Rathore 2024; Xu 2025 |
| Switch point | one frozen value after the pilot | Rathore tried 1k, 11k, 31k of 41k |
| Points per Adam step | a few thousand (x, y, μ) points, resampled each step | 256 (Grossmann, 1D) to 18,432 (Chuang and Barba) |
| Fixed L-BFGS set | Sobol points in the 4D input space | Wu 2023; Markidis 2021; Mishra and Molinaro 2022 |
| Loss weights | none needed with Candidate A; gradient-norm weights only as contingency | Wang 2021 |
| Safeguards | gradient-norm clipping in Adam; keep the best L-BFGS checkpoint by validation error | Lazareva and Tarakanov 2026 (preprint); kept because they are cheap and change no settled choice |
| Seeds | at least 3 per frozen setting | research plan, Section 4 |

## 5. Stopping, selection, and retry rules

These choices change S_P directly, so they need an owner decision before the main runs. Proposed rules:

1. **Stop rule.** Train with a fixed budget per target (Adam steps plus an L-BFGS cap), then gate. A rule that stops as soon as validation error meets the target is cheaper but needs references for the validation set, and its result depends on how often we check. If it is used, the check interval is frozen and the validation solves are charged (C18). Either way, no stop by judgment (C15).
2. **What "establishing accuracy" costs.** Treat both methods the same way. The classical grid-refinement study that picks the coarsest passing grid goes into S_C; the validation reference solves and monitoring go into S_P. Report the crossover with and without these terms so readers can see their effect.
3. **Selection.** If several seeds are trained, the deployed model is the one with the lowest validation error. The deployment estimate charges all seeds trained under the policy, not only the winner (C16).
4. **Retry.** A run that diverges, stops early without meeting the target, or fails the gate is kept and labeled. The deployment policy states the maximum attempts before the PINN is declared to fail that target. That failure is a valid outcome (research plan, Section 1).
5. **Gate rule.** A target passes only if every held-out parameter setting meets it, or a stated quantile does. The plan does not yet say which; worst case is stricter and fits C8. Decide before the gate and apply the same rule to the classical solver.

## 6. Run labels for training records

Each training run ends with one label in its record, so failures are counted, not lost.

| Label | Meaning |
|---|---|
| `passed` | meets the target on all held-out parameters under the gate rule |
| `missed_target` | finished the budget; error above target |
| `missed_some_parameters` | mean error passes, but some held-out parameters fail |
| `optimizer_stalled` | L-BFGS stopped on line search or tolerance with gradient norm above the recorded threshold |
| `diverged` | NaN or infinite loss or weights |
| `overfit_points` | training loss low, validation error rising on fresh points |
| `stopped` | stopped by a person or the budget guard before the planned end |

Where the cause is clear, add a short note: network too small, optimizer stalled or slow, or too few or badly placed points. Each points to a different fix with a different cost. The label stays factual; the cause is a note.

## 7. Pilot checks before freezing

Small runs, each with its own record and ledger row. They fill the open items in research plan Section 7.

1. Cost per training step in FP32 and FP64, on CPU and on GPU if available, measured with the planned energy counters (C2, C3).
2. On the 1D heat pilot: hard versus soft boundary handling, and Adam only versus Adam then L-BFGS (C1, C4, C5).
3. Two network sizes, to bracket accuracy and query cost (C13).
4. Two batch sizes and two L-BFGS point counts (C6, C11, C12).
5. GPU power sampling on the pilot machine: update period, and the shortest query block that gives stable joules under the Yang et al. practice (C24).
6. L-BFGS stop reasons are recorded and a NaN stops the run (C4, C9).

After these, freeze one recipe per target and do not change it during the main trials. Any later change gets a recorded reason, as the research plan requires.

## 8. Code plan

Following the [coding rules](coding-rules.md); module names are the starting layout there.

| Module | Holds |
|---|---|
| `problems.py` | k, its gradient, f, the boundary multiplier, parameter box, sampling of training, validation, and sealed held-out parameter sets |
| `pinn.py` | the model with built-in normalization, residual, Adam and L-BFGS phases, stop reasons, run labels |
| `evaluate.py` | one relative L2 function on grid G, used for both methods |
| `measure.py` | timing and energy windows per stage and per query block |
| `configs/*.toml` | every value in Section 4, the stop and retry rules, seeds, dtype, device, threads |

Tests, all fast and on CPU:

- The residual function returns near zero for a manufactured solution, in both the expanded and divergence forms, with derivatives taken through the boundary multiplier.
- û is exactly zero on boundary points.
- The training, validation, and held-out parameter sets do not overlap, and the held-out set includes the box corners.
- Two runs with the same seed and config on CPU give the same loss history.
- A NaN in the loss raises and marks the run failed.
- The evaluation function gives the same result for identical inputs from either method.

## 9. Sources used in this pass

All checked on 2026-11-17. PDFs are stored under the ignored `downloads/` path with SHA-256 hashes in each note, and read through the Markdown cache.

- New notes, shortlist Tier E: [Rathore et al. 2024](../references/rathore-2024-loss-landscape.md), [Xu et al. 2025](../references/xu-2025-fp64.md), [Sukumar and Srivastava 2022](../references/sukumar-2022-exact-bc.md), [Sun et al. 2020](../references/sun-2020-surrogate-no-data.md) (promoted from the background list), [Urbán et al. 2025](../references/urban-2025-optimization.md), [De Ryck et al. 2024](../references/deryck-2024-operator-preconditioning.md), [Wu et al. 2023](../references/wu-2023-adaptive-sampling.md), and [Wang et al. 2023](../references/wang-2023-expert-guide.md) (preprint).
- Full-text methods sections added to existing notes: Wang 2021, Wang 2022, Krishnapriyan 2021, Mishra and Molinaro 2022, PINNacle, Grossmann 2024, and the Tier D notes for Markidis 2021, Chuang and Barba 2022, Wang, Wang, Perdikaris 2021, Yang et al. 2024 (preprint version), and McGreivy and Hakim 2024.
- Background list only: Lazareva and Tarakanov 2026 and Zhang et al. 2026 (preprints, training and cost details added to their entries), and DeepXDE (Lu et al. 2021), moved there because other notes cover its points.

All reads were by an AI agent; a team member should check the claims used in the final report.

## 10. Decisions needed from the team

- Gate rule: worst case or a stated quantile over held-out parameters (Section 5, item 5).
- Whether validation reference solves and the classical grid study are charged to setup cost, as proposed in Section 5.
- Stop rule: fixed budget or target-based.
- Device and precision for PINN training and queries, after the C3 and C24 pilot checks.
- Maximum retry attempts in the deployment policy.
- Whether FiLM conditioning (C14) is allowed as a fallback if the four-input MLP fails the gate.
