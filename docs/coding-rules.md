# Coding rules

These rules apply to all code in this repository, written by members or AI agents. They sit under [AGENTS.md](../AGENTS.md). The [writing guide](writing-style.md) also covers comments, docstrings, and commit messages. Use the [research-coding skill](../.agents/skills/research-coding/SKILL.md) when writing or reviewing code.

## Layout

Keep the tree flat. Create a path only when the first real file needs it; Git does not keep empty folders.

```text
src/pinn_energy_break_even/   one package, flat modules
  problems.py                 equations, parameter sets, reference solutions
  classical.py                finite-difference solvers
  pinn.py                     model, loss, training
  measure.py                  timing and energy readings
  evaluate.py                 shared error check for both methods
  crossover.py                break-even analysis
configs/                      one TOML file per run setting
scripts/                      thin command-line entry points
tests/                        test_<module>.py, fast, CPU only
notebooks/                    exploration only, never imported
outputs/<run-id>/             generated files, ignored by Git
```

The module names are a starting point, not a contract. Split a module only when it grows past about 400 lines or holds two unrelated jobs. Do not add subpackages, base classes, plugin systems, or registries until two real uses need them. The first code PR adds `pyproject.toml` with the Python version and pinned dependency versions.

## Write less code

- Solve the whole task with the least new code. If one clear line does the job, use one line.
- Reuse what exists in this order: this repository, the standard library, an installed dependency, then new code.
- Do not add a dependency for a few lines. A new dependency needs a reason in the PR and a pinned version.
- Use plain functions. Use a class only when it holds state that several functions share, such as a model.
- No options, flags, wrappers, or "for later" code that no current task uses. Delete dead and commented-out code.
- Keep values in the form the library gives them. Do not convert between NumPy, PyTorch, and lists without a reason.
- A known limit gets one comment in the form `shortcut: <the limit>, <when to fix it>`.

## Comments and names

- Comment only the reason the code cannot show. Do not restate the code, add banners, or explain Python.
- Public functions get a one-line docstring that states units and array shapes when they matter.
- Names follow the research plan's symbols where that helps (`k`, `u`, `theta`). Use SI units and put the unit in the name when it is not obvious (`energy_j`, `elapsed_s`).
- No emojis, decorative output, or chatty log messages. Logs state what happened and the value.
- No `TODO` without a linked issue.

## Research correctness

These rules protect the comparison. Breaking one can change the result.

- **Settings live in config.** Bounds, grids, tolerances, learning rates, epochs, batch sizes, and seeds come from `configs/`, not from literals in code. Record the config hash in the run record.
- **One evaluation path.** Both methods use the same function, held-out parameters, output grid, and reference to compute relative L2 error. Never tune on the held-out set.
- **Seeds are explicit.** Pass seeds as arguments and set every random source the code uses. State the floating-point type; use float64 for reference solutions.
- **Timing is honest.** Use `time.perf_counter`. Synchronize the GPU before reading a timer. Keep warm-up, setup, training, and query phases separate.
- **Fail loudly.** No bare `except`, no silent skipping of NaN or infinite values. A diverged run raises or is recorded as failed; it is not dropped.
- **Never overwrite evidence.** Write each run to a new `outputs/<run-id>/` folder and stop if it already exists.
- **No numbers without a run.** Do not put result values in code, docs, or plots unless they came from a recorded run.
- **Verify before measuring.** Check the 1D heat solver against its exact solution and the finite-difference solver's order of accuracy on a refined grid before any energy trial. Report a failed check; do not loosen the tolerance to pass it. The [convergence-study](../.agents/skills/convergence-study/SKILL.md) and [benchmark-and-mms-planner](../.agents/skills/benchmark-and-mms-planner/SKILL.md) skills help plan these checks.

## Tests

- New logic with a branch, loop, parser, or numerical method gets a small test. Trivial changes need none.
- Use `unittest` from the standard library so the existing checks keep working. Tests run on CPU in seconds.
- Numerical tests use a tolerance with a one-line reason for its size.
- A bug fix includes a test that fails without the fix.

## Work in small steps

- Read the code you will change and its callers before editing. For changes over about 50 lines, state the plan first.
- One purpose per change: implement, run, check, then commit. Do not mix refactors with result-affecting changes.
- Notebooks are for exploring. Clear outputs before committing, and move any code a result depends on into the package with a test.
- Before a PR, review the diff for lines that are not needed and for changes that could affect a result. Use the [research-review skill](../.agents/skills/research-review/SKILL.md) for any change to solvers, evaluation, measurement, or analysis.
- AI-written code follows these same rules. A member reviews it before merge and checks that it does what the PR claims.
