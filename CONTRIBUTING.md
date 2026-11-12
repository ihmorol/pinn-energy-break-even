# Contributing

Read the [project rules](AGENTS.md), [research plan](docs/research-plan.md), and [writing guide](docs/writing-style.md) before starting. These are shared requirements for members and AI agents.

## Open the workspace

Clone the private repository using an account with access:

```bash
git clone https://github.com/ihmorol/pinn-energy-break-even.git
cd pinn-energy-break-even
python -B -X utf8 -m unittest discover -s tests -v
python -B -X utf8 scripts/check_workspace.py
```

The workspace checks need Python 3.11 or newer and Git. They use the Python standard library. The solver environment is not set up yet. Choose and record PyTorch, SciPy, and measurement-tool versions during the pilot; do not treat these workspace checks as a training setup.

Use repository-relative paths in tracked files. Keep local environments, machine paths, and tokens out of shared configuration. Text files use UTF-8 and LF line endings; the repository includes editor and Git settings for Windows and Linux.

## Take one task

Use [GitHub Issues](https://github.com/ihmorol/pinn-energy-break-even/issues) for task ownership and progress. Claim a task before starting, state what files you expect to change, and record any dependency on another task. Leave scientific scope and protocol decisions in the research plan rather than copying them into several status documents.

Keep a PR focused on one purpose. For parallel work, split file ownership so agents or members do not overwrite each other. If someone else changed the same file, read the changes before editing. Do not reset another person's work to make a merge easier.

A task is done when its acceptance criteria are met, its evidence and settings can be found, relevant checks pass, and the result has been reviewed. A documented convergence failure may be a completed research task. A failed run is not missing work to erase.

## Branches and commits

`main` is the shared branch. It is the explicit exception to the work-branch naming rule. Create a work branch from current `main`:

```bash
git switch main
git pull --ff-only
git switch -c feat/validate-heat-pilot
```

Work branches use `<type>/<kebab-case-description>`:

| Type | Use |
|---|---|
| `feat` | New capability |
| `fix` | Bug fix |
| `hotfix` | Urgent production fix |
| `refactor` | Code changes without behavior changes |
| `chore` | Tools, dependencies, configuration, or CI |
| `docs` | Documentation only |
| `test` | Tests only |

The description has 2 to 5 words, uses present tense, contains no articles, and describes the change. The full name must be at most 60 characters. Do not use generic names such as `dev`, `patch`, `update`, `temp`, `wip`, `fix-stuff`, `new-feature`, or `test-branch`.

Make small commits grouped by purpose. Include related regression tests with a fix. Inspect `git diff --cached` before committing and exclude secrets, local logs, raw downloads, or unrelated changes. Push the work branch and open a PR against `main`. Do not force-push or rewrite shared history.

Agents need authorization to commit, push, change repository settings, or publish content. A request that clearly authorizes one of these actions is enough for that action; it does not authorize unrelated later work. Members must review AI-written work and follow the teacher's disclosure rules.

## Put work in the right place

| Location | Contents |
|---|---|
| `docs/research-plan.md` | Scope, work plan, and protocol decisions |
| `docs/proposal/` | Unchanged submitted files and their hash manifest |
| `references/` | Source records and checked paper notes |
| `experiments/` | Small run records and the study electricity ledger |
| `.agents/skills/` | Shared instructions for recurring research tasks |
| `scripts/`, `tests/` | Workspace checks and their tests |

When the first pilot is implemented, add reusable solver and measurement code under `src/pinn_energy_break_even/`, runnable settings under `configs/`, and tests under `tests/`. Add those paths with actual files rather than empty scaffolding. Keep notebooks, if needed, for exploration; move reusable work into tested code.

Write large generated outputs and checkpoints under `outputs/<run-id>/`, which Git ignores. Store each external download in its own new directory under `downloads/`, also ignored. Run processing scripts from a separate trusted location; use isolated Python for untrusted inputs. Do not execute code from a downloaded paper or archive without inspecting it and getting the required authorization.

An ignored directory is not a backup. Before deleting any real run output, keep it in approved shared storage and record its location and hash in the run record. Do not upload private files to a storage or analysis service without approval. Track small evidence summaries and their source locations so other members can reproduce the report.

## Before a PR

Run:

```bash
python -B -X utf8 -m unittest discover -s tests -v
python -B -X utf8 scripts/check_workspace.py
git diff --check
```

Add the relevant solver tests once research code exists. State what was checked, what failed, and what was skipped. Do not describe a passing workspace check as proof of scientific correctness.

Check the prose against the writing guide, verify claims against their sources, and keep the proposal hashes unchanged. Use the PR checklist for evidence and energy accounting. Do not add a second handoff log, a session transcript, or the old topic-selection documents.
