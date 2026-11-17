# Background papers (lower relevance, kept for later)

These papers came up in the 2026-11-17 searches for the [gap analysis](../docs/gap-analysis.md). Two entries were moved here from the shortlist on the same day: DeepXDE (Lu et al. 2021) and Chatain et al. 2025; each entry says why. They are not part of the [shortlist](shortlist.md) and have no paper notes, because they do not support a gap or a design rule directly. They are kept here so we can pick one up later without searching again.

Rules for this file:

- Every entry was checked in Crossref (published papers) or on its arXiv page (preprints) on 2026-11-17. "Checked claim" is all we read, usually the abstract. Nothing else from these papers is verified.
- Before citing an entry in the report, move it to the shortlist with a full note using the [template](paper-note-template.md), and read the passage being cited.
- Adding an entry here is not a reason to widen the fixed scope.

Citation counts are OpenAlex `cited_by_count` on 2026-11-17.

## Peer-reviewed


### Penwarden, Zhe, Narayan, Kirby (2023)

- **Citation:** A metalearning approach for Physics-Informed Neural Networks (PINNs): Application to parameterized PDEs. *Journal of Computational Physics* 477:111912. [10.1016/j.jcp.2023.111912](https://doi.org/10.1016/j.jcp.2023.111912). Cites 110.
- **Checked claim (arXiv abstract):** Metalearning and transfer learning "greatly accelerate the PINNs optimization process" for parameterized PDEs. The baseline and cost unit are not named in the abstract.
- **Use it if:** the report discusses ways to cut PINN training cost (S_P) as future work. Do not use these methods in our study without approval; they would change the PINN under test.

### Jay et al. (2023)

- **Citation:** Mathilde Jay, Vladimir Ostapenco, Laurent Lefevre, Denis Trystram, Anne-Cécile Orgerie, Benjamin Fichel. An experimental comparison of software-based power meters: focus on CPU and GPU. *2023 IEEE/ACM 23rd International Symposium on Cluster, Cloud and Internet Computing (CCGrid)*, 106-118. [10.1109/CCGrid57682.2023.00020](https://doi.org/10.1109/CCGrid57682.2023.00020). Cites 179.
- **Checked claim (abstract):** Compares several software-based power meters for CPU and GPU against high-precision physical power meters under intensive workloads.
- **Use it if:** we need to justify picking or rejecting a tool such as CodeCarbon. Promote it to the shortlist if the pilot uses a software power meter. The results section was not read (the open copy on HAL blocked automated access).

### Bouza, Bugeau, Lannelongue (2023)

- **Citation:** How to estimate carbon footprint when training deep learning models? A guide and review. *Environmental Research Communications* 5(11):115014. [10.1088/2515-7620/acf81b](https://doi.org/10.1088/2515-7620/acf81b). Cites 242.
- **Checked claim (abstract):** Introduces and compares energy-tracking tools, comparing their estimates on two image-processing networks across server types, with advice on choosing a tool.
- **Use it if:** the report needs a short reference on carbon-tracking tools. Not about PDE solvers.

### Anzt, Tomov, Dongarra (2017)

- **Citation:** On the performance and energy efficiency of sparse linear algebra on GPUs. *International Journal of High Performance Computing Applications* 31(5):375-390 (online 2016). [10.1177/1094342016672081](https://doi.org/10.1177/1094342016672081). Cites 34.
- **Checked claim (abstract):** Compares performance and energy efficiency of sparse kernels (SpMV, SpMM) and a GPU LOBPCG eigensolver against a multi-threaded CPU version.
- **Use it if:** we discuss whether the classical solver's energy depends on CPU or GPU placement. Our classical solver is CPU SciPy, so this is context.

### Hesthaven, Rozza, Stamm (2016)

- **Citation:** *Certified Reduced Basis Methods for Parametrized Partial Differential Equations.* SpringerBriefs in Mathematics. [10.1007/978-3-319-22470-1](https://doi.org/10.1007/978-3-319-22470-1). Cites 1511.
- **Checked claim:** Title and metadata only; not read.
- **Use it if:** the report's limitations section notes that reduced-order models are a classical many-query alternative that our fixed scope does not test. Read the relevant chapter first.

### Lu, Meng, Mao, Karniadakis (2021)

- **Citation:** DeepXDE: A deep learning library for solving differential equations. *SIAM Review* 63(1):208-228. [10.1137/19M1274067](https://doi.org/10.1137/19M1274067). Crossref cited-by 2,470.
- **Checked claim (full text, Section 2):** PINN error splits into approximation, optimization, and generalization error; "for smooth PDE solutions L-BFGS can find a good solution with less iterations than Adam". Proposes residual-based adaptive refinement (RAR).
- **Use it if:** the report needs a citation for the three-part PINN error split. Moved here on 2026-11-17 from a short-lived note: Rathore et al. 2024 and Markidis 2021 already cover the optimizer point, and Wu et al. 2023 covers sampling.

### Wang, Li, Xu, et al. (2026), FD-Bench

- **Citation:** Haixin Wang, Ruoyan Li, Fred Xu, Fang Sun, Kaiqiao Han, Zijie Huang, Ching Chang, Xiao Luo, Wei Wang, Yizhou Sun. FD-Bench: A Modular and Fair Benchmark for Data-driven Fluid Simulation. *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining* (KDD 2026). [10.1145/3770855.3817497](https://doi.org/10.1145/3770855.3817497). Cites 8.
- **Checked claim (abstract):** A benchmark for data-driven fluid models that claims "the first systematic framework for direct comparison with traditional numerical solvers", across 10 flow scenarios.
- **Use it if:** we need a recent example of a fair-comparison protocol against numerical solvers. It covers data-driven, time-dependent fluid models, not PINNs or energy.

### Bischof and Kraus (2025)

- **Citation:** Rafael Bischof, Michael A. Kraus. Multi-Objective Loss Balancing for Physics-Informed Deep Learning. *Computer Methods in Applied Mechanics and Engineering* 439:117914. [10.1016/j.cma.2025.117914](https://doi.org/10.1016/j.cma.2025.117914). Cites 401.
- **Checked claim (abstract):** Weighting of competing PINN loss terms matters; compares Learning Rate Annealing, GradNorm, and SoftAdapt, and proposes ReLoBRaLo, tested on Burgers, Kirchhoff plate, Helmholtz, and over 20 PINNacle PDEs.
- **Use it if:** we use soft boundary penalties (model-equations Candidate B) and need a loss-weighting method. Not needed with hard boundary enforcement.

### Luo et al. (2025)

- **Citation:** Kuang Luo, Jingshang Zhao, Yingping Wang, Jiayao Li, Junjie Wen, Jiong Liang, Henry Soekmadji, Shaolin Liao. Physics-informed neural networks for PDE problems: a comprehensive review. *Artificial Intelligence Review* 58(10):323. [10.1007/s10462-025-11322-7](https://doi.org/10.1007/s10462-025-11322-7). Cites 385.
- **Checked claim (abstract):** Review of PINN architectures, resampling, loss and activation functions, and feature embeddings.
- **Use it if:** a second recent review is wanted. Prefer Toscano et al. 2025 (shortlist Tier F).

## Preprints (not peer-reviewed; context only)

### Zhang, Roberts, Marwah, Khodak (2026)

- **Citation:** Breakeven complexity: A new perspective on neural partial differential equation solvers. arXiv:2605.15399 (v2, 2026-11-08). No published version found.
- **Checked claim (arXiv HTML, first 100k characters):** Defines break-even as the number of forward solves before a neural solver beats an error-equivalent classical solver, with data generation and training in the budget (Sec. 3.3). Hyperparameter sweeps and warm-up are excluded (Sec. 4.1, App. B). Cost is wall-clock on NVIDIA L40S GPUs; FLOPs rejected; power named as possible future work (Sec. 4.1). No PINNs.
- **Use it if:** we compare our break-even definition with another one. It is the closest break-even framework found, so re-check for a published version before the final report; if published, promote it to the shortlist.
- **Extra check (full text, Sections 3.3 and 4, read 2026-11-17):** cost is wall-clock time; the classical solver is downscaled until its error matches the neural solver. The authors note their model assumes simulation cost is about the same for all parameters, which can fail when the parameter changes problem difficulty.

### Lazareva and Tarakanov (2026)

- **Citation:** Loss-Conditional PINNs for Parametric PDE Families. arXiv:2606.04420.
- **Checked claim (arXiv HTML):** One parametric PINN against retraining a per-instance PINN; break-even K* = T_LC / T_base (Sec. 5.6). Table 8 values: Burgers about 3.5, Helmholtz 1D about 8.3, 2D about 15, 3D about 19, Schrödinger about 58. Wall-clock only, four seeds, Apple M4 Max GPU. Classical solvers are used only as error references. Sec. 5.5 and Table 8 disagree on the Burgers figure.
- **Use it if:** we need an example of a parametric PINN amortizing against retraining PINNs. It does not compare with a classical solver.
- **Training details (full text, Section 3.4, read 2026-11-17):** tanh network with four hidden layers of 64, Xavier init; Adam at 1e-3 with cosine annealing and gradient-norm clipping at 1.0; a new parameter sample at every step; L-BFGS finish on fixed quadrature with a revert-on-worse safeguard. For parameters that change the PDE operator, FiLM conditioning gave about ten times lower relative L2 error than plain input concatenation. Contingency idea for our pipeline only (preprint).

### Nooraiepour, Both, Kadeethum, Sadeghnejad (2026)

- **Citation:** Partial Differential Equations in the Age of Machine Learning: A Critical Synthesis of Classical, Machine Learning, and Hybrid Methods. arXiv:2603.07655.
- **Checked claim (abstract):** Conceptual review contrasting classical and ML PDE methods, with an error budget and hybrid design principles. No measurements.
- **Use it if:** the introduction needs a recent overview. Prefer the peer-reviewed reviews already in the shortlist (Cuomo et al. 2022, Karniadakis et al. 2021).

### Chatain, Rizvi-Martel, Rabusseau, Oberman (2025)

- **Citation:** Numerical PDE solvers outperform neural PDE solvers. arXiv:2507.21269v1. No published version found on 2026-11-17 (gap analysis, Section 2).
- **Checked claim (abstract, 2026-11-12):** DeepFDM, a differentiable finite-difference model, reaches one to two orders of magnitude lower error than tested neural solvers with 10 to 20 times fewer training epochs.
- **Use it if:** the discussion mentions learned solvers built on classical stencils. Moved here from shortlist Tier A on 2026-11-17: it is an unrefereed preprint about a method we do not use, and no project document cited it. Its note was removed; the PDF hash was df5693b2aa200d0dc39349bca8d0a779772d79fc6d9d3b45c2b380c7cab97ab4.

## Not kept

These came up in the searches but could not be checked on a primary page: the "PINNs rarely break even" claim attributed to arXiv:2511.04576, a Research Square meta-learning PINN preprint (rs-7497594), neuromorphic FEM energy papers, and a Springer chapter on CodeCarbon overestimation. Do not cite them from search summaries.
