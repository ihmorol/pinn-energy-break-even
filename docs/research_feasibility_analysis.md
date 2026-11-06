# Shape Optimization with Physics-Informed Neural Networks (PINNs)
## Research Feasibility & Green Computing Alignment Analysis

*Prepared: 2026-11-01 · Course: Green Computing*

---

## 1. One-paragraph pitch (for the faculty)

> Data centers consumed ~415 TWh in 2024 (~1.5% of global electricity), and cooling is the largest share of their overhead (~30–40% of facility energy). Most of that cooling energy is decided at the **design stage** — by the geometry of heat sinks, cold plates, and airflow ducts. Classical shape optimization needs hundreds of expensive CFD/FEM solves and hand-derived adjoint gradients. We propose to build a **mesh-free, fully differentiable PINN pipeline** that solves the governing physics (2D steady heat conduction with convective boundaries) and **simultaneously optimizes the shape** to minimize peak temperature — then we **validate against a classical finite-difference solver and measure the energy (kWh/CO₂) of both design loops**. The project applies computing to energy-efficient design *and* practices green-AI measurement of its own footprint.

---

## 2. Current state of research (what the literature says)

### 2.1 The field is established and active

| Year | Work | Relevance |
|---|---|---|
| 2021 | Cai, Wang, Yin, Karniadakis — *PINNs for Heat Transfer Problems* (ASME J. Heat Transfer, ~2,000 citations) | Foundational review; explicitly covers heat-sink design minimizing peak chip temperature |
| 2023 | Son et al. — *PINNs for Microprocessor Cooling* (IEEE) | Free-form heat-sink design; PINN predicts heat distribution across designs |
| 2023 | Sun et al. — *PINN surrogate + optimization of airfoils* (CMAME, ~175 citations) | PINN simultaneously models flow and maximizes lift-to-drag ratio |
| 2024 | Zhang, Lin, Wang — *Physics-informed shape optimization using coordinate projection* (Sci. Reports) | **Closest template for our project**: joint shape + field networks, validated in COMSOL, PyTorch + DeepXDE on an A40 GPU, ~1 h training per case, ~4 GB memory |
| 2024 | Grossmann et al. — *Can PINNs beat the FEM?* (IMA J. Applied Math, ~444 citations) | The honest-baseline paper: FEM is 1–3 orders faster for forward 2D Poisson solves; PINNs win as **amortized surrogates** for many-query / inverse / design problems |
| 2025 | Luo — *PINNs for PDE problems* (Springer AI Review, ~400 citations) | Up-to-date survey for the literature review chapter |
| 2025 | Du et al. — *PINNs for Advanced Thermal Management* (~80 citations) | Confirms PINN suitability for thermal design with limited data |
| 2025 | Liu et al. — CNN-PINN-DRL airfoil shape optimization | Shows the hybrid/extension directions we can list as future work |
| 2026 | Tay et al. — *Two-element airfoil optimization using NVIDIA Modulus* (AIAA J.) | Proof the production-grade tooling path exists |

**Key takeaway:** nobody doubts PINN shape optimization works — it's published in AIAA, CMAME, Sci. Reports, IEEE. The open, interesting question (and our defensible angle) is the **energy economics of the design loop**, which the literature barely quantifies.

### 2.2 The one thing we must be honest about

Grossmann et al. (2024) showed PINNs do **not** beat FEM at *solving a PDE once* (FEM 1–3 orders of magnitude faster on 2D Poisson). Our claim must therefore **never** be "PINNs are faster solvers." The defensible claims are:

1. **Amortization** — after training, evaluating thousands of candidate shapes is cheap (inference), so many-query design loops can win on total cost.
2. **Differentiability** — autodiff gives shape sensitivities for free; classical optimization needs a hand-built (or commercial, expensive) adjoint solver.
3. **Mesh-freeness** — no re-meshing per candidate shape, which is a real cost in classical loops.
4. And we **measure** all of this, including kWh — so even a negative result is a legitimate course research outcome.

---

## 3. Domain knowledge audit (the teacher's question)

The teacher asks: *do you have the domain knowledge to build this?* The honest answer is a **knowledge matrix**, not a "yes."

| Domain | What we need | Do we have it? | How we close the gap |
|---|---|---|---|
| Physics | 2D steady heat conduction ∇·(k∇T) + Q = 0; Dirichlet / Neumann / **Robin (convection)** boundary conditions; nondimensionalization | Core calculus + numerical methods course covers this; it is textbook-level PDE | Cai et al. 2021 review §heat sink; verify against hand-computed 1D fin solution |
| Numerics | Collocation sampling, residual minimization, convergence checking, finite-difference reference solver | Yes (numerical methods course) | Write a 50-line NumPy FDM solver — doubles as our validation baseline |
| Deep learning | MLPs, PyTorch autodiff, loss weighting, Adam + L-BFGS | Yes (ML coursework) | DeepXDE tutorials; Zhang et al. 2024 as recipe |
| Shape optimization | Shape parameterization (Bézier/B-spline boundary or coordinate projection), volume constraints, objective gradients via autodiff | **Gap** — but small: with PINNs the whole pipeline is differentiable, so we do NOT need classical adjoint theory | Zhang et al. 2024 method; start with 2–4 shape parameters (fin height, thickness, spacing) |
| Green computing metrics | PUE, energy attribution, carbon measurement | Course domain | Use CodeCarbon to log kWh/CO₂ of every experiment — this *is* the course deliverable |

**What we deliberately do NOT need:** turbulence modeling, 3D meshes, HPC, adjoint-solver mathematics (autodiff replaces it), commercial CFD licenses.

**De-risking statement for the teacher:** we scope to the *simplest physics that still carries the green story* — steady 2D heat conduction with convective cooling. If convection-coupled flow proves hard, we drop to pure conduction (still a valid fin-design study); if PINN shape optimization underperforms, the PINN-vs-FDM *energy-per-design-iteration* comparison is itself a publishable course result. Every failure mode degrades to a valid deliverable.

---

## 4. Green computing relevance — three layers

### Layer 1 — Application (strongest argument)
- Data centers: **~415 TWh in 2024, ≈1.5% of global electricity** (IEA); projected to roughly double by 2030 (AI demand).
- Global average **PUE ≈ 1.54** (Uptime Institute 2025) → ~35% of facility energy is overhead, and **cooling is the largest chunk (~30–40%)**.
- Every watt saved by better heat-sink/cold-plate/duct geometry multiplies: lower fan/pump power, lower chiller load, possibility of higher-temperature setpoints (free cooling).
- Transport angle (alternative application): aerodynamic drag reduction → fuel/charge energy; PINN airfoil optimization is published and repeatable.

### Layer 2 — Methodology
Design optimization is a *many-query* problem: hundreds of geometry evaluations. This is exactly where surrogates amortize (see §2.2 claims 1–3). We quantify it: **kWh per optimized design, PINN loop vs. FDM/FEM loop**. To our knowledge this specific energy accounting is rarely reported — it's a genuine (course-scale) contribution.

### Layer 3 — Meta (green AI hygiene)
We run the project the way green computing says you should: small models (6×50 MLP, like Zhang et al.), measured footprints (CodeCarbon), CPU/free-Colab-GPU only, reported in the final report. **The project's own carbon budget becomes a section of the paper.**

---

## 5. Feasibility assessment

### 5.1 Compute
- Zhang et al. 2024 trained their shape-optimization PINN in **~1 hour on a single A40 (~4 GB)**. Our 2D conduction problem is smaller.
- **Free Google Colab GPU is sufficient.** A modern laptop CPU suffices for the FDM baseline and small PINNs.
- Frameworks are mature and open-source: **DeepXDE** (PyTorch backend, Pythonic — recommended) or **NVIDIA PhysicsNeMo** (formerly Modulus; heavier, production-grade). Reference solver: NumPy FDM or scikit-fem/FEniCS. Measurement: CodeCarbon.

### 5.2 Scope (recommended minimum viable project — ~12 weeks)

| Weeks | Milestone |
|---|---|
| 1–2 | Literature review (use table §2.1); reproduce a DeepXDE 2D Poisson example |
| 3–4 | FDM reference solver for 2D fin/plate with convective boundary; verify against 1D analytical fin solution |
| 5–7 | PINN solver for the same problem; match FDM within a few % |
| 8–9 | Shape parameterization (2–4 params, e.g., fin height/thickness/spacing) + joint optimization loop (objective: minimize peak temperature subject to volume budget) |
| 10 | Energy accounting: kWh per design loop (PINN vs FDM-driven loop), CodeCarbon logs |
| 11–12 | Report + presentation: results, honest comparison, limitations (fixed topology, penalty constraints, sampling sensitivity) |

### 5.3 Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| PINN training instability (loss balancing) | Medium | Non-dimensionalize; self-adaptive loss weights (used by Zhang et al.); Adam→L-BFGS curriculum |
| Shape optimization converges to weak optimum | Medium | Start with 2 parameters; compare against a brute-force parameter sweep on the FDM solver (always available as ground truth) |
| Scope creep into Navier–Stokes | High ( temptation) | Freeze physics at conduction; flow is "future work" |
| "PINN vs FEM" criticism | Certain (a sharp teacher will raise it) | Pre-empt with §2.2 framing — we cite Grossmann et al. ourselves and *measure* the tradeoff |
| Compute shortfall | Low | Colab free tier + CPU baselines |

**Overall verdict: FEASIBLE** — 2D, steady-state, textbook physics, open tooling, free compute, with a guaranteed-minimum deliverable even in the worst case.

---

## 6. Convincing the faculty — anticipated Q&A

**Q1: "Is this green computing or mechanical engineering?"**
A: The deliverable is an *energy-efficiency study of a computational design method*. We optimize geometries that decide real cooling energy (Layer 1), we compare design loops by energy consumed (Layer 2), and we report our own experiment footprint (Layer 3). Green computing is both "make computing green" and "use computing to make energy use green" — we do both.

**Q2: "Do you have the domain knowledge?"**
A: Present the matrix in §3: required depth is undergraduate PDE + ML; the only gap (shape parameterization) is closed by one reproducible paper (Zhang et al. 2024) and the plan de-risks it with a guaranteed fallback deliverable.

**Q3: "PINNs are slower than FEM — why use them?" (they may cite Grossmann et al.)**
A: We cite the same paper in our proposal. We don't claim faster forward solves; we claim amortized many-query design loops + free differentiable gradients, and we measure kWh for both loops. If PINN loses, that's a valid, well-argued negative result.

**Q4: "What's new here?"**
A: (a) Energy-accounted comparison of PINN vs classical design loops (rarely quantified); (b) application framing on data-center thermal design; (c) a fully reproducible, footprint-reported pipeline.

**Q5: "Is this too hard for one trimester?"**
A: The 12-week plan has a fallback at every stage: no optimization → solver comparison; no PINN advantage → measured negative result; both are course-worthy.

---

## 7. Sources

- Zhang, Lin, Wang (2024). *Physics-informed shape optimization using coordinate projection.* Scientific Reports 14:6537. https://www.nature.com/articles/s41598-024-57137-4
- Grossmann et al. (2024). *Can physics-informed neural networks beat the finite element method?* IMA J. Applied Mathematics 89(1):143. https://academic.oup.com/imamat/article/89/1/143/7680268
- Cai, Wang, Yin, Karniadakis (2021). *Physics-informed neural networks for heat transfer problems.* ASME J. Heat Transfer 143(6):060801. https://asmedigitalcollection.asme.org/heattransfer/article/143/6/060801/1104439
- Son et al. (2023). *Physics-informed neural networks for microprocessor cooling.* IEEE. https://ieeexplore.ieee.org/document/10305161
- Sun et al. (2023). *Physics-informed deep learning for simultaneous surrogate modeling and optimization* (airfoil L/D). CMAME. https://www.sciencedirect.com/science/article/pii/S0045782523001664
- Luo (2025). *Physics-informed neural networks for PDE problems.* Artificial Intelligence Review (Springer). https://link.springer.com/article/10.1007/s10462-025-11322-7
- Tay et al. (2026). *Optimization of two-element airfoils using NVIDIA Modulus.* AIAA Journal. https://arc.aiaa.org/doi/10.2514/1.C038303
- Volume-preserving physics-informed geometric shape optimization (2024). https://arxiv.org/html/2407.19064v2
- NVIDIA PhysicsNeMo (formerly Modulus). https://github.com/NVIDIA/physicsnemo · https://developer.nvidia.com/physicsnemo
- DeepXDE. https://deepxde.readthedocs.io
- IEA — Data centre electricity consumption (~415 TWh, 2024; doubling by 2030). https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks
- Our World in Data — data centre energy share (~1.5% of global electricity). https://ourworldindata.org/data-centre-energy-use
- Uptime Institute Global Data Center Survey 2025 (average PUE 1.54). https://uptimeinstitute.com/resources/research-and-reports
- NeuralFoil / AeroSandbox (physics-informed airfoil analysis, pure Python). https://peter.sharpe.ai/neuralfoil
