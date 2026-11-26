# Reading list and methodology map

**Made:** 2026-11-26 by Claude Code (AI agent) for the team. Not yet checked by a team member.
**Basis:** every title and abstract of the 55 shortlisted studies, plus the full texts listed in [verification.md](verification.md). Scores use the judging sheet in [team-shortlist.md](team-shortlist.md) (C1 relevance, C2 cost evidence, C3 fairness, C4 gap value, C5 source; 0 to 2 each). All 55 scores and reasons are in [team-selection.csv](team-selection.csv), where the team can change them.

**Citation rule (team decision, 2026-11-26):** preprints are not cited in the report. They may be read when they are highly relevant. We apply the same rule to theses, because they are not peer reviewed. A preprint with a journal version is cited through the journal version.

## 1. What to read: 17 studies

### Cite and read (12)

Numbers match the bracketed sources in the methodology figure.

| # | Study | Published in | Rating | Why it matters | Stages | Access |
|---|---|---|---|---|---|---|
| 1 | Feng et al. 2026, parametric PINN for contaminant source identification ([DOI](https://doi.org/10.1016/j.watres.2026.127290)) | Water Research | JUFO 3 | Peer-reviewed parametric PINN that beats direct COMSOL inversion in total time, offline training included, once the number of inversions passes a break-even threshold. The strongest citable prior for GC2. Read first. | 2, 12, 13 | Abstract only so far |
| 2 | Winkler and Stoll 2026, flow surrogates ([DOI](https://doi.org/10.1016/j.jocs.2026.103075)) | Journal of Computational Science | JUFO 1 | Break-even formula of the same form as ours. Training is charged, the configuration search is not (GC4). | 5, 11, 12 | Read (note in `references/`) |
| 3 | Chen et al. 2023, ThermPINN full-chip thermal analysis ([DOI](https://doi.org/10.1109/iccad57390.2023.10323696)) | IEEE/ACM ICCAD 2023 | Not on JUFO or NO data | Parametric PINN against COMSOL over 3171 cases with training and inference time counted. | 12, 13 | Closed: library or authors |
| 4 | Wang et al. 2026, extended parametric PINNs ([DOI](https://doi.org/10.1016/j.csite.2026.108226)) | Case Studies in Thermal Engineering | JUFO 1 | One parametric PINN training (8.72 h GPU) against 1.30 h per parameter for a classical CPU solver. By our arithmetic it pays back after about 7 parameters, on different hardware. | 2, 12 | Open access; download by hand |
| 5 | Buoso et al. 2021, parametric PINN for heart mechanics ([DOI](https://doi.org/10.1016/j.media.2021.102066)) | Medical Image Analysis | JUFO 3 | Parametric PINN 30 times faster than the reference FE model, training included. | 2, 12 | Open access; download by hand |
| 6 | Roohi 2026, GPU neural closure for Fokker-Planck ([DOI](https://doi.org/10.1016/j.jcp.2026.115261)) | Journal of Computational Physics | JUFO 2 | Break-even in simulation runs with data and training charged (about 20 and 55 runs). | 5, 11 | Read (arXiv copy) |
| 7 | Luo et al. 2025, MR-DINO ([DOI](https://doi.org/10.1137/23m157956x)) | SIAM Journal on Scientific Computing | JUFO 3 | Cost advantage stated after construction cost is counted, and amortized over many runs. | 11 | Read (arXiv copy) |
| 8 | Cao et al. 2025, parametric TSONN for aerofoils ([DOI](https://doi.org/10.1080/19942060.2025.2559110)) | Engineering Applications of Computational Fluid Mechanics | JUFO 1 | Parametric physics-trained solver costs about 40 single-flow solves to train. Helps size *S*<sub>P</sub>. | 4, 5 | Read (arXiv copy) |
| 9 | Haidak et al. 2026, parametric PINN for cylinder flows ([DOI](https://doi.org/10.1063/5.0356861)) | Physics of Fluids | JUFO 1 | Parametric PINN with hard boundary conditions, tested on unseen parameters against a finite-volume reference. Supports our network design and held-out testing. | 1, 2 | Closed: library or authors |
| 10 | Wang, Wang and Perdikaris 2021, physics-informed DeepONets ([DOI](https://doi.org/10.1126/sciadv.abi8605)) | Science Advances | JUFO 3 | Method anchor: parametric PDEs solved by physics-informed training without paired solver data. | 2, 3 | Open access |
| 11 | Lee et al. 2026, FPGA thermal prediction ([DOI](https://doi.org/10.1002/aisy.202501108)) | Advanced Intelligent Systems | JUFO 1 | Measured power (1.71 W) of a deployed surrogate. An energy example, but not compared with FE energy. | 10 | Open access; download by hand |
| 12 | Yang et al. 2025, parameterized PINN thermal simulation ([DOI](https://doi.org/10.1109/tpel.2025.3547390)) | IEEE Transactions on Power Electronics | JUFO 3 | A top-journal parametric unsupervised PINN used for design exploration against COMSOL, with no break-even. Shows why our question matters. | 2 | Closed: library or authors |

Items 10 and 12 score only 5 of 10, below the selection rule. They are kept on purpose: 10 is the method anchor for stage 2, and 12 is the top-journal motivation example.

### Read only, do not cite (5)

These shape our claims even though the report will not cite them. Not citing a preprint does not let us ignore it: our novelty wording must stay true with these included. The narrowed gap statement in [gap-validation.md](gap-validation.md) already does.

| | Study | Status | Why read it | Stages | Access |
|---|---|---|---|---|---|
| A | Li, Jiang and Song 2026, parametric PINN for chip cooling | arXiv preprint | Explicit runtime break-even (about 108 designs) for a physics-only parametric PINN. Rules out "first PINN break-even". | 2, 12, 13 | Read (note) |
| B | Jediný 2025, PINN against FDM in plasma | Bachelor's thesis, Charles University | Separate energy and time break-even, energy estimated from TDP. Nearest prior for GC1 and GC3. | 10, 13 | Read (note) |
| C | Zhang et al. 2026, breakeven complexity | arXiv preprint | Method standard: error-matched classical solver, tuning cost counted. | 5, 6, 12 | Read (note) |
| D | Sun et al. 2026, FEVessel | Submitted manuscript (arXiv) | Label-free model against a tuned multigrid solver at a stated tolerance. | 9, 12 | Read (note) |
| E | Huang and Stuart 2026, cost-accuracy trade-offs | arXiv preprint | The accuracy target decides which method is cheaper per query (GC5). | 13 | Read earlier (note) |

### Optional extras

Read only if time allows: Xu et al. 2026 (ECMOR 2026; training amortized after a few queries against FD with AMG; unrated venue, closed), Srinivasan et al. 2025 (ACM CODS-COMAD; estimated energy for a PINN variant), Aarabi Dahej et al. 2026 (Industrial & Engineering Chemistry Research; parametric PINN surrogates with no training cost).

## 2. Peer-reviewed sources already in our corpus

These already have notes in `references/` and need no new reading. The figure uses numbers 13 to 18 for them.

| # | Study | Published in | Used for |
|---|---|---|---|
| 13 | Grossmann et al. 2024 | IMA Journal of Applied Mathematics | PINN against FEM at matched accuracy; reference and accuracy gate |
| 14 | McGreivy and Hakim 2024 | Nature Machine Intelligence | Fair comparison rules: equal accuracy and an efficient baseline |
| 15 | Markidis 2021 | Frontiers in Big Data | PINNs on Poisson against a conjugate-gradient solver |
| 16 | Chuang and Barba 2022 | Proceedings of SciPy 2022 | PINN training pitfalls and cost against finite differences |
| 17 | Henderson et al. 2020 | Journal of Machine Learning Research | Energy measurement and reporting with hardware counters |
| 18 | Khan et al. 2018 | ACM TOMPECS | RAPL readings track wall power |

## 3. Methodology v2 and the stage map

**Figure:** `methodology and all/methodology-flowchart-v2.pdf` (also `.png`, `.svg`, and the editable `.json` spec). It keeps the 13 stages of the first figure. The changes are small and stay inside the fixed scope:

- Stage 1 names a validation set as well as the training and held-out sets, as the research plan already requires.
- The loop runs for at least 3 seeds, and failed runs are kept.
- Stage 5 charges *S*<sub>P</sub> with all seeds, tuning and failed runs, not only the final training runs. Winkler and Stoll [2] leave the search uncharged, and Zhang et al. (C) show why it matters.
- Stage 6 picks, for each accuracy target, the coarsest grid that meets it, so the classical side is not over-resolved [13, 14]. **Proposed**, needs team approval.
- Stage 10 names the counters: RAPL for CPU and DRAM, NVML for the GPU, one boundary, fixed clocks [17, 18].
- Stage 12 reports *N*\* at stated accounting levels: training only, then adding seeds and failures, then tuning. **Proposed**, needs team approval. It can explain why published break-even counts range from about 7 to about 46,000.
- Stage 13 reports energy and run-time *N*\* separately and uses each phase's mean power to explain any gap between them.

Not drawn, because it changes scope and needs the owner's approval: adding a classical surrogate (interpolation or reduced basis) as a third method, as [plan-alignment-review.md](../plan-alignment-review.md) proposes.

| Stage | What happens | Cite | Read-only background |
|---|---|---|---|
| 1 Problem setup | 2D steady diffusion, two parameters, disjoint training, validation and held-out sets, targets 1% and 0.1% | 9, 13, 15 | |
| 2 Parametric PINN | Inputs *x*, *y*, μ<sub>1</sub>, μ<sub>2</sub>; boundary built in; trained on the equation only | 5, 9, 10, 12 | A |
| 3 Equation error | PDE residual by automatic differentiation | 10, 16 | |
| 4 Loss and training | Adam then L-BFGS, fixed step budget | 8, 16 | |
| 5 PINN query and *S*<sub>P</sub> | Training energy over all seeds, tuning and failures; energy per query | 2, 6, 8 | C |
| 6 Grid for the target | Coarsest grid meeting the target | 13, 14 | C |
| 7 Matrix setup | Affine split built once, valid reuse only | 14, 15 | |
| 8 Reference answer | Finer grids with a Richardson check | 13 | |
| 9 FD query | Setup energy *S*<sub>C</sub>, energy per query *e*<sub>C</sub> | 14, 15 | D |
| Accuracy check | Both methods within the target on held-out parameters | 13, 14 | |
| 10 Energy trials | Repeated query blocks, counters, one boundary | 11, 17, 18 | B |
| 11 Total cost | *E* = *S* + *N*·*e* for each method, same form for run time | 2, 6, 7 | |
| 12 Break-even point | *N*\* = (*S*<sub>P</sub> − *S*<sub>C</sub>) / (*e*<sub>C</sub> − *e*<sub>P</sub>) at each accounting level | 1, 2, 3, 4, 5 | A, C, D |
| 13 Result per target | Energy and run-time *N*\* with uncertainty, or none | 1, 3, 4 | A, B, E |

## 4. What the citation rule changes

- **Proposal reference 2 is a preprint.** Huang et al. 2026 (arXiv) is cited in the submitted proposal. The submitted files stay as they are. In the report, cite peer-reviewed sources for the same points: McGreivy and Hakim [14] for weak baselines, Winkler and Stoll [2] and Roohi [6] for break-even accounting, and Feng et al. [1] for a parametric PINN break-even.
- **The citable evidence for GC2 now rests on [1], [3], [4] and [5].** Feng et al. [1] needs a full-text read before we write about it: whether its PINN is trained without solver data, how its break-even is counted, and whether accuracy is matched. If it is a physics-only break-even, the narrowed gap statement still holds, because it has no energy and no matched-accuracy, same-machine comparison.
- **Closed-access items 3, 9 and 12** need the university library or a request to the authors. Until then, cite only what their abstracts say.

## 5. All 55 scores

Sorted by reading list, then by total score. "Cite?" applies the rule above. The full reasons are in [team-selection.csv](team-selection.csv).

| List | ID | Year | Title | Published in | Cite? | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|
| 1 | R02724 | 2026 | [Contaminant source identification at point-source contaminated site...](https://doi.org/10.1016/j.watres.2026.127290) | Water Research | yes | 2 | 2 | 0 | 2 | 2 | 8 |
| 2 | R00504 | 2026 | [No Free Lunch in Flow Surrogates under Time-Varying Boundary Condit...](https://doi.org/10.1016/j.jocs.2026.103075) | Journal of Computational Science (2026) | yes | 2 | 2 | 1 | 2 | 2 | 9 |
| 3 | R03609 | 2023 | [Fast Full-Chip Parametric Thermal Analysis Based on Enhanced Physic...](https://doi.org/10.1109/iccad57390.2023.10323696) | 2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD) | yes | 2 | 2 | 1 | 2 | 2 | 9 |
| 4 | R01189 | 2026 | [Extended parametric physics-informed neural networks (ePPINNs) for...](https://doi.org/10.1016/j.csite.2026.108226) | Case Studies in Thermal Engineering | yes | 2 | 2 | 0 | 2 | 2 | 8 |
| 5 | R02880 | 2021 | [Personalising left-ventricular biophysical models of the heart usin...](https://doi.org/10.1016/j.media.2021.102066) | Medical Image Analysis | yes | 2 | 2 | 0 | 2 | 2 | 8 |
| 6 | R00637 | 2026 | [Accelerating Kinetic Fokker-Planck Simulations via a GPU-Native Dee...](https://doi.org/10.1016/j.jcp.2026.115261) | Journal of Computational Physics (2026) | yes | 2 | 2 | 1 | 1 | 2 | 8 |
| 7 | R00718 | 2025 | [Efficient PDE-Constrained Optimization Under High-Dimensional Uncer...](https://doi.org/10.1137/23m157956x) | SIAM Journal on Scientific Computing (2025) | yes | 2 | 2 | 1 | 1 | 2 | 8 |
| 8 | R00692 | 2025 | [A surrogate model based on parametric neural network solvers for la...](https://doi.org/10.1080/19942060.2025.2559110) | Engineering Applications of Computational Fluid Mechanics (2025) | yes | 1 | 2 | 0 | 1 | 2 | 6 |
| 9 | R01247 | 2026 | [A parametric physics-informed neural network framework for cylinder...](https://doi.org/10.1063/5.0356861) | Physics of Fluids | yes | 1 | 1 | 1 | 1 | 2 | 6 |
| 10 | R00018 | 2021 | [Learning the solution operator of parametric partial differential e...](https://doi.org/10.1126/sciadv.abi8605) | Science Advances | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| 11 | R01850 | 2026 | [Ultralow‐Power Real‐Time On‐Chip Thermal Prediction via Finite Elem...](https://doi.org/10.1002/aisy.202501108) | Advanced Intelligent Systems | yes | 1 | 2 | 0 | 1 | 2 | 6 |
| 12 | R03325 | 2025 | [A Parameterized Thermal Simulation Method Based on Physics-Informed...](https://doi.org/10.1109/tpel.2025.3547390) | IEEE Transactions on Power Electronics | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| A | R00383 | 2026 | [Parameterized Physics-Informed Neural Networks for Efficient Simula...](https://doi.org/10.48550/arxiv.2611.10666) | arXiv | no: preprint | 2 | 2 | 0 | 2 | 1 | 7 |
| B | R01555 | 2025 | [Machine Learning Approach to the Solution of Reaction-Diffusion Equ...](https://openalex.org/W7135832291) | Bachelor's thesis, Charles University (2025) | no: thesis | 2 | 1 | 1 | 2 | 1 | 7 |
| C | R00627 | 2026 | [Breakeven complexity: A new perspective on neural partial different...](https://doi.org/10.48550/arxiv.2605.15399) | arXiv | no: preprint | 2 | 2 | 2 | 2 | 1 | 9 |
| D | R00643 | 2026 | [FEVessel: Mesh-Independent Analysis of 3D Pressure Vessels with the...](https://doi.org/10.48550/arxiv.2607.17318) | arXiv | no: preprint | 2 | 2 | 1 | 2 | 1 | 8 |
| E | R00657 | 2026 | [Cost-Accuracy Trade-offs: Neural Operator vs Classical Numerical So...](https://doi.org/10.48550/arxiv.2609.24021) | arXiv | no: preprint | 1 | 1 | 2 | 2 | 1 | 7 |
| opt | R02483 | 2026 | [Lattice Green’s Neural Networks: A Learn-Solve Paradigm for Fast El...](https://doi.org/10.3997/2214-4609.202637152) | ECMOR 2026 | yes, weak venue | 2 | 2 | 1 | 1 | 2 | 8 |
| opt | R00895 | 2025 | [Towards Sustainable Scientific Machine Learning: Fast and interpret...](https://doi.org/10.1145/3799830.3799865) | Proceedings of the 13th ACM IKDD International Conference on Data Science | yes, weak venue | 1 | 1 | 1 | 1 | 2 | 6 |
| opt | R02666 | 2026 | [Physics-Informed Neural Network Surrogates for Chemical Processes G...](https://doi.org/10.1021/acs.iecr.6c02300) | Industrial & Engineering Chemistry Research | yes | 1 | 1 | 1 | 1 | 2 | 6 |
| - | R00670 | 2026 | [Classical, Machine Learning, and Hybrid Solvers for Partial Differe...](https://doi.org/10.48550/arxiv.2610.32911) | arXiv | no: preprint | 2 | 2 | 1 | 2 | 1 | 8 |
| - | R00614 | 2026 | [Shape Derivative-Informed Neural Operators with Application to Risk...](https://doi.org/10.48550/arxiv.2603.03211) | arXiv | no: preprint | 2 | 2 | 1 | 1 | 1 | 7 |
| - | R00649 | 2026 | [When a neural surrogate cannot accelerate a solver: runtime share,...](https://doi.org/10.48550/arxiv.2608.23075) | arXiv | no: preprint | 1 | 2 | 1 | 1 | 1 | 6 |
| - | R00244 | 2025 | [Soliton profiles: Classical Numerical Schemes vs. Neural Network -...](https://doi.org/10.48550/arxiv.2512.24634) | arXiv preprint; probable version in Chaos, Solitons & Fractals (2026) | only the journal version | 1 | 1 | 1 | 1 | 1 | 5 |
| - | R00319 | 2026 | [Physics-Informed Neural Networks as Fast Surrogate Models for Elect...](https://doi.org/10.48550/arxiv.2608.19209) | arXiv | no: preprint | 1 | 1 | 1 | 1 | 1 | 5 |
| - | R00598 | 2025 | [Reduced-Basis Deep Operator Learning for Parametric PDEs with Indep...](https://doi.org/10.48550/arxiv.2511.18260) | arXiv | no: preprint | 1 | 1 | 1 | 1 | 1 | 5 |
| - | R00750 | 2025 | [Comparing pretraining methods with different fidelities for a 2D co...](https://doi.org/10.1515/polyeng-2024-0228) | Journal of Polymer Engineering | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| - | R01145 | 2026 | [EquiNO: A physics-informed neural operator for multiscale simulations](https://doi.org/10.1016/j.jcp.2026.114745) | Journal of Computational Physics (2026) | yes | 1 | 1 | 1 | 0 | 2 | 5 |
| - | R01457 | 2024 | [Brain-inspired spiking neural networks in Engineering Mechanics: a...](https://doi.org/10.1007/s00366-024-01967-3) | Engineering with Computers | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| - | R02939 | 2023 | [Physics-informed neural networks for data-free surrogate modelling...](https://doi.org/10.1016/j.matdes.2023.112034) | Materials & Design | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| - | R03090 | 2026 | [A robust physics-constrained neural operator framework for efficien...](https://doi.org/10.1038/s41467-026-73183-0) | Nature Communications | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| - | R03386 | 2025 | [Rapid parametric electrostatic modeling of TSV port cross-section u...](https://doi.org/10.1117/12.3077052) | International Conference on Signal Processing and Communication Security (ICSPCS 2025) | yes, weak venue | 1 | 1 | 1 | 1 | 1 | 5 |
| - | R03460 | 2026 | [Modeling the Immune Response with Machine Learning: Validation and...](https://doi.org/10.5753/sbcas_estendido.2026.21588) | Anais Estendidos do XXVI Simpósio Brasileiro de Computação Aplicada à Saúde (SBCAS 2026) | yes, weak venue | 1 | 1 | 1 | 1 | 1 | 5 |
| - | R03662 | 2024 | [20.4 A 28nm Physics Computing Unit Supporting Emerging Physics-Info...](https://doi.org/10.1109/isscc49657.2024.10454502) | 2024 IEEE International Solid-State Circuits Conference (ISSCC) | yes | 1 | 1 | 0 | 1 | 2 | 5 |
| - | R00177 | 2025 | [Beyond Accuracy: EcoL2 Metric for Sustainable Neural PDE Solvers](https://doi.org/10.48550/arxiv.2505.12556) | arXiv | no: preprint | 1 | 1 | 0 | 1 | 1 | 4 |
| - | R00220 | 2025 | [NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks](https://doi.org/10.1016/j.jcp.2026.115161) | Journal of Computational Physics (2026) | yes | 0 | 1 | 0 | 1 | 2 | 4 |
| - | R00780 | 2026 | [Fast parametric three-dimensional physics-informed neural network a...](https://doi.org/10.1016/j.rineng.2026.110582) | Results in Engineering | yes | 1 | 0 | 0 | 1 | 2 | 4 |
| - | R00993 | 2024 | [HxPINN: A hypernetwork-based physics-informed neural network for re...](https://doi.org/10.1080/10407790.2024.2325648) | Numerical Heat Transfer, Part B: Fundamentals | yes | 1 | 1 | 0 | 0 | 2 | 4 |
| - | R02174 | 2026 | [Energy-efficient operation of neural operators for virtual sensing](https://doi.org/10.48550/arxiv.2609.30580) | arXiv | no: preprint | 0 | 2 | 0 | 1 | 1 | 4 |
| - | R02561 | 2026 | [Accelerating coupled transport modeling: Hybrid AI-Physics approach...](https://doi.org/10.1016/j.aitf.2026.100042) | AI Thermal Fluids | yes, weak venue | 1 | 1 | 0 | 1 | 1 | 4 |
| - | R02862 | 2026 | [Domain-Decomposition Pinns for Rapid Prediction of Stirred-Tank Mix...](https://doi.org/10.69997/pse.127236) | Proceedings of the 3rd Foundations of Process/Product Analytics and Machine Learning (FOPAM 2026) | yes, weak venue | 1 | 1 | 0 | 1 | 1 | 4 |
| - | R00370 | 2026 | [From Grey-Box to Green-Box: When can Physics-Informed Machine Learn...](https://doi.org/10.48550/arxiv.2609.33387) | arXiv | no: preprint | 0 | 1 | 0 | 1 | 1 | 3 |
| - | R00807 | 2026 | [Selecting PINNs and neural operators for repeated engineering analysis](https://doi.org/10.31224/8628) | engrXiv preprint (2026) | no: preprint | 1 | 0 | 0 | 1 | 1 | 3 |
| - | R00810 | 2025 | [Performance-Carbon Trade-Offs across Architectural Biases in Shear...](https://doi.org/10.48550/arxiv.2509.24517) | arXiv | no: preprint | 0 | 1 | 0 | 1 | 1 | 3 |
| - | R01518 | 2024 | [Physics‐Based Spiking Neural Network as a Surrogate Model for Visco...](https://doi.org/10.1002/pamm.202400066) | PAMM | yes, weak venue | 1 | 1 | 0 | 0 | 1 | 3 |
| - | R01955 | 2026 | [DMR-CU: A Dual-Mode Reconfigurable Posit Computation Unit for PINN...](https://doi.org/10.1109/icaibd69640.2026.11637284) | 2026 9th International Conference on Artificial Intelligence and Big Data (ICAIBD) | yes, weak venue | 0 | 1 | 0 | 1 | 1 | 3 |
| - | R02184 | 2026 | [Reconfigurable Computing in Neural Network‐Enhanced Finite Element...](https://doi.org/10.1002/pamm.70245) | Proceedings in Applied Mathematics and Mechanics | yes, weak venue | 1 | 1 | 0 | 0 | 1 | 3 |
| - | R02608 | 2026 | [Multi-Fidelity Physics-Informed Neural Networks for Fast Electromag...](https://doi.org/10.54097/q4brzy12) | Journal of Computing and Electronic Information Management | weak venue: avoid | 1 | 1 | 1 | 0 | 0 | 3 |
| - | R03112 | 2026 | [$S^2$GPT-PINN: Reduced Basis and Hyper Reduction-Driven Double Redu...](https://doi.org/10.4208/cicp.oa-2025-0152) | Communications in Computational Physics | yes | 0 | 0 | 0 | 1 | 2 | 3 |
| - | R00092 | 2023 | [Real-Time FJ/MAC PDE Solvers via Tensorized, Back-Propagation-Free...](https://doi.org/10.48550/arxiv.2401.00413) | arXiv | no: preprint | 0 | 1 | 0 | 0 | 1 | 2 |
| - | R00218 | 2025 | [Physics-Informed Neural Networks and Neural Operators for Parametri...](https://doi.org/10.48550/arxiv.2511.04576) | arXiv | no: preprint | 1 | 0 | 0 | 0 | 1 | 2 |
| - | R00235 | 2025 | [Tensor-Compressed and Fully-Quantized Training of Neural PDE Solvers](https://doi.org/10.48550/arxiv.2512.09202) | arXiv | no: preprint | 0 | 1 | 0 | 0 | 1 | 2 |
| - | R00275 | 2026 | [SPINONet: Scalable Spiking Physics-informed Neural Operator for Com...](https://doi.org/10.48550/arxiv.2603.21674) | arXiv | no: preprint | 0 | 1 | 0 | 0 | 1 | 2 |
| - | R01786 | 2026 | [Power-efficient physics-informed neural networks with bio-inspired...](https://openalex.org/W7162611103) | Thesis, Nanyang Technological University (2026) | no: thesis | 0 | 1 | 0 | 0 | 1 | 2 |
| - | R01799 | 2026 | [Comparison of neural network architectures on the task of modeling...](https://doi.org/10.18419/opus-19222) | Thesis, University of Stuttgart (2026) | no: thesis | 0 | 1 | 0 | 0 | 1 | 2 |
