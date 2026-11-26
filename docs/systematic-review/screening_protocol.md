# Screening protocol: title/abstract stage

Version 1.0, eligibility rules confirmed by the requesting team member on 2026-11-23. Source: the project's submitted proposal, `docs/research-plan.md`, `docs/problem-definition.md`, and `docs/gap-analysis.md`. Full review protocol: `review-protocol.md`. The screening procedure was changed on the same day (amendment 1 below); the eligibility rules and exclusion codes did not change.

Review (scoping review for gap validation): "Energy and runtime break-even of physics-informed and other neural PDE solvers against classical numerical solvers".

Question: Has any study measured the energy of a neural PDE solver, or accounted for its training cost against repeated queries (a break-even or amortization analysis), in comparison with a classical numerical solver?

## Eligibility

- Problem: solving partial differential equations (PDEs), including families of PDE problems that vary in a parameter, coefficient, source, boundary condition or geometry.
- Method: a neural PDE solver (definition below).
- Concept: the computational cost of the neural solver is evaluated in at least one of these ways:
  - (i) Energy, power, or carbon of the computation is reported (measured or estimated). A classical comparator is not required for this route.
  - (ii) The cost is compared with a classical numerical solver and the comparison involves repeated use: a break-even or amortization analysis, offline (training) plus online (query) cost accounting, or a many-query or parametric workload.
- For route (ii), a physics-informed model compared with a classical solver on a parametric or many-query workload is enough. For any other neural surrogate, route (ii) needs an explicit break-even, amortization, or offline-plus-online cost accounting. A plain per-query speed-up claim is not enough for these models.
- Design: an original computational study, or a review that also reports its own new computation.
- Full-text-only criteria (whether cost is reported for both methods, whether training cost is included, whether accuracy is matched, how energy is measured, the value of any break-even count) must NOT be used to exclude at this title/abstract stage.

## "Neural PDE solver" (interpret broadly at screening)

Counts: a neural network that produces the PDE solution or a large part of it. Examples: PINNs and their variants (VPINN, XPINN, cPINN, hp-VPINN, PIKAN), deep Ritz and deep Galerkin methods, physics-informed DeepONet, physics-informed neural operators (PINO), neural operators (FNO, DeepONet), graph-network or CNN surrogates of PDE simulations, neural weather or climate emulators, and hybrids where a network replaces part of a classical solve (learned initial guess, learned preconditioner, learned correction).

Does not count on its own: Gaussian processes, polynomial chaos, or other non-neural surrogates; neural networks used only for data analysis, control, or classification; a network that only predicts a scalar from tabular data with no PDE behind it.

Exception, treat as unclear: the abstract says "surrogate model" or "machine learning" for a PDE simulation without saying whether a neural network is used.

## "Physics-informed model"

A neural model trained with the PDE residual (or a variational or energy form of the PDE) in its loss, with or without data. Examples: PINN, physics-informed DeepONet, PINO, deep Ritz.

## "Classical numerical solver"

Counts: finite difference, finite element, finite volume, spectral, boundary element, lattice Boltzmann, multigrid, Krylov or direct sparse solvers, reduced-basis or other reduced-order models built from classical solves, commercial or open solvers (COMSOL, ANSYS, Abaqus, OpenFOAM, PETSc), and numerical weather prediction models.

Does not count as a cost comparator: a classical solver used only to make training data or a reference for accuracy, with no cost comparison.

## "Energy, power, or carbon of the computation"

Counts: joules, kWh, watts, energy efficiency, power draw, carbon or CO2 emissions of training or running the model or solver; tools such as RAPL, NVML, nvidia-smi, CodeCarbon, Carbontracker, or a power meter.

Does not count: energy as a physical quantity of the modelled system (the energy consumption of a building, battery, power grid or machine, or an "energy functional" or "energy norm" in the mathematics).

## Decisions

- "include" (code INC): the record clearly describes a neural PDE solver and clearly meets route (i) or route (ii).
- "unclear" (code UNC): a neural PDE solver is plausibly involved and route (i) or (ii) is plausibly met, but the title/abstract is not enough. Examples: (a) a parametric physics-informed model "faster than" a solver, with no detail of what was timed; (b) "computational efficiency" or "cost" compared with FEM or CFD for a surrogate used in design optimization, uncertainty quantification or real-time use; (c) "green", "sustainable" or "efficient" computing mentioned for a neural PDE model without saying energy was reported; (d) no abstract, but the title suggests a neural PDE solver together with energy, break-even, amortization, or a many-query cost comparison.
- "exclude": give ONE code, the first criterion that clearly fails, checked in this order:
  - E1 publication type: editorial, erratum, correction, retraction notice, letter, news item, book front matter, conference abstract with no paper, patent, dataset or software record only, or a review, survey, tutorial or perspective with no new computation of its own.
  - E2 problem or method: not about solving PDEs with a neural PDE solver. Examples: ordinary differential equations only, time-series forecasting with no PDE, non-neural surrogates, physics-informed methods for data analysis.
  - E3 no cost element: the record evaluates accuracy, convergence or theory only, with no sign of computational cost, time, speed, efficiency, energy, power or carbon of the computation. Also use E3 when "energy" only means a physical quantity of the modelled system.
  - E4 no comparator and no energy: cost is reported only for the neural model or only against other neural models, and no energy, power or carbon of the computation is reported.
  - E5 runtime only, no repeated use: a runtime, speed-up or FLOP comparison with a classical solver that has no energy element and no repeated-use element. For physics-informed models, this means a single problem with no parametric or many-query workload, and no break-even or amortization. For other neural surrogates, this means no explicit break-even, amortization, or offline-plus-online cost accounting.
  - E9 other reason (explain).

## Principles

- Sensitive: missing an eligible study is worse than an extra full-text check; when in doubt between advancing and excluding, choose "unclear".
- Decisive: most records are clearly irrelevant; "unclear" only when a neural PDE solver and a cost element (energy, break-even, amortization, or a parametric or many-query cost comparison) are both plausible.
- Judge the record text only. Use the publication type in the record header for E1.
- A review or survey that says it also reports its own experiment or benchmark is not E1.
- Records in other languages are judged on content and flagged, not excluded for language.

## Amendment log

| Date | Change | Reason | Records to re-screen |
|------|--------|--------|----------------------|
| 2026-11-23 | Amendment 1. Dual AI screening of every record replaced by three zones: (1) scripted ranking of all records by title/abstract terms and metadata, with no record dropped for venue alone when it carries a strong gap signal; (2) one AI reader screens the titles of the top-ranked records; (3) the same reader screens their abstracts and ranks a final 40-50; the team then reads those and selects the studies used. These rules still decide each title and abstract judgement. | Requested by the team to limit token use; a human pilot of 100 labels was not feasible. | None; no record had been screened. |
