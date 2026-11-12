# Research plan

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.

**Course:** Green Computing

**Status:** Proposal submitted; implementation and experiments have not started.

## 1. Submission baseline

The research direction is fixed by the [submitted two-page proposal](ENERGY_CROSSOVER_PROPOSAL.pdf). The [Word source](ENERGY_CROSSOVER_PROPOSAL.docx) and PDF remain unchanged as the submission record. This document is the active working reference for the research team and supervisor.

The question is whether the setup and training costs of a parametric PINN are recovered through repeated use on **new parameter settings**, compared with an efficient classical PDE solver at matched accuracy. We will estimate the energy and runtime break-even points separately. Computational cost means measured runtime in this project, not an assumed operation count.

No crossover, an impractically distant crossover, and insufficient evidence for a reliable crossover are all valid outcomes. No measured results or claims of superiority are established yet.

## 2. Fixed workload and methods

| Component | Committed scope |
|---|---|
| Pilot | A 1D heat problem with a known solution. Validate the solver implementations, energy telemetry, timing approach, and feasible budget. This is a pilot, not a second full benchmark campaign. |
| Main problem | Steady diffusion on a 2D square. Two bounded parameters control a spatially varying conductivity; geometry and boundary conditions remain fixed. |
| PINN | A small parametric network implemented in PyTorch. Inputs are spatial coordinates and the two conductivity parameters; output is the solution value. Train across the parameter family, rather than retrain a separate network for every query. |
| Classical solver | Finite differences implemented with SciPy sparse solvers. Establish accuracy through grid refinement and an exact or independently checked reference solution. |
| Query | For one previously unseen parameter setting, return the solution on the common fixed output grid. Include the work needed to produce that output, not just an isolated kernel call. |
| Workload | Both methods receive the same held-out parameter settings and output grid. Keep final held-out parameters out of training and tuning. |

The exact equations, conductivity function, source term, fixed boundary values, parameter bounds, and reference construction will be specified during the pilot. These are implementation decisions within the submitted scope, not an invitation to add benchmark families.

Changing geometry, varying boundary conditions, extra parameter dimensions, additional PDE families, and broad solver/model surveys are outside this study. The 0.01% accuracy target is optional; the two-parameter PINN is not.

### Reuse and query fairness

- Retain meshes, sparsity patterns, and any mathematically valid factorization or preconditioner reuse in the classical baseline. A new conductivity setting can change the matrix, so factorization reuse must remain valid for that setting.
- Retain the trained PINN and reusable inference setup across queries.
- Neither method is charged for recomputing an identical cached answer. Repeated-query blocks must represent the defined workload of new parameter settings, not an artificial cache advantage.
- Document necessary assembly, data movement, and output-grid evaluation costs. Account for setup and per-query work consistently rather than assuming the classical solver starts from zero or PINN inference is free.

## 3. Accuracy and validation gate

Compare results using relative L2 error on the shared output grid:

$$
\varepsilon_{\mathrm{rel}} = \frac{\lVert u-u_{\mathrm{ref}}\rVert_2}{\lVert u_{\mathrm{ref}}\rVert_2}.
$$

| Target | Relative L2 error | Role |
|---|---|---|
| 1% | 1e-2 | Primary target |
| 0.1% | 1e-3 | Primary target |
| 0.01% | 1e-4 | Stretch target, only within the fixed training budget |

Use a known solution for the 1D pilot. For the main experiment, use an exact or independently checked reference and classical grid refinement; the baseline is not automatically its own ground truth. Define the reference-error allowance and the acceptance rule across held-out parameters before the full comparison.

Full energy trials for a target begin only when usable measurements are established and **both methods pass the accuracy check for that target**. Record errors and convergence failures separately for runs that miss the target. Do not compare an inaccurate fast run against an accurate slow run as though they solve the same task.

## 4. Measurement and cost accounting

### Hardware and measurement boundary

Run the comparison on one controlled machine. During the pilot, record the CPU/GPU, software versions, available counters, sampling resolution, and operating conditions. Define a common measurement boundary for both methods and state which components it includes or excludes. Device readings must not be described as whole-machine electricity without that coverage.

Available CPU and GPU energy counters will establish what can be measured. CodeCarbon may log readings or estimates, but estimates must be labeled as estimates. Do not silently compare GPU-only PINN readings with CPU-only classical readings as equivalent system totals. If the available telemetry requires modeled power, revise the measurement claim with the supervisor before the main trials.

### Trial protocol

- Separate setup, PINN training, and repeated-query energy and runtime. Classical setup is not assumed to be zero.
- Warm up before timed query blocks, synchronize GPU work for timing, and use long enough blocks to resolve energy above measurement noise.
- Repeat trials and use at least **three training seeds**. Record seed-to-seed and measurement variability, not just the best run.
- Fix and record the query distribution/order, batching, thread settings, device placement, repetition count, and treatment of idle/background energy. State how warm-up and preprocessing enter the accounting.
- Record energy units, elapsed-time units, counter coverage, and whether each value is measured or estimated. Energy is accumulated over the measurement interval, not inferred from a single instantaneous power sample without justification.

### Deployment cost versus study cost

Maintain a complete experiment log, including failed attempts and tuning. State a retry policy and which setup, training, failed-attempt, and tuning costs enter each deployment-cost estimate. Do not hide failures or assume a successful seed can always be selected at no cost.

Report the electricity used by the entire study in a separate log. This includes exploratory runs, validation, tuning, failures, and repeated measurements; it is distinct from the cost model for deploying one solver/model under the stated policy. Set a compute budget during the pilot and keep the stretch target inside it.

## 5. Break-even analysis

For a fixed workload, hardware configuration, and accuracy target, estimate cumulative energy as:

$$
E_P(N) = S_P + N e_P, \qquad E_C(N) = S_C + N e_C.
$$

Here, P is the PINN, C is the classical solver, S is setup energy including training where applicable, e is the measured or explicitly estimated mean energy per query, and N is the number of new parameter queries. The linear model assumes the stated workload and reuse policy; validate its adequacy rather than treating every query as inherently identical in cost.

When the per-query costs differ, the candidate intersection is:

$$
N^* = \frac{S_P-S_C}{e_C-e_P}.
$$

Use the actual cost curves to determine which method is cheaper on each side and whether the intersection is meaningful for nonnegative query counts. Equal or statistically indistinguishable slopes do not justify a reliable finite crossover. Distinguish no crossing, one method already being cheaper throughout, an uncertain crossing, and an extrapolated crossing beyond practical usage.

Replacing energy with runtime gives the separate computational break-even model. A faster method need not consume less energy, and an energy crossover need not coincide with a runtime crossover.

Report uncertainty ranges from repeated trials and training seeds. Keep runs that fail accuracy separate from accuracy-qualified comparisons. State any extrapolation, the usable query-count range, and the limits imposed by hardware, parameter bounds, measurement coverage, and solver/model choices.

## 6. Twelve-week work plan

| Weeks | Phase | Decision or output |
|---|---|---|
| 1–2 | Pilot and protocol | Check energy readings; solve the 1D pilot; confirm hardware and compute budget; freeze parameter ranges and evaluation protocol. |
| 3–5 | Classical and neural implementations, in parallel | Build and validate the reusable 2D finite-difference baseline; train the parametric PINN and log all attempts. |
| 6 | Accuracy check | Evaluate unseen parameters on the same grid. Admit only accuracy-qualified comparisons to full energy trials. |
| 7–9 | Energy trials | Measure setup and repeated-query costs with synchronized timing, repeated trials, and the declared measurement boundary. |
| 10–12 | Analysis and report | Estimate energy/runtime crossovers and uncertainty; report failures or absent crossovers; prepare figures, comparison table, and final report. |

## 7. Pilot decisions still to freeze

The direction is settled; the following protocol details are not yet settled:

- [ ] Controlled machine, energy-counter access, common component coverage, and any supervisor-approved estimation fallback.
- [ ] Exact 1D pilot and 2D diffusion specification, conductivity parameterization and bounds, boundary values, source, and reference construction.
- [ ] Training/validation/held-out parameter sets, fixed output grid, classical refinement procedure, and accuracy acceptance rule.
- [ ] Small network configuration, training budget, at least three seeds, stopping rules, and deployment retry policy.
- [ ] Query workload, batching, warm-up, repetitions, timing synchronization, background-energy treatment, and uncertainty method.
- [ ] Reproducible run settings and the experiment/study-energy logging format.

Freeze these after the pilot and before main trials. Record any necessary later protocol change and its reason; do not silently change the comparison to favor either method.

## 8. Deliverables and limits

- Validated classical solver and parametric PINN code.
- Trained models or documented convergence failures under the stated budget.
- Energy and runtime crossover plots, including uncertainty and cases with no reliable crossover.
- A comparison table at each attempted accuracy target, separating accuracy failures from qualified measurements.
- Reproducible run settings, hardware/software details, seeds, and complete experiment records.
- A separate log of the electricity used by the study itself.
- The final research report explaining when the lower-energy method can be selected for this workload.

Conclusions will remain specific to the tested hardware, problem family, parameter range, and accuracy requirements. The study does not promise that PINNs win, that energy and runtime rankings differ, or that its result generalizes to every PDE solver.

## 9. References from the submitted proposal

1. Grossmann, T. G., Komorowska, U. J., Latz, J., & Schönlieb, C.-B. (2024). *Can physics-informed neural networks beat the finite element method?* IMA Journal of Applied Mathematics. https://doi.org/10.1093/imamat/hxae011
2. Huang, Y., Wang, X., Yao, S., Zeng, F., & Peng, W. (2026). *Classical, machine learning, and hybrid solvers for partial differential equations: An evidence-weighted review and decision framework* [Preprint]. arXiv. https://arxiv.org/abs/2610.32911
