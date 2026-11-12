---
name: experiment-run
description: Prepare, run, and record experiments for the PINN energy break-even study. Use for pilot solves, training, validation, timing, energy trials, retries, or run-log work so approval, accuracy, measurement coverage, and failures are handled before claims are made.
---

# Experiment run

Read the [project rules](../../../AGENTS.md), the relevant part of the [research plan](../../../docs/research-plan.md), and the [experiment guide](../../../experiments/README.md). Use the [run template](../../../experiments/run-template.json) only for an actual planned run. Do not turn a request for a plan into permission to execute it.

## Check before execution

Confirm the purpose, task authorization, approved machine, protocol state, and compute budget. Confirm that code and dependencies exist and that the requested command has been inspected. Do not install a GPU stack, rent compute, or start a long training job as an unmentioned setup step.

For full energy trials, both methods must already meet the stated accuracy target and measurements must be usable. Check the shared held-out parameters, output grid, valid classical reuse, PINN seed, query workload, and counter coverage. Do not compare CPU-only and GPU-only readings as equivalent whole-machine totals.

If a required choice is missing, name the blocker and prepare the next safe step. Do not invent hardware, parameter bounds, telemetry, energy values, successful validation, or approval. Keep the 0.01% target optional within budget.

## Run and record

Create a unique record for the actual attempt. Include the code commit and any dirty-tree changes, settings and hashes, software/hardware, seeds, reference method, and measurement boundary. Record warm-up, synchronization, query blocks, repetitions, and the stop condition.

Keep setup, training, and query phases separate, with joules and seconds. Label counter readings, integrated power, modeled estimates, and missing readings correctly. A missing value is not zero. Preserve raw measurements and log failures, retries, tuning, and stopped runs.

Record raw artifact locations and hashes before analysis. Add study-electricity entries without double counting overlapping intervals or devices. Keep deployment retry accounting separate from the electricity spent on the whole study.

Stop at the declared budget or stop condition. If the task is interrupted, mark the record truthfully rather than rerunning without approval. Do not delete evidence because it is inconvenient or fails a target.

## Report

State what ran, what passed, what failed, and what was measured or estimated. Separate template/example values from real data. Do not claim a crossover from an accuracy failure or from slopes that cannot support a reliable intersection. Use the [research-review skill](../research-review/SKILL.md) before accepting a result for the report.
