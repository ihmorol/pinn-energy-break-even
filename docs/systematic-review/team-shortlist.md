# Shortlist for team selection

**What this is:** the 45 highest-ranked eligible studies from the scoping review (Zone 3 output), plus 10 reserves. The team reads each title and abstract, scores it with the sheet below, and selects 20-30 to chart and cite.
**How it was made:** [search-log.md](search-log.md) (search and flow counts) and [screening-decisions.csv](screening-decisions.csv) (every Zone 3 decision). Ranking and notes are by one AI reader from titles and abstracts only. Nothing here has been checked against full texts yet.
**Verified:** every study was checked against Crossref or arXiv on 2026-11-26. Venue quality levels and published versions are in [verification.md](verification.md), along with full-text facts for the papers read.
**Where to mark:** [team-selection.csv](team-selection.csv). It has one row per study and empty columns for the five scores, the total, the decision, a reason and the reviewer's name.

**Easiest way to read and score:** open `outputs/systematic-review/team-reading.html` in a browser. It shows each study's title, abstract, venue, verification status and the AI screener's note, with 0/1/2 buttons for each criterion, an automatic total and rule suggestion, and an Export CSV button whose columns match `team-selection.csv`. Scores are saved in that browser only. If the file is missing, rebuild it from the repository root with `python -I docs/systematic-review/search/build_reading_pack.py`.

Abstracts are not stored in this tracked file, or in any tracked file, because they are third-party text. That is why the reading page lives in the ignored `outputs/` folder. Share it within the team only.

## Judging sheet

Score each study 0, 1 or 2 on each criterion from its title and abstract.

| Criterion | 2 | 1 | 0 |
|---|---|---|---|
| C1 Relevance | Neural PDE solver (best: physics-informed and parametric) compared with a classical solver, with training or offline cost counted | Compared with a classical solver per query only | No classical comparison (energy-only studies can still score on C2 and C4) |
| C2 Cost evidence | Energy measured on hardware, or runtime with training counted | Per-query runtime or an energy estimate (CodeCarbon, Green Algorithms, simulated hardware) | A claim with no number |
| C3 Fairness | Matched accuracy and an efficient classical baseline are stated | One of the two is stated | Neither is stated |
| C4 Gap value | Could falsify or narrow one of our gap claims (GC1-GC5 in [gap-validation.md](gap-validation.md)) | Supports a method or design choice in our protocol | Background only |
| C5 Source | Peer-reviewed journal or archival conference | Preprint or thesis with a full method | Unclear source |

**Decision rule:**

- Select a study if the total is 6 or more and C1 is at least 1.
- Always select a study with C4 = 2, even if it is a preprint, because it decides whether our gap holds.
- Aim for 20-30 studies that cover both the energy route (GC1) and the break-even route (GC2).

## Ranked list (45)

Order: priority score (5 = closest to a gap claim), then the order of the screening notes. "Tests" names the gap claims a study could inform. Status comes from the index records (journal, conference, preprint, thesis). Scopus and Web of Science indexing will be checked only for the studies the team selects. Citations are OpenAlex counts on 2026-11-23.

| # | ID | Study | Year | Venue (status) | Cites | Tests | Why it is here |
|---:|---|---|---|---|---:|---|---|
| 1 | R00627 | [Breakeven complexity: A new perspective on neural partial differential equation solvers](https://doi.org/10.48550/arxiv.2605.15399) | 2026 | arXiv (preprint) | 1 | GC2,GC3 | Breakeven complexity metric: forward solves before a learned solver pays off against an error-matched classical solver; counts data, training and tuning (runtime units) |
| 2 | R00670 | [Classical, Machine Learning, and Hybrid Solvers for Partial Differential Equations: An...](https://doi.org/10.48550/arxiv.2610.32911) | 2026 | arXiv (preprint) | 0 | GC2,GC5 | Amortization law; FNO on parametric Darcy breaks even only after more than 30,000 queries below 1% error |
| 3 | R00657 | [Cost-Accuracy Trade-offs: Neural Operator vs Classical Numerical Solver](https://doi.org/10.48550/arxiv.2609.24021) | 2026 | arXiv (preprint) | 4 | GC5 | Neural operators vs problem-matched classical solvers per query (FLOPs and wall clock); classical wins as accuracy tightens |
| 4 | R00177 | [Beyond Accuracy: EcoL2 Metric for Sustainable Neural PDE Solvers](https://doi.org/10.48550/arxiv.2505.12556) | 2025 | arXiv (preprint) | 4 | GC1 | EcoL2: carbon (CodeCarbon estimate) across data, training and deployment for PINN-type and operator solvers; no classical line |
| 5 | R00504 | [No Free Lunch in Flow Surrogates under Time-Varying Boundary Conditions: A Two-Regime Study](https://doi.org/10.48550/arxiv.2607.23667) | 2026 | arXiv; journal version in Journal of Computational Science (journal) |  | GC2,GC3 | Flow surrogates 1e3-1e4 times faster than FE solver; pay off from the first or third query beyond the training set |
| 6 | R00383 | [Parameterized Physics-Informed Neural Networks for Efficient Simulation of Embedded...](https://doi.org/10.48550/arxiv.2611.10666) | 2026 | arXiv (preprint) | 0 | GC2 | Parametric PINN (4 geometry inputs) vs FE: 4 orders less time per prediction; training under 4 h on one consumer GPU |
| 7 | R00692 | [A surrogate model based on parametric neural network solvers for laminar flows around aerofoils](https://doi.org/10.1080/19942060.2025.2559110) | 2025 | Engineering Applications of Computational... (journal) | 17 | GC2 | Parametric physics-trained solver for all laminar aerofoil flows: training costs about 40 single-flow solves; no labelled data |
| 8 | R01189 | [Extended parametric physics-informed neural networks (ePPINNs) for efficient solution of...](https://doi.org/10.1016/j.csite.2026.108226) | 2026 | Case Studies in Thermal Engineering (journal) | 1 | GC2 | Parametric PINN (8.72 h GPU, whole Ra range) vs 1.30 h per parameter for LRBF on CPU: break-even computable; different hardware |
| 9 | R01457 | [Brain-inspired spiking neural networks in Engineering Mechanics: a new physics-based...](https://doi.org/10.1007/s00366-024-01967-3) | 2024 | Engineering With Computers (journal) | 13 | GC1 | Spiking physics-based network in an FE solver; energy measured on a neuromorphic chip; 40% faster than classical FEM (check what energy is compared) |
| 10 | R01555 | [Machine Learning Approach to the Solution of Reaction-Diffusion Equations in...](https://openalex.org/W7135832291) | 2025 | Digital Repository (National Repository... (thesis) |  | GC1,GC2,GC3 | Thesis: PINN vs second-order FDM (ADI) on reaction-diffusion; accuracy, energy usage and time; estimated break-even near 1300 steps |
| 11 | R02880 | [Personalising left-ventricular biophysical models of the heart using parametric...](https://doi.org/10.1016/j.media.2021.102066) | 2021 | Medical Image Analysis (journal) | 106 | GC2 | Parametric PINN for heart mechanics: 30 times faster than the reference FE model including training time |
| 12 | R03662 | [20.4 A 28nm Physics Computing Unit Supporting Emerging Physics-Informed Neural Network and...](https://doi.org/10.1109/isscc49657.2024.10454502) | 2024 | Digest of technical papers/Digest of... (conference) | 10 | GC1 | ISSCC chip for both PINN and FEM on edge devices; energy efficiency of both on one chip (check full text) |
| 13 | R00018 | [Learning the solution operator of parametric partial differential equations with...](https://doi.org/10.1126/sciadv.abi8605) | 2021 | Science Advances (journal) | 1464 | GC2 | Physics-informed DeepONet trained without paired data on parametric PDEs; up to 1000 times faster than a conventional solver (inference) |
| 14 | R00244 | [Soliton profiles: Classical Numerical Schemes vs. Neural Network - Based Solvers](https://doi.org/10.48550/arxiv.2512.24634) | 2025 | arXiv (preprint) | 2 | GC2 | Classical schemes vs PINNs and operator learning for soliton PDEs: classical wins single instances; operators pay off over many instances |
| 15 | R00319 | [Physics-Informed Neural Networks as Fast Surrogate Models for Electrochemical Flow Reactors](https://doi.org/10.48550/arxiv.2608.19209) | 2026 | arXiv (preprint) | 0 | GC2 | Parametric PINN vs finite-difference solver, sub-percent error; inference 5.34 times faster (training not stated) |
| 16 | R00598 | [Reduced-Basis Deep Operator Learning for Parametric PDEs with Independently Varying...](https://doi.org/10.48550/arxiv.2511.18260) | 2025 | arXiv (preprint) | 6 | GC2 | RB-DeepONet trained label-free with offline-online split; speedups vs RB-Galerkin and FEM-based operators |
| 17 | R00614 | [Shape Derivative-Informed Neural Operators with Application to Risk-Averse Shape Optimization](https://doi.org/10.48550/arxiv.2603.03211) | 2026 |  (preprint) |  | GC2 | Shape-DINO: counting training data generation, 1-2 orders fewer PDE solves for optimization under uncertainty |
| 18 | R00637 | [Accelerating Kinetic Fokker-Planck Simulations via a GPU-Native Deep Neural Network...](https://doi.org/10.1016/j.jcp.2026.115261) | 2026 | Journal of Computational Physics (journal) | 5 | GC2 | Neural closure inside a Fokker-Planck particle solver; break-even cost analysis including offline costs |
| 19 | R00643 | [FEVessel: Mesh-Independent Analysis of 3D Pressure Vessels with the Label-Free Pretrained...](https://doi.org/10.48550/arxiv.2607.17318) | 2026 | arXiv (preprint) | 1 | GC2,GC5 | Label-free pretrained FE operator warm-starts AMG: 9.2 times end-to-end speedup at 1e-3 tolerance |
| 20 | R00649 | [When a neural surrogate cannot accelerate a solver: runtime share, closed-loop drift, and...](https://doi.org/10.48550/arxiv.2608.23075) | 2026 | arXiv (preprint) | 2 | GC2,GC4 | Negative result: surrogate cannot accelerate the solver; closed-form break-even; gated loop is a slowdown |
| 21 | R00718 | [Efficient PDE-Constrained Optimization Under High-Dimensional Uncertainty Using...](https://doi.org/10.1137/23m157956x) | 2025 | SIAM Journal on Scientific Computing (journal) | 54 | GC2 | MR-DINO (SISC): 1-2 orders more cost-efficient than PDE-based optimization after construction costs |
| 22 | R00807 | [Selecting PINNs and neural operators for repeated engineering analysis](https://doi.org/10.31224/8628) | 2026 | Engineering Archive (engrXiv) (preprint) | 0 | GC2 | Review with analytical cost break-even condition for PINNs and neural operators in repeated engineering analysis |
| 23 | R00810 | [Performance-Carbon Trade-Offs across Architectural Biases in Shear Flow Forecasting](https://doi.org/10.48550/arxiv.2509.24517) | 2025 | arXiv (preprint) | 0 | GC1,GC3 | Carbon across training and inference for flow forecasting models; runtime unreliable proxy for carbon |
| 24 | R00895 | [Towards Sustainable Scientific Machine Learning: Fast and interpretable PDE Solvers via...](https://doi.org/10.1145/3799830.3799865) | 2025 | Joint International Conference on Data... (conference) | 0 | GC1 | RBF-PIELM vs PINNs: estimated (Green Algorithms) energy 3800 times lower; still behind mesh-based solvers |
| 25 | R00993 | [HxPINN: A hypernetwork-based physics-informed neural network for real-time monitoring of an...](https://doi.org/10.1080/10407790.2024.2325648) | 2024 | Numerical Heat Transfer Part B Fundamentals (journal) | 33 | GC2 | Hypernetwork PINN for many operating conditions; inference 35-40 times faster than numerical solution |
| 26 | R01247 | [A parametric physics-informed neural network framework for cylinder-induced thermal flows](https://doi.org/10.1063/5.0356861) | 2026 | Physics of Fluids (journal) | 0 | GC2 | One parametric PINN over Re 20-200 vs OpenFOAM; inference about 3000 times faster; relative L2 0.68% |
| 27 | R01850 | [Ultralow‐Power Real‐Time On‐Chip Thermal Prediction via Finite Element Method–Machine...](https://doi.org/10.1002/aisy.202501108) | 2026 | Advanced Intelligent Systems (journal) | 4 | GC1 | FE-trained surrogate on FPGA at 1.71 W; 21 times more energy-efficient than GPU; 2600 times faster than FE |
| 28 | R01955 | [DMR-CU: A Dual-Mode Reconfigurable Posit Computation Unit for PINN and FDM on Edge Devices](https://doi.org/10.1109/icaibd69640.2026.11637284) | 2026 | International Conference on Artificial... (conference) | 0 | GC1 | Reconfigurable unit for PINN inference and FDM on edge devices; energy efficiency (check whether per solve) |
| 29 | R02174 | [Energy-efficient operation of neural operators for virtual sensing](https://doi.org/10.48550/arxiv.2609.30580) | 2026 | arXiv (preprint) | 1 | GC1 | Metered operating energy of neural-operator inference with fixed clocks; preparation costs separated |
| 30 | R02483 | [Lattice Green’s Neural Networks: A Learn-Solve Paradigm for Fast Elliptic Flow Simulation](https://doi.org/10.3997/2214-4609.202637152) | 2026 | ECMOR XVII (conference) | 1 | GC2 | Learned Green-function kernel for elliptic flow: training cost amortized after a handful of queries |
| 31 | R03325 | [A Parameterized Thermal Simulation Method Based on Physics-Informed Neural Networks for...](https://doi.org/10.1109/tpel.2025.3547390) | 2025 | IEEE Transactions on Power Electronics (journal) | 25 | GC2 | Parameterized PINN for power-module thermal design; hundreds of times faster than numerical simulation in design sweeps |
| 32 | R03609 | [Fast Full-Chip Parametric Thermal Analysis Based on Enhanced Physics Enforced Neural Networks](https://doi.org/10.1109/iccad57390.2023.10323696) | 2023 | 2023 IEEE/ACM International Conference on... (conference) | 41 | GC2 | Parameterized ThermPINN with training plus inference counted vs a thermal simulator (3171 cases) |
| 33 | R00092 | [Real-Time FJ/MAC PDE Solvers via Tensorized, Back-Propagation-Free Optical PINN Training](https://doi.org/10.48550/arxiv.2401.00413) | 2023 | arXiv (preprint) | 10 | GC1 | Optical PINN training energy (1.36 J for 20-D HJB), simulated photonic hardware |
| 34 | R00220 | [NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks](https://doi.org/10.1016/j.jcp.2026.115161) | 2025 | Journal of Computational Physics (journal) | 2 | GC1 | Spiking PINNs reduce communication and energy demand (estimated) |
| 35 | R00235 | [Tensor-Compressed and Fully-Quantized Training of Neural PDE Solvers](https://doi.org/10.48550/arxiv.2512.09202) | 2025 | arXiv (preprint) | 3 | GC1 | Quantized tensor-compressed PINN training accelerator: 159-2324 times energy savings vs full precision |
| 36 | R00275 | [SPINONet: Scalable Spiking Physics-informed Neural Operator for Computational Mechanics...](https://doi.org/10.48550/arxiv.2603.21674) | 2026 | arXiv (preprint) | 2 | GC1 | Spiking physics-informed operator; energy reduction over repeated evaluations |
| 37 | R01518 | [Physics‐Based Spiking Neural Network as a Surrogate Model for Viscoplastic Material Law in...](https://doi.org/10.1002/pamm.202400066) | 2024 | PAMM (journal) | 5 | GC1 | PINN and spiking PINN replace a material law in FEM; energy consumption compared |
| 38 | R01786 | [Power-efficient physics-informed neural networks with bio-inspired learning](https://openalex.org/W7162611103) | 2026 | DR-NTU (Nanyang Technological University) (thesis) |  | GC1 | Thesis: spiking physics-informed solver; inference cost 1-3 orders below PINN baselines |
| 39 | R01799 | [Comparison of neural network architectures on the task of modeling heat plume dimensions in...](https://doi.org/10.18419/opus-19222) | 2026 |  (thesis) | 0 | GC1 | Thesis: neural surrogates of FE parameter studies; training energy compared between architectures |
| 40 | R00370 | [From Grey-Box to Green-Box: When can Physics-Informed Machine Learning Reduce Carbon...](https://doi.org/10.48550/arxiv.2609.33387) | 2026 | arXiv (preprint) | 0 | GC1 | Training emissions to reach an error threshold for physics-informed ML in SHM (not a PDE solver; methods context) |
| 41 | R03090 | [A robust physics-constrained neural operator framework for efficient geothermal resource...](https://doi.org/10.1038/s41467-026-73183-0) | 2026 | Nature Communications (journal) | 4 | GC2 | Physics-constrained neural operator (Nature Communications); 1400 times faster than numerical methods for ensembles |
| 42 | R01145 | [EquiNO: A physics-informed neural operator for multiscale simulations](https://doi.org/10.1016/j.jcp.2026.114745) | 2026 | Journal of Computational Physics (journal) | 13 | GC2 | Physics-informed neural operator for FE2 multiscale; speedup over FE2 for many-query use |
| 43 | R02939 | [Physics-informed neural networks for data-free surrogate modelling and engineering...](https://doi.org/10.1016/j.matdes.2023.112034) | 2023 | Materials & Design (journal) | 70 | GC2 | PINN design surrogate; 500-fold faster process optimization than conventional approaches |
| 44 | R02666 | [Physics-Informed Neural Network Surrogates for Chemical Processes Governed by Partial...](https://doi.org/10.1021/acs.iecr.6c02300) | 2026 | Industrial & Engineering Chemistry Research (journal) | 0 | GC2 | Parametric PINN surrogates for tubular reactors; over 3 orders faster than a numerical solver |
| 45 | R02561 | [Accelerating coupled transport modeling: Hybrid AI-Physics approach for...](https://doi.org/10.1016/j.aitf.2026.100042) | 2026 | AI Thermal Fluids (journal) | 2 | GC2 | Hybrid surrogate 1e6 times faster than OGS per query, with training explicitly excluded from the speedup |

## Reserve list (10)

Read these if a shortlisted study is dropped or the team wants more break-even examples.

| # | ID | Study | Year | Venue (status) | Cites | Tests | Why it is here |
|---:|---|---|---|---|---:|---|---|
| 1 | R00750 | [Comparing pretraining methods with different fidelities for a 2D cooling problem in...](https://doi.org/10.1515/polyeng-2024-0228) | 2025 | Journal of Polymer Engineering (journal) | 0 | GC2 | PINN vs FEM pretraining for parameterized cooling: PINN more costly, FEM weaker on parameterized inputs |
| 2 | R00780 | [Fast parametric three-dimensional physics-informed neural network approach for fluid flows...](https://doi.org/10.1016/j.rineng.2026.110582) | 2026 | Results in Engineering (journal) | 4 | GC2 | Parametric 3D PINN over Re benchmarked against finite volume; cost vs FV not stated |
| 3 | R02184 | [Reconfigurable Computing in Neural Network‐Enhanced Finite Element Analysis in Structural...](https://doi.org/10.1002/pamm.70245) | 2026 | PAMM (journal) | 0 | GC1 | NN initial guess in an FE solver on FPGA; energy and time vs CPU/GPU (check what energy is reported) |
| 4 | R02608 | [Multi-Fidelity Physics-Informed Neural Networks for Fast Electromagnetic Simulation of RF...](https://doi.org/10.54097/q4brzy12) | 2026 | Journal of Computing and Electronic... (journal) | 0 | GC2 | Multi-fidelity PINN for RF passives; 41 times faster than reference solver once trained |
| 5 | R02724 | [Contaminant source identification at point-source contaminated sites using a parametric...](https://doi.org/10.1016/j.watres.2026.127290) | 2026 | Water Research (journal) | 0 | GC2 | Parametric PINN for contaminant source identification instead of repeated forward simulations |
| 6 | R02862 | [Domain-Decomposition Pinns for Rapid Prediction of Stirred-Tank Mixing Flows across...](https://doi.org/10.69997/pse.127236) | 2026 | Proceedings of the 3rd Foundations of... (conference) |  | GC2 | Domain-decomposition PINN for stirred tanks; inference time down 99% vs repeated CFD; offline CFD cost amortized |
| 7 | R03112 | [$S^2$GPT-PINN: Reduced Basis and Hyper Reduction-Driven Double Reduction for...](https://doi.org/10.4208/cicp.oa-2025-0152) | 2026 | Communications in Computational Physics (journal) | 0 | GC2 | Reduced-basis pre-trained PINN for parametric PDEs; efficiency vs PINNs and RB |
| 8 | R03386 | [Rapid parametric electrostatic modeling of TSV port cross-section using physics-informed...](https://doi.org/10.1117/12.3077052) | 2025 | International Conference on Signal... (conference) | 0 | GC2 | Parametric PINN vs COMSOL: 52 times faster in parameter sweeps |
| 9 | R03460 | [Modeling the Immune Response with Machine Learning: Validation and Computational Cost...](https://doi.org/10.5753/sbcas_estendido.2026.21588) | 2026 | Anais Estendidos do XXVI Simpósio... (conference) | 0 | GC2 | PINN and NN surrogates vs GPU finite volume: 6.6 times faster inference; matters in multi-execution |
| 10 | R00218 | [Physics-Informed Neural Networks and Neural Operators for Parametric PDEs](https://doi.org/10.48550/arxiv.2511.04576) | 2025 | arXiv (preprint) | 10 | GC2 | PINNs and neural operators for parametric PDEs; reports 1e3-1e5 multi-query speedups (check if own experiments) |

## Context papers excluded by the rules but useful to cite

These failed an eligibility rule but are worth citing in the literature section.

| ID | Study | Why excluded | Use |
|---|---|---|---|
| R03063 | PIELM against FEM at equal accuracy, IEEE Access 2026 | E5: single problems, runtime only | A physics-informed method beating FEM at matched accuracy in single solves. It contrasts with Grossmann et al. 2024 for gradient-trained PINNs. |
| R00310 | IGA-ODIL against PINNs, 2026 preprint | E5 | Shows the cost of PINN optimization against a discretization-based residual method. |
| R02451 | Meta-learned PINNs, break-even at 13-16 tasks, 2025 preprint | E4: compared with retrained PINNs, not a classical solver | Nearest PINN break-even, but against retraining. Same pattern as Lazareva and Tarakanov 2026 in [gap-analysis.md](../gap-analysis.md). |
| R00314 | Loss-conditional PINNs for parametric families, 2026 preprint | E4 | Amortizes PINN training over a parameter family without solver data. |
| R00876 | Critical synthesis of classical and ML PDE methods, Artificial Intelligence Review 2026 | E1: review | Peer-reviewed review for the introduction. |
| R02652 | Unifying view of PINNs and neural operators, IJCAI 2026 survey | E1: survey | Frames "how cost is amortized across instances" as a design axis. |
| R02542 | Energy paradox in AI for seismic computing, 2026 position paper | E1 | Energy framing for computing-heavy PDE workloads. |

The core context papers already in our corpus stay in [references/shortlist.md](../../references/shortlist.md): Grossmann et al. 2024, Markidis 2021, Chuang and Barba 2022, McGreivy and Hakim 2024, Henderson et al. 2020, Khan et al. 2018, Yang et al. 2024.
