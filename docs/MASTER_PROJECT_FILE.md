# Green computing course project: shape optimization with physics informed neural networks

This is the only file you need. It holds everything from the earlier notes in one place: the idea explained from zero, three topic options with real research behind each, the feasibility check, the knowledge audit, the weekly plan, the questions a teacher is likely to ask, and the full source list.

Written November 2026 for the green computing course.

---

## 1. The project in one paragraph

Data centers burned about 415 TWh of electricity in 2024 (that is more than the whole United Kingdom uses in a year), and roughly a third of it goes to cooling. How much cooling a machine needs is decided mostly by geometry: the shape of heat sinks, cold plates (liquid cooling plates), and air ducts. Finding better shapes normally means running hundreds of heavy physics simulations. We want to teach a neural network the physics of heat so it can search for better shapes cheaply, measure how much the improved shape beats a standard one under identical conditions, and translate that into an order-of-magnitude energy saving estimate with its assumptions stated. The project uses computing to design energy-saving hardware; it also logs its own small experiment footprint, the way green-AI practice asks.

---

## 2. The idea from zero

### 2.1 The story in five steps

1. Computer chips make heat. A chip that gets too hot slows itself down or dies, so the heat has to go somewhere.
2. Heat sinks carry that heat away. A heat sink is the metal piece with fins that sits on top of a processor. Heat flows from the chip into the metal, then from the metal into moving air. Fans push that air, and fans, pumps, and chillers all cost electricity.
3. The shape of the heat sink decides how well it works. Fins add surface area, and heat escapes through surfaces. But more fins also block the airflow. So there is a trade-off, and no engineer can guess the best shape by eye.
4. Engineers answer "which shape is best" with simulation. They write the physics as equations, solve them on a computer for one candidate shape, and read off the highest temperature. The traditional solvers are accurate but heavy, and you must redo the whole expensive solve for every single shape you try.
5. Shape optimization means automating that search. Instead of a human testing 20 shapes, the computer tests hundreds: simulate, measure, adjust, repeat. Our project teaches a neural network the physics so this loop becomes cheap, and then honestly checks whether it beats the obvious alternative: sweeping the few knob values with the fast classical solver.

One sentence: we teach a network the physics of heat so the computer can search fin shapes by itself, we measure the improvement honestly, and we translate it to energy savings with assumptions stated.

### 2.2 Why "heat conduction" keeps coming up

Heat conduction is heat moving through solid material. Touch the far end of a spoon sitting in hot tea and it gets warm; that is conduction. The rule is simple: heat flows from hot to cold, faster when the temperature gap is bigger and the material conducts better (metal yes, plastic no).

There is a second process: convection, which is heat leaving the solid into moving air or water. A breeze cools you more than still air for the same reason. Engineers squeeze this into one number, h, which basically means "how strongly the fan is working."

A heat sink is exactly these two processes stacked. Heat conducts through the metal, then escapes to the air at every exposed surface. Both fit inside one equation, the heat equation (a formula that predicts the temperature at every point of an object). Solve it on a computer for a given shape and you get the temperature everywhere, including the hottest spot. That hottest spot is the number we want to push down.

So the chain is: shape, then equation, then temperature, then how hard the fan must work, then energy. The equation is the bridge between shape and energy, which is why it appears in a computing course project.

We picked this physics on purpose. It is the simplest physics that still contains the real design trade-off, it is textbook material, and a simple fin has a hand-computed formula we can check our code against. Fluids and turbulence can stay as future work.

### 2.3 Where data centers fit in

A data center is a building full of thousands of computers serving websites, banking, and AI. Every one of them makes heat all day. If the building gets hot, machines fail, so the building spends electricity on fans, pumps, and chillers. That is not pocket change: data centers used about 415 TWh in 2024, around 1.5% of all electricity on Earth, and the IEA expects that to roughly double by 2030 because of AI. Cooling takes roughly 30 to 40% of a facility's energy. The industry metric is PUE (Power Usage Effectiveness), which is total building energy divided by energy that actually reaches the computers. The global average is 1.54, meaning about 54 cents of overhead per dollar of computing, and cooling is the biggest slice of that overhead.

Now the connection to shape: the geometry of heat sinks, cold plates, and ducts decides how much cooling work is needed. A heat sink that spreads heat better lets fans run slower. A duct with less resistance lets air move with less fan power. The car analogy works well here. At highway speed a car burns most of its fuel pushing air out of the way, and engineers fix that by smoothing the shape, not by building a bigger engine. Same trick: do not buy a bigger chiller, improve the shape the air has to deal with. Someone has to find those shapes, and that is our project.

### 2.4 How physics gets solved on a computer (and why it hurts)

Physics equations talk about every point in space, but computers need finite lists of numbers. Two classic fixes:

- FDM (Finite Difference Method): overlay graph paper on the shape and approximate the equation at each grid point using its neighbors. Simple enough to write in about 50 lines of Python. We will build one as our trusted reference.
- FEM (Finite Element Method): cut the shape into thousands of small triangles (together called a mesh), assume simple behavior inside each piece, and solve one big algebra system. This is the industry standard, what tools like ANSYS and COMSOL do. Accurate, but meshing is tedious, every new shape needs a new mesh, and every solve costs time and electricity.
- CFD (Computational Fluid Dynamics) is the same idea for flowing air or water. One serious 3D CFD run can take hours to days.

The pain for design work is that trying 500 shapes means meshing and solving 500 times. That pain is exactly the opening for the next section.

### 2.5 What a PINN actually is

A neural network is a flexible mathematical function with millions of adjustable knobs (weights). Input numbers, output numbers, and training means automatically adjusting the knobs until the output is good.

Normal networks learn from examples, like photos labeled cat or dog. We have no examples. The trick of a PINN (Physics Informed Neural Network) is that the physics equation itself plays the role of the training data:

1. The network's only job: take a location (x, y) inside the heat sink, output the temperature there.
2. Sprinkle random points inside the shape, called collocation points.
3. At each point, plug the network's temperature into the heat equation. The equation should balance to zero. Whatever is left over is the residual, the local violation of physics.
4. Add the total residual to a wrongness score (the loss function), along with penalties for wrong behavior at the edges.
5. Adjust the knobs until the wrongness score is small. At that point the network satisfies the equation everywhere, so the network literally is the temperature field. Ask it the temperature at any point and it answers instantly.

Why this is interesting for us:

- Mesh-free: no triangles, no re-meshing for each new shape.
- Data-free: physics replaces the need for collected training data.
- Differentiable: because everything is one smooth mathematical pipeline, derivatives come out for free. This turns out to be the big one, as you will see next.

One honest note we keep in our own slides: a 2024 study (Grossmann et al.) showed that for solving a PDE (a physics equation with rates of change across space) once, classic FEM is usually faster and more accurate, by 1 to 3 orders of magnitude on a standard test problem. Our own grid solver will very likely beat our PINN on speed at this scale, and the report will say so plainly. We claim no speed win. The payoff is elsewhere: free gradients for the shape search, a mesh-free parametric temperature field, and an honest, measured comparison.

### 2.6 Shape parameters, and how the network optimizes them

A shape parameter is a knob that controls the drawing. Think of the pen tool in design software, where a few control points define a smooth curve: move a point and the curve changes. For us the knobs are things like fin height, fin thickness, and fin spacing. Three knobs give a searchable space of thousands of heat sinks. Shape optimization means finding the knob values with the lowest hottest temperature, subject to a fixed metal budget (otherwise you win by just being infinitely big, which is cheating).

A vocabulary point teachers like: shape optimization adjusts the outline of a given design (fins stay fins). Topology optimization invents the layout from scratch, where material exists at all, holes, branches. That is much harder, and we are not doing it.

Historically, step "which way should each knob move?" was the nightmare. It needs derivatives like "if fin height rises one millimeter, what happens to the hottest temperature?" Classically those come from an adjoint solver, which is pages of hand-derived math or an expensive license. With a neural network pipeline, the framework computes every derivative automatically (this is called autodiff), so the knobs get nudged downhill by the same gradient descent that trains ordinary networks. No manual derivative math, ever. That is the whole reason to use a PINN for shape work.

Better still, the shape network and the physics network can be trained together, so finding the best shape and learning the physics happen at the same time. That is the method of our template paper (Zhang et al. 2024), and it is what we would reproduce first.

Our starter problem, fully concrete: a 2D metal plate (the heat sink base) with a hot strip (the chip) and fins. Knobs: fin height and thickness, maybe spacing. Goal: lowest hottest temperature under a metal volume budget. Physics: steady 2D heat conduction (nothing changes with time) with the convective edge at the fins. Reality check: the same problem solved by our own 50-line grid solver, plus the textbook formula for a simple fin.

Two honesty notes. First, fan energy never appears directly in this model: it enters through the convection coefficient h, so any statement about fan power saved is a proxy with assumptions attached, and we will label it that way. Second, with only 2 or 3 knobs, a brute-force sweep using the fast grid solver is a genuine competitor to the PINN loop. We treat the sweep as the baseline to beat, not a formality.

### 2.7 How the training actually runs (our recipe, step by step)

This is the concrete answer to "how do you teach an equation to a network." All of it runs on free tools: roughly 150 to 200 lines of PyTorch written by hand, or fewer with DeepXDE doing the plumbing.

1. Describe the problem: the plate region, the chip face held at a fixed temperature, insulated edges, and fin surfaces that leak heat to the air (the fan edge, with strength set by h).
2. Build a small network: about six hidden layers of 50 units each (tanh activations). Input: a point (x, y). Output: the temperature there. At the start it outputs noise.
3. Sprinkle points: a few thousand random points inside the plate (collocation points), plus separate points on each edge type.
4. Grade it by physics, not by an answer key. At interior points, plug the network's temperature into the heat equation; the leftover is the residual (how badly the equation is violated). PyTorch computes the derivatives, including the second derivatives, automatically (autodiff). On the chip face, penalize the wrong temperature. On insulated edges, penalize heat leaking out. On fin surfaces, penalize breaking the convective leak rule. Add everything into one wrongness score (the loss).
5. Train: adjust the network's knobs to shrink the loss (Adam optimizer first, twenty to fifty thousand small steps, then L-BFGS to polish). When the residual is near zero everywhere and every edge behaves correctly, the network has no choice left: the only temperature field that satisfies the equation and the edges is the physical one. That is what "learning the physics" means. It is graded by the law, so passing the test means being right.
6. Validate before trusting it: check against the hand formula for a simple fin, then against our grid solver. A few percent of agreement unlocks the next stage.
7. Add the shape knobs: make fin height and thickness extra inputs and train on random knob values, so one network covers the whole small design space (a parametric PINN). Then "how much does peak temperature change per knob" comes from autodiff, and gradient descent over the knobs walks toward better shapes. The template paper instead trains a shape network and the physics network jointly; that is the stretch version, attempted only after the parametric version works.

A realism note on step 5, because it is the step that most often goes wrong in practice: the loss terms fight each other, and a network can look plausible while converging to the wrong field. That is why step 6 is not optional, and why the plan gives the solver its own weeks before any optimization is attempted.

---

## 3. Words you will hear (glossary)

| Term | Plain meaning |
|---|---|
| PDE | Physics equation with rates of change across space. The heat equation is one. |
| Boundary condition | What happens at the edges. Pinned temperature (the chip face), insulated edge (no heat escapes), or heat leaking to moving air (the fan edge, called Robin). |
| Steady-state | After the fan has run a while, temperatures stop changing. That settled state is what we simulate. |
| 2D | Flat-land simplification, a thin plate instead of a real 3D part. Cuts cost by around 100x and is the standard first step. |
| Loss function | The single number measuring how wrong the model currently is. Training means making it small. |
| Collocation points | Random sample points where we test whether the physics equation holds. |
| Residual | How badly the equation is violated at one point. Should be near zero. |
| Adam, L-BFGS | Automatic knob-adjusting algorithms used in training. Adam first (fast, rough), L-BFGS after (slow, precise). |
| Autodiff | The software computes exact derivatives through any chain of math, so "objective change per knob" is one line of code. |
| Surrogate model | A cheap stand-in for an expensive simulator. Once trained, the PINN answers in milliseconds what a solver takes minutes for. |
| Amortization | Pay once (training), then answer thousands of questions cheaply. The economic argument for surrogates in design loops. |
| Objective function | The score you minimize (hottest temperature) or maximize. |
| Constraint | A rule the design must obey, like a metal volume budget. |
| Validation | Proving your code is right by checking against something trusted: a hand formula, then our grid solver, then published results. |
| Negative result | A well-run experiment showing your method is not better. Still a legitimate research outcome, and we measure honestly either way. |
| TWh | Terawatt-hour, a trillion watt-hours. 415 TWh is more than the UK's yearly electricity. |
| PUE | Data center efficiency: total energy divided by computer energy. 1.54 means 54% overhead. |
| CodeCarbon | A free Python library that logs the kWh and CO2 of your training runs. Our green measuring tool. |
| DeepXDE, PyTorch | Free open-source Python libraries. PyTorch does neural networks and autodiff. DeepXDE is ready-made PINN machinery built on it. |
| NVIDIA PhysicsNeMo | Heavier, production-grade PINN framework (formerly Modulus). We only mention it as the industrial option. |
| Google Colab | Free cloud notebooks with a GPU (the math chip that speeds up training). Enough for this project. |
| Airfoil, lift-to-drag | Airplane wing cross-section and its efficiency ratio. The other classic shape optimization application, and our backup domain. |
| Reproducible | Someone else can rerun your code and get your numbers. Open tools plus a public repo gets you there. |

---

## 4. Three topic options

Before the options, the one idea that ties them together, because this is our novelty claim:

The PINN literature optimizes shapes for performance (peak temperature, torque, lift) and stops there. The green question comes next: how much operating energy does the better shape actually save? In the papers we reviewed, that question is rarely asked, and it is where our contribution lives. Whichever topic we pick, we contribute (1) a green objective: the shape target is an energy proxy (the cooling strength the fan must supply, pumping power, electrical losses), not just peak temperature; (2) an honest translation: the measured relative improvement of the optimized shape under identical conditions, plus an order-of-magnitude yearly kWh illustration with every assumption listed. A 2D course-scale model cannot guarantee facility savings and we will not pretend it can; (3) an application gap: our literature scan found PINN-based cold plate geometry optimization sparse, and efficiency objectives absent from the PINN motor papers we found (both to be verified with a deeper review before we claim them).

One scale note, because it decides what we do and do not claim. The design loop itself costs a few kWh of GPU time. For illustration: a 1% cooling improvement in one data center hall would save tens of thousands of kWh per year, on the order of ten thousand times the design cost. That illustration is why the shape, not the search, is the valuable output, and why we do not sell the loop's own energy as a contribution. We still log our experiments with CodeCarbon, as reporting hygiene.

### Option A: heat sink shape optimization for data centers

The original topic. Teach a PINN the heat physics of a finned metal plate and let it find fin shapes that keep a chip cool with the least fan energy.

Green numbers: data centers at about 415 TWh (2024), cooling at 30 to 40% of facility energy, average PUE 1.54.

Research behind it: Cai et al. 2021 (ASME review, around 2,000 citations, covers heat sink design with PINNs), Son et al. 2023 (IEEE, free-form heat sink design), Zhang, Lin and Wang 2024 (Scientific Reports, our template paper: trained in about one hour on one GPU using DeepXDE and PyTorch, validated in COMSOL), Du et al. 2025 (thermal management review). The field is settled enough that nobody will tell us "this cannot work."

Our novelty: existing papers optimize for peak temperature and stop. We frame the objective as an energy proxy (required cooling strength) and translate the measured improvement into a savings estimate with assumptions stated.

Starter problem: the one from section 2.6. Feasibility: the easiest of the three. 2D steady conduction is textbook physics, validation is a 50-line solver plus a hand formula, and it runs on a free Colab GPU. Full details are in the plan below.

### Option B: cooling plate shape optimization for EV batteries

An EV battery pack sits on a cold plate, a flat metal plate with liquid channels. The channel shape (width, spacing, pin-fins) decides how evenly the cells stay cool. Batteries that run hot, or unevenly cool, age faster and deliver less range, and every watt the pump spends comes straight out of driving range.

Green numbers: cooling parasitics directly cut EV range; temperature uniformity controls battery lifetime, and replacing a pack is a huge carbon cost. Bonus: the same plate geometry problem serves liquid cooling in data centers, so one physics gives two green stories.

Research behind it: Li et al. 2024 in Energy (around 80 citations, liquid cold plate battery cooling), Guo et al. 2022 (around 83 citations, mini-channel plate with pin-fins, exactly the geometry family we would tune), and a 2024 PINN battery pack thermal study that hit sub-degree accuracy with millisecond inference. The literature scan confirmed the gap: cold plate optimization by CFD is mature, PINN thermal prediction exists, but studies combining PINNs with cold plate geometry optimization are explicitly sparse. That sparse intersection is our claim.

Our novelty: a PINN-based cold plate shape optimization with a temperature-uniformity-plus-pumping-power objective, plus an order-of-magnitude range and lifetime estimate with assumptions stated. Nobody in the papers we found does the combined thing.

Starter problem: a 2D plate, five battery cells as rectangular heat sources, knobs for channel width and pitch, objective to minimize both the hottest cell and the cell-to-cell spread under a pumping budget. Validation with our grid solver, with trends checked against Li et al. and Guo et al. Around 70% of the Option A code is reusable.

### Option C: electric motor geometry optimization

Electric motors turn electricity into motion in factories, pumps, fans, EVs, and trains. The geometry of the iron core (rotor, stator, slots, magnets, air gap) decides how much electricity is wasted as heat. We would teach a PINN the 2D magnetic physics of a motor cross-section and tune the core geometry to cut losses.

Green numbers: this is the biggest single stat available to us. Motor systems consumed 53% of global electricity in 2023, about 13,500 TWh, per the IEA. In industry alone it is 72% of electricity. Motors run for decades, so a geometry decision made on a laptop multiplies for twenty years. A 1% efficiency gain across motor systems is on the order of hundreds of TWh.

Research behind it: the template paper (Zhang et al. 2024) is itself magnetostatics (the magnetic version of the same Poisson-type equation), with a shape network, iron versus air material contrast handled through domain decomposition, and COMSOL validation. Son et al. 2023 (around 98 citations) built a PINN for motor modeling. Sakamoto did multi-objective motor design optimization with a physics-assisted network. Stensson 2023 did PINN thermal modeling of motors.

Our novelty: published PINN motor work does dynamics modeling or surrogate models, and Zhang et al. targeted field and torque values. An efficiency or loss-minimization objective with a projected electricity saving is absent from the papers we found. That is ours.

Starter problem: first reproduce Zhang et al.'s C-shaped iron core case (we get a published number to match, which de-risks the whole option), then add one knob family (core limb width or air gap size) and switch the objective to loss proxies, like keeping peak magnetic flux below the level where iron wastes energy. Hardest of the three, but the only one where milestone one is reproducing a published benchmark. The blunt risk: the huge material contrast (iron versus air, a factor of about 1,000) is known to make PINN training hard, and reproducing the benchmark alone could eat much of the term. Choose C only if the panel accepts a genuinely riskier project.

### Comparing the three

| Criterion | A: heat sink | B: battery plate | C: motor |
|---|---|---|---|
| Headline green stat | 415 TWh, cooling 30-40% of it | EV range and battery lifetime | 53% of all global electricity |
| Research base | Strongest (template paper is the same problem) | Good (gap confirmed, neighbors strong) | Good (template is the same equation) |
| Novelty defensibility | Medium (method known, accounting new) | High (sparse intersection confirmed) | High (green objective absent) |
| Physics difficulty | Easiest | Easy (conduction plus channel cooling) | Medium (magnetics, material contrast) |
| Code reuse if starting from A | (baseline) | About 70% | About 40% |
| Published benchmark to reproduce | Similar to Zhang et al. | No single paper (that is the gap) | Yes, Zhang et al. case 1 |
| Worst-case fallback | Solver comparison | Solver comparison | Published reproduction plus comparison |
| Teacher wow factor | High, familiar story | High, EV story | Highest, the 53% stat |

What we looked at and dropped (worth mentioning to the teacher, it shows we chose rather than settled):

- Wind turbine airfoils: PINN airfoil optimization is already crowded (Sun et al. 2023 with around 175 citations, Liu et al. 2025), so novelty is thin, and flow physics is harder for one trimester.
- HVAC duct shapes: fine green story, but we found no shape-optimization precedent to lean on, and realistic duct flow is turbulent, which is too hard for one trimester.
- EV energy prediction (EV-PINN): a different project family, not shape optimization. Kept as a citation only.

Recommendation. If the priority is finishing safely inside the trimester, take A. If the faculty rewards novelty and accepts real risk, take C, knowing the benchmark reproduction alone could eat much of the term. B is the middle path, nearly A-level feasibility with a fresher gap. Whichever we take, present all three as one research program (differentiable design optimization for operating-energy reduction) with the chosen topic as the course project and the other two as the extension roadmap. That turns one course project into a research agenda, and that is what impresses a panel.

---

## 5. Do we have the domain knowledge?

The teacher's question is not really "are you experts." It is "do you know what you do not know." So we answer with this matrix, not with a yes.

| Domain | What we need | Where we stand | How we close the gap |
|---|---|---|---|
| Physics | 2D steady heat conduction, the three edge types, nondimensionalization | Covered by calculus and numerical methods courses; textbook material | Cai et al. 2021 review, then verify our code against the hand-computed fin formula |
| Numerics | Sampling points, residual minimization, convergence checks, a reference grid solver | Covered by the numerical methods course | Write the 50-line NumPy solver; it doubles as validation |
| Deep learning | Neural networks, PyTorch autodiff, loss balancing, Adam then L-BFGS | Covered by ML coursework | DeepXDE tutorials, Zhang et al. as the recipe |
| Shape optimization | Parameterization (a few knobs), volume constraints, gradients via autodiff | The one real gap, but small: autodiff computes the shape gradients, so no classical adjoint solver is needed. Making those gradients behave in practice is part of the research risk | Zhang et al. 2024 method, starting with 2 or 3 knobs |
| Green computing metrics | PUE, energy attribution, carbon measurement | This is the course domain | CodeCarbon on every experiment, which is itself a course deliverable |

What we deliberately avoid: turbulence, 3D meshes, HPC clusters, commercial CFD licenses, and hand-derived adjoint mathematics.

The de-risking sentence for the teacher: we scope to the simplest physics that still carries the green story, steady 2D conduction. If convection coupling proves hard, we drop to pure conduction, still a valid fin study. If PINN shape optimization underperforms the brute-force sweep, that measured comparison is itself a valid result. The hardest single step is PINN training convergence; the fixes are known (problem scaling, loss weighting, published recipes) but not guaranteed, which is why the validated solver is a standalone milestone before any optimization. Every failure mode degrades to a deliverable.

---

## 6. Is it doable in one trimester?

Compute: the template paper trained its shape optimization network in about one hour on a single GPU using about 4 GB of memory. Our conduction problem is smaller. A free Google Colab GPU is enough, and a laptop CPU handles the classical baseline. Tooling is mature and free: DeepXDE with a PyTorch backend as the main framework, NumPy for the reference solver, scikit-fem or FEniCS if we want a stronger classical baseline, CodeCarbon for energy measurement.

Ambition ladder, so nobody expects the wrong thing:

- Realistic: a validated PINN matching the grid solver within a few percent; 2 to 3 shape knobs optimized by gradient search on a parametric PINN; a savings illustration with assumptions stated; a documented comparison, whichever way it lands.
- Stretch: the template paper's joint shape-plus-physics training, reproducing its published benchmark case; an optimized geometry that beats the brute-force sweep.
- Deliberately out: beating classical solvers on speed at this scale, 3D, fluid flow, turbulence, hardware experiments, production-grade savings claims.

What matters: validated solvers, honest assumptions, the measured comparison, rerunnable code. What does not: speed records, novelty for its own sake, model size.

Twelve-week plan:

| Weeks | Milestone |
|---|---|
| 1-2 | Literature review from the table in section 4; reproduce a DeepXDE 2D example |
| 3-4 | Grid solver for the 2D plate with convective edges; verify against the 1D fin formula |
| 5-7 | PINN solver for the same problem; match the grid solver within a few percent |
| 8-9 | Parametric PINN with 2 to 3 shape knobs and gradient search (joint shape-plus-physics training only as a stretch); objective: lowest hottest temperature under a volume budget; run the brute-force knob sweep on the grid solver as the baseline |
| 10 | Savings translation: measured relative improvement plus an order-of-magnitude kWh illustration with assumptions; CodeCarbon log of our own experiments |
| 11-12 | Report and presentation, including the honest comparison and the limitations |

Risks and what we do about them:

| Risk | Likelihood | Response |
|---|---|---|
| PINN training does not converge well (loss terms fight each other; the documented failure mode of this method) | Medium to high | Nondimensionalize the problem, self-adaptive loss weights (as Zhang et al. did), Adam then L-BFGS; the validated-solver milestone comes before optimization, so a stall is caught early |
| Shape optimization converges to a weak optimum | Medium | Start with 2 knobs; always cross-check against a brute-force knob sweep on the grid solver |
| A brute-force sweep beats the PINN loop at this scale | Real possibility with 2-3 knobs | Report it honestly; the comparison is itself the result. PINN advantages (instant queries, free gradients) grow as knob count grows |
| Scope creep into fluids | High, it is tempting | Freeze physics at conduction, fluids are future work |
| Someone cites "PINNs are slower than FEM" | Certain, a sharp teacher will | We cite that same paper first and reframe; both loops' energy gets logged as a secondary data point, not the headline |
| Compute shortfall | Low | Colab free tier and CPU baselines |

Overall verdict: feasible, with one honest caveat about what that word means. The plan will run, something will be measured, and every failure mode still leaves a deliverable. What is not guaranteed: that the PINN wins its comparisons, or that a 2D result transfers to real hardware. Both are open questions the project answers with data instead of assumptions.

What this project can and cannot claim:

Can:

- Build and validate both solvers (PINN and classical grid) on the same 2D problem.
- Measure whether the PINN design loop beats brute-force sweeping at course scale, in time and in kWh.
- Report the optimized shape's relative improvement under identical conditions.
- Give an order-of-magnitude energy savings illustration, assumptions stated.
- Log the project's own footprint.

Cannot:

- Guarantee facility-level savings from a 2D toy model.
- Prove PINNs beat FEM in general; for single solves we expect the opposite (Grossmann et al.).
- Cover turbulence, 3D geometry, or time-dependent effects in this term.
- Promise PINN training succeeds on every variant; instability is documented and we have mitigations, not guarantees.

---

## 7. Questions teachers may ask, and honest answers

**Is this green computing or mechanical engineering?** The deliverable is a design method that targets operating energy: we optimize hardware geometry for lower energy use, we translate the measured improvement into a savings illustration with assumptions stated, and we log our own experiment footprint. Green computing points both directions.

**Do you have the domain knowledge?** Section 5 is the answer: required depth is undergraduate PDEs plus ML, one identified gap (shape parameterization), closed by one reproducible paper, with a fallback at every stage.

**Why simulate instead of building prototypes?** Hardware prototypes cost weeks and money per iteration. Simulation explores hundreds of designs first, and hardware validation happens once at the end. That is standard modern engineering practice.

**Why not just use ANSYS or COMSOL?** Licenses cost more than a course budget, they are closed boxes we cannot instrument to measure energy per design query, and our research question is the method comparison itself. Studying a commercial black box cannot produce that.

**PINNs are slower than FEM for solving equations, why bother? And with 3 knobs, why not just try every combination?** Both fair, and we run the second one ourselves: a brute-force sweep on the fast grid solver is the baseline the PINN loop has to beat. If the sweep wins at this scale, we report that; the comparison is the research, not a formality. We also cite Grossmann et al. (2024) first: for a single solve, FEM wins. Our claim is about the loop, not the solve: instant queries after one training, plus free derivatives. Both loops' energy gets logged as a secondary data point, and whichever way it lands, the main output (the measured improvement of the optimized shape) does not change.

**What is new here, papers already exist?** The method transfer is known; in the papers we reviewed, the green question is not asked. Three things: an energy-proxy objective, a measured relative improvement with an assumptions-stated savings illustration (rarely reported), and a reproducible pipeline whose own footprint is logged.

**Is 2D steady conduction too simplified to matter?** It is the standard first rung. It already contains the real trade-off (more fin area versus more airflow blockage), it is verifiable by hand, and the simplification is stated as a limitation with fluids as future work. The template paper validates the same approach.

**How will you know your PINN is correct?** A validation ladder: hand-derived formula first, then our own grid solver, then agreement within a few percent. Only after that do we optimize anything.

**Is your savings number real?** It is an illustration, not a measurement: built from a 2D model with a simplified convection coefficient and stated assumptions, good to an order of magnitude. Saying exactly that in the report is part of the deliverable, not a weakness.

**What if the PINN does not converge or fails?** Every stage has a fallback: no shape optimization means a solver comparison, no PINN advantage means a measured and explained negative result. The project cannot end empty-handed by construction, though the worst case, a PINN that never reaches acceptable accuracy, leaves a weaker but still valid failure-analysis deliverable.

**How much compute do you need?** A free Colab GPU plus a laptop for the classical side. The template paper trained in about an hour on one GPU, and our problem is smaller.

**Why these three topics and not others?** We evaluated wind turbine blades (crowded field, thin novelty) and HVAC ducts (no feasibility precedent, turbulent flow) and dropped them for stated reasons. The three survivors share one research question, differ in physics difficulty and green-story strength, and each has a real research base.

---

## 8. Sources

Method and theory:

- Zhang, Lin, Wang (2024). Physics-informed shape optimization using coordinate projection. Scientific Reports 14:6537. https://www.nature.com/articles/s41598-024-57137-4 (the template paper, magnetostatics, DeepXDE, one GPU, about one hour per case)
- Grossmann et al. (2024). Can physics-informed neural networks beat the finite element method? IMA Journal of Applied Mathematics 89(1):143. https://academic.oup.com/imamat/article/89/1/143/7680268 (the honest baseline)
- Cai, Wang, Yin, Karniadakis (2021). Physics-informed neural networks for heat transfer problems. ASME Journal of Heat Transfer 143(6):060801. https://asmedigitalcollection.asme.org/heattransfer/article/143/6/060801/1104439/Physics-Informed-Neural-Networks-for-Heat-Transfer
- Luo (2025). Physics-informed neural networks for PDE problems. Artificial Intelligence Review. https://link.springer.com/article/10.1007/s10462-025-11322-7
- Du et al. (2025). PINNs for advanced thermal management.
- Son et al. (2023). Physics-informed neural networks for microprocessor cooling. IEEE. https://ieeexplore.ieee.org/document/10305161
- Volume-preserving physics-informed geometric shape optimization (2024). https://arxiv.org/html/2407.19064v2

Aerodynamics (backup domain and rejected-option evidence):

- Sun et al. (2023). Physics-informed deep learning for simultaneous surrogate modeling and optimization. CMAME. https://www.sciencedirect.com/science/article/pii/S0045782523001664
- Tay et al. (2026). Optimization of two-element airfoils using NVIDIA Modulus. AIAA Journal. https://arc.aiaa.org/doi/10.2514/1.C038303
- Liu et al. (2025). CNN-PINN-DRL driven shape optimization of airfoils.

Topic B (battery cold plate):

- Li et al. (2024). Performance enhancement of a battery thermal management system. Energy. https://www.sciencedirect.com/science/article/abs/pii/S0360544224015044
- Guo et al. (2022). Mini-channel cold plate with pin fins for battery thermal management.
- PINN battery pack thermal simulation with cylindrical heat sources (2024). https://www.researchgate.net/publication/386584843

Topic C (electric motors):

- IEA 4E EMSA. Electric motor systems: why are they important? (53% of global electricity, 2023). https://www.iea-4e.org/emsa/publications/policy-brief-electric-motor-systems-why-are-they-important
- IEC. Energy efficient motors (confirms the 53% figure). https://www.iec.ch/basecamp/energy-efficient-motors
- IEA. Motor-driven system electricity use by subsector. https://www.iea.org/data-and-statistics/charts/motor-driven-system-electricity-use-as-a-share-of-electricity-use-by-industry-subsector
- Son (2023). A novel physics-informed neural network for modeling electric motors.
- Sakamoto. Multi-objective motor design optimization with physics-assisted neural network.
- Stensson (2023). PINN for thermal modeling of an electric motor.
- Lim (2024). EV-PINN. https://arxiv.org/abs/2411.14691

Green computing context:

- IEA. Data centres and data transmission networks (415 TWh in 2024, doubling by 2030). https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks
- Our World in Data. Data centre energy use (~1.5% of global electricity). https://ourworldindata.org/data-centre-energy-use
- Uptime Institute. Global Data Center Survey 2025 (average PUE 1.54). https://uptimeinstitute.com/resources/research-and-reports

Tools:

- DeepXDE. https://deepxde.readthedocs.io
- NVIDIA PhysicsNeMo (formerly Modulus). https://github.com/NVIDIA/physicsnemo
- NeuralFoil / AeroSandbox. https://peter.sharpe.ai/neuralfoil
