# Three Candidate Research Topics
## PINN Shape Optimization for Green Computing — with Real Research Bases and Novelty Claims

*Companion docs: research_feasibility_analysis.md (Topic 1 in depth) · concepts_glossary_faculty_qa.md (background from zero)*
*Prepared: 2026-11-01*

---

## 0. The shared novelty (our strongest card)

All three topics answer **one shared research question**, which is where our novelty lives:

> **"What is the energy cost of a computational design loop — and can a differentiable, physics-informed surrogate reduce it?"**

The PINN shape-optimization literature optimizes shapes for *performance* (temperature, torque, lift). It almost never reports the **energy consumed by the optimization itself**, and rarely frames the objective as *operating-energy reduction*. Our contribution applied to whichever topic we pick:

1. **Energy-accounted design loop** — kWh/CO₂ per optimized design, PINN loop vs. classical solver loop (CodeCarbon instrumented), anchored by the honest baseline of Grossmann et al. 2024.
2. **Green objective function** — the shape target is *operating energy* (fan/pump power, loss reduction), not just peak temperature or torque.
3. **Reproducible, footprint-reported pipeline** — open code, small models, measured carbon budget.

This framing survives the "what's new?" question because the *method transfer* is known — the *accounting and the green objective* are not.

---

## 1. Topic 1 (original): Data-center / electronics heat-sink shape optimization

| | |
|---|---|
| **Plain language** | Teach a PINN the physics of heat flowing through a finned metal plate; let it automatically find fin shapes that keep a chip cool with the least fan energy. |
| **Green stat** | Data centers ≈ **415 TWh (2024), >1× the UK's electricity**; cooling ≈ **30–40%** of facility energy (avg. PUE 1.54). |
| **Research base** | Cai et al. 2021 (ASME review, ~2,000 cites) · Son et al. 2023 (IEEE, free-form heat-sink PINN) · **Zhang, Lin & Wang 2024 (Sci. Reports — our template; ~1 h training on 1 GPU)** · Du et al. 2025. |
| **Novelty gap** | Existing works optimize for peak temperature; none report design-loop energy or frame the objective as fan/cooling-power minimization. |
| **Feasibility** | ★★★ Easiest — 2D steady heat conduction, textbook physics, NumPy FDM validation, free Colab. |
| **Full details** | See research_feasibility_analysis.md |

---

## 2. Topic 2: EV battery cold-plate (microchannel) shape optimization

### 2.1 Plain language
Electric-vehicle battery packs sit on **cold plates** — flat metal plates with liquid channels machined through them. The *shape of those channels* (width, spacing, pin-fin layout) decides how evenly the battery cells stay cool. Batteries that run hot, or unevenly cool, age faster and deliver less range — and every watt the cooling pump spends is subtracted from driving range. We would teach a PINN the 2D heat physics of a battery pack on a cold plate and optimize the channel/fin geometry.

### 2.2 Green-computing relevance
- EV efficiency: cooling parasitics (pump + chiller load) directly reduce vehicle range; thermal management quality also controls battery **lifetime** (replacement = huge embodied carbon).
- Temperature *uniformity* (delta-T across cells) is the known driver of pack aging — a genuinely green objective, not just "make it cold."
- Secondary angle: the same cold-plate geometry problem serves data-center liquid cooling of GPUs — one physics, two green stories.

### 2.3 Actual research base (real, recent, citable)
- **Li et al. 2024, *Energy*** (cited ~80) — liquid cold-plate battery thermal management performance enhancement: https://www.sciencedirect.com/science/article/abs/pii/S0360544224015044
- **Guo et al. 2022** (cited ~83) — mini-channel cold plate with **pin fins** as novel BTMS concept: the exact geometry family we would parameterize.
- **PINN battery-pack thermal field prediction** (2024, sub-°C accuracy, **millisecond inference**): https://www.researchgate.net/publication/386584843 — proves the PINN surrogate works on pack geometry with cylindrical heat sources.
- **Son et al. 2023 (IEEE)** — free-form heat-sink design PINN; method transfers directly to cold plates.
- Literature status: CFD/surrogate cold-plate optimization is mature, and PINN battery thermal *prediction* exists — **but studies combining PINNs with cold-plate geometric optimization are explicitly sparse (confirmed in literature scan, 2024–2025). That sparse intersection is our claim.**

### 2.4 Novelty we claim
First (course-scale) PINN-based **shape optimization of a cold plate** with a **delta-T + pumping-power objective** and energy-accounted design loop. Nobody in the found literature does the combined thing.

### 2.5 Starter problem (concrete)
- 2D plate; battery cells = rectangular heat sources (e.g., 5 cells, fixed total heat).
- Knobs: channel width, channel pitch, (optional) pin-fin density along channels.
- Physics: steady conduction with internal heat generation; channel walls = convective (Robin) boundaries.
- Objective: minimize max cell temperature **and** cell-to-cell temperature spread, subject to a pumping-power proxy budget.
- Validation: NumPy FDM; limits checked against Li et al./Guo et al. trends (more channels → cooler but more pumping).
- Physics risk is nearly identical to Topic 1 — **~70% of the Topic 1 codebase is reusable.**

---

## 3. Topic 3: Electric-motor geometry optimization for efficiency (electromagnetic PINN)

### 3.1 Plain language
Electric motors turn electricity into motion — in factories, pumps, fans, compressors, EVs, trains. The geometry of the motor's iron core (rotor, stator, slots, magnets, air gap) decides how much electricity is wasted as heat. We would teach a PINN the 2D magnetic physics inside a motor cross-section and optimize core geometry to reduce losses — i.e., waste less electricity for the same mechanical work.

### 3.2 Green-computing relevance — the biggest single number available to us
- **Electric motor systems consumed 53% of global electricity in 2023 (~13,462 TWh)** per the IEA 4E EMSA: https://www.iea-4e.org/emsa/publications/policy-brief-electric-motor-systems-why-are-they-important (also confirmed by IEC: https://www.iec.ch/basecamp/energy-efficient-motors)
- 72% of *industrial* electricity goes to motor-driven systems; even a **1% efficiency gain across motor systems ≈ hundreds of TWh**.
- Motors are designed once and run for decades — geometry decisions made on a computer multiply for 20+ years. This is the strongest "shape → energy" multiplier of all three topics.

### 3.3 Actual research base (real, recent, citable)
- **Zhang, Lin & Wang 2024 (Sci. Reports)** — *this is our template paper and it IS magnetostatics*: 2D magnetic vector potential (∇²A = −μJ, a Poisson-type equation), shape-projection network, iron/vacuum material contrast (μ = 1000) via domain decomposition, COMSOL-validated, DeepXDE + PyTorch on one GPU: https://www.nature.com/articles/s41598-024-57137-4
- **Son et al. 2023** (cited ~98) — PINN architecture for modeling electric motors.
- **Sakamoto, Multi-Objective Motor Design Optimization with Physics-Assisted Neural Network** (cited ~17) — proof that PANN/PINN-assisted motor design optimization is an active research direction.
- **Stensson 2023** — PINN thermal modeling of electric motors (the multi-physics extension path).
- **EV-PINN (2024)** — https://arxiv.org/abs/2411.14691 — energy prediction for EV powertrains (context/framing citation).

### 3.4 Novelty we claim
Zhang et al. optimized magnetostatic shapes for *field/torque targets* (make B reach a target, maximize torque). Published PINN motor work is mostly *dynamics modeling* or *FEM surrogates*. Open gap we take: **PINN shape optimization with an efficiency/loss-minimization objective** (e.g., minimize magnetic-field distortion and loss proxies in the iron) **plus design-loop energy accounting** — a green objective the literature doesn't do.

### 3.5 Starter problem (concrete)
- 2D C-shaped iron core with a coil (Zhang et al.'s Case 1 — directly reproducible as our first milestone, giving us a *published benchmark to match*).
- Then add one design knob family (core limb width / air-gap size) and switch the objective to loss-proxy minimization (e.g., minimize peak flux density below saturation — the real driver of iron losses).
- Validation: reproduce Zhang et al.'s published numbers first, then our own FDM/FEniCS magnetostatic solve.
- Hardest of the three (material contrast, new physics domain), but the only one where **milestone 1 has a published number to reproduce**, which de-risks it unusually well.

---

## 4. Runners-up considered and rejected (show this to the faculty — it demonstrates selection rigor)

| Candidate | Why not (for this course) |
|---|---|
| **Wind-turbine airfoil/blade optimization** | PINN airfoil optimization is already crowded (Sun 2023 ~175 cites; Liu 2025 CNN-PINN-DRL ~30 cites) → novelty is thin; requires flow physics (harder than conduction/magnetostatics); wind-turbine-specific niche exists but faculty will note the crowded field. |
| **HVAC duct/junction shape optimization** | Green story fine (buildings ≈ 30–40% of global electricity), but the research base for feasibility is thin (only pressure-drop *prediction* PINNs found, no shape-optimization precedent), and realistic duct flow is turbulent → hard physics for one trimester. |
| **EV-PINN energy prediction** (arXiv 2411.14691) | Not shape optimization — different project family. Kept as a citation only. |

---

## 5. Side-by-side comparison

| Criterion | T1: Heat sink / DC cooling | T2: Battery cold plate | T3: Electric motor |
|---|---|---|---|
| Green headline stat | 415 TWh DC electricity; cooling ~30–40% of it | EV range & battery lifetime; also DC liquid cooling | **53% of ALL global electricity** |
| Research base strength | ★★★ (template paper = same problem) | ★★☆ (gap confirmed, adjacent papers strong) | ★★☆ (template = same PDE; objective gap open) |
| Novelty defensibility | ★★☆ (method known; accounting novel) | ★★★ (explicitly sparse intersection) | ★★★ (green objective absent in literature) |
| Physics difficulty | ★ Easiest (conduction) | ★★ Conduction + channel convection | ★★☆ Magnetostatics + material contrast |
| Codebase reuse from T1 | — | ~70% | ~40% (different PDE, same pipeline) |
| Published benchmark to reproduce | Zhang et al. (similar) | No single paper (gap) | **Yes — Zhang et al. Case 1** |
| Worst-case fallback | solver comparison | solver comparison | reproduce published case + comparison |
| Faculty "wow" factor | High (familiar DC story) | High (EV story) | **Highest (53% stat)** |

## 6. Recommendation

**Primary: Topic 1 (heat sink) — recommended if we weight feasibility and the trimester deadline.**
**Alternative: Topic 3 (motor) — recommended if the faculty rewards novelty and headline impact; the Zhang et al. reproduction milestone makes it safer than it looks.**
**Topic 2 is the safest "second choice" — nearly Topic-1 feasibility with a fresher gap, and a great EV narrative.**

Whatever we pick, we present all three as **one research program** ("energy-accounted differentiable design optimization for green computing") with the chosen one as the course project and the other two as the extension roadmap. That converts "one course project" into "a research agenda" — exactly what impresses a faculty panel.

---

## 7. New sources for Topics 2 & 3

- IEA 4E EMSA, *Electric motor systems: why are they important?* (2023 figures: 53% of global electricity). https://www.iea-4e.org/emsa/publications/policy-brief-electric-motor-systems-why-are-they-important
- IEC, *Energy efficient motors* (confirms 53% figure). https://www.iec.ch/basecamp/energy-efficient-motors
- IEA, motor-driven system electricity share by subsector. https://www.iea.org/data-and-statistics/charts/motor-driven-system-electricity-use-as-a-share-of-electricity-use-by-industry-subsector
- Li et al. 2024, *Energy* — battery cold-plate BTMS performance enhancement. https://www.sciencedirect.com/science/article/abs/pii/S0360544224015044
- PINN battery-pack thermal simulation with cylindrical heat sources (2024). https://www.researchgate.net/publication/386584843
- Sakamoto — Multi-objective motor design optimization with physics-assisted neural network (PANN).
- Son et al. 2023 — Novel PINN for modeling electric motors (~98 citations).
- Lim 2024 — EV-PINN: battery power/energy prediction. https://arxiv.org/abs/2411.14691
- Stensson 2023 — PINN thermal modeling of an electric motor.
- Liu et al. 2025 — CNN-PINN-DRL airfoil shape optimization (runner-up evidence).
- Sun et al. 2023 — PINN airfoil surrogate + optimization, CMAME (runner-up evidence). https://www.sciencedirect.com/science/article/pii/S0045782523001664
