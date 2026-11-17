# Model equations, inputs, outputs, and loss

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.

This document explains the mathematical design discussed in the chat. It uses readable Unicode symbols and plain-text equations so the notation remains visible in Markdown viewers without a math renderer. It is a technical explanation, not a session transcript or a frozen experiment protocol.

The [research plan](research-plan.md) remains the source of approved scope and protocol decisions. The main study is 2D steady diffusion with two conductivity parameters. Exact conductivity functions, parameter bounds, source values, and boundary values still need to be frozen during the pilot. No solver run or measured result is reported here.

## 1. Model input and output

```text
                 Parametric PINN
(x, y, μ₁, μ₂) ───────────────────→ û(x, y; μ₁, μ₂)
```

The model predicts one solution value at a supplied location and conductivity setting.

| Symbol | Meaning | Role |
|---|---|---|
| x, y | Spatial coordinates | Network inputs |
| μ₁, μ₂ | Physical parameters controlling conductivity | Network inputs; vary between PDE queries |
| μ = (μ₁, μ₂) | One conductivity setting | Constant within one PDE query |
| u | True PDE solution | Unknown function to approximate |
| û | Predicted solution | Physical model output |
| w | Neural-network weights and biases | Learned during training; frozen during deployment |
| k(x, y; μ) | Conductivity field | Known function calculated from coordinates and μ |
| f(x, y) | Source term | Fixed, known function |
| g(x, y) | Boundary values | Fixed, known function |
| Ω | Spatial domain | Fixed square |
| Θ | Allowed parameter domain | Fixed after the pilot |

Physical parameters μ and learned weights w are different quantities. This is a forward problem: we supply μ, calculate k, and predict u. The network does not identify μ or learn an unknown conductivity field.

For B points:

```text
Input shape:   B × 4
Output shape:  B × 1
```

Energy, runtime, and the break-even query count are not network outputs. They are measured or calculated outside the model.

## 2. General steady-diffusion equation

```text
−∇ · (k ∇u) = f           inside Ω = (0, 1)²

u = g                    on the boundary ∂Ω
```

The spatial gradient is:

```text
∇u = (∂u/∂x, ∂u/∂y)
```

Define the derivative notation:

```text
uₓ  = ∂u/∂x              uᵧ  = ∂u/∂y
uₓₓ = ∂²u/∂x²            uᵧᵧ = ∂²u/∂y²
kₓ  = ∂k/∂x              kᵧ  = ∂k/∂y
```

The expanded equation is:

```text
−[k(uₓₓ + uᵧᵧ) + kₓuₓ + kᵧuᵧ] = f
```

All derivatives are with respect to the spatial coordinates, holding μ₁ and μ₂ constant. Spatially varying conductivity requires the kₓuₓ and kᵧuᵧ terms; using only −k times the Laplacian would omit them.

There is no time input, time derivative, or initial condition for this steady main problem. The separate 1D heat pilot is not specified by this example.

**Source evidence:** Huang et al., Section 4.4, page 15, state the variable-coefficient Darcy equation −∇·(a∇u) = f on a square with zero boundary values. Their Supplement S10 specifies −∇·(a∇u) = 1. Relabeling permeability a as conductivity k preserves the mathematical operator. See [source 1](#source-1-variable-coefficient-equation-and-break-even).

## 3. A proposed example, not a finalized problem

For explaining the model, consider this nondimensional conductivity family:

```text
k(x, y; μ₁, μ₂) = 1 + μ₁x + μ₂y

−1/4 ≤ μ₁ ≤ 1/4
−1/4 ≤ μ₂ ≤ 1/4

f(x, y) = 1
```

For coordinates in the unit square:

```text
1/2 ≤ k ≤ 3/2
```

Conductivity therefore remains strictly positive for every permitted parameter pair.

Its spatial derivatives are:

```text
kₓ = μ₁
kᵧ = μ₂
```

Substitution gives:

```text
−(1 + μ₁x + μ₂y)(uₓₓ + uᵧᵧ) − μ₁uₓ − μ₂uᵧ = 1
```

The formula, bounds, and source above are proposed implementation choices from this discussion. They are not equations copied from a reference paper or approved protocol settings.

## 4. Input format and deployment queries

One input row is:

```text
[x, y, μ₁, μ₂]
```

Three evaluation locations for the same parameter query could be:

```text
x      y      μ₁      μ₂
0.10   0.20   0.15   −0.10
0.50   0.50   0.15   −0.10
0.90   0.80   0.15   −0.10
```

Coordinates vary between rows; the parameter pair stays fixed. During training, a batch can contain points from many parameter pairs, allowing one network to learn the parameter family.

For a complete deployment query, supply one new parameter pair μ* and evaluate the model at all M points of the common output grid:

```text
Input rows                         Output values
[x₁, y₁, μ₁*, μ₂*]                û(x₁, y₁; μ*)
[x₂, y₂, μ₁*, μ₂*]       →        û(x₂, y₂; μ*)
...
[xM, yM, μ₁*, μ₂*]                û(xM, yM; μ*)
```

The resulting M × 1 vector can be reshaped into a 2D solution field. Producing this whole field counts as one PDE parameter query, not M separate PDE queries.

### Optional input normalization

For the proposed bounds in Section 3, one possible normalization is:

```text
x̃  = 2x − 1
ỹ  = 2y − 1
μ̃₁ = 4μ₁
μ̃₂ = 4μ₂
```

Each normalized input lies in [−1, 1]. PDE derivatives must still be taken with respect to the original physical coordinates. Keeping normalization inside the differentiable model allows automatic differentiation to include the required chain-rule factors.

## 5. Boundary conditions and enforcement

For the proposed zero-Dirichlet example:

```text
Left edge:      u(0, y; μ) = 0
Right edge:     u(1, y; μ) = 0
Bottom edge:    u(x, 0; μ) = 0
Top edge:       u(x, 1; μ) = 0
```

These values do not change with μ.

### Candidate A: enforce the boundary through the output

Let v be the raw scalar output of the MLP. Return the physical prediction as:

```text
û(x, y; μ) = x(1 − x)y(1 − y) × v(x, y, μ₁, μ₂; w)
```

```text
Four inputs → MLP → raw output v → boundary multiplier → solution û
```

The multiplier is zero on all four edges. The physical prediction satisfies the zero boundary conditions by construction, so no boundary penalty is required.

PDE derivatives must be taken through the complete expression for û, including the multiplier. Differentiating only v would produce the wrong residual.

This is the recommended candidate for the particular zero-boundary example. Nonzero boundary values require a suitable boundary lifting or another enforcement method; this exact multiplier alone does not enforce arbitrary g.

### Candidate B: enforce the boundary through a penalty

Use the raw network prediction directly:

```text
û = v
```

Add a boundary-error term to the loss. This is soft enforcement, so a boundary error can remain after training. The hard-versus-soft choice must be recorded and frozen during the pilot.

## 6. PDE residual and loss function

### Residual

For the general problem:

```text
r = −[k(ûₓₓ + ûᵧᵧ) + kₓûₓ + kᵧûᵧ] − f
```

For the proposed conductivity and source:

```text
r = −(1 + μ₁x + μ₂y)(ûₓₓ + ûᵧᵧ) − μ₁ûₓ − μ₂ûᵧ − 1
```

An exact solution has r = 0 throughout the interior. Conductivity and source values are calculated from known functions. Automatic differentiation calculates the spatial derivatives of û.

### Interior physics loss

Sample Nᵣ points from the joint spatial and parameter domain Ω × Θ. Let rᵢ be the residual at the i-th sampled input.

```text
L_PDE(w) = (1/Nᵣ) × Σᵢ rᵢ²

The sum runs from i = 1 to Nᵣ.
```

With hard zero-boundary enforcement, the basic loss is:

```text
L(w) = L_PDE(w)
```

### Soft boundary loss

For Nᵦ boundary samples, let ûⱼ be the prediction and gⱼ the prescribed boundary value:

```text
L_BC(w) = (1/Nᵦ) × Σⱼ (ûⱼ − gⱼ)²

The sum runs from j = 1 to Nᵦ.
```

The combined loss is:

```text
L(w) = λᵣ × L_PDE(w) + λᵦ × L_BC(w)
```

λᵣ and λᵦ are training loss weights, not query inputs. With zero Dirichlet values, gⱼ = 0.

Interior solution labels are not required for this residual-trained PINN. Reference solutions are needed for validation and the final accuracy test. Adding solution-label supervision would be a separate training choice and its data-generation cost would need accounting.

**Source evidence:** Grossmann et al., Section 2.2, preprint PDF page 6, give an unnumbered training loss formed from mean squared PDE, boundary, and initial-condition residuals. Removing the initial-condition term for a steady problem, adding parameter inputs, and choosing hard boundary enforcement or weighted losses are adaptations for our study. See [source 2](#source-2-pinn-loss-and-accuracy).

## 7. Accuracy evaluation is separate from training loss

For the shared output grid:

```text
Relative error = ‖û − u_ref‖₂ / ‖u_ref‖₂
```

Here, û and u_ref are solution vectors on the same grid for the same parameter pair. For a vector q:

```text
‖q‖₂ = √(Σⱼ qⱼ²)
```

Our primary targets are:

```text
1% error:     relative error ≤ 0.01
0.1% error:   relative error ≤ 0.001
```

The optional stretch target is 0.01%, within the approved budget. The acceptance rule over held-out parameters and the reference-error allowance still need to be frozen during the pilot.

A low sampled residual loss does not by itself establish that the solution passes these error targets. Held-out parameters must remain outside training and tuning. Full energy trials for a target begin only when both methods pass its accuracy check.

**Source evidence:** Grossmann et al., Section 3.1, preprint PDF pages 7 and 8, state that both methods are assessed on the same mesh against ground truth using relative ℓ₂ error. The explicit vector formula and target values above follow our research plan.

## 8. What stays fixed and what varies

| Category | Fixed after protocol approval | Varies |
|---|---|---|
| Physical problem | Geometry, conductivity formula, parameter bounds, source, boundary values | Parameter pair and spatial location |
| Network design | Input normalization, architecture, activation, boundary-enforcement method | Weights during training |
| Training protocol | Budget, sampling rules, optimizer recipe, stopping rules, seed policy | Collocation samples according to the fixed rule; training seeds |
| Accuracy evaluation | Output grid, reference procedure, error definition, held-out test set | Predictions from each method |
| Deployment | Trained weights and reusable inference setup | New parameter pairs |
| Cost comparison | Controlled hardware, measurement boundary, query protocol and reuse policy | Measured energy and runtime |

Use at least three training seeds, as required by the research plan. Architecture, sample counts, loss weights, stopping rules, hardware, and budget remain pilot decisions until approved. The proposed example in this document does not freeze them.

## 9. Energy measurement and break-even analysis

### Measurement quantity

For a declared set of covered components, energy is the integral of their combined power over the measurement window:

```text
E = ∫ P_total(t) dt       from start time to end time

P_total(t) = sum of component powers within the declared boundary

Watts × seconds = joules
```

For cumulative energy counters, use the corrected start-to-end counter difference instead. The integral above is a measurement formulation, not a displayed equation quoted from Henderson et al.

Henderson et al., Section 4.3.1, page 10, Equation (1), give the process-attribution formula:

```text
e_total = PUE × Σ_processes
          (p_dram × e_dram + p_cpu × e_cpu + p_gpu × e_gpu)
```

Here, the p terms are resource-usage shares for attributable processes, and the e terms are component energies. This sum is over processes, not time samples. PUE is a facility-overhead factor, not an additional direct counter reading. Do not apply it without a justified model or present component readings as whole-machine electricity. See [source 3](#source-3-energy-accounting).

### Complete query cost

For one new parameter pair:

- PINN: evaluate the trained physical model on the common output grid, including necessary data movement and output handling.
- Classical solver: calculate conductivity, assemble or update the sparse system, solve it using valid reuse, and return the field on the same output grid.

A previously trained PINN does not retrain for each query. Classical meshes, sparsity patterns, and mathematically valid factorization or preconditioner reuse are retained.

### Cumulative energy model

```text
PINN:       E_P(N) = S_P + N × e_P
Classical:  E_C(N) = S_C + N × e_C
```

| Symbol | Meaning |
|---|---|
| S_P | PINN setup and training energy under the declared deployment policy |
| S_C | Classical setup energy |
| e_P | Mean PINN energy per complete parameter query |
| e_C | Mean classical energy per complete parameter query |
| N | Number of new parameter queries |

Setting the cumulative energies equal gives the candidate intersection:

```text
N_E* = (S_P − S_C) / (e_C − e_P)
```

The separate runtime intersection is:

```text
N_T* = (T_P,upfront − T_C,upfront) / (t_C − t_P)
```

T denotes upfront time; t denotes mean query time. Energy and runtime intersections need not coincide.

For the usual case S_P > S_C, the PINN recovers its extra upfront energy only if e_P < e_C. Equal or statistically uncertain slopes do not support a reliable finite crossover. Check the cost curves, nonnegative query counts, uncertainty, and linear-model adequacy before reporting either intersection.

### Reference-paper amortization equation

Huang et al., Section 4.5, page 16, Equation (1), state:

```text
N* = (N_tr × c_gen + C_train) / (c_cl − c_nn)

   = (γ × N_tr + τ) / (1 − 1/S),    for S > 1
```

```text
N_tr     : number of solver-generated training solutions
c_gen    : cost of generating one training solution
C_train  : training and tuning cost
c_cl     : classical cost per query at matched accuracy
c_nn     : neural surrogate cost per query
γ        : c_gen / c_cl
τ        : C_train / c_cl
S        : c_cl / c_nn
```

This is a computational-cost equation for learned surrogates; the paper's measured experiment uses FNO, not our residual-trained PINN, and it does not establish our electricity crossover. Our energy model adapts the amortization structure, includes both methods' setup costs, and requires our own measurements.

Training-data generation in that equation must not be confused with sampling PINN collocation points. Any reference generation, validation, tuning, or failed runs we carry out still belongs in the separate study-electricity account. The declared deployment model must state which of those costs it includes.

## 10. Source evidence and access limits

The following equations and passages were checked against the existing local PDFs on 2026-11-13. This document was prepared with AI assistance from that source check and the discussion; it needs team review before being used in a submission.

### Source 1: variable-coefficient equation and break-even

Yingchao Huang, Xin Wang, Shanshan Yao, Fanhua Zeng, Wei Peng. *Classical, Machine Learning, and Hybrid Solvers for Partial Differential Equations: An Evidence-Weighted Review and Decision Framework*. arXiv:2610.32911v1, 2026. **Preprint, not a verified journal publication.**

- [Primary source](https://arxiv.org/abs/2610.32911v1)
- [Workspace paper note](../references/huang-2026-solver-review.md)
- Local PDF: `downloads/huang-2026-solver-review/huang-2026-solver-review.pdf`
- Section 4.4, page 15: variable-coefficient Darcy equation on the square.
- Section 4.5, page 16, Equation (1): computational break-even formula and its S > 1 condition.
- Supplement S10, PDF page 54 (supplement printed page 19): particular problem with source 1 and zero boundary values.

Its random-field permeability family differs from our proposed two-parameter conductivity family. Its formula supports the operator and cost structure, not our candidate parameterization or an energy result.

### Source 2: PINN loss and accuracy

Tamara G. Grossmann, Urszula Julia Komorowska, Jonas Latz, Carola-Bibiane Schönlieb. *Can physics-informed neural networks beat the finite element method?* IMA Journal of Applied Mathematics 89(1), 143-174, 2024.

- [Published paper](https://doi.org/10.1093/imamat/hxae011)
- [Checked preprint version](https://arxiv.org/abs/2302.04107v1)
- [Workspace paper note](../references/grossmann-2024-pinn-vs-fem.md)
- Local PDF: `downloads/grossmann-2024-pinn-vs-fem/grossmann-2024-pinn-vs-fem.pdf`
- Section 2.2, preprint PDF page 6: unnumbered loss combining squared PDE, boundary, and initial-condition residuals.
- Section 3.1, preprint PDF pages 7 and 8: common-mesh comparison against ground truth using relative ℓ₂ error.

The checked page numbers refer to the preprint, not the journal pagination. The study compares FEM and PINNs using runtime; it does not measure energy or test our two-parameter PINN.

### Source 3: energy accounting

Peter Henderson, Jieru Hu, Joshua Romoff, Emma Brunskill, Dan Jurafsky, Joelle Pineau. *Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning*. Journal of Machine Learning Research 21(248), 1-43, 2020.

- [Published paper and PDF](https://www.jmlr.org/papers/v21/20-312.html)
- [Workspace paper note](../references/henderson-2020-energy-reporting.md)
- Local PDF: `downloads/henderson-2020-energy-reporting/henderson-2020-energy-reporting.pdf`
- Section 3.1, page 4: energy units and power-versus-energy distinction.
- Section 4.3.1, page 10, Equation (1): process-attributed CPU, GPU, and DRAM energy with PUE.

This paper supports measurement coverage and accounting. It does not give an experimentally verified PINN-versus-classical energy crossover.
