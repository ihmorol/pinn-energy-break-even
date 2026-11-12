---
name: research-review
description: Review the study's methods, measurements, plots, and report claims before accepting or publishing them. Use for research-code review, experiment analysis, result tables, crossover claims, and paper drafts; check evidence and fairness without assuming PINNs will win.
---

# Research review

Read the [project rules](../../../AGENTS.md) and the relevant [research plan](../../../docs/research-plan.md) sections. Review the supplied change and its evidence, not unrelated files or old topic history. Load the [writing skill](../research-writing/SKILL.md) when reviewing prose.

Check the following where they apply:

- The methods solve the agreed workload on the same held-out parameters and output grid at the same relative L2 target. The reference is checked, grid refinement is documented, and the held-out set was not used for tuning.
- The classical baseline retains valid setup/factorization/preconditioner reuse. Queries represent new parameter settings rather than an artificial cache or repeated-solve disadvantage.
- Setup, training, and query costs are separated. Timing is synchronized where needed, query blocks are long enough for the telemetry, and CPU/GPU measurement coverage is comparable. Estimates are labeled.
- At least three training seeds and repeated measurements support the planned comparison. Failed attempts, tuning, retry rules, and study electricity remain visible. Accuracy failures are not ranked as valid fast solutions.
- The break-even model uses the observed slopes and setup costs. A zero or uncertain denominator, negative intersection, no crossing, or distant extrapolation is handled explicitly. Check energy and runtime separately.
- A claim can be traced to raw readings or a checked source. Configuration, code version, hardware, units, and artifact locations let another member repeat the work. Do not treat a plot's appearance as proof that its values are correct.
- The wording follows the shared guide and preserves uncertainty. No unsupported novelty, hidden failure, invented experience, or unverified citation has been added.

Separate blocking problems from suggestions. For each problem, give the file or evidence location, what is wrong, why it matters to the comparison, and the smallest useful correction. State what you could not check. Return a concise no-issues finding only for the material actually reviewed.

A review does not authorize fixing files, rerunning expensive work, changing the protocol, or publishing results. Use the current request's permissions. Do not approve a claim merely because workspace tests pass.
