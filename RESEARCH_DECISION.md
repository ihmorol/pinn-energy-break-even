# Research decision: one feasible project, not three parallel projects

**Prepared:** 2026-11-06  
**Status:** Recommendation and scope proposal, not a record of instructor approval.  
**Companion specification:** [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)

## TL;DR

**Start a fixed-geometry, sparse-sensor cooling-calibration study for one simplified server cold plate. Compare an inverse PINN against classical parameter fitting, then test the cooling-power decisions each estimate produces. Do not start shape optimization.**

The question is not “Can we make PINNs work somewhere in green computing?” It is:

> On a fixed 2D thermal benchmark, when do sparse, noisy temperature measurements support a reliable minimum-pump-flow decision, and does an inverse PINN improve that decision over classical fitting enough to justify its computation?

This is a deliberately reduced version of **Option B + Track 1**, restricted to server cooling. It removes moving geometry, EV batteries, unknown heat generation, arbitrary cooling fields, and facility control. It is one experiment pipeline, not an inverse project followed by a separate neural shape-optimization project.

**Verdict: Accept with Revisions.** The bounded version is plausible for a 12-week course project, subject to early numerical and resource gates. Its novelty is a **candidate contribution, not verified novelty**. A publishable positive result, a PINN advantage, and real-world energy savings are not guaranteed.

## 1. What the source document gets right

The supplied `PINNs in Green Computing Research.txt` contains useful project discipline:

- Validate an analytical special case, then a classical numerical reference, before trusting neural predictions (lines 4–5).
- Expect conventional solvers to be strong baselines on small forward problems (lines 49–51).
- Nondimensionalize, monitor boundary residuals, and use a limited training recipe rather than unbounded tuning (lines 52–57).
- Do not translate a lower temperature directly into fan or pump electricity savings (lines 58–64).
- Independently verify any decision selected using a learned model (lines 65–66).

Those principles should survive. The proposed expansion into multiple applications and research tracks should not.

## 2. Corrections needed before committing months

| Source claim or implication | Assessment | Required correction |
|---|---|---|
| Four to eight sensors can recover spatially varying cooling **and** an unknown hotspot profile (lines 85–86). | Not generally identifiable. Different heat inputs and cooling fields can explain the same measurements. A neural network does not create missing information. | Fix heat input and conductivity. Estimate at most two bounded cooling coefficients. Test whether those coefficients can be distinguished at the stated noise level. |
| Classical inverse estimation requires expensive adjoints or MCMC, so an inverse PINN has a decisive advantage (lines 77, 86, 123). | Misleading. With two unknowns, bounded least squares plus finite-difference sensitivities is a practical baseline. Classical automatic differentiation and adjoint methods also exist. | Compare with an actual classical inverse solver, not a forward solver asked to do no fitting. Let the experiment decide. |
| Adding inverse sensing is only a minor extension and is “highly publishable” (lines 83–86). | A small code change can introduce a large statistical and validation problem. Publication depends on evidence and the closest prior work. | Treat inverse calibration as the **whole research task**, not an add-on to geometry optimization. |
| A channel correlation restores “exact” physical penalties at almost no additional cost (lines 61–64). | Correlations have boundary-condition and flow-regime limits. Fully developed laminar heat transfer can be nearly flow-independent; coolant warming and hydraulic losses remain relevant. | Declare the heat-transfer and power laws, their assumptions, and a coolant-warming bound. Call synthetic operating-energy calculations what they are. |
| Very thin, dense fins are an inevitable optimum if convection is fixed (lines 59–60). | This depends on the geometry family, allowed fin count, material/footprint constraints, manufacturing bounds, and what is held fixed in the flow system. | Do not use an unspecified pathology to justify another large modeling extension. Remove geometry changes from this project. |
| Classical solves take 5–10 ms; training takes about an hour; code reuse is about 70% (lines 44, 51, 105–120). | These are not measured project results. Runtime depends on grid, solver, tolerances, hardware, and training convergence. There is no existing code here to reuse. | Measure a pilot and set a total experiment budget. Do not plan around a line count or a runtime promise. |
| More design dimensions will establish a PINN advantage (line 51). | Exhaustive grid search becomes expensive, but classical optimization need not use exhaustive grids. | Do not add dimensions to make the baseline lose. No speed or amortization claim without matched tasks and measured total cost. |
| Cooling fractions, PUE, and global electricity totals establish project savings (lines 3, 17). | They motivate the domain but do not quantify this device's benefit. PUE 1.54 implies about 35% **total non-IT overhead** for that ratio, not automatically 35% cooling. | Base the experiment on equal heat load, a temperature constraint, and an explicit pump-power model. Keep global extrapolations out. |

**Document-quality warning:** many equations and parameter values are missing from the TXT export. It is not an executable mathematical specification. The companion requirements supply a new, internally specified benchmark rather than pretending to recover the missing equations.

## 3. Which ideas are feasible, and which should we start?

| Idea in the document | Feasibility under the proposed course constraints | Decision for this project |
|---|---|---|
| Option A: heat-sink forward PINN and a few shape knobs | Reasonable course exercise if physics and constraints are consistent; application novelty is limited and full-loop efficiency gains are uncertain. | Do not select as the main research question. Retain only the analytical-validation discipline. |
| Option B: cold plate with moving channels and multiple heat sources | Possible after substantial modeling work, but “simple Poisson” hides geometry, coolant, and pumping assumptions. | Keep the cooling application; freeze geometry and use one known heat load. |
| Option C: motor core | Interface physics and meaningful loss estimation add learning and implementation work beyond smooth conduction. Magnetostatics alone does not establish motor operating-energy savings. | Exclude. |
| Track 1: unrestricted inverse sensing plus shape design | Overloaded and potentially unidentifiable as written. | **Select only its bounded inverse-calibration part, followed by one scalar operating decision.** |
| Track 2: battery SOH/RUL and knee prediction | Technically accessible public-data research, but battery-level splits, early-life information limits, degradation assumptions, and strong recent baselines are substantial work. Not an automatic novelty shortcut. | Exclude from this project. Do not run a second track. |
| Track 3: cooling control plus workload scheduling | A low-order simulator is possible. Credible control comparisons, workload effects, and safety validation make the complete version a larger project. | Exclude RL, workload scheduling, and online control. |
| Track 4: inverse building-wall properties | A bounded 1D inverse study is possible; multilayer parameters can also be confounded. It changes the application and prior-work search. | Exclude. |

This changes the original proposal: **shape optimization becomes out of scope**, not a stretch goal. The folder contains no syllabus, rubric, or approval record establishing that shape optimization is mandatory. Confirm that course-fit point before implementation; do not silently add shape optimization back if an approval issue arises.

## 4. The chosen contribution

### Paper type and story

**Type:** a new-setting / evaluation study, not a claimed new PINN architecture.

**One-sentence story:** Compare neural and classical calibration of a low-dimensional cooling model by the thermal violations, pump-power overhead, and computation of the operating decisions they produce, rather than by temperature-fit error alone.

### What could be new

The candidate contribution is an explicit **decision-reliability versus computation** benchmark:

1. Determine whether six virtual sensors contain enough information to estimate an average cooling level and a spatial trend.
2. Compare inverse PINN and classical fitting on exactly the same information and parameter bounds.
3. Propagate those estimates through the same conventional solver to a minimum-flow decision.
4. Measure where noise, fewer sensors, and one predeclared model mismatch invalidate apparent energy savings.

A nested scalar model tests whether the second coefficient is actually useful. A no-calibration controller tests whether simply avoiding an overprovisioned flow explains the savings. A known-parameter oracle shows the headroom left by each method.

**What is not new by itself:** using a PINN, estimating a Robin coefficient, adding an affine coefficient, using six sensors, using CodeCarbon, or attaching “green computing” to a heat equation.

### Novelty verification status

A live literature check was attempted through the configured gstack browser. It could not run because its compatible Chromium runtime is missing. No replacement browsing route was used, and no new software was installed.

Consequently, **no current literature-gap claim has been verified in this assessment**. The following are leads already present in the supplied files, not newly checked sources:

| Lead from the existing documents | Why it must be compared | Candidate distinction to verify, not assume |
|---|---|---|
| Grossmann et al. (2024), *Can physics-informed neural networks beat the finite element method?* [paper link](https://academic.oup.com/imamat/article/89/1/143/7680268) | Solver benchmarking and honest computation accounting. | This project evaluates inverse-calibration decisions, not only forward solves. |
| Zhang, Lin and Wang (2024), *Physics-informed shape optimization using coordinate projection*. [paper link](https://www.nature.com/articles/s41598-024-57137-4) | Original shape-optimization template. | This project does not deform geometry or jointly train a shape network. |
| Cited inverse convective-heat-transfer PINN study, arXiv:2507.09356. [source lead](https://arxiv.org/html/2507.09356v1) | Directly overlaps coefficient reconstruction from thermal measurements. | Need to check whether it already evaluates matched classical inversions and downstream pump decisions under mismatch. Authors, full title, and methods still need verification. |
| Wang et al. (2023), *Phyllis: Physics-Informed Lifelong Reinforcement Learning for Data Center Cooling*. [source lead](https://tanrui.github.io/pub/Phyllis-eEnergy23.pdf) | Existing physics-informed, energy-focused cooling decisions. | Fixed component, static calibration, and no RL; narrower scale alone does not establish a valuable gap. |

Before full experiments, build a five-paper comparison table from primary texts. Search at least: `inverse PINN convective coefficient sparse sensors classical inverse heat transfer`; `cold plate parameter identification pump flow thermal constraint`; and `physics informed cooling calibration model mismatch energy cost`. Record databases, search dates, queries, and exclusions. “No overlapping result retrieved” is not proof of firstness.

## 5. Feasibility and capability match

### What is actually known

The existing plans propose 12 weeks, a laptop CPU, free Colab, undergraduate numerical-methods/ML background, and synthetic reference data. They do **not** verify team size, weekly hours, actual memory, a submission date, physical data access, or instructor acceptance of this narrowed topic.

There are no solver implementations, datasets, tests, or result logs in the inspected project folder. The quoted roughly 4 GB memory / one-hour runtime belongs to a cited template, not a project benchmark.

### Planning envelope for the narrowed version

- One fixed rectangle; one steady linear PDE; at most two inverse parameters.
- One small PyTorch model; a CPU numerical solver remains the reference.
- No physical-data dependency. All sensor readings are explicitly synthetic.
- Proposed effort reserve: **180–240 focused team-hours across 12 weeks**, including testing and writing. This is a planning estimate, not known availability.
- Proposed compute ceiling: **40 GPU-hours total**, with measured active training memory below 3.5 GiB and CPU reference solves. These limits must be checked against actual resources before work starts.
- Hold out the last two weeks for reporting. Stop training expansion when a gate fails.

| Risk | Level | Bound or mitigation |
|---|---|---|
| Identifiability | Medium–high | Test classical sensitivities and fitting first; remove the spatial coefficient if unsupported. |
| PINN convergence | Medium | One architecture, two recipes maximum, timed pilot and fixed total budget. |
| Physical realism of energy estimates | Medium–high | Explicit synthetic laws, known hydraulic assumptions, withheld-flow check, no deployment claim. |
| Data access | Low for the synthetic study | No inaccessible sensor dataset or lab dependency. Physical validation remains absent. |
| Scope and timeline | Manageable only after narrowing | No geometry, RL, aging, second application, or second neural network. |
| Publication novelty | Unresolved | Literature gate before full experiment spending; no venue or acceptance guarantee. |

### Five-dimension evaluation

These are research-positioning scores, **not measured performance scores**. They start at 5; upward movements below are mechanism-based and unconfirmed.

| Dimension | Score / 10 | Basis |
|---|---:|---|
| Higher: better decisions | 6 | Calibrating a wrong nominal model can improve a thermal decision. That mechanism supports comparison with no calibration, not an assumed PINN win over classical fitting. |
| Faster: lower computation | 3 | A two-parameter classical inverse is strong; repeated PINN training creates a likely cost disadvantage. No speed claim is the project goal. |
| Stronger: reliability under noise/mismatch | 7 | The proposed experiment directly tests identifiable versus unsupported spatial inference and downstream violations. Improvement over baselines must still be demonstrated. |
| Cheaper: less data / total cost | 5 | Both estimators receive the same small sensor set. There is no evidence that the PINN needs fewer sensors or less total computation. |
| Broader: transfer across domains | 4 | Cross-domain generalization is deliberately excluded to make the project finishable. |

Emphasize decision validity and the cost of obtaining it. Do not broaden the application to inflate these scores.

### Paradigm-shift probe

This is **incremental research**, not a paradigm-shift proposal. It questions an assumption in these project documents (that inverse PINNs automatically add value), but no evidence here establishes that the whole field ignores this issue. There is no new enabling technology or basis for a landmark claim. That is compatible with a useful course study.

## 6. What counts as an actual result?

A result is a reproducible measured outcome from the specified experiment:

- Numerical error and energy-balance error of the reference solver.
- Whether the sensor data resolve one or two cooling parameters.
- Parameter, temperature, and held-out-flow prediction errors for each estimator.
- Independently evaluated thermal violations and simulated pump-power decisions.
- Full computation time, peak memory, and available energy estimates, including failed fits.

A negative outcome can answer the research question. For example: “The scalar classical fit selected decisions as well as the two-parameter PINN, at lower computation cost.” That is a result, not permission to hide the baseline or add a new topic.

**Simulation results are not measurements of a real cold plate.** If “actual results” means proven physical electricity savings in deployed hardware, the currently stated resources do not establish that capability. This proposal produces a controlled simulation study and clearly labeled energy scenarios.

Completing a course study, demonstrating a positive method effect, and earning a publication are three different milestones. None implies the next.

## 7. Start here

1. **Confirm resources and course fit.** Accept the fixed-geometry replacement explicitly with the instructor; verify time, CPU/RAM, and GPU access. Verify the closest literature before calling the angle novel.
2. **Build and test the classical benchmark first.** Verify the analytical slab special case, heat balance, mesh convergence, and a nontrivial feasible flow interval. Then test whether six noisy readings identify two coefficients.
3. **Only then train one inverse PINN.** Its job is to compete against the working classical inverse under the companion specification, not to establish its own correctness from training loss.

**The first milestone is not a trained network. It is a trustworthy reference problem with a measurable decision and identifiable unknowns.**
