Green Computing · research design

# Reaching the energy and computational break-even point between PINNs, and classical solvers.

Planned study. Nothing here is measured yet; values marked as candidates are frozen during the pilot.

## Problem definition

A parametric physics-informed neural network (PINN) is usually argued to be cheap to query once trained, but its training costs energy and time that a classical solver never spends. Within our literature search, nobody has measured whether that upfront cost is ever paid back: earlier comparisons report runtime for single solves or cost in modeled units, not metered electricity across a parameter family at matched accuracy. We ask how many new parameter queries N\* a parametric PINN must answer before its cumulative electricity, and separately its cumulative runtime, equals that of a tuned finite-difference solver that is re-solved for every query. The workload is one 2D steady-diffusion family, −∇·(k(x; μ)∇u) = f on the unit square, where two bounded parameters μ set a spatially varying conductivity. Both methods answer the same held-out parameters on the same output grid, at relative L2 error targets of 10⁻² and 10⁻³, on one controlled machine with a declared measurement boundary. The answer comes with an uncertainty interval and may be a finite crossover, a crossover too far away to be useful, or no reliable crossover; each is a valid result.

## Solution approach

1. **Define the problem.** Fix the family −∇·(k∇u) = f on (0, 1)² with the working candidate k = 1 + μ₁x + μ₂y, μ ∈ \[−¼, ¼\]², f = 1 and u = 0 on the boundary. Split parameters into disjoint training, validation and held-out sets, fix the shared output grid G, and set relative L2 error targets of 10⁻² and 10⁻³ (10⁻⁴ optional).
2. **Pilot and freeze.** Check the CPU, DRAM and GPU energy counters and their noise floor. Validate both methods on a 1D steady heat problem with a known solution. Size the query blocks (K queries, R repeats), the compute budget and the measured N range. Then freeze equations, bounds, network, seeds and budget, and tag the protocol in Git.
3. **Build both solvers.** Classical: five-point finite differences with k at cell faces; build A₀, A₁, A₂ once, then form A(μ) = A₀ + μ₁A₁ + μ₂A₂ and solve for each query. A refined-grid solution with a Richardson check gives the reference uref. PINN: one network (x, y, μ₁, μ₂) → û with the boundary condition built in, trained on the PDE residual over Ω × Θ with at least three seeds. Failed runs are kept and enter SP = Sprep + Etrain / q.
4. **Pass the accuracy gate.** Both methods answer the held-out parameters on G. A target goes forward only when both pass it; a miss is recorded as a result and kept out of the cost comparison.
5. **Measure energy and runtime.** Inside one declared boundary (CPU package + DRAM + GPU board, read for both methods): warm-up, K × R query blocks, synchronized timing and fixed clocks. Record setup cost S and per-query cost e in joules, times T and t in seconds, and mean power P̄ = E / t for each phase.
6. **Estimate the break-even points.** Fit E(N) = S + N·e for each method and check that the slope is stable. Compute N\*E = (SP − SC) / (eC − eP) and the runtime N\*T separately, with bootstrap intervals over seeds and trials. Classify the outcome as no crossing, one method cheaper throughout, an uncertain crossing, or an extrapolated crossing.
7. **Report.** A comparison table per accuracy target, crossover plots with uncertainty bands, and answers to Q1 to Q4 (existence, coincidence, accuracy effect, variance). The electricity used by the whole study is reported apart from the deployment cost model.

**Figure 1. Methodology.** Seven phases from problem definition to report. The pilot ends in a frozen protocol; both solvers are then built in parallel and meet at one accuracy gate on held-out parameters. Only qualified targets enter energy and runtime trials, which run inside one declared measurement boundary. Accuracy failures skip the trials and go straight to the comparison table. Every run, including failed and retried ones, is also logged to a separate study electricity ledger. PDE values shown are working candidates.

## Kept out of the diagram

The twelve-week timeline, the literature review, team roles, and repository and writing rules are project management, not method, so the figure leaves them out. They stay in the research plan.