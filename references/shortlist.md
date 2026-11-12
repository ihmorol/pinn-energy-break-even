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
7. [Chatain et al. (2025), arXiv:2507.21269](chatain-2025-numeric-outperform.md). Classical discretization embedded in learning cuts training cost by 10-20x epochs against neural baselines.
8. [Kapoor et al. (2025), arXiv:2505.12556, EcoL2](kapoor-2025-ecol2.md). Accuracy-versus-emissions metric across data, training, and deployment for neural PDE solvers.

## Tier B: PINN training cost, failure modes, and accuracy targets (solution design)

9. [Wang, Yu, Perdikaris (2022), J. Comput. Phys. 449](wang-2022-pinn-ntk-failure.md). NTK analysis of why PINNs fail to train; justifies seed variance and failure logging in the protocol.
10. [Wang, Teng, Perdikaris (2021), SIAM J. Sci. Comput. 43(5)](wang-2021-gradient-pathologies.md). Gradient pathologies and mitigations; mitigation costs belong in the ledger.
11. [Krishnapriyan et al. (2021), NeurIPS 2021](krishnapriyan-2021-failure-modes.md). Failure modes on diffusion operators; motivates the accuracy gate.
12. [Mishra and Molinaro (2022), IMA J. Numer. Anal. 43(1)](mishra-molinaro-2022-generalization.md). Generalization error bounds; anchors the fixed collocation budget and accuracy rule.
13. [Hao et al. (2024), NeurIPS 2024 D&B, PINNacle](hao-2024-pinnacle.md). Matched-condition benchmark design reference.
14. [Cuomo et al. (2022), J. Sci. Comput. 92(3)](cuomo-2022-pinn-survey.md). Field survey for the introduction.

## Tier C: energy measurement and green computing context (protocol and introduction)

15. [Strubell, Ganesh, McCallum (2019), ACL P19-1355](strubell-2019-energy-policy.md). Origin of ML energy accounting; canonical measured-power-then-extrapolate example.
16. [Schwartz et al. (2020), CACM 63(12), Green AI](schwartz-2020-green-ai.md). Efficiency as an evaluation criterion; the framing for our report.
17. [Lacoste et al. (2019), arXiv:1910.09700](lacoste-2019-carbon-emissions.md). Modeled-emission calculator (CodeCarbon ancestor); reference for the "modeled estimate" label.
18. [Patterson et al. (2022), IEEE Computer 55(7)](patterson-2022-carbon-plateau.md). Publishing emissions catches estimates off by 100x-100,000x; inference share context.
19. [Luccioni et al. (2024), FAccT 2024](luccioni-2024-power-hungry.md). Deployment energy per 1,000 inferences; per-query cost deserves measurement care.
20. [Dodge et al. (2022), FAccT 2022](dodge-2022-carbon-cloud.md). Location- and time-specific carbon factors; how to label any carbon conversion we report.
21. [Reddi et al. (2024), MLPerf Power, HPCA 2025](mlperf-power-2024.md). Standardized power benchmarking rules; discipline reference for our energy trials.
22. [Wilson et al. (2025), arXiv:2509.24517](wilson-2025-carbon-forecasting.md). Runtime alone is an unreliable proxy for carbon in PDE forecasting; supports measuring both.
23. [Yoo et al. (2026), arXiv:2609.30580](yoo-2026-energy-inference.md). Metered joules for neural-operator inference with fixed clocks; reusable protocol idea.
24. [Karniadakis et al. (2021), Nature Reviews Physics 3(6)](karniadakis-2021-physics-informed-ml.md). Authoritative field review (~10,150 citations); the introduction-context citation for the PINN research program. Local PDF is the DOE accepted manuscript.

## Verified entries without a stored PDF (shortlist only)

These were verified against Crossref, OpenAlex, or the arXiv API on 2026-11-12 but were not downloaded (no open-access PDF found, or the paper is supporting context only). Access is listed as the reason.

- Mishra and Molinaro (2022), inverse-problem companion, IMA J. Numer. Anal. 42(3):981-1022, DOI 10.1093/imanum/drab032, arXiv:2007.01138, ~406 citations. Open-access preprint exists; not downloaded because the forward-problem note covers our need.
- De Ryck and Mishra (2022), "Generic bounds on the approximation error for physics-informed (and) operator learning", NeurIPS 2022, arXiv:2205.11393, ~53 citations. Open-access preprint exists; not downloaded (approximation theory context).
- Fuks and Tchelepi (2020), "Limitations of Physics Informed Machine Learning for Nonlinear Two-Phase Transport in Porous Media", J. Mach. Learn. Model. Comput. 1(1):19-37, DOI 10.1615/jmachlearnmodelcomput.2020033905, ~322 citations. No open-access PDF found; add if failure-regime examples beyond diffusion are ever needed (scope check first).
- Anthony, Kanding, Selvan (2020), Carbontracker, arXiv:2007.03051, ~661 citations. Overlaps with the Lacoste and Henderson notes.
- Wu et al. (2022), "Sustainable AI", MLSys 2022, arXiv:2111.00364, ~557 citations. Industry-scale context; not load-bearing for our protocol.
- Novo and Terrés (2025), "Can neural networks learn finite elements?", J. Comput. Appl. Math. 453:116168, DOI 10.1016/j.cam.2024.116168, arXiv:2405.06488, ~3 citations. Numerical-analysis follow-up to Grossmann et al.
- Yang, Adamek, Armour (2024), NVML power-sensor accuracy study, SC24, DOI 10.1109/SC41406.2024.00028, ~58 citations. No open-access PDF found. Read this before trusting nvidia-smi watt readings in the energy trials; it is likely to become a needed reference during the pilot.
- Kirchdoerfer and Ortiz (2016), "Data-driven computational mechanics", CMAME 304:81-101, DOI 10.1016/j.cma.2016.02.001, ~834 citations. Background only; outside our fixed scope.
- Li, Jiang, Song (2026), parametric PINN for microfluidic cooling, arXiv:2611.10666, 0 citations. Application-level example of the amortization narrative; not a benchmark.

## What the search found and did not find

Within the scope searched (arXiv, Crossref, OpenAlex, DBLP attempts, and web search, checked 2026-11-12): no published study reports metered (counter-measured) PINN training electricity compared against a classical PDE solver at matched accuracy. The nearest works measure modeled carbon in PDE contexts (EcoL2, Wilson et al.), metered inference-only joules (Yoo et al.), or time-only comparisons (Grossmann et al., Huang and Stuart 2026). This statement is a search-scope claim, not a proof of absence; record any counterexample found later.
