# Project requirements: sparse-sensor cooling calibration and pump decisions

**Version:** 1.0, proposed scope baseline  
**Prepared:** 2026-11-06  
**Short name:** Cold-Plate Calibration Benchmark  
**Decision rationale:** [RESEARCH_DECISION.md](RESEARCH_DECISION.md)

> **Scope contract:** One fixed, simplified server cold plate. One steady conduction model. One known heat input. At most two unknown cooling coefficients. One inverse PINN. One scalar flow decision. Matched classical baselines. No shape optimization, second application, or additional neural architecture.

This document specifies future work. **No solver has been implemented or validated, no experiment has been run, and no performance result is asserted here.** Numerical values below define a proposed synthetic benchmark, not measured hardware. Instructor approval and actual resources remain prerequisites.

## 1. Goal and research question

### 1.1 Goal

Produce a reproducible simulation study that establishes whether sparse temperature measurements support useful cooling calibration, and whether an inverse physics-informed neural network (PINN) improves the resulting cooling decisions over conventional parameter fitting at an acceptable computation cost.

A PINN is a neural temperature model trained using both measurements and the heat equation. An inverse problem estimates unknown physical parameters from measurements. Neither method is presumed superior.

### 1.2 One research question

> For a fixed 2D server-cooling benchmark, how do sensor noise, sensor count, and one bounded spatial model mismatch affect minimum-pump-flow decisions obtained from inverse PINN versus classical calibration?

The primary comparison is **inverse PINN versus a classical inverse**, not inverse PINN versus an uncalibrated forward solver.

### 1.3 Candidate contribution and evidence standard

The candidate contribution is a decision-oriented evaluation: coefficient identifiability, thermal-policy compliance, simulated pump-power overhead, and full computation cost in one matched protocol.

Novelty is provisional until G0's primary-literature review. The following are not novelty claims: using PINNs, estimating convection, using an affine coefficient profile, using six sensors, or logging CodeCarbon.

### 1.4 Three distinct definitions of success

| Level | Required evidence | Does it require PINNs to win? |
|---|---|---|
| Valid course deliverable | Verified reference, working classical inverse, bounded PINN attempt, locked evaluation, reproducible results including failures and limitations. | No. |
| Positive scientific result for the PINN | Better prespecified decision outcomes at comparable thermal compliance, or another clearly measured benefit, against the matched classical inverse. Training cost and variation must be included. | Yes, for a claim of PINN benefit. |
| Publication-ready contribution | Valid experiments plus verified differentiation from closest work and a result appropriate to a specific venue. | Not necessarily, but a negative result is not automatically publishable. |

“Actual results” means measured experiment outputs, not a guaranteed favorable conclusion. Because data are synthetic, the project does **not** demonstrate physical cold-plate or facility electricity savings.

## 2. Authority, assumptions, and resource envelope

### 2.1 What the existing project notes establish

- A proposed 12-week trimester project.
- Laptop CPU and free Colab as planned resources.
- Claimed undergraduate numerical-methods, PDE, and ML background.
- No existing implementation, dataset, experiment results, or measured project runtime in the inspected directory.
- Shape optimization in the original proposal, but no instructor-issued requirement establishing that it is mandatory.

Existing planning documents remain unchanged and are background. Once the team adopts this document, its scope supersedes the broader technical wishlist for this project. This is not a claim that adoption has already occurred.

### 2.2 Confirm before implementation

Record these items in the future run manifest before G0 closes:

| Item | Required record |
|---|---|
| Course fit | Instructor acceptance of a fixed-geometry inverse/operating-decision study instead of shape optimization. |
| Deadline | Actual start date, submission date, and available weeks. |
| Capacity | Team size, named task owners, and weekly focused hours. Do not infer these from the proposal. |
| Skills | One owner able to implement/debug a sparse linear solver and one able to debug PyTorch autodifferentiation; the same person may fill both roles. |
| Hardware | CPU, RAM, operating system, GPU/VRAM if available, and Colab availability. |
| Evidence access | Ability to obtain/read primary related papers. No lab or physical sensors are assumed. |

### 2.3 Proposed planning limits

These are budgets to approve, not observed requirements:

- **Duration:** 12 weeks; last two weeks reserved for figures, report, and presentation.
- **Effort reserve:** 180–240 focused team-hours total. Reassess before implementation if this capacity is unavailable.
- **GPU ceiling:** 40 GPU-hours for the entire project, including failed attempts, tuning, repeats, and final runs.
- **Per PINN fit:** at most 25 minutes wall time, including refinement; timeout is a recorded failed fit.
- **Measured training-memory ceiling:** 3.5 GiB active allocated GPU memory; record reserved memory too. A cited paper's memory use does not prove this requirement is met.
- **Architecture allowance:** one architecture and at most two predeclared training recipes.
- **Tools:** Python, NumPy, SciPy, PyTorch, pytest, Matplotlib, optional CodeCarbon. Pin actual compatible versions when the environment is built. Do not add a second PINN framework.
- **Spending:** no paid compute, new physical equipment, or commercial software without separate approval.

A pilot must show the frozen run matrix fits the budget with at least 20% time reserve. If not, invoke the stop rules; do not silently cut seeds after seeing results or buy more compute.

## 3. Locked scope and exclusions

### 3.1 In scope

1. One rectangular solid slab used as a simplified cold-plate thermal surrogate.
2. Steady 2D conduction with known conductivity and known heating.
3. Synthetic temperature observations from a separately refined conventional solver.
4. At most two bounded coefficients describing cooling at a known calibration flow.
5. One inverse PINN and conventional bounded least-squares calibration.
6. One-dimensional, bounded pump-flow selection using the same conventional forward solver for all estimators.
7. One sensor-count ablation, a small fixed noise matrix, and one spatial-mismatch family.
8. Time, memory, numerical accuracy, and available computation-energy estimates.
9. A report that allows the classical method, scalar model, or no-calibration policy to win.

### 3.2 Explicitly out of scope, including stretch goals

- Shape, channel, fin-count, topology, or free-form coordinate optimization.
- Parametric geometry PINNs, neural operators, coordinate-projection networks, and a second network.
- CFD/Navier–Stokes, turbulence, 3D conjugate heat transfer, transient PDEs, phase change, radiation, and temperature-dependent materials.
- Unknown heat generation, unknown conductivity, unknown hydraulic resistance, or arbitrary neural representations of h(x).
- Simultaneous EV, motor, battery-aging, building-envelope, or full-data-center applications.
- RL, workload scheduling, online control, real-time deployment, and safety certification.
- Hardware experiments, manufacturing claims, battery-life/embodied-carbon claims, and facility-level savings projections.
- Automatic hyperparameter search, adding sensors until a desired result appears, or enlarging parameter dimension to weaken classical baselines.
- A requirement to outperform FEM/FDM, obtain a particular savings percentage, or publish in a named journal tier.

## 4. Mathematical benchmark

### 4.1 Geometry, units, and proposed constants

| Quantity | Symbol | Proposed value | Interpretation |
|---|---|---:|---|
| Plate length | L | 0.05 m | x direction |
| Plate thickness | H | 0.005 m | y direction |
| Out-of-plane depth | B | 0.05 m | Converts boundary heat flux to watts |
| Conductivity | k | 200 W/(m K) | Known, homogeneous, constant |
| Total imposed heat | Q | 50 W | Fixed and equal for every method |
| Heated area | LB | 0.0025 m² | Entire lower face |
| Inward heating flux | q'' = Q/(LB) | 20,000 W/m² | Uniform lower-face flux |
| Representative coolant temperature | Tc | 25 °C | Fixed effective bulk reference, not a solved fluid temperature |
| Cooling coefficient scale | h_ref | 2,000 W/(m² K) | Synthetic reference value |
| Reference flow | Vdot_ref | 2 L/min = 3.3333e-5 m³/s | Known benchmark flow |
| Dimensionless flow | r = Vdot/Vdot_ref | [0.5, 1.5] | The sole operating decision |
| Calibration flow | r_cal | 1.0 | No other flow enters calibration data |
| Plate temperature limit | Tlim | 38.5 °C | Benchmark threshold, not a processor safety specification |
| Shared policy margin | m | 2.0 K | Fixed allowance, not a statistical confidence bound |
| Numerical allowance | epsilon_grid | 0.05 K | Must be supported by refinement checks |

Only temperature **differences** enter the thermal model; °C differences equal kelvin differences. Never compute relative temperature errors using an arbitrary absolute-temperature offset.

A single pre-freeze revision of benchmark constants is permitted only for G1/G2 feasibility criteria, with rationale recorded before any comparative PINN results. Changing constants to produce a PINN advantage is prohibited.

### 4.2 Governing equation and boundary conditions

Domain: Omega = (0,L) × (0,H). Solve

\[
\nabla\cdot(k\nabla T)=0.
\]

Let n be the outward unit normal and define outward heat flux q_out = -k grad(T) dot n.

- **Bottom y=0:** q_out = -q''. This is inward heating, not a prescribed temperature.
- **Top y=H:** q_out = h(x,r) [T(x,H)-Tc].
- **Sides x=0,L:** q_out = 0.

There is no Dirichlet boundary in this benchmark. Positive top convection removes the all-Neumann temperature ambiguity. Do not apply a fixed-temperature output transform merely because the source document recommends one for a different boundary-value problem.

The target temperature is the peak **modeled plate temperature**, not semiconductor junction temperature. Contact resistances and chip internals are excluded.

### 4.3 Low-dimensional cooling model

Define xi = 2x/L - 1 and

\[
h(x,r;a,b)=h_{ref}\,r^{1/3}\,[a+b\,\xi],
\qquad 0.8\le a\le1.2,\quad -0.2\le b\le0.2.
\]

- a describes average effective cooling.
- b describes a linear spatial trend.
- The box ensures a+b xi >= 0.6, so convection stays positive.
- Estimate **only a and b**; all other quantities are known inputs.
- The scalar nested model fixes b=0 and estimates a only.
- The coefficients are assumed independent of flow over the bounded interval. The experiment checks model prediction at withheld flows but does not prove this assumption for hardware.

The r^(1/3) relationship is an **imposed synthetic heat-transfer closure**, motivated by developing-flow scaling but not established as a correlation for a specified manufactured channel. Do not present it as a physically validated cold-plate law. Fully developed laminar channels may behave differently.

For a symmetric slab and uniform heating, changing b to -b reflects the temperature field but leaves peak temperature and the optimum flow unchanged. Recovering b's sign is not an energy benefit. Evaluate whether learning its magnitude helps compared with the scalar model.

### 4.4 Flow and pump-power closure

Use an explicitly assumed fixed hydraulic law and constant efficiency:

\[
\Delta p(r)=\Delta p_{ref}r,\qquad
P_{el}(r)=\frac{\Delta p(r)\dot V_{ref}r}{\eta}=P_{ref}r^2.
\]

The primary energy metric is **normalized electrical pump power** P_el/P_ref = r². No hydraulic parameter is inferred from temperature data.

For a clearly labeled illustrative watts/kWh scenario only, use:

- Delta p_ref = 20,000 Pa;
- eta = 0.4;
- P_ref approximately 1.667 W at 2 L/min.

These are illustrative assumptions, not pump measurements. Calibration coefficients represent thermal changes at unchanged/known hydraulics; do not interpret them as proof of fouling or blockage that would also alter the pressure curve.

### 4.5 Coolant-warming approximation

For the proposed water properties rho=1,000 kg/m³ and cp=4,180 J/(kg K), the simple bulk rise estimate is

\[
\Delta T_{bulk}=Q/(\rho c_p\dot V).
\]

At the minimum flow, this is approximately 0.72 K by hand calculation. G1 must verify the bound remains below 1 K for the frozen benchmark. This quantifies an omitted effect; it does not validate a uniform coolant temperature or certify the 2 K margin.

Do not expand into coolant PDEs if the bound fails. Revise the benchmark within the one allowed pre-freeze revision or stop the energy-decision claim. Sub-kelvin numerical accuracy must not be confused with sub-kelvin physical accuracy.

### 4.6 Independent analytical checks

For b=0 and spatially uniform h, the exact solution is

\[
T(y)=T_c+q''/h+q''(H-y)/k.
\]

Nominal rises are 10 K across convection and 0.5 K across the solid. These are analytical scales, not simulation results.

For scalar cooling, verify the continuous flow solution independently. Set

\[
D=T_{lim}-T_c-m-\epsilon_{grid}-q''H/k,
\qquad r_{req}=\left(\frac{q''}{h_{ref}aD}\right)^3.
\]

If D<=0 or r_req>1.5, the policy problem is infeasible. Otherwise r_star=max(0.5,r_req). The numerical grid selector must agree to within one flow-grid increment.

## 5. Classical reference requirements

**REF-01.** Implement a conservative, cell-centered finite-volume solver on the rectangle using NumPy/SciPy sparse linear algebra. This is the conventional numerical reference; do not add FEM as a second implementation.

**REF-02.** Apply heat input and Robin losses as boundary-face fluxes, with the boundary-to-cell conduction resistance treated consistently. Document corner treatment and interpolation. Do not rely on a promised “50-line” implementation.

**REF-03.** Use 40×8, 80×16, and 160×32 cell grids for convergence studies. Start classical fitting and operating selection at 80×16 and truth generation/evaluation at 160×32. Refine only if required by the numerical tolerances; log the change.

**REF-04.** Before generating experimental data, pass:

- Uniform-h exact-solution maximum error <=0.02 K at nominal and flow endpoints.
- Relative total heat imbalance <=0.1%, using the same discrete boundary fluxes as the solver.
- Difference in peak temperature and each sensor temperature between decision and truth grids <=0.05 K on predefined pilot parameter/flow cases.
- Demonstrated convergence toward the analytical solution, not just agreement between two grids.
- Finite temperatures above Tc for positive heating; symmetry/reflection tests where appropriate.

**REF-05.** Freeze a numerical allowance consistent with those checks. If epsilon_grid=0.05 K is not supported, refine; do not relax temperature comparisons after viewing method results.

**REF-06.** Generate synthetic measurements on the finer grid. Fitting must not access latent truth parameters or full-field data. Separate-grid generation reduces discretization reuse, but matched-model cases still assume the same physics family; mismatch tests address only the specified additional departure.

## 6. Sensors, data access, and identifiability

### 6.1 Fixed virtual sensor locations

Use six interior diagnostic sensors, with coordinates given as (x/L,y/H):

1. (0.08, 0.80)
2. (0.24, 0.20)
3. (0.40, 0.80)
4. (0.60, 0.20)
5. (0.76, 0.80)
6. (0.92, 0.20)

The three-sensor ablation uses indices **1, 3, 6**. Sensor placement is fixed before comparative results; no learned or optimized placement is in scope. These are virtual interior measurements, not a claim that a particular physical sensor package can be installed there.

Because the slab is nearly uniform through its thickness, lateral coverage matters more than adding repeated depths at one x. Sensor count alone is not proof of identifiability.

### 6.2 Observation model

At r=1,

\[
y_i=T_{truth}(x_i,y_i;r=1)+\varepsilon_i,
\qquad\varepsilon_i\sim\mathcal N(0,\sigma_T^2).
\]

Freeze noise in **kelvin**: sigma_T in {0, 0.25, 0.75} K for the main experiment. The zero-noise condition tests correctness; 0.75 K is a stress condition. No “percent sensor noise” shorthand.

Every estimator receives the same observed values, locations, known constants, parameter bounds, and noise metadata for a dataset. It does not receive truth fields, true a/b, mismatch coefficients, or withheld-flow temperatures.

### 6.3 Identifiability gate before PINN work

At the pilot points (a,b)=(0.9,-0.15), (1,0), (1.1,0.15):

1. Compute finite-difference sensitivities of the six predicted temperatures to a and b.
2. Check derivative stability after halving the perturbation size.
3. Scale each parameter by its half-range (0.2) and temperature by sigma_ref=0.25 K. Report singular values and condition number of this noise-scaled sensitivity matrix.
4. Fit noiseless finer-grid data with the classical two-parameter inverse from all declared starting points.
5. Compute a b-profile of weighted squared sensor residuals, optimizing a at each b. Use Delta chi-square=3.84 as an **approximate local diagnostic**, not a certified uncertainty interval.

Proposed go/no-go criteria:

- Numerical rank two and scaled sensitivity condition number <=50 at all three pilot points.
- Noiseless recovery: |a_hat-a_true|<=0.02 and |b_hat-b_true|<=0.04.
- The profile's nominal 95% b-interval at sigma_ref has total width <=0.20 and does not extend to both b bounds at at least two pilot points, including a nonzero-b case.

These criteria are provisional experiment-design gates, not observed results or universal identifiability theorems. Report profiles even if local rank passes. Do not use percentage error in b when b is near zero.

**If this gate fails after the one permitted pre-freeze revision:** fix b=0 for the inferential project. Retain spatially varying truth as an explicit model-limitation test, collapse duplicate scalar baselines, and withdraw spatial-recovery claims. Do not add a third parameter, sensors, a new geometry, or unknown heat input to rescue the story.

## 7. Required methods and fair comparison

### 7.1 Estimators

| ID | Method | Role |
|---|---|---|
| F2 | Two-parameter conventional inverse | Primary baseline: bounded nonlinear least squares using the reference solver. |
| F1 | Scalar conventional inverse, b=0 | Tests whether spatial calibration is needed at all. |
| P2 | Two-parameter inverse PINN | Candidate method under test. If G2 reduces dimension, it becomes P1. |

For F2, minimize squared sensor residuals with bounds and finite-difference parameter sensitivities using `scipy.optimize.least_squares`. Use fixed starting points (a,b)=(1,0), (0.85,-0.15), (1.15,0.15); choose the converged fit with the lowest sensor objective. F1 uses a starts {0.85,1,1.15}. Include all three starts in time/energy totals.

Do not penalize one estimator with extra priors or information. No regularization is required initially because the parameter family is bounded and small. If regularization becomes necessary, it requires a pre-freeze amendment giving both methods the same prior and reporting its effect.

Normalize the data term using sigma_eff=max(sigma_T,0.05 K) to avoid division by zero. This numerical floor does not change the stated noise or represent actual sensor uncertainty.

### 7.2 PINN specification

**PINN-01.** One fully connected temperature network: 2 coordinate inputs, four hidden layers of 32 tanh units, one scalar temperature output. Use dimensionless coordinates X=x/L, Y=y/H and temperature theta=(T-Tc)/DeltaT_ref, with DeltaT_ref=q''/h_ref=10 K.

**PINN-02.** Estimate only the network weights and the allowed physical coefficient(s). Enforce a/b bounds with a documented bounded transform initialized at (1,0). Log near-bound saturation. Truth at a boundary is not grounds for changing bounds after the fact.

**PINN-03.** Train only at r=1. The network is **not** a flow surrogate. Do not query it at new flows; all downstream flow decisions use the shared numerical solver.

**PINN-04.** Use dimensionless PDE, boundary, and data losses:

- Interior residual: (H²/DeltaT_ref)(T_xx+T_yy).
- Boundary residuals: (q_out minus prescribed outward flux)/q'', using the signs in Section 4.2. For the top face the prescribed flux is h(T-Tc).
- Sensor residuals: (T_pred-y_i)/sigma_eff.

Use a separate mean squared term for each boundary, rather than allowing a large boundary sample count to hide another boundary. Monitor held-out residuals and total heat balance. Small training loss alone is not a correctness test.

**PINN-05.** Start with float64, 1,024 interior points, and 128 points per boundary per Adam step. Use fixed seeded validation collocation points. Avoid mini-batch normalization layers and dropout, which complicate derivatives without serving this scope.

**PINN-06.** At most two recipes:

- A: dimensionless losses with fixed initial weights; Adam at 1e-3 for up to 10,000 steps, followed by fixed-collocation L-BFGS refinement with at most 1,000 closure evaluations.
- B: same model and iteration caps, adding clipped gradient-norm balancing between the PDE, boundary, and sensor loss groups during Adam. Freeze weights for L-BFGS.

For recipe B, start weights at one; every 100 Adam steps calculate each group's gradient norm with respect to network weights. Normalize inverse-gradient target weights to mean one, clip to [0.1,10], and update with an exponential average of 0.9 old + 0.1 target. Use epsilon=1e-12 in divisions. Keep individual boundary contributions visible in logs. Do not introduce another balancing strategy.

Both recipes remain subject to the 25-minute wall-time cap. Run pilot recipes on the pilot set, choose once using prespecified field-consistency and time criteria, and freeze it before the final matrix.

**PINN-07.** At the fitted coefficients, compare PINN temperatures with the conventional forward solution at those **same coefficients**. For a usable fit, require held-out temperature RMSE <=0.25 K, peak-temperature disagreement <=0.5 K, and total heat imbalance <=1%. These are physics-consistency diagnostics, distinct from accuracy against latent truth.

**PINN-08.** Nonfinite outputs, timeout, failed physical consistency, and optimizer failure receive explicit statuses. A failed PINN returns no calibrated decision. Do not replace it with the best seed or a classical fit under the PINN label.

## 8. Operating decision and attribution

### 8.1 Shared selector

For every usable estimate, select the lowest-power candidate on the same grid:

\[
r_j=0.5+0.005j,\quad j=0,1,\ldots,200.
\]

Minimize r_j² subject to

\[
T_{max,model}(r_j;\hat a,\hat b)+\epsilon_{grid}
\le T_{lim}-m.
\]

Enumerate the finite grid using the conventional solver. This is a 1D operating decision, not neural optimization. Use the smallest r when values tie. Do not optimize noise level, safety margin, or geometry.

If no grid point satisfies the constraint, return **NO_FEASIBLE_ACTION**. Never silently return r=1.5 and label it feasible.

### 8.2 Decision references

Apply identical heat load, limits, margin, grid, and hydraulic law to:

- **FIXED:** fixed r=1.5, representing an uncalibrated high-flow reference. Check truth feasibility; high flow is not guaranteed to satisfy every case.
- **NOMINAL:** no calibration, a=1,b=0, followed by the same selector. This tests whether simply reducing an overprovisioned flow explains apparent savings.
- **F1, F2, P2/P1:** calibrated estimates and the same selector.
- **ORACLE:** use the known truth model to select on the same grid with the same 2 K margin and numerical allowance. Under spatial mismatch, the oracle knows the mismatch too; no estimator does.

Do not attribute savings versus FIXED to the PINN unless its incremental benefit over F2 and NOMINAL is demonstrated.

### 8.3 Independent decision evaluation

Evaluate the selected r on the finer truth solver, never on the estimator's own field or calibration loss. Record both:

1. **Temperature-limit compliance:** T_truth,max + epsilon_grid <= Tlim.
2. **Margin-policy compliance:** T_truth,max + epsilon_grid <= Tlim-m.

The 2 K margin is a fixed policy allowance, not a learned uncertainty interval or a safety guarantee. Report violations of both thresholds and their maximum positive magnitude.

Against the margin-matched oracle, record signed normalized power gap `(r_selected² / r_oracle²) - 1`. A negative gap may mean the estimate has consumed the required margin; it is not automatically superior efficiency. Report policy-compliant comparisons separately.

Cases without an oracle-feasible action must not be silently excluded. Report them as benchmark-infeasible, along with false feasible decisions. Abstention/failed fits must appear in the denominator of all-dataset completion rates.

### 8.4 Simulated savings and annual illustrations

Relative modeled pump-power reduction against FIXED is `1 - (r_selected/1.5)²`. Report it only with compliance status and case counts. For fair policy comparisons, count margin-compliant results separately from merely temperature-limit-compliant results.

A watts-to-kWh illustration may use the assumed P_ref from Section 4.4:

\[
\Delta E_{op}=\frac{H_{op}}{1000}
[P_{ref}(1.5)^2-P_{ref}r_{selected}^2]\quad\mathrm{kWh}.
\]

Always state H_op, the fraction of cases to which the operating assumption applies, and whether calibration is repeated. Never multiply by global data-center electricity, PUE, or installed device counts to imply deployment savings.

## 9. Locked experiment matrix

Run G1/G2 pilots first. Freeze the experiment matrix at G2; select and freeze the PINN recipe at G3 using pilot results only. No final-matrix result may influence recipe selection.

### 9.1 Main matched-model experiment

Truth pairs:

- (1.0, 0.0): nominal.
- (0.8, 0.0): low cooling.
- (1.2, 0.0): high cooling / possible lower-bound decision.
- (0.9, 0.18): spatial trend with lower average cooling.
- (1.1, -0.18): opposite spatial trend with higher average cooling.

Use six sensors × three noise levels {0,0.25,0.75} K × three paired repetitions for each of five truth cases: **45 observation datasets**.

Use noise seeds {1101,1102,1103} and corresponding network initialization seeds {2101,2102,2103}. Pair each observation dataset across methods. At zero noise, the repeated observations coincide; those repetitions test neural initialization variability, not independent sensor noise.

### 9.2 Sensor-count ablation

Use the three sensor indices in Section 6.1, truth cases (1,0), (0.9,0.18), and (1.1,-0.18), sigma_T=0.25 K, and the same three paired repetitions: **9 additional datasets**. Derive three-sensor readings from the corresponding six-sensor observations so noise does not confound sensor count.

Do not redesign sensor placement for this ablation.

### 9.3 Spatial model mismatch

Use truth (a,b)=(0.9,0.15) with

\[
h_{truth}(x,r)=h_{ref}r^{1/3}
\left[a+b\xi+c\frac{3\xi^2-1}{2}\right],
\qquad c\in\{-0.1,+0.1\}.
\]

The extra quadratic term has zero spatial mean. It is unavailable to both inverse methods. Verify positivity for all x and allowed r.

Use six sensors, noise {0.25,0.75} K, and three paired repetitions: **12 additional datasets**.

This is **one mismatch family** with two signs. It tests spatial mis-specification, not a wrong flow exponent, unknown hydraulic resistance, coolant warming, or real-device generalization.

### 9.4 Withheld-flow prediction

For every usable fitted model, predict fields at r=0.75 and r=1.25 with the shared forward solver, and compare against truth. No measurements at those flows enter calibration. Also independently evaluate the selected action.

Matched-model held-out-flow accuracy does not validate the assumed r^(1/3) law physically; the same synthetic exponent is used to construct truth.

### 9.5 Run count and statistical reporting

- Maximum final PINN fits: **66** (45+9+12).
- At 25 minutes each, the fit ceiling is 27.5 GPU-hours, leaving 12.5 GPU-hours within the total cap for pilots, tuning, failures, and reruns. Confirm practical headroom at G3.
- Pair comparisons at dataset level. Report all three repetitions, mean/standard deviation or median/range as appropriate, and counts for every condition.
- Three repetitions provide limited uncertainty information. Do not call this a powered statistical trial, combine heterogeneous scenarios into a misleading significance claim, or report zero observed violations as a proven zero failure probability.
- Re-run only for documented infrastructure failures using the identical configuration and seed. Preserve the original failed attempt and its cost.

## 10. Metrics and required outputs

| Category | Required output |
|---|---|
| Reference correctness | Analytical error, grid convergence, discrete energy imbalance, analytical-versus-grid flow decision. |
| Identifiability | Scaled sensitivity matrix/singular values, profile curves, noiseless recovery, bound hits. |
| Coefficient estimation | Absolute a and b errors; b/a error where useful; not relative b error near zero. |
| Field prediction | Temperature-rise relative L2 error, temperature RMSE in K, peak error in K, including withheld flows. |
| PINN physical consistency | Same-fitted-parameter reference disagreement, independent PDE/boundary residuals, heat imbalance. |
| Decision completion | Usable fit count, timeout/failure count, no-action count, false-feasible count. |
| Thermal outcome | Temperature-limit and margin-policy violation fractions and maximum positive exceedance in K. |
| Operating energy | r, r², compliant reduction against FIXED, incremental result against NOMINAL/F2, signed margin-matched oracle gap. |
| Computation | Calibration, multistart, downstream selection and end-to-end wall time; peak memory; available energy estimates by stage. |

Every dataset row must retain truth-case ID, seed, observations, estimator, estimated coefficients, fit status, selected r or null, evaluation temperatures, both compliance flags, normalized power, and runtime. Keep latent truth in evaluator-only inputs, not estimator inputs.

Minimum final figures:

1. Reference convergence and analytical check.
2. Identifiability/profile evidence.
3. Temperature error and parameter error by method/noise.
4. Power versus thermal-policy compliance, including NOMINAL and ORACLE.
5. Sensor-count and spatial-mismatch effects.
6. End-to-end computation cost and failure counts.

No elaborate dashboard or application UI is required. Plain tables and reproducible plots are sufficient.

## 11. Computation energy and sustainability claims

**ENERGY-01.** Time every stage with an appropriate monotonic timer; synchronize GPU work before timing completion. Separate calibration from common downstream selection and full end-to-end totals.

**ENERGY-02.** Include initialization, all classical starts, PINN training/refinement, failed attempts, and tuning in a project-total ledger. Do not compare GPU inference alone with a full CPU optimization loop.

**ENERGY-03.** Where CodeCarbon/hardware telemetry is supported, record its version, measurement interval, device coverage, sampled versus estimated power, and carbon-intensity assumptions. Use offline/local logging. Do not transmit experiment data to an external tracking service without approval.

**ENERGY-04.** If energy attribution is unavailable on Colab/Windows, mark it missing. Report runtime and a separately labeled energy sensitivity estimate using stated average-power bounds; do not insert a plausible-looking measured kWh value. Do not add a large instrumentation task to rescue a missing sensor.

**ENERGY-05.** CPU/GPU differences are part of the systems comparison. Identify hardware and power coverage; do not claim algorithm-only efficiency from unlike machines.

**ENERGY-06.** Any net operating-versus-computation comparison must state deployment count, operating hours, and calibration frequency. Show the per-device case; do not assume one calibration benefits thousands of unrelated devices.

For a positive assumed operating reduction DeltaP_W and extra calibration energy DeltaE_compute_kWh, a scenario break-even time is

\[
H_{BE}=1000\,\Delta E_{compute,kWh}/\Delta P_W.
\]

If DeltaP_W<=0, there is no positive operating-saving break-even. If no incremental measured benefit over the classical method exists, do not claim that the PINN's added computation is environmentally justified.

No carbon reduction follows merely from logging carbon, fitting a lower temperature, or choosing a lower modeled flow.

## 12. Milestones, acceptance gates, and stop rules

| Gate | Deadline | Required evidence | Failure action |
|---|---|---|---|
| **G0: permission, resources, novelty positioning** | End Week 1 | Course-fit/resource record; scope accepted by the team; primary-text comparison of at least five relevant papers with dated search log and a one-sentence distinguishing question. | Do not claim novelty or begin full experimental spending. If course shape requirement conflicts, revise the proposal explicitly; do not append another workstream. |
| **G1: physics and reference** | End Week 3 | REF-04 checks; supported numerical allowance; coolant-rise bound; positive h; exact scalar decision agreement; at least one declared pilot has an interior feasible decision. | One documented pre-freeze benchmark revision shared with G2 is allowed. If still invalid, stop the energy-optimization claim and complete a numerical-methods report. |
| **G2: inverse identifiability** | End Week 4 | Section 6.3 sensitivities, profiles, and recovery criteria. | Reduce to scalar cooling; keep the same pipeline and report limits. No new geometry, extra unknowns, or application pivot. |
| **G3: PINN and budget feasibility** | End Week 7 | One frozen recipe; known-parameter and inverse pilot consistency; at least two of three inverse pilot fits pass PINN-07; active memory <=3.5 GiB; final matrix fits 40-hour budget with reserve. | End PINN tuning. Retain bounded failed experiments and complete classical/decision-limit results. No third recipe, larger network, or extra compute by default. |
| **G4: frozen evaluation** | End Week 10 | All feasible planned runs attempted or failures explicitly logged; independent action evaluation; baselines/ablations/mismatch included; no test-driven retuning. | Report negative/incomplete method evidence honestly; do not omit hard cases or add a favorable application. |
| **G5: delivery** | End Week 12 | Reproducible artifacts, results table, limitations, report and presentation. | State which acceptance items are missing. No claim of complete validation if a prerequisite failed. |

An informative project may contain a mix of lower-bound, interior, and no-feasible-action cases. Do not require every case to have an interior optimum or force positive savings.

### Hypotheses to test, not promises

- **H1:** Two cooling coefficients are identifiable at the reference sensor/noise configuration. G2 can falsify this before neural training.
- **H2:** Modeling spatial cooling improves decisions over F1/NOMINAL in at least some prespecified cases without worse compliance. If effects are within numerical/repetition variability, conclude no demonstrated value.
- **H3:** The PINN has a decision-quality or information-efficiency advantage over F2 that matters relative to its cost. A tie or worse result does not support H3, even if both beat FIXED.
- **H4:** Calibration-based decisions remain useful under the chosen noise and spatial-mismatch tests. Violations and abstentions bound this claim; they are not discarded outliers.

There is no minimum improvement percentage that the experiment must produce to be considered complete. Define any later claim threshold before evaluating the relevant data.

## 13. Proposed implementation and reproducibility deliverables

These are future artifacts, not files claimed to exist now:

```text
configs/benchmark.yaml              # frozen physics, sensors, laws, budgets
configs/experiments.yaml            # cases, seeds, methods, matrix
src/thermal_model.py                # constants, cooling law, analytic checks
src/reference_solver.py             # conservative finite-volume forward solve
src/inverse_classical.py            # F1/F2 fitting and profile diagnostics
src/inverse_pinn.py                 # the one network and two allowed recipes
src/flow_decision.py                # shared grid selector and compliance logic
src/evaluate.py                     # evaluator-only truth access and metrics
scripts/run_experiments.py          # seeded runs, timeouts, resume-by-ID
scripts/make_results.py             # tables and plots from saved rows
tests/                             # solver, inverse, decision, units, leakage tests
results/<run-id>/                   # immutable config, logs, metrics, versions
report/                            # final report, figures, presentation
requirements.txt                   # exact reproducible package versions
README.md                          # one small reproducible example and full-run guide
```

Paths are illustrative required responsibilities; avoid building a general plugin/configuration framework. The single run manifest is the source of truth for exact values and software versions.

Required tests include:

- Uniform-convection analytic temperature and flow decision.
- Boundary-flux signs, heat balance, refinement, and positivity.
- b to -b reflection/peak invariance in the symmetric model.
- Parameter bounds and noiseless classical recovery.
- Known-parameter PINN versus reference consistency.
- Out-of-range r and nonpositive coefficients rejected.
- Fully feasible, lower-bound feasible, no-feasible-action, and nonfinite-temperature decision cases.
- Same shared selector and margin for every method.
- Estimators cannot read evaluator-only truth or withheld-flow observations.
- W/m², watts, m³/s, L/min, normalized power, and kWh conversions.
- Fixed seeds, immutable result IDs, and infrastructure reruns that preserve failed attempts.

## 14. Change control and weekly scope check

Before adding any work item, answer:

1. Which requirement, gate, or hypothesis does it serve?
2. Is it required to interpret the existing experiment, or merely interesting?
3. Does it add a physical unknown, PDE, application, architecture, or data dependency?
4. What is its time/compute cost, and what already-planned work is removed?
5. Was the request motivated by seeing an unfavorable method result?

If it adds an excluded component, it is **rejected for this project** unless the team/instructor explicitly approves a revised scope, budget, and deadline. “Future work” is not permission to implement it during this term.

After the Week-4 freeze, constants, sensor positions, parameter bounds, noise matrix, decision margin, and evaluation metrics do not change in response to final results. Bug fixes must be documented and all affected methods/cases rerun consistently; preserve the old results as superseded, not erased.

At each weekly review, record:

- Evidence produced and current gate status.
- Remaining person-hours and consumed GPU-hours.
- Failures and unresolved assumptions.
- One next task tied to the next gate.
- Any rejected scope expansion.

## 15. Definition of done

- [ ] Instructor/course-fit and resource assumptions are explicitly recorded.
- [ ] Closest-work matrix exists; novelty statement is bounded by what was actually read.
- [ ] Analytical verification, heat balance, convergence, and numerical allowances pass.
- [ ] Identifiability evidence determines whether one or two coefficients are supported.
- [ ] Classical inverse and no-calibration baselines are operational and not weakened.
- [ ] The PINN receives a fixed-budget, reproducible evaluation, with failure counted if applicable.
- [ ] Flow decisions use the same selector and are independently evaluated on truth.
- [ ] Noise, three-sensor ablation, withheld flows, and the specified spatial mismatch are reported.
- [ ] All method comparisons show denominators, repetitions, failures, and compliance alongside energy.
- [ ] Runtime/memory and available energy evidence include full costs, not inference alone.
- [ ] Real measurements, numerical results, and illustrative annual scenarios are clearly separated.
- [ ] Code, frozen configurations, logs, result tables, report, and presentation are reproducible.
- [ ] No excluded workstream was added to compensate for an unfavorable result.

**Next action:** close G0, then implement the conventional slab solver and its analytical checks. Do not start by training the PINN.
