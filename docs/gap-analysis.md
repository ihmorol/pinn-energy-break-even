# Gap analysis

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.
**Written:** 2026-11-17 (AI-assisted; needs team review before use in the report)
**Status:** Literature phase. No solver, PINN, or energy run exists yet. Nothing here is a measured result.

## 1. Evidence rule

Each gap below rests first on **peer-reviewed** work (journals and archival conferences). Preprints are listed after it, marked "preprint", and are never the only support for a claim we plan to make.

A paper is used only when:

- its venue, volume, pages, and DOI resolve in Crossref (checked 2026-11-17), and
- the claim we use appears in its abstract or full text, read from the publisher, OpenAlex, arXiv, or the cached PDF. Search-engine summaries were not accepted.

Citation counts are OpenAlex `cited_by_count` on 2026-11-17. They show reach, not quality.

Limits: the 2026-11-17 search was targeted, not systematic. "Not found" means not found in our corpus, the 2026-11-12 search, or this search.

## 2. Venue status of the first-search papers

This section describes the 24 papers of the first search. Chatain et al. 2025 has since moved to the background file (Section 5, item 7), so 23 remain in the shortlist.

**Peer-reviewed (17):** Grossmann et al. 2024 (IMA J. Appl. Math.), Raissi et al. 2019 (J. Comput. Phys.), Karniadakis et al. 2021 (Nat. Rev. Phys.), Cuomo et al. 2022 (J. Sci. Comput.), de Hoop et al. 2022 (J. Mach. Learn.), Wang, Teng, Perdikaris 2021 (SIAM J. Sci. Comput.), Wang, Yu, Perdikaris 2022 (J. Comput. Phys.), Krishnapriyan et al. 2021 (NeurIPS), Mishra and Molinaro 2022 (IMA J. Numer. Anal.), Hao et al. 2024 (NeurIPS D&B), Henderson et al. 2020 (JMLR), Strubell et al. 2019 (ACL), Schwartz et al. 2020 (CACM), Patterson et al. 2022 (IEEE Computer), Luccioni et al. 2024 (FAccT), Dodge et al. 2022 (FAccT), Reddi et al. MLPerf Power (HPCA 2025).

**Not peer-reviewed (7):** Huang et al. 2026, Huang and Stuart 2026, Chatain et al. 2025, Kapoor et al. 2025, Wilson et al. 2025, Yoo et al. 2026 (all arXiv), and Lacoste et al. 2019 (non-archival workshop). A Crossref title search on 2026-11-17 found no published version of Kapoor, Wilson, Huang and Stuart, or Chatain.

The problem: the earlier version of this file leaned on the seven preprints for G2, G3, and G5. Huang et al. 2026 is also reference 2 of the submitted proposal. The proposal cannot change, but the report must label it unrefereed.

## 3. New peer-reviewed papers to add

All DOIs below resolved in Crossref. "Checked claim" is what we read on a primary page; nothing else from these papers should be cited until a member reads it.

### PINN and physics-informed cost against classical solvers

| Paper | Venue | Cites | Checked claim | Use for us |
|---|---|---|---|---|
| McGreivy and Hakim 2024, "Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations", [10.1038/s42256-024-00897-5](https://doi.org/10.1038/s42256-024-00897-5) | Nature Machine Intelligence 6:1256-1269 | 268 | 79% (60/76) of papers claiming to beat a standard numerical method used a weak baseline. "Rule 1 is to make comparisons at either equal accuracy or equal runtime." "Rule 2 is to compare to an efficient numerical method." PINN papers were excluded from the 76 because "standard numerical methods are known to outperform PINNs for solving forward problems" (arXiv HTML of the paper). | Primary source for the 79% figure (we cited it through Huang 2026). Peer-reviewed basis for matched accuracy and a strong classical baseline. |
| Chuang and Barba 2022, "Experience report of physics-informed neural networks in fluid simulations: pitfalls and frustration", [10.25080/majora-212e5952-005](https://doi.org/10.25080/majora-212e5952-005) | Proc. SciPy 2022, 28-36 | 67 | About 32 hours of PINN training were needed to match a 16 × 16 finite-difference run that took under 20 seconds (2D Taylor-Green). The cylinder case gave no physical solution. | Peer-reviewed PINN versus finite differences on time at matched accuracy. Time only, no parameters, no energy. |
| Markidis 2021, "The Old and the New: Can Physics-Informed Deep-Learning Replace Traditional Linear Solvers?", [10.3389/fdata.2021.669097](https://doi.org/10.3389/fdata.2021.669097) | Frontiers in Big Data 4:669097 | 344 | On Poisson, low frequencies converge fast but high frequencies need "an exceedingly long time". PINN-plus-classical hybrids performed on par with PETSc CG. | Accuracy-target risk for a PINN on an elliptic problem. No energy. |
| Wang, Wang, Perdikaris 2021, "Learning the solution operator of parametric partial differential equations with physics-informed DeepONets", [10.1126/sciadv.abi8605](https://doi.org/10.1126/sciadv.abi8605) | Science Advances 7:eabi8605 | 1436 | Learns parametric PDE solution operators "even in the absence of any paired input-output training data", predicting "up to three orders of magnitude faster compared to conventional PDE solvers". | Peer-reviewed precedent for physics-only parametric training, which is our PINN's setup. The speed claim is per query; the abstract gives no break-even. |
| Sun, Gao, Pan, Wang 2020, "Surrogate modeling for fluid flows based on physics-constrained deep learning without simulation data", [10.1016/j.cma.2019.112732](https://doi.org/10.1016/j.cma.2019.112732) | Comput. Methods Appl. Mech. Eng. 361:112732 | 1330 | A parametric surrogate trained "without relying on any simulation data", with boundary conditions built into the network. It is motivated by many-query cost, but the abstract states no runtime comparison with CFD. | Supports our hard boundary candidate (model-equations Candidate A) and the many-query motivation. |
| Penwarden, Zhe, Narayan, Kirby 2023, "A metalearning approach for Physics-Informed Neural Networks (PINNs): Application to parameterized PDEs", [10.1016/j.jcp.2023.111912](https://doi.org/10.1016/j.jcp.2023.111912) | J. Comput. Phys. 477:111912 | 110 | Metalearning and transfer learning "greatly accelerate the PINNs optimization process" for parameterized PDEs (arXiv abstract). The abstract does not name the baseline or cost unit. | Shows PINN training cost for parameter families is a known, open cost problem. |

### Energy measurement validity

| Paper | Venue | Cites | Checked claim | Use for us |
|---|---|---|---|---|
| Yang, Adámek, Armour 2024, "Accurate and Convenient Energy Measurements for GPUs: A Detailed Study of NVIDIA GPU's Built-In Power Sensor", [10.1109/SC41406.2024.00028](https://doi.org/10.1109/SC41406.2024.00028) | SC24, 1-17 | 77 | 70+ GPUs over 12 generations; on A100 and H100 "only 25% of the runtime is sampled"; proposed mitigations cut energy error by an average of 35%. | Required before trusting nvidia-smi joules for PINN training or queries. Was already flagged in the shortlist and is now verified. |
| Khan, Hirki, Niemi, Nurminen, Ou 2018, "RAPL in Action", [10.1145/3177754](https://doi.org/10.1145/3177754) | ACM TOMPECS 3:1-26 | 472 | RAPL readings are "highly correlated with plug power", "promisingly accurate enough", with negligible overhead. | Peer-reviewed support for RAPL as our CPU/DRAM counter. |
| Jay et al. 2023, "An experimental comparison of software-based power meters: focus on CPU and GPU", [10.1109/CCGrid57682.2023.00020](https://doi.org/10.1109/CCGrid57682.2023.00020) | IEEE/ACM CCGrid 2023, 106-118 | 179 | Compares several software power meters against high-precision physical meters under intensive CPU and GPU workloads. | Basis for choosing and labeling our tools. The results section was not readable (HAL blocked the fetch), so read it before quoting numbers. |
| Bouza, Bugeau, Lannelongue 2023, "How to estimate carbon footprint when training deep learning models? A guide and review", [10.1088/2515-7620/acf81b](https://doi.org/10.1088/2515-7620/acf81b) | Environ. Res. Commun. 5:115014 | 242 | Compares the energy estimated by several tracking tools on two image networks across server types. | Peer-reviewed reference for tool choice. It does not cover PDE solvers. |

### Classical side

| Paper | Venue | Cites | Checked claim | Use for us |
|---|---|---|---|---|
| Anzt, Tomov, Dongarra 2017, "On the performance and energy efficiency of sparse linear algebra on GPUs", [10.1177/1094342016672081](https://doi.org/10.1177/1094342016672081) | Int. J. High Perform. Comput. Appl. 31:375-390 (online 2016) | 34 | Compares performance and energy efficiency of sparse kernels and an LOBPCG eigensolver on GPU against a multi-threaded CPU version. | Shows sparse-solver energy is measurable and depends on CPU versus GPU placement. It does not compare against neural solvers. |
| Hesthaven, Rozza, Stamm 2016, *Certified Reduced Basis Methods for Parametrized Partial Differential Equations*, [10.1007/978-3-319-22470-1](https://doi.org/10.1007/978-3-319-22470-1) | SpringerBriefs in Mathematics | 1511 | Title-level only; not read. | The classical family built for many-query parametrized PDEs. Our scope fixes finite differences, so reduced basis is a limit to state in the report, not a method to add. |

## 4. Research gaps, rebuilt on peer-reviewed evidence

The cell-by-cell evidence, with page and section locations and the published runtime ratios, is in [gap-evidence.md](gap-evidence.md).

### G1. No metered-energy comparison of a PINN against a classical solver at matched accuracy

**Peer-reviewed evidence.** Every peer-reviewed PINN-versus-classical comparison we found measures time only: Grossmann et al. 2024 (FEM), Chuang and Barba 2022 (finite differences, 32 h versus under 20 s), and Markidis 2021 (PETSc CG). Wang, Wang, Perdikaris 2021 report speed, not energy. The peer-reviewed energy papers (Henderson, Strubell, Patterson, Luccioni, Dodge, MLPerf Power, Yang, Khan, Jay, Bouza, Anzt) cover ML or HPC workloads, not a PINN against a PDE solver.

**Preprint evidence.** Kapoor 2025 and Wilson 2025 estimate carbon with CodeCarbon and Carbontracker. Yoo 2026 meters neural-operator inference only.

**Gap.** Holds, and it is the strongest of the five. No peer-reviewed or preprint study found reports counter-measured joules for both a PINN and a classical solver at the same accuracy.

### G2. No break-even count for a parametric PINN against a classical solver

**Peer-reviewed evidence.** Physics-only parametric training is established (Wang, Wang, Perdikaris 2021; Sun et al. 2020), and its training cost is a known problem (Penwarden et al. 2023). Grossmann et al. 2024 name parameterized PDEs as not covered. None of these abstracts reports a query count at which training cost is paid back against a classical solver.

**Preprint evidence.** Break-even against classical solvers exists only for supervised operators (Huang et al. 2026; Zhang et al. 2026, arXiv:2605.15399). The parametric-PINN break-even in Lazareva and Tarakanov 2026 (arXiv:2606.04420) is measured against retrained PINNs, not a classical solver.

**Gap.** Holds, with one correction: a parametric PINN is not new in itself. Our contribution is the measured break-even, not the model.

### G3. Energy break-even and runtime break-even are never reported separately

**Peer-reviewed evidence.** Henderson et al. 2020 show FLOPs are a weak proxy for energy (R² = 0.083). Anzt et al. 2017 show energy efficiency of sparse solvers depends on CPU or GPU placement. Neither tests runtime against energy for a PINN-versus-solver comparison.

**Preprint evidence.** Wilson 2025: runtime is an unreliable proxy for carbon. Huang and Stuart 2026: the Darcy runtime gain came from hardware-efficient tensor operations, not fewer FLOPs.

**Gap.** Holds, but the direct support that runtime and energy rankings can differ in PDE work is preprint-only. In the report, state Q2 as an open question and do not present a divergence as expected.

### G4. Tuning, failed runs, and uncertainty are not carried into a break-even estimate

**Peer-reviewed evidence.** PINN training can fail or stall: Chuang and Barba 2022 (no physical cylinder solution), Krishnapriyan et al. 2021, and Wang et al. 2021 and 2022. McGreivy and Hakim 2024 find outcome-reporting and publication bias, so negative results go unreported.

**Gap.** Holds. No study found counts failed runs and tuning in a PINN-versus-classical break-even with an uncertainty interval. McGreivy and Hakim also support reporting "no crossover" as a result.

### G5. No PINN evidence on how the accuracy target moves the break-even point

**Peer-reviewed evidence.** Markidis 2021: high-frequency error on Poisson takes "an exceedingly long time". Chuang and Barba 2022: 32 hours to reach the accuracy of a coarse 16 × 16 finite-difference grid. Grossmann et al. 2024: FEM faster at equal or better accuracy.

**Preprint evidence.** Huang and Stuart 2026: operators plateau near 5×10⁻³ on 2D Darcy.

**Gap.** Holds. The peer-reviewed evidence points the same way as the preprint: the PINN may not reach 1e-3 within budget. Under our plan, that is a reportable result.

### Narrow statement of the gap

From peer-reviewed sources alone: PINNs have been compared with classical solvers on time, and physics-only parametric training exists, but no study found measures electricity for both methods, or reports the number of new parameter queries at which a parametric PINN's training cost is paid back in energy and in runtime, at matched accuracy against an efficient classical solver. Our study tests this on one 2D steady-diffusion family on one machine, and should claim nothing wider.

## 5. Changes to make in our literature

1. Done 2026-11-17: the six high-relevance papers (McGreivy and Hakim, Chuang and Barba, Markidis, Wang, Wang, Perdikaris, Yang et al., Khan et al.) have notes and sit in shortlist Tier D. The other six are in [references/background-papers.md](../references/background-papers.md) with short context, no notes. No PDFs were downloaded.
2. Cite McGreivy and Hakim 2024 directly for the 79% figure and the two fairness rules, instead of citing it through Huang 2026.
3. Move the seven preprints to a clearly labeled "preprint" tier. They can support context, but no gap or design rule should rest on them alone.
4. Use Yang et al. 2024 and Khan et al. 2018 as the measurement references for GPU and CPU counters, next to Henderson et al. 2020.
5. Fix [problem-definition.md](problem-definition.md) Section 2, point 2. It cites de Hoop et al. for "classical solvers win as the accuracy target tightens". Our check of de Hoop's cached text found FE only as a data/truth solver. Keep that claim on Huang and Stuart (preprint), and add Markidis 2021 and Chuang and Barba 2022 as peer-reviewed support for the accuracy-cost concern.
6. Re-check the preprints for published versions before the final report.
7. Done 2026-11-17: Chatain et al. 2025 moved from the shortlist to [background-papers.md](../references/background-papers.md) (unrefereed, not cited by any project document), so the first-search corpus is now 23 papers. Eight training-method papers were added as shortlist Tier E for the [training pipeline plan](training-pipeline.md).

## 6. Gaps in our own work

1. **No implementation.** No solver, PINN, or measurement code exists. `experiments/study-energy.csv` has a header and no rows. All six pilot decisions in plan Section 7 are open.
2. **Two conductivity candidates.** [problem-definition.md](problem-definition.md) Section 3 uses `k = k_min + (k_max − k_min)(θ₁ s₁ + θ₂ s₂)`. [model-equations.md](model-equations.md) Section 3 and `methodology and all/Break-Even Methodology.md` use `k = 1 + μ₁x + μ₂y`, `μ ∈ [−¼, ¼]²`. Choose one at the pilot.
3. **Baseline strength.** McGreivy and Hakim's rule 2 asks for an efficient numerical method. Our reference solution lists only SciPy `spsolve` and CG with Jacobi or ILU, while the closest priors use multigrid. The pilot must show our choice is efficient at our grid sizes.
4. **Stale notes.** 19 of 24 notes record abstract-level access only. No note has been read by a human member.
5. **Open checks.** Huang et al. 2026 author list; Grossmann Allen-Cahn text versus figure; Jay et al. results section.

## 7. From gaps to research questions: where to start

| Question (problem definition Section 6) | Gap | First thing needed |
|---|---|---|
| Q1. Does an energy crossover exist in a usable query range? | G1, G2 | A working counter setup and both solvers passing the accuracy gate |
| Q2. Do energy and runtime crossovers coincide? | G3 | Energy and time logged for the same runs |
| Q3. How does the target (1e-2, 1e-3) move N*? | G5 | Accuracy gate results at both targets |
| Q4. How wide is the seed uncertainty on N*? | G4 | Three or more seeds, failures kept in the ledger |

All four depend on the pilot (plan Section 7; [reference-solution.md](reference-solution.md) Section 8). In order:

1. On the chosen machine, confirm RAPL and nvidia-smi access, and run a short idle and load check. Apply the Yang et al. 2024 sampling caveat.
2. Freeze one conductivity function, the parameter bounds, and the output grid.
3. Build the 1D pilot: finite differences plus a small PINN against a known solution.
4. Benchmark `spsolve` against preconditioned CG on the pilot grid to settle the baseline (Section 6, item 3).
5. Write the first run records and ledger rows. From then on every run is logged, failures included.

None of these runs is authorized yet. The plan requires approval of the machine, protocol, and compute budget first.
