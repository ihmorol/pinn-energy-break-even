# Project skills

These skills are shared instructions stored in the checkout. They do not require the owner's personal skill folders, API keys, or a specific agent host. Read [AGENTS.md](../../AGENTS.md) first. The [writing guide](../../docs/writing-style.md) applies whether or not a skill is loaded.

| Skill | When to use it |
|---|---|
| [research-writing](research-writing/SKILL.md) | Draft or edit prose for any part of this project |
| [research-coding](research-coding/SKILL.md) | Write, change, or review solver, training, measurement, or analysis code |
| [literature-check](literature-check/SKILL.md) | Check a paper, citation, or literature claim |
| [experiment-run](experiment-run/SKILL.md) | Plan, run, or record a pilot, training job, validation, or energy trial |
| [research-review](research-review/SKILL.md) | Review a method, result, figure, or report claim before accepting it |
| [read-documents](read-documents/SKILL.md) | Read a PDF, Word file, slide deck, spreadsheet, or unfamiliar folder without wasting tokens |

Hosts that support `.agents/skills/` may discover these skills after reopening the checkout. If a skill is not listed, ask the agent to read its `SKILL.md` directly. Do not assume that writing a file has installed it in every host. The root Claude, Gemini, and Copilot entry files point to the same shared rules.

The writing skill uses the requested humanlike-writing drafting approach and humanizer review approach. It is an original project checklist, not a copy of those installed packages. If both named skills are available, load them too, with the shared research rules taking precedence. Do not add their example claims or personal experiences to our work.

The research skills are also written for this project's limited scope. They do not install packages, start jobs, grant permissions, or publish files. Use the relevant tools only within the current task's authorization.

When changing a skill, try a realistic task and an edge case. Check both the answer and the actions it took. A writing test is not a detector test, and a skill test is not a measured research run.

## Third-party research-coding skills

These skills come from public repositories. They help with solver code, verification, statistics, and figures during the implementation phase. Each folder keeps the upstream license.

| Skill | When to use it |
|---|---|
| [numerical-stability](numerical-stability/SKILL.md) | Check stability limits for the explicit 1D heat scheme |
| [time-stepping](time-stepping/SKILL.md) | Choose and control the time step for the heat solver |
| [differentiation-schemes](differentiation-schemes/SKILL.md) | Pick finite-difference stencils and their error order |
| [linear-solvers](linear-solvers/SKILL.md) | Choose a direct or iterative solver for the 2D steady-diffusion system |
| [convergence-study](convergence-study/SKILL.md) | Run grid refinement and find the observed order of accuracy |
| [benchmark-and-mms-planner](benchmark-and-mms-planner/SKILL.md) | Plan verification with manufactured or exact solutions |
| [performance-profiling](performance-profiling/SKILL.md) | Find where solver or training time goes |
| [sympy](sympy/SKILL.md) | Derive exact solutions and source terms |
| [statistical-analysis](statistical-analysis/SKILL.md) | Analyze results across training seeds |
| [scientific-critical-thinking](scientific-critical-thinking/SKILL.md) | Check design, bias, and claims before accepting a result |
| [scientific-visualization](scientific-visualization/SKILL.md) | Design honest, readable figures |
| [matplotlib](matplotlib/SKILL.md) | Write the plotting code |

Sources:

- The first seven come from [HeshamFS/materials-simulation-skills](https://github.com/HeshamFS/materials-simulation-skills) at commit `a4bd93c`, under Apache-2.0.
- The last five come from [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) at commit `ec59a29`, under MIT.

Local changes: upstream `evals/` folders and READMEs were left out. Multi-line `description` fields were joined into one line for the workspace check. Two links to an upstream file outside the skill folder now point to that file on GitHub. Trailing spaces and extra blank lines at file ends were removed from six `performance-profiling` files. The rest is upstream text, so its style does not follow the writing guide; do not copy it into project prose.

The project rules come first. Some of these skills suggest installing packages, running helper scripts, or reporting in a fixed format such as APA. Follow those steps only when the current task allows it. The helper scripts need Python with NumPy in the project's environment.
