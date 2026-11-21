# Five-minute class presentation: speeches and memory plan

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.

**Purpose:** three short, formal speeches for the class talk, a way for each member to remember their part, and a checked critique of our method for questions. The talk presents the [methodology flowchart](methodology-flowchart-a4.pdf); questions are prepared in [defense-qa.md](defense-qa.md).

**Status:** the proposal is submitted. No solver, PINN, or energy run exists. Every number in the speeches comes from a cited paper. Nothing is our measurement.

**Sources:** `docs/research-plan.md`, `Break-Even Methodology.md`, the flowchart PDF, `docs/gap-analysis.md`, `docs/gap-evidence.md`, `docs/training-pipeline.md`, and the paper notes in `references/`, all as of 2026-11-17. AI-assisted draft; the team should check it and say it in their own words.

---

## 1. Time plan

The three speeches total about 620 words. Short sentences need short pauses, so plan for 125 to 130 words a minute. That gives about 4 minutes 45 seconds to 5 minutes, which is tight. Rehearse with a timer. If you go over 4:50, use the cuts in Section 4; they save about 15 seconds.

| Time | Speaker | Job | Words |
|---|---|---|---|
| 0:00 to 1:25 | Member 1 | Background, the gap, and the research question | about 180 |
| 1:25 to 3:45 | Member 2 | Walk through the methodology flowchart | about 290 |
| 3:45 to 5:00 | Member 3 | Limits, proposed extra questions, current status, close | about 150 |

Keep the flowchart on screen for the whole talk. Member 1 can show the title slide first, then switch to the flowchart when saying "N star".

## 2. One idea that links the three parts

All three parts point to one picture from our own method: **the total-cost graph** at the bottom of the flowchart (boxes "Total cost" and "Break-even point").

- The horizontal axis is the number of new queries, N.
- The **classical solver** line starts low, because it needs no training, but rises fast, because every query is a full solve.
- The **PINN** line starts high, because of training, but rises slowly, because each query is one network pass.
- If the two lines cross, the crossing is **N star**.

Member 1 explains why the lines have these shapes. Member 2 shows how we measure the start and the slope of each line. Member 3 states the limits of the result and the three extra questions we propose about it.

---

## 3. The speeches

**Bold words** are the cue words. They match the memory cards in Section 4. Square brackets are actions, not words to say. Each sentence is short on purpose: pause at every full stop.

### Member 1: background and research question

> [Greeting.] Our topic is the **energy break-even point** between PINNs and classical solvers.
>
> In engineering, we often solve the **same equation many times**, with new settings. We compare two methods for this task.
>
> A **classical solver**, such as finite differences, needs no training. But it solves the full problem again for every new setting. So its cost grows with every query.
>
> A **PINN** is a neural network that learns the physics. It is trained once for all settings. Training takes a lot of energy. After that, each new answer is fast.
>
> So the PINN costs more at the start, and less per query. After enough queries, its total cost may become lower. That point is the **break-even point**.
>
> Earlier papers compared these methods on **time only**. The classical solver was usually much faster. In one paper, the PINN needed **32 hours** for the same accuracy. The classical solver needed less than 20 seconds. **None of them measured energy.**
>
> So we ask: after how many new queries does the PINN use less total energy? We call this number **N star**.
>
> Now [Member 2] will explain our method.

### Member 2: the methodology flowchart

> This flowchart shows our full method. It has **five steps**: set up, split, check, measure, and cross.
>
> [Point at the top box.] First, the **setup**. Our test problem is steady heat diffusion on a square plate. The edges stay at zero. Two numbers change the material from place to place. One new pair of numbers is one new query. A short trial run, the pilot, will fix these values. Both methods answer on the same grid. Our error targets are 1 percent and 0.1 percent.
>
> [Point at the left side.] Then the chart **splits**. On the left is the **PINN**. Its input is the position and the two numbers. The edge rule is built into the network. So it only has to learn the equation. We train it **three times**, each with a new random seed. We count all the training energy, even for failed runs.
>
> [Point at the right side.] On the right is the **finite difference** solver. It divides the plate into a grid. The matrix parts are **built once**. For a new query, we only rescale them and solve. A finer grid gives the reference answer, only for checking.
>
> [Point at "Accuracy check".] Next, both methods meet at the **accuracy check**. If one method misses the target, we record it. We do not compare costs for that target.
>
> [Point at "Energy trials".] If both pass, we **measure**. We run many queries in a row. We read the energy meters on the **CPU, memory, and GPU**. We also record the time.
>
> [Point at the bottom boxes.] Last, we draw the total cost of each method as a line. It is the setup cost, plus N times the cost of one query. Where the two lines **cross** is N star. We find one N star for energy, and one for time. If the lines never cross, we report that too.
>
> Now [Member 3] will discuss the limitations.

### Member 3: limits, extra questions, and close

> Our design follows two **fair-test rules** from McGreivy and Hakim. Same accuracy, and an efficient classical solver.
>
> Our study also has **clear limits**. [Point at the top box.] We test one problem family. It is 2D, smooth, and steady. So our N star belongs to this problem only. [Point at "Energy trials".] We use one machine. Other hardware may give a different N star. And we count device energy while running. Cooling and making the hardware are not included.
>
> We also propose **three extra questions**. [Point at the left side.] First, **retraining**. How often can the design change before the PINN loses its savings? [Point at "Accuracy check".] Second, **checking**. How much energy does it cost to check PINN answers with a classical solve? [Point at "Energy trials".] Third, **placement**. Does the result change when PINN queries run on the CPU instead of the GPU?
>
> At present, **nothing is measured yet**. The pilot is our next step. We will report every outcome, including no break-even.
>
> Thank you. We welcome your questions.

---

## 4. How each member can remember their part

### Shared rules

1. **Learn the first and last line by heart.** The middle can change a little. The opening and the hand-over must not.
2. **Remember points, not sentences.** Recall the cue word, then say the point in short sentences.
3. **Count on one hand.** Each member has four or five points. Count them on your fingers while you practise.
4. **Use the flowchart as your map.** Every point in every speech belongs to a box on the chart. Pointing at the box brings back the point.
5. **Draw it.** Each member has a small sketch below. Draw it from memory three times before the talk.

### Member 1: four points and the cost graph

| Finger | Point | Cue words |
|---|---|---|
| 1 | The task: one equation, solved for many settings | same equation many times |
| 2 | Two methods: classical solves every time; PINN trains once | classical solver, PINN, break-even point |
| 3 | What earlier papers did, and what they missed | time only, 32 hours, none measured energy |
| 4 | Our question | N star |

**Sketch to draw:** the total-cost graph.

```text
 total energy
   |                  /   classical: starts low, rises fast
   |                /
   |              /
   |  ----------X----------   PINN: starts high (training), rises slowly
   |          /
   |        /             X = N star
   |      /
   |    /
   |  /
   +------------------------------ number of queries, N
```

Points 1 and 2 explain the two lines. Point 3 says nobody measured these lines in energy. Point 4 is the X.

**Memory line:** "Task, Two methods, Gap, N star."

### Member 2: five steps on one hand

The flowchart itself is your picture. Its shape is a **Y**, then a **gate**, then a **meter**, then an **X**.

```text
        [ SET UP ]          thumb:  set up the problem
          /    \
     PINN        FD         index:  split into two solvers
          \    /
        [ GATE ]            middle: accuracy check
           |
        [ METER ]           ring:   measure energy and time
           |
           X                little: two lines cross = N star
```

| Finger | Step | Must say |
|---|---|---|
| Thumb | **Set up** | heat diffusion on a plate, edges at zero, two numbers, pilot fixes values, same grid, 1% and 0.1% |
| Index | **Split** | PINN on the left (edge rule built in, three seeds, failed runs counted); finite difference on the right (built once, rescale and solve) |
| Middle | **Check** | both must pass, a miss is recorded |
| Ring | **Measure** | many queries in a row, CPU, memory, GPU, time too |
| Little | **Cross** | setup plus N times query cost; one N star for energy, one for time; maybe no crossing |

**Memory line:** "Set, Split, Check, Measure, Cross."

**Tip:** as you say each step, point at that box on the screen. Your hand will lead your memory.

### Member 3: rules, limits, three questions

Each point sits on a box of the flowchart. Point at it as you speak. The closing lines ("At present..." to "...your questions") are learned by heart, so they need no finger.

| Finger | Point | Box to point at | Must say |
|---|---|---|---|
| Thumb | **Fair-test rules** | whole chart | same accuracy, efficient classical solver (McGreivy and Hakim) |
| Index | **Clear limits** | top box, then "Energy trials" | one problem family (2D, smooth, steady); one machine; device energy only, no cooling or hardware making |
| Middle | **Retraining** | left side (PINN) | how often can the design change before the PINN loses its savings? |
| Ring | **Checking** | "Accuracy check" | energy cost of checking PINN answers with a classical solve |
| Little | **Placement** | "Energy trials" | PINN queries on CPU instead of GPU |

**Sketch to draw:** the flowchart as a Y. Put a box around the top (limits), then mark the left branch (retraining), the gate (checking), and the meter (placement).

**Memory line:** "Rules, Limits, Retrain, Check, Place."

**For the limits, count three small ones:** one problem, one machine, device energy.

### Practice plan

| When | What to do |
|---|---|
| Day 1 | Each member reads their speech aloud three times. Record it on a phone and listen once. |
| Day 2 | Speak from the memory card only, not the script. Draw your sketch from memory. |
| Day 3 | Full run with all three, with a timer. Practise the two hand-overs until they are smooth. |
| Before class | One last timed run. If over 4 minutes 50 seconds, use the cuts below. |

**Cuts, if time runs short** (about 15 seconds in total):

- Member 1: drop "The classical solver was usually much faster."
- Member 2: drop "One new pair of numbers is one new query." and "We also record the time."
- Member 3: drop "Cooling and making the hardware are not included." and "The pilot is our next step."

### Words to say carefully

These words must stay because they are part of the method. Practise them slowly.

| Word | Say it like |
|---|---|
| PINN | "pin" |
| finite difference | FAI-nait DIF-rens |
| diffusion | di-FYOO-zhun |
| accuracy | AK-yu-ra-see |
| query, queries | KWEE-ree, KWEE-rees |
| N star | en star |
| matrix | MAY-triks |
| limitations | li-mi-TAY-shuns |
| nonlinear | non-LI-ni-ar |
| 2D | two D |
| placement | PLAYS-ment |
| retraining | ree-TRAY-ning |
| McGreivy and Hakim | mak-GREE-vee and HA-kim |
| pilot | PAI-lot |
| 0.1 percent | zero point one percent |

Words we left out on purpose, with what we said instead: cumulative (total), electricity (energy), parametric (trained once for all settings), conductivity (the material), methodology (method), crossover (where the lines cross), relative L2 error (error), held-out (test), optimizer names Adam and L-BFGS (train), uncertainty interval (left for questions).

---

## 5. Critique of our method and target, checked

This is the material behind Member 3's part and the answers in [defense-qa.md](defense-qa.md). "Our reasoning" marks a point that no source states for our problem.

### What the design does well

| Design choice | Why it matters | Source |
|---|---|---|
| Accuracy check before any cost comparison | Rule 1: "make comparisons at either equal accuracy or equal runtime". Markidis ran CG to machine precision against a PINN near 1e-3 to 5e-3 error, so those two runs were not matched | McGreivy and Hakim 2024 (Nat. Mach. Intell.); Markidis 2021 Sec. 2.1 |
| Strong classical baseline with valid reuse | Rule 2: compare "to an efficient numerical method"; 79% (60/76) of the fluid-related ML papers they reviewed that claim to beat a standard method used a weak baseline | McGreivy and Hakim 2024 |
| One machine, one declared meter boundary | Grossmann et al. ran the PINN on a GPU and FEM on CPU cores; Chuang and Barba used A100 GPUs for the PINN and different hardware for the classical code | gap-evidence.md, rows 1 and 2 |
| Failed runs and three or more seeds in the cost | PINN training can fail outright | Krishnapriyan et al. 2021 (NeurIPS); Wang, Yu, Perdikaris 2022 (J. Comput. Phys.); Chuang and Barba 2022 (no physical cylinder solution) |
| Energy and runtime as two separate answers | Operation counts explained little of energy use (R² = 0.083) | Henderson et al. 2020 (JMLR), p14 |
| Meters, not estimates | RAPL readings are "highly correlated with plug power"; the GPU sensor needs care | Khan et al. 2018 (ACM TOMPECS); Yang et al. 2024 (SC24) |
| "No crossover" is a valid outcome | Reporting bias hides negative results | McGreivy and Hakim 2024 |

### Evidence that supports the PINN side

The critique should be fair to the PINN too. Grossmann et al. 2024 found FEM faster in nearly every test, but in 3D Poisson the trained PINN's evaluation was two to three orders of magnitude faster than FEM interpolation (Sec. 6). Wang, Wang, Perdikaris 2021 report queries up to about 1000 times faster than a classical solver, but that leaves out training time (0.03 to 9.25 GPU-hours). So a cheap PINN query is plausible; whether it pays back the training is the open question.

### Engineering limitations

[Issue #11](https://github.com/ihmorol/pinn-energy-break-even/issues/11) sorts these. Item 1 stays a stated limit, with an optional contrast check (R7). Items 2 to 5 become proposed research items R1, R2, R4, and R5; the one-machine limit becomes R3 (CPU and GPU placement). In the talk, Member 3 states the limits (one problem family, one machine, device energy) and proposes R1, R2, and R3. All proposals wait for the owner's approval.

1. **A simple test problem.** The family is 2D, steady, linear in u, and smooth: k = 1 + μ₁x + μ₂y keeps k between 0.5 and 1.5. Real engineering models are often 3D, nonlinear, time-dependent, or have sharp material contrasts. The published PINN-versus-classical gaps grow on harder problems: Grossmann et al. 2024 report FEM faster by one to three orders of magnitude on 2D and 3D Poisson but five to six on Allen-Cahn. So N\* from our problem cannot be carried to a harder one, in either direction (our reasoning).
2. **A fixed design space.** The PINN is trained for one geometry, one set of boundary values, and one parameter box (research plan, Sec. 2). A query outside the box, a new shape, or a new boundary condition needs new training, and that training energy starts a new cost line. The classical solver handles such changes with a new grid or matrix and no training. Design work often changes these things, so the useful number of queries before retraining may be smaller than N\* (our reasoning; the plan keeps geometry and boundaries fixed on purpose).
3. **No built-in error check in use.** Lower loss generally goes with lower error, but good solutions need near-zero loss (Rathore et al. 2024, Sec. 4), so a loss value alone does not certify a query's error (training-pipeline.md C7). In our study a reference solve grades every held-out answer; in real use, checking a PINN answer would need a classical solve, which adds energy. The classical solver's error can be reduced and estimated by grid refinement, as our own reference does with a Richardson check.
4. **Device energy is not the full energy cost.** We meter CPU, memory, and GPU while running. This leaves out facility overhead such as cooling, which Henderson et al. 2020 handle through a PUE factor, and the energy to build the hardware. Kapoor et al. 2025 (preprint) count data collection, training, and deployment as life-cycle stages for PDE learning models. A GPU bought only for PINN training carries a cost our N\* does not include (our reasoning).
5. **The break-even may lie beyond real use.** A finite N\* helps an engineer only if their project needs that many queries. For an FNO on parametric Darcy flow, Huang et al. 2026 (preprint) report no model under 1% error breaking even before 3.1×10⁴ queries. Our report should state the query range a real design study would need next to N\*.

### Protocol risks (for questions only)

These are risks in how we run the study. They are not in the speeches.

1. **Baseline efficiency is not yet shown.** The reference-solution plan lists SciPy `spsolve` and CG with Jacobi or ILU, while the closest prior studies use multigrid (gap-analysis.md, Sec. 6, item 3). The pilot must show our solver is efficient at our grid sizes.
2. **The per-query costs may be too small to meter.** k = 1 + μ₁x + μ₂y keeps k between 0.5 and 1.5, a smooth, low-contrast problem. At 1% error a coarse grid may be enough, so e_C could be very small. GPU power readings update about every 20 ms on a V100 and 100 ms on an A100, and on A100 and H100 only about 25% of the runtime is sampled (Yang et al. 2024), so both per-query costs must come from long blocks (at least 5 s, training-pipeline.md C24). If e_C ≤ e_P, the PINN never catches up (our reasoning, not a prediction).
3. **Reaching 0.1% may be costly, but the evidence is mixed.** Tighter targets need more training iterations in the linear model of De Ryck et al. 2024 (order κ ln(1/ε)). Chuang and Barba needed more than 8 hours for about 1e-3, but on unsteady fluid flow, a harder problem than ours. Markidis found high frequencies slow to learn on Poisson, yet L-BFGS-B brought the training residual to 2.79e-5 (residual, not solution error). Our solution is smooth, so it may be easier. We do not know yet; the gate will show it.
4. **The linear cost model may not hold.** CG iterations can change with μ, so e_C may not be constant (training-pipeline.md C26, from Zhang et al. 2026, preprint). The plan checks slope stability for both methods.
5. **Three seeds is a minimum, not a strong sample.** Other studies use 5 (Rathore et al. 2024) or at least 10 (Krishnapriyan et al. 2021). We report failure counts, not rates (C23).
6. **The meter boundary has a fairness question.** If the GPU board is inside the boundary for both methods, its idle power is charged to the CPU-only classical solver too (our reasoning). The pilot must state how idle and background energy are treated (research-plan.md, Sec. 4). The boundary also leaves out the power supply, board, and fans, so values are device energy, not whole-machine electricity.
7. **Open decisions change N\* directly.** Gate rule (worst case or a quantile), stop rule, whether validation reference solves are charged to S_P, retry limit, and FP32 versus FP64 are not decided (training-pipeline.md Sec. 10). Two conductivity candidates also still exist in our docs (gap-analysis.md, Sec. 6, item 2).

### Weak points of the target

- **N\* is narrow by design.** It holds for one PDE family, one parameter box, one machine, and two error targets. It cannot be stated as "PINNs break even after N queries" in general.
- **The gap rests on a targeted search, not a systematic one** (gap-analysis.md, Sec. 1). Say "we found no study" rather than "no study exists".
- **Some support is preprint only.** Huang et al. 2026 (reference 2 of the proposal), Kapoor et al. 2025, Wilson et al. 2025, and Zhang et al. 2026 are arXiv preprints. The point that energy and runtime rankings can differ in PDE work has only preprint support, so Q2 is an open question, not an expected finding.
- **Published time ratios do not transfer.** Markidis's PINN took about 69 times as long as one CG solve (6,380 s against 92.28 s, same CPU, not matched in accuracy). Chuang and Barba's took over 5,700 times as long (32 hours against under 20 s, matched accuracy, different hardware). Both PINNs were trained for one problem each. Training once for a whole family may cost more or less; no paper we read reports which.

---

## 6. Questions after the talk

The full defense list, with short answers and who answers each, is in [defense-qa.md](defense-qa.md). Learn the questions marked ★ first.

---

## 7. Checks before the talk

- Do not say "we found", "we measured", or "results show". Nothing is measured.
- If asked about the plate values, say "working choice; the pilot fixes it".
- Say "we propose" for the three extra questions and for reduced basis. They are in issue #11 and are not yet approved or in the research plan.
- Each member checks the numbers in their speech against `docs/gap-evidence.md`.
- Follow the course rules on disclosing AI help with these speeches.
