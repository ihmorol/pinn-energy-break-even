# Defense questions and answers

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.

**Purpose:** prepare the three members for questions after the five-minute talk ([speeches](class-presentation-5min.md), [methodology flowchart](methodology-flowchart-a4.pdf)). Each answer is short and gives one reason or source.

**Status:** the proposal is submitted. No solver, PINN, or energy run exists. Nothing below is a measured result. Items marked "proposed" are in [issue #11](https://github.com/ihmorol/pinn-energy-break-even/issues/11) and wait for the owner's approval.

**Sources:** `docs/research-plan.md`, `docs/gap-analysis.md`, `docs/gap-evidence.md`, `docs/training-pipeline.md`, and the notes in `references/`, as of 2026-11-17. AI-assisted draft; each member should check the answers they will give.

---

## How to answer

1. **Answer first, then one reason.** Two or three short sentences are enough.
2. **Say "we plan" or "we propose".** Never "we found" or "results show". Nothing is measured.
3. **If you do not know, say so.** "We have not decided that yet. The pilot will settle it." This is a full answer.
4. **Pass the question.** If it belongs to another member's part, say "[Name] will answer that."
5. **Do not argue.** If a point is fair, agree and say how the design handles it, or that it is a stated limit.

**Who answers:** Member 1 covers motivation and literature. Member 2 covers the method, the solvers, accuracy, and measurement. Member 3 covers break-even analysis, outcomes, limits, and proposed work.

**Most likely questions** are marked ★. Learn those answers first.

---

## Most likely questions from the supervisor

A supervisor already knows the proposal. They usually ask about progress, fairness, whether the measurements can be trusted, and what they must approve. This is our estimate of the order, most likely first. "Go to" gives the full answer below.

| Rank | Likely question | Go to | Why a supervisor asks it | Who |
|---|---|---|---|---|
| 1 | Where are you now, and are you on schedule? | I1, K1 | First question at any progress check | 3 |
| 2 | What exactly is new in your work? | A8, B1 | Checks that the contribution is clear and narrow | 1 |
| 3 | Is your classical baseline strong enough? | E2, B8 | A weak baseline gives a false win (McGreivy and Hakim) | 2 |
| 4 | How will you measure energy, and can we trust it? | G1, G2 | The whole result depends on the meters | 2 |
| 5 | Which machine and budget? What do you need from me? | G6, K7 | The supervisor must approve these before any run | 3 |
| 6 | How do you make sure both methods reach the same accuracy? | F1, F5 | Matched accuracy is the core fairness rule | 2 |
| 7 | What if there is no crossover? Is the project still useful? | I3, H4 | Tests whether a negative result is planned for | 3 |
| 8 | Your new questions were not in the proposal. Is this scope creep? | K6, J5 | Protects the 12-week plan | 3 |
| 9 | What is your biggest risk? | K8 | Shows the team knows where the plan can fail | 2 |
| 10 | What goes into the PINN's setup cost? Do failed runs count? | H2, D6, D10 | Hidden training cost would bias N star | 3 |
| 11 | How do you show uncertainty? Are three seeds enough? | H7, D7 | One lucky run must not decide the result | 3 |
| 12 | Where does the reference answer come from? | F3, F4 | The grading must not favor one method | 2 |
| 13 | Why such a simple problem? | C1, C5 | Checks that the result is not trivial | 2 |
| 14 | Why report energy and time separately? | A7, H8 | Checks the Green Computing angle | 1 |
| 15 | Has anyone done a break-even before? | B2 | Checks the literature is current | 1 |
| 16 | Why not reduced basis? | E4 | A supervisor who knows numerics may raise it | 3 |
| 17 | How can others repeat your work? | K2 | Reproducibility | 2 |

**How to use this list:** each member learns the full answers for their rows first, then the ★ questions in the sections below.

---

## A. Topic and motivation

| # | Question | Answer | Who |
|---|---|---|---|
| A1 ★ | What is a PINN, in one line? | A neural network trained so its output satisfies the equation. The equation error is part of its training loss (Raissi et al. 2019). | 1 |
| A2 ★ | What is the break-even point? | The number of new queries at which the total costs of both methods are equal. After it, the method with the cheaper query costs less in total. | 1 |
| A3 ★ | Why is this a Green Computing topic? | Training uses real energy. Strubell et al. 2019 and Schwartz et al. 2020 made training cost a research issue. People say PINN queries are cheap, but they rarely count training. We count both, with meters. | 1 |
| A4 | Who would use your result? | An engineer who must solve the same equation for many settings, for example in a design sweep or an optimization. N star tells them how many queries they need before training pays back. | 1 |
| A5 ★ | Isn't it already known that classical solvers win? | For single solves, published work says the classical solver is usually much faster (Grossmann et al. 2024; Chuang and Barba 2022). Our case is different: one PINN trained for many settings. Whether that pays back in energy has not been measured, within our search. | 1 |
| A6 | Isn't it obvious the PINN wins after enough queries? | Only if one PINN query costs less than one classical solve at the same accuracy. On a small, smooth problem, a classical solve can be very cheap. Then the lines never cross. We do not assume either result. | 3 |
| A7 | Why energy, and not only time? | A faster method does not always use less energy. Henderson et al. 2020 found operation counts a weak guide to energy (R² = 0.083). So we report energy and time separately. | 1 |
| A8 | What is new in your work? | A measured energy break-even, at matched accuracy, between one parametric PINN and a classical solver, with failed runs and uncertainty included. The PINN model itself is not new. | 1 |

## B. Literature and research gap

| # | Question | Answer | Who |
|---|---|---|---|
| B1 ★ | What exactly is the gap? | Within our search, no study measures energy for both a PINN and a classical solver at the same accuracy. None reports a break-even query count for a parametric PINN against a classical solver. | 1 |
| B2 ★ | Has anyone computed a break-even before? | Yes, for other models. Huang et al. 2026 (preprint) did it for an FNO: below 1% error, none broke even before about 31,000 queries. Lazareva and Tarakanov 2026 (preprint) compared a parametric PINN with retrained PINNs, not with a classical solver. Neither measured energy. | 1 |
| B3 | Which papers compared PINNs and classical solvers? | Grossmann et al. 2024 (against FEM), Chuang and Barba 2022 (finite differences), and Markidis 2021 (PETSc CG). All measured time only, for single problems. | 1 |
| B4 | How big were the gaps in those papers? | In Chuang and Barba, the PINN needed about 32 hours to match a finite-difference run that took less than 20 seconds. Grossmann et al. found FEM faster in nearly every test. | 1 |
| B5 | Did your search cover everything? | No. It was a targeted search, not a systematic one. So we say "within our search". We propose a documented search before the final report. | 1 |
| B6 | Why do you cite preprints? | Only for background. Every gap we claim rests first on peer-reviewed work. Preprints are labeled, and we check for published versions. | 1 |
| B7 | Kapoor et al. measured PINN carbon. Doesn't that fill the gap? | It is a preprint that estimates carbon with CodeCarbon. It has no classical solver line to compare against, so there is no break-even. | 1 |
| B8 | What does McGreivy and Hakim's paper say? | They reviewed machine-learning papers on fluid equations. 79% of those that claimed to beat a standard method used a weak baseline. Their two rules are compare at equal accuracy, and against an efficient method. Our design follows both. | 1 |

## C. Problem choice

| # | Question | Answer | Who |
|---|---|---|---|
| C1 ★ | Why steady diffusion? | It is simple, well studied, and every setting has an answer we can check. With our current choice, the conductivity stays between 0.5 and 1.5, so every setting is solvable. | 2 |
| C2 | What are the exact values? | Our working choice is −∇·(k∇u) = 1 on the unit square, u = 0 on the edges, k = 1 + μ₁x + μ₂y, with μ₁ and μ₂ between −¼ and ¼. The pilot will fix the final values. | 2 |
| C3 | Why only two parameters? | Two parameters keep training and testing within our 12-week budget. Our plan keeps the shape and boundaries fixed on purpose. | 2 |
| C4 ★ | Why not a 3D, nonlinear, or time-dependent problem? | That is outside our scope, and we state it as a limit. Our N star belongs to this problem family only. We propose an optional check with stronger contrast if budget remains. | 3 |
| C5 | Isn't the problem too easy to mean anything? | It is a controlled first measurement. If a PINN cannot break even on an easy problem, that is useful to know. If it can, harder problems are the next step. | 3 |
| C6 | Why a 1D pilot first? | To check the energy meters, both codes, and the budget on a problem with a known answer, before the main study. | 2 |

## D. PINN design

| # | Question | Answer | Who |
|---|---|---|---|
| D1 ★ | What network do you use? | A small fully connected network with tanh. Inputs are x, y, μ₁, and μ₂. Candidates are 3 or 4 hidden layers with width 32 or 64. The pilot picks the smallest one that passes. | 2 |
| D2 ★ | How do you handle the boundary? | We multiply the network output by x(1−x)y(1−y). That is zero on every edge, so the boundary rule always holds. Training then needs only the equation error (Sukumar and Srivastava 2022; Sun et al. 2020). | 2 |
| D3 | Which optimizer? | Adam first, then L-BFGS. This order is common in the papers we read (Rathore et al. 2024; Markidis 2021; Grossmann et al. 2024). | 2 |
| D4 | Why double precision (FP64)? | In single precision, PyTorch's L-BFGS can stop too early (Xu et al. 2025). The pilot measures the extra cost of FP64 on our machine before we decide. | 2 |
| D5 | When do you stop training? | By a fixed rule frozen before the main runs, never by judgment. We are choosing between a fixed step budget and stopping when the validation error meets the target. | 2 |
| D6 ★ | What if training fails? | The run is kept, labeled, and its energy counted. A declared policy sets the maximum retries. If the PINN still misses a target, that is a reported result. | 2 |
| D7 | Why only three seeds? | Three is our minimum. We report how many runs failed, not a failure rate. We propose five seeds if the budget allows. | 3 |
| D8 | Does the PINN see the test settings during training? | No. Training, validation, and test settings are kept apart. Our plan also puts the corners of the parameter range in the test set. | 2 |
| D9 | Why a PINN and not DeepONet or FNO? | Those usually learn from solver data. A PINN learns from the equation alone. Our scope fixes the PINN. | 2 |
| D10 | Do you charge the PINN for tuning? | Yes. Tuning runs count in the study energy log, and they are reported next to the setup cost. | 3 |

## E. Classical solver

| # | Question | Answer | Who |
|---|---|---|---|
| E1 | Why finite differences and not FEM? | The domain is a square, so finite differences are simple and standard. Our plan fixes this choice. | 2 |
| E2 ★ | Is your classical solver weak on purpose? | No. We build the matrix parts once and reuse them for every query. We propose that the pilot compare direct solve, conjugate gradient with ILU, and multigrid, and keep the fastest that passes each target. We use the coarsest grid that meets the target. | 2 |
| E3 | Can you reuse the factorization across queries? | Not in general. A new setting changes the matrix, so an old factorization is not valid. We only allow mathematically valid reuse: the matrix parts, the grid, and the sparsity pattern. | 2 |
| E4 ★ | Why not reduced basis? | It is a classical method built for many queries. We have proposed it as a third method. That would compare a neural surrogate with a classical one. | 3 |
| E5 | Does the classical solver run on CPU or GPU? | The pilot decides and we justify it. Anzt et al. 2017 show that sparse-solver energy depends on this choice. | 2 |

## F. Accuracy and fairness

| # | Question | Answer | Who |
|---|---|---|---|
| F1 ★ | How do you measure accuracy? | Relative L2 error on one shared grid, against a reference answer. | 2 |
| F2 | Why 1% and 0.1%? | Two practical levels of accuracy. 0.01% is an optional stretch target, only within the training budget. | 2 |
| F3 ★ | Where does the reference answer come from? | The same finite-difference method on a much finer grid, with a grid-refinement (Richardson) check. It is used only to grade both methods. | 2 |
| F4 | Isn't it unfair to grade with the classical method itself? | The reference is a much finer grid, checked across grid sizes, not the answer being graded. Our plan says the baseline is not automatically its own ground truth. | 2 |
| F5 ★ | What if only one method reaches the target? | Then we do not compare costs at that target. The miss is recorded and reported as a result. | 2 |
| F6 | Worst-case or average error? | Not decided yet. Worst case is stricter. Whichever we choose, the same rule applies to both methods. | 2 |
| F7 | Do both methods answer on the same points? | Yes, one fixed output grid for both. Any interpolation needed to reach that grid is counted in the query cost. | 2 |
| F8 | Why not compare at equal time instead? | McGreivy and Hakim allow equal accuracy or equal time. Equal accuracy fits our question, because an engineer needs a required accuracy. | 1 |

## G. Energy measurement

| # | Question | Answer | Who |
|---|---|---|---|
| G1 ★ | How do you measure energy? | RAPL counters for the CPU and memory (Khan et al. 2018), and the NVIDIA power sensor for the GPU. Both methods are measured inside the same boundary, on one machine. | 2 |
| G2 ★ | Is the GPU sensor accurate? | Not for short runs. Yang et al. 2024 showed that on A100 and H100 cards only about 25% of the runtime is sampled. So we measure blocks of at least 5 seconds, four times, with random gaps, and training as one long window. | 2 |
| G3 | Why not a wall power meter? | It is not in the current plan. We label our numbers as device energy (CPU, memory, GPU), not whole-machine electricity. | 2 |
| G4 | Why not just use CodeCarbon? | It can give estimates. We prefer counter readings, and any estimate is labeled as an estimate (Henderson et al. 2020). | 2 |
| G5 | What about idle and background power? | The pilot fixes how we treat it, and we state it. We propose to report N star with and without idle GPU power for the CPU-only runs. | 2 |
| G6 | Which machine will you use? | Not chosen yet. The machine, protocol, and compute budget need approval first. | 2 |
| G7 | Does your energy include cooling or making the GPU? | Not in the measured result. We propose adding cooling and carbon as clearly labeled estimates. | 3 |
| G8 | How do you time GPU work? | We synchronize the GPU before stopping the clock, so no work escapes the timer. We also warm up before timed blocks. | 2 |

## H. Break-even analysis

| # | Question | Answer | Who |
|---|---|---|---|
| H1 ★ | What is the formula? | Each method's total cost is setup cost plus N times the cost per query. The lines meet at N star = (S_P − S_C) / (e_C − e_P). | 2 |
| H2 ★ | What is in the PINN setup cost? | Training energy of all runs under the retry policy, model loading, and (as proposed) the reference solves used for validation. | 3 |
| H3 | What is in the classical setup cost? | Grid and matrix-part setup, and (as proposed) the grid-refinement study that picks the grid. | 3 |
| H4 ★ | What if one PINN query costs more than one classical solve? | Then the PINN never catches up. We report that. | 3 |
| H5 | What if the lines cross at a huge N? | We call it an extrapolated crossing and say it is outside the usable range. We propose to compare N star with query counts that real tasks need. | 3 |
| H6 | Is the cost really a straight line? | That is an assumption we check. We record the cost of every query and check that the slope is stable for both methods. | 3 |
| H7 ★ | How do you show uncertainty? | We repeat trials and use at least three training seeds, then build an interval by resampling. If the slopes overlap within the uncertainty, we do not claim a crossing. | 3 |
| H8 | Do energy and time give the same N star? | We do not know. We report two separate answers. That is one of our research questions. | 3 |
| H9 | What is the difference between study energy and deployment cost? | Study energy is everything we used, including failures and tuning. Deployment cost is what one user pays under a stated policy. We report them separately. | 3 |

## I. Results and expectations

| # | Question | Answer | Who |
|---|---|---|---|
| I1 ★ | Do you have results? | No. The proposal is submitted. The pilot is next. | 3 |
| I2 ★ | What do you expect? | We do not predict a winner. Published time ratios range from about 69 to over 5,700, but those PINNs were trained for one problem each, so they do not carry over. | 3 |
| I3 ★ | What if there is no crossover? | That is a valid result, and we will report it. McGreivy and Hakim show that negative results often go unreported. | 3 |
| I4 | Will your result hold for other problems or machines? | No. It holds for this problem family, this parameter range, this machine, and these accuracy targets. | 3 |

## J. Limits and proposed work

| # | Question | Answer | Who |
|---|---|---|---|
| J1 ★ | What are your main limits? | One problem family, one machine, and device energy only. | 3 |
| J2 | What is the retraining question? | If the design changes, the PINN must retrain. We propose to report how often the design can change before the PINN loses its savings. | 3 |
| J3 ★ | Does a PINN answer need checking? | A low training loss does not prove a low error (Rathore et al. 2024). We propose to measure the energy cost of checking answers with a classical solve. | 3 |
| J4 | What is the placement question? | We propose to run PINN queries on both CPU and GPU and see if N star changes. | 3 |
| J5 | Why are these only proposals? | They are listed in issue #11 and need the owner's approval before they enter the research plan. | 3 |

## K. Project and process

| # | Question | Answer | Who |
|---|---|---|---|
| K1 | What is your timeline? | Twelve weeks: pilot in weeks 1 to 2, build both methods in 3 to 5, accuracy check in 6, energy trials in 7 to 9, analysis and report in 10 to 12. | 3 |
| K2 | How can others repeat your work? | Settings live in config files. We freeze the protocol with a Git tag, use fixed seeds, keep every run record, and the repository is public. | 2 |
| K3 | What if you run out of time or budget? | The 0.01% target and optional checks go first. The two main targets and three seeds stay. | 3 |
| K4 | Who did what? | Each member answers this in their own words. | All |
| K5 | Did you use AI tools? | Answer honestly, following the course's AI-use rules. | All |
| K6 | Your proposal did not include these extra questions. Is this scope creep? | They are proposals only, in issue #11, and wait for approval. Most reuse data the main study already collects. The main study comes first; nothing is added unless approved. | 3 |
| K7 | What do you need from me? | Approval of the machine, the protocol, and the compute budget before any run. Then decisions on the proposals in issue #11 and the open protocol choices, such as the accuracy rule and the stop rule. | 3 |
| K8 | What is your biggest risk? | Two risks. The PINN may not reach 0.1% within budget, which we would report as a result. And the cost of one query may be too small to measure, so we measure long blocks of queries. | 2 |

---

## Before the talk

- Each member reads the ★ questions in their part and says the answers aloud once.
- Check every number you plan to say against `docs/gap-evidence.md`.
- If a question is not here, use the rules in "How to answer".
