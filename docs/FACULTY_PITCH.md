# Project pitch: shape optimization with physics informed neural networks

Course project proposal, green computing. One page, bullet points.

---

## The idea

- Computer chips make heat. Cooling them costs electricity.
- How much energy cooling needs is decided by shape: heat sink fins, cooling plates, air ducts.
- We teach a neural network the laws of heat (a PINN, physics informed neural network).
- The network then searches shapes by itself, aiming for ones that keep chips cool with less energy.
- Then we measure how much the better shape beats a standard one, and translate that into a yearly kWh estimate with assumptions stated.

## Why this is green computing

- Data centers used about 415 TWh in 2024. More than the whole UK uses in a year. Expected to double by 2030 (AI demand).
- Cooling is 30 to 40% of that. Average efficiency (PUE) is 1.54: about a third of energy is overhead.
- Better shapes mean slower fans and smaller chillers. A design made on a laptop saves energy for years.
- Sense of scale (illustration): the design work costs a few kWh of GPU time. A 1% cooling saving in one data center hall would be tens of thousands of kWh per year. That ratio is why the shape is the valuable output.
- Car analogy: engineers save fuel by smoothing the shape, not by building a bigger engine.

## What is new (our novelty)

- Published PINN shape optimization targets performance numbers (peak temperature, torque) and stops. The green question comes next: how much energy does the better shape actually save?
- We claim three things:
  - A green objective: minimize operating energy (fan power, pump power, losses), not just peak temperature.
  - An honest translation: measured relative improvement, plus an order-of-magnitude yearly kWh estimate with assumptions stated. No facility guarantees from a 2D model.
  - Application gaps: our literature scan found PINN + cold plate geometry sparse and efficiency objectives absent from PINN motor work (to be verified by a deeper review).
- What we do NOT claim: no speed win. At this 2D scale, classical solvers are faster and we expect our simple solver to beat our PINN. We measure it and report it either way.
- One hygiene note (not a novelty claim): we log the energy our own experiments consumed (CodeCarbon), as green-AI practice asks. The design loop costs a few kWh; the shape it finds saves thousands per year. The shape is the story.

## How it works, in short

- The network takes a point (x, y) and outputs the temperature there.
- It has no training data. The physics equation is the teacher: we check the equation at random points and score how badly it is violated (the loss).
- Training adjusts the network until physics holds everywhere. Then the network is the temperature field, and answers are instant.
- Shape knobs (fin height, thickness, spacing) are numbers we can tune.
- Because everything is differentiable (autodiff), the software tells us which way to move each knob to lower the temperature. No hand-derived math needed.
- We search for the lowest peak temperature under a fixed metal budget.
- Step-by-step training recipe: MASTER_PROJECT_FILE.md, section 2.7.

## Three topic options (we present one, mention all)

- Option A: data center heat sink.
  - Green stat: 415 TWh, cooling 30-40% of it.
  - Easiest physics (2D steady heat conduction), strongest published base.
  - Novelty: energy-proxy objective plus a measured improvement translated to savings, assumptions stated.
- Option B: EV battery cooling plate.
  - Liquid channel shape decides how evenly battery cells stay cool. Uneven heat shortens battery life and cuts range.
  - Green stat: less pumping = more driving range; better uniformity = longer battery life.
  - Novelty: literature scan confirms PINN + cold plate geometry is an open gap.
- Option C: electric motor geometry.
  - Motor systems consumed 53% of all global electricity in 2023 (about 13,500 TWh, IEA).
  - Core geometry decides how much electricity is wasted as heat. Motors run for decades.
  - Novelty: existing PINN motor work targets torque, not efficiency or energy savings.
  - Blunt risk: reproducing the published benchmark alone could eat much of the term. Highest payoff, highest risk.
- Dropped on purpose: wind turbine blades (already crowded field), HVAC ducts (no feasibility precedent, turbulent flow).

## Recommendation

- Pick A to finish safely inside the trimester.
- Pick C if the panel rewards novelty and accepts real risk.
- Present all three as one research program: "differentiable design optimization for operating-energy reduction."

## Research base (real, recent)

- Zhang, Lin, Wang 2024 (Scientific Reports): PINN shape optimization, trained in about 1 hour on one GPU. Our template.
- Cai et al. 2021 (ASME): PINNs for heat transfer, about 2,000 citations. Foundational.
- Grossmann et al. 2024 (IMA J.): honest baseline. FEM is faster for solving one equation once.
- Son et al. 2023 (IEEE): free-form heat sink design with PINNs.
- Li et al. 2024 (Energy) and Guo et al. 2022: battery cold plate design.
- IEA 4E EMSA 2023: motor systems use 53% of global electricity.
- Full source list with links: see MASTER_PROJECT_FILE.md, section 8.

## Feasibility

- Physics: 2D, steady-state, textbook level. No turbulence, no 3D, no clusters.
- Tools: all free and open source. DeepXDE + PyTorch for the PINN, NumPy for the classical reference solver, CodeCarbon for energy logging.
- Compute: free Google Colab GPU. Template paper trained in about 1 hour on one GPU.
- Realistic: validated 2D PINN, 2-3 shape knobs optimized, savings illustration with assumptions.
- Stretch: reproducing the template paper's joint shape-plus-physics benchmark.
- Out of scope on purpose: speed records, 3D, fluids, turbulence, hardware tests.
- Plan (12 weeks):
  - Weeks 1-2: literature + reproduce a tutorial example.
  - Weeks 3-4: build the simple reference solver, verify against a hand formula.
  - Weeks 5-7: PINN solver matches the reference within a few percent.
  - Weeks 8-9: shape knobs + optimization loop, plus a brute-force sweep baseline on the grid solver.
  - Week 10: translate the measured improvement into a savings estimate (assumptions stated); log our own footprint.
  - Weeks 11-12: report and presentation.

## Domain knowledge (the direct answer to "do you have it?")

- Required: undergraduate PDEs + numerical methods + ML coursework. We have this.
- One gap: shape parameterization. Narrowed by following one template paper (Zhang et al. 2024); making it work in practice is part of the research.
- We deliberately avoid: turbulence, 3D meshes, HPC, commercial licenses, hand-derived adjoint math.

## Risks and honest framing

- "PINNs are slower than FEM" is true for solving one equation once (Grossmann et al. 2024). We cite that paper ourselves.
  - Our claim is different: after one training, thousands of shape checks are nearly free, and gradients come automatically.
  - Both loops' energy still gets logged as a secondary data point. A negative result is still a valid result.
- With only 2-3 knobs, a brute-force sweep on the fast grid solver may beat the PINN loop. We run the sweep as the honest baseline and report whichever wins. The comparison is the research.
- PINN training can be unstable. Known fixes exist (loss weighting, scaling), used by the template paper.
- Scope creep into fluids. We freeze physics at conduction; fluids are future work.
- Every failure mode degrades to a deliverable: no optimization = solver comparison, no PINN advantage = measured negative result.

## Validation (how we prove our code is right)

- Step 1: check against a hand-computed textbook formula for a simple fin.
- Step 2: check against our own simple grid solver (FDM, finite difference method).
- Step 3: PINN must agree within a few percent before we optimize anything.

## What we can and cannot claim

- Can: validate both solvers, honestly compare the design loops (time and kWh), report the shape's relative improvement, give a savings illustration with assumptions, log our own footprint.
- Cannot: guarantee facility savings from a 2D model, prove PINNs beat FEM in general, handle turbulence or 3D this term, promise PINN training always succeeds.

## Expected deliverables

- A validated PINN solver for the chosen 2D problem.
- An automatic shape optimization loop with a green objective.
- A savings illustration: measured relative improvement plus an order-of-magnitude yearly kWh estimate, assumptions stated.
- An experiment footprint log (CodeCarbon) as green-AI hygiene.
- Reproducible open-source code and a final report with limitations stated.
