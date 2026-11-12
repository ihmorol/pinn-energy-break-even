# Reaching the energy and computational break-even point between PINNs, and classical solvers.

Green Computing research project. The proposal is submitted; solver implementation and experiments have not started.

We will compare the cumulative energy and runtime of a parametric physics-informed neural network (PINN) and a classical PDE solver at matched accuracy. The question is how many new parameter queries it takes to recover the PINN's setup and training costs. A crossover may not exist, or it may be too far away to be useful. Either is a valid result.

## Start here

Read the [research plan](docs/research-plan.md) for the fixed scope and the [contribution guide](CONTRIBUTING.md) for setup and team work. Members and AI agents must follow [AGENTS.md](AGENTS.md) and the [writing guide](docs/writing-style.md). Use the owner's words when a supplied example fits; otherwise use simple, common words.

The study has a 1D heat pilot and one main 2D steady-diffusion experiment on a square. Two bounded parameters control the spatially varying conductivity; geometry and boundary conditions stay fixed. The methods are a small parametric PyTorch PINN and finite differences with SciPy sparse solvers, including valid classical reuse. Each query returns the solution for an unseen parameter setting on a fixed output grid.

The primary relative L2 error targets are 1% and 0.1%. The 0.01% target is optional within the training budget. Both methods must pass the accuracy check before full energy trials for a target. The plan records the remaining choices about hardware, telemetry, the exact equations, and the evaluation protocol.

## Workspace

| Location | What to use it for |
|---|---|
| [Research plan](docs/research-plan.md) | Scope, twelve-week plan, and protocol decisions |
| [Submitted PDF](docs/proposal/ENERGY_CROSSOVER_PROPOSAL.pdf) and [Word file](docs/proposal/ENERGY_CROSSOVER_PROPOSAL.docx) | The original two-page submission and its source |
| [Writing guide](docs/writing-style.md) | Required word choice, style, and fact checks |
| [References](references/README.md) | Source records and paper notes |
| [Experiments](experiments/README.md) | Run records, failures, and study electricity accounting |
| [Project skills](.agents/skills/README.md) | Shared instructions for writing, literature, runs, and review |
| [GitHub Issues](https://github.com/ihmorol/pinn-energy-break-even/issues) | Tasks, ownership, and progress |

The submitted files keep their original heading, *The energy crossover*, and their original bytes. The title at the top of this README is the current project name. The [proposal manifest](docs/proposal/manifest.json) records both file hashes.

## Check the checkout

Use Python 3.11 or newer. From the repository root, run:

```bash
python -B -X utf8 -m unittest discover -s tests -v
python -B -X utf8 scripts/check_workspace.py
```

These checks use the standard library. They check the workspace, not solver accuracy or measured results. GitHub Actions runs them on Windows and Linux. The research dependencies will be chosen and recorded during the pilot.

Use `main` as the shared branch and a named work branch for each change. See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch rules, file locations, and PR checks. The first work is to confirm energy telemetry, validate the 1D pilot, and freeze the main experiment protocol.
