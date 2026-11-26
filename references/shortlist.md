# Literature shortlist for the break-even study

Built on 2026-11-12 by an AI-assisted deep research pass (four parallel verification tracks plus a recent-literature discovery track). Every identifier below was resolved against the arXiv API, Crossref, or OpenAlex, and the title was matched before the entry was accepted. Paper notes live in this directory, one per downloaded paper. PDFs are stored one per directory under the ignored `downloads/` path, with source and SHA-256 recorded in each note. Search snippets were never accepted as verification, and no entry below is copied from another list without its own identifier check.

Ranking criteria, in order: (1) directness of support for our break-even question, (2) usefulness for building and defending the experiment protocol, (3) venue strength and citation impact, (4) recency. Impact alone did not decide the order: the core picks are the papers our work starts from, not the most cited ones.

## Core papers (the work starts from these three)

1. [Grossmann et al. (2024), IMA Journal of Applied Mathematics](grossmann-2024-pinn-vs-fem.md). The direct predecessor: PINN versus FEM on Poisson, Allen-Cahn, and Schrödinger problems, matched accuracy, wall-clock time only. Its own limitations section names parameterized PDEs with amortized training as not covered, and the paper measures no energy. Our study is the parametric, energy-measured continuation of exactly that comparison. Note: `grossmann-2024-pinn-vs-fem.md`.
2. [Huang et al. (2026), arXiv:2610.32911 (proposal reference 2)](huang-2026-solver-review.md). The amortization law and decision framework our break-even analysis instantiates. Gives the closest quantitative prior for N* (break-even beyond 30,000 queries at errors below 1 percent on parametric Darcy flow) and the P0-P4 evidence ladder that places our planned comparison at rung P3. Note: `huang-2026-solver-review.md`.
3. [Henderson et al. (2020), JMLR 21(248)](henderson-2020-energy-reporting.md). The measurement-methodology anchor: counter-based tooling (Intel RAPL, nvidia-smi), the warning that extrapolated estimates are unreliable, and the reporting protocol (boundary, units, raw data, carbon statement) that our run records and study ledger follow. Note: `henderson-2020-energy-reporting.md`.

Why not the most cited papers as core: Raissi et al. 2019 (~22,900 citations) defines the method but not the measurement question; it stays as the mandatory method citation (rank 4). Karniadakis et al. 2021 (~10,150) is the field review and stays as introduction context.

## Tier A: break-even and cost-accuracy line (problem definition)

4. [Raissi, Perdikaris, Karniadakis (2019), J. Comput. Phys. 378](raissi-2019-pinn.md). Foundational PINN paper; defines the method under test. Local PDF is the Part I preprint, not the published text (recorded in the note).
5. [de Hoop, Huang, Qian, Stuart (2022), J. Mach. Learn. 1(1)](dehoop-2022-cost-accuracy.md). The cost-accuracy frame for parametric surrogates; justifies matched accuracy as the fair basis.
6. [Huang and Stuart (2026), arXiv:2609.24021](huang-stuart-2026-cost-accuracy.md). Closest published design analog in the post-training amortized regime; finds classical solvers win as accuracy tightens. Unrefereed preprint.
7. [Kapoor et al. (2025), arXiv:2505.12556, EcoL2](kapoor-2025-ecol2.md). Accuracy-versus-emissions metric across data, training, and deployment for neural PDE solvers.

## Tier B: PINN training cost, failure modes, and accuracy targets (solution design)

8. [Wang, Yu, Perdikaris (2022), J. Comput. Phys. 449](wang-2022-pinn-ntk-failure.md). NTK analysis of why PINNs fail to train; justifies seed variance and failure logging in the protocol.
9. [Wang, Teng, Perdikaris (2021), SIAM J. Sci. Comput. 43(5)](wang-2021-gradient-pathologies.md). Gradient pathologies and mitigations; mitigation costs belong in the ledger.
10. [Krishnapriyan et al. (2021), NeurIPS 2021](krishnapriyan-2021-failure-modes.md). Failure modes on diffusion operators; motivates the accuracy gate.
11. [Mishra and Molinaro (2022), IMA J. Numer. Anal. 43(1)](mishra-molinaro-2022-generalization.md). Generalization error bounds; anchors the fixed collocation budget and accuracy rule.
12. [Hao et al. (2024), NeurIPS 2024 D&B, PINNacle](hao-2024-pinnacle.md). Matched-condition benchmark design reference.
13. [Cuomo et al. (2022), J. Sci. Comput. 92(3)](cuomo-2022-pinn-survey.md). Field survey for the introduction.

## Tier C: energy measurement and green computing context (protocol and introduction)

14. [Strubell, Ganesh, McCallum (2019), ACL P19-1355](strubell-2019-energy-policy.md). Origin of ML energy accounting; canonical measured-power-then-extrapolate example.
15. [Schwartz et al. (2020), CACM 63(12), Green AI](schwartz-2020-green-ai.md). Efficiency as an evaluation criterion; the framing for our report.
16. [Lacoste et al. (2019), arXiv:1910.09700](lacoste-2019-carbon-emissions.md). Modeled-emission calculator (CodeCarbon ancestor); reference for the "modeled estimate" label.
17. [Patterson et al. (2022), IEEE Computer 55(7)](patterson-2022-carbon-plateau.md). Publishing emissions catches estimates off by 100x-100,000x; inference share context.
18. [Luccioni et al. (2024), FAccT 2024](luccioni-2024-power-hungry.md). Deployment energy per 1,000 inferences; per-query cost deserves measurement care.
19. [Dodge et al. (2022), FAccT 2022](dodge-2022-carbon-cloud.md). Location- and time-specific carbon factors; how to label any carbon conversion we report.
20. [Reddi et al. (2024), MLPerf Power, HPCA 2025](mlperf-power-2024.md). Standardized power benchmarking rules; discipline reference for our energy trials.
21. [Wilson et al. (2025), arXiv:2509.24517](wilson-2025-carbon-forecasting.md). Runtime alone is an unreliable proxy for carbon in PDE forecasting; supports measuring both.
22. [Yoo et al. (2026), arXiv:2609.30580](yoo-2026-energy-inference.md). Metered joules for neural-operator inference with fixed clocks; reusable protocol idea.
23. [Karniadakis et al. (2021), Nature Reviews Physics 3(6)](karniadakis-2021-physics-informed-ml.md). Authoritative field review (~10,150 citations); the introduction-context citation for the PINN research program. Local PDF is the DOE accepted manuscript.

## Tier D: peer-reviewed additions (added 2026-11-17)

Added after a second search limited to journals and archival conferences, done for the [gap analysis](../docs/gap-analysis.md). Each was verified in Crossref and has a note, but no stored PDF; notes record abstract-level access unless stated. Lower-relevance papers from the same search are kept in [background-papers.md](background-papers.md), not here.

24. [McGreivy and Hakim (2024), Nature Machine Intelligence 6(10)](mcgreivy-hakim-2024-weak-baselines.md). Primary source for the 79% weak-baseline figure and the two fairness rules (equal accuracy or runtime; efficient numerical method). Replaces citing that figure through Huang et al. 2026.
25. [Chuang and Barba (2022), Proc. SciPy 2022](chuang-barba-2022-pinn-pitfalls.md). PINN against finite differences at matched accuracy: about 32 hours of training against under 20 seconds. Time only.
26. [Markidis (2021), Frontiers in Big Data 4](markidis-2021-pinn-linear-solvers.md). PINNs on Poisson against PETSc CG; slow high-frequency convergence. Closest peer-reviewed evidence for our equation type.
27. [Wang, Wang, Perdikaris (2021), Science Advances 7(40)](wang-wang-perdikaris-2021-pi-deeponet.md). Physics-only training across a parameter family with no solver data; shows the parametric PINN itself is not our contribution.
28. [Yang, Adamek, Armour (2024), SC24](yang-2024-nvml-power-sensor.md). nvidia-smi samples only 25% of runtime on A100 and H100; needed before trusting GPU joules. Promoted from the list below.
29. [Khan et al. (2018), ACM TOMPECS 3(2)](khan-2018-rapl-in-action.md). RAPL readings are highly correlated with plug power; support for our CPU and DRAM counter.

## Tier E: how to train and check the PINN (added 2026-11-17)

Added after a full-text read of the methods and training sections, for the [training pipeline plan](../docs/training-pipeline.md). Identifiers were checked against the arXiv API and, where a DOI exists, Crossref. PDFs are stored under `downloads/` with hashes in each note. These papers decide training settings and failure handling; none of them measures energy. Papers already in Tier D (McGreivy and Hakim 2024) were not added twice.

30. [Rathore et al. (2024), ICML 2024](rathore-2024-loss-landscape.md). The PINN loss is ill-conditioned because of the differential operator; Adam then L-BFGS beats either alone; L-BFGS often stops early. Main support for our optimizer schedule and stop-reason logging.
31. [Xu et al. (2025), NeurIPS 2025](xu-2025-fp64.md). In FP32, PyTorch L-BFGS stops on rounding noise; FP64 removes the failure modes on their benchmarks. Decides how we check precision in the pilot.
32. [Sukumar and Srivastava (2022), CMAME 389](sukumar-2022-exact-bc.md). Exact Dirichlet conditions through a distance-function multiplier. Support for Candidate A in [model-equations.md](../docs/model-equations.md).
33. [Sun, Gao, Pan, Wang (2020), CMAME 361](sun-2020-surrogate-no-data.md). Parametric PINN with parameters as inputs, no solver data, hard Dirichlet conditions: the same design as ours. Promoted from the background list.
34. [Urbán, Stefanou, Pons (2025), J. Comput. Phys. 523](urban-2025-optimization.md). Small networks (2 to 3 layers of 20 to 30) reach high accuracy with better quasi-Newton optimizers. Bears on network size and so on query energy.
35. [De Ryck et al. (2024), ICLR 2024](deryck-2024-operator-preconditioning.md). Training iterations grow with operator conditioning and with tighter tolerance in a linear model. A prediction for how S_P moves between targets.
36. [Wu et al. (2023), CMAME 403](wu-2023-adaptive-sampling.md). Residual-point sampling compared: grid worst, low-discrepancy and resampling good for smooth solutions. Peer-reviewed support for our sampling choice.
37. [Wang, Sankaran, Wang, Perdikaris (2023), arXiv:2308.08468](wang-2023-expert-guide.md). Preprint. A full training recipe (scaling, Adam settings, resampling, loss balancing). Used only where a peer-reviewed source agrees.

## Tier F: 2025-2026 peer-reviewed additions for the gap analysis (added 2026-11-17)

A search limited to papers published in 2025-2026 in journals or archival conferences (Crossref and OpenAlex, then the papers' own pages). Most recent PINN papers found were applications or method variants, not cost comparisons. These three are the ones that matter for our study beyond the 2025 training papers already in Tier E (Xu et al., Urbán et al.); others from the same search are in [background-papers.md](background-papers.md). Each has a note, no stored PDF.

38. [Wang, Bhartari, Li, Perdikaris (2025), NeurIPS 38](wang-2025-pinn-gradient-alignment.md). Current state of the art for PINN training (second-order SOAP optimizer, 2-10x accuracy gains on 10 benchmarks). Keeps our PINN side from being a weak baseline; complements Urbán et al. 2025 on quasi-Newton optimizers.
39. [Chung et al. (2025), ML.ENERGY Benchmark, NeurIPS 38](chung-2025-ml-energy-benchmark.md). Newest peer-reviewed inference-energy measurement method; settings alone changed energy by more than 40%.
40. [Toscano et al. (2025), Machine Learning for Computational Science and Engineering 1](toscano-2025-pinns-to-pikans.md). Most cited recent PINN review; up-to-date companion to Karniadakis et al. 2021. No PINN-versus-classical cost comparison in the part read.

## Tier G: scoping-review full-text additions (added 2026-11-26)

Found by the scoping review in [docs/systematic-review/](../docs/systematic-review/README.md) and read in full (items 41-44 from arXiv copies, items 45-47 from the publisher or repository PDF). Each has a note and a stored PDF with its hash.

41. [Li, Jiang, Song (2026), arXiv:2611.10666](li-2026-parametric-pinn-microfluidic.md). Preprint. Physics-only parametric PINN against COMSOL FEM with an explicit wall-clock break-even of about 108 design evaluations, training included. It is not at matched accuracy, the hardware differs, and there is no energy. It removes "first PINN break-even" as a possible claim. (Earlier listed below as "not a benchmark"; that description was wrong.)
42. [Zhang et al. (2026), arXiv:2605.15399](zhang-2026-breakeven-complexity.md). Preprint. Breakeven complexity against an error-matched classical solver on the same hardware, with tuning counted. Supervised and foundation models only. This is the method standard closest to ours.
43. [Winkler and Stoll (2026), Journal of Computational Science](winkler-stoll-2026-flow-surrogates.md). Break-even formula of the same form as our cost model, for supervised flow surrogates; it leaves the configuration search uncharged.
44. [Sun et al. (2026), arXiv:2607.17318](sun-2026-fevessel.md). Submitted manuscript. Label-free (energy-trained) operator against AMG-preconditioned CG at a stated tolerance, with training time reported.
45. [Jediný (2025), bachelor's thesis, Charles University](jediny-2025-pinn-fdm-plasma-thesis.md). Single-problem PINN against an ADI finite-difference solver, with separate break-even points for time (N = 1253) and energy (N = 1303) over grid resolution. Energy is estimated from utilization times TDP, the hardware differs, and the break-even is extrapolated. It is the nearest prior energy break-even for a PINN.
46. [Tandale and Stoffel (2024), Engineering with Computers](tandale-2024-spiking-fem.md). Spiking network inside an FE solver: runtime against classical FE, and modelled per-forward-pass energy across hardware. No network-against-FEM energy comparison.
47. [Xue et al. (2026), Nature Communications](xue-2026-geothermal-operator.md). Physics-constrained neural operator with a 1,400-fold speedup that excludes model construction and data generation. An example of a speedup reported without training cost.

## Verified entries without a stored PDF (shortlist only)

These were verified against Crossref, OpenAlex, or the arXiv API on 2026-11-12 but were not downloaded (no open-access PDF found, or the paper is supporting context only). Access is listed as the reason.

- Mishra and Molinaro (2022), inverse-problem companion, IMA J. Numer. Anal. 42(3):981-1022, DOI 10.1093/imanum/drab032, arXiv:2007.01138, ~406 citations. Open-access preprint exists; not downloaded because the forward-problem note covers our need.
- De Ryck and Mishra (2022), "Generic bounds on the approximation error for physics-informed (and) operator learning", NeurIPS 2022, arXiv:2205.11393, ~53 citations. Open-access preprint exists; not downloaded (approximation theory context).
- Fuks and Tchelepi (2020), "Limitations of Physics Informed Machine Learning for Nonlinear Two-Phase Transport in Porous Media", J. Mach. Learn. Model. Comput. 1(1):19-37, DOI 10.1615/jmachlearnmodelcomput.2020033905, ~322 citations. No open-access PDF found; add if failure-regime examples beyond diffusion are ever needed (scope check first).
- Anthony, Kanding, Selvan (2020), Carbontracker, arXiv:2007.03051, ~661 citations. Overlaps with the Lacoste and Henderson notes.
- Wu et al. (2022), "Sustainable AI", MLSys 2022, arXiv:2111.00364, ~557 citations. Industry-scale context; not load-bearing for our protocol.
- Novo and Terrés (2025), "Can neural networks learn finite elements?", J. Comput. Appl. Math. 453:116168, DOI 10.1016/j.cam.2024.116168, arXiv:2405.06488, ~3 citations. Numerical-analysis follow-up to Grossmann et al.
- Kirchdoerfer and Ortiz (2016), "Data-driven computational mechanics", CMAME 304:81-101, DOI 10.1016/j.cma.2016.02.001, ~834 citations. Background only; outside our fixed scope.

## What the search found and did not find

Within the scope searched (arXiv, Crossref, OpenAlex, DBLP attempts, and web search, checked 2026-11-12): no published study reports metered (counter-measured) PINN training electricity compared against a classical PDE solver at matched accuracy. The nearest works measure modeled carbon in PDE contexts (EcoL2, Wilson et al.), metered inference-only joules (Yoo et al.), or time-only comparisons (Grossmann et al., Huang and Stuart 2026). This statement is a search-scope claim, not a proof of absence; record any counterexample found later.
