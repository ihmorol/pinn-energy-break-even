---
name: research-coding
description: Write, change, or review this project's solver, training, measurement, and analysis code. Use for any code task, even a small fix, so the code stays minimal and the comparison stays fair and reproducible.
---

# Research coding

Read the [project rules](../../../AGENTS.md) and the [coding rules](../../../docs/coding-rules.md). Read only the research plan sections and source files the task touches.

If the host has the `ponytail` skill, load it too. The project rules take precedence over it.

## Before writing

State what the change must do, its inputs and outputs, and what it does not include. List every place it must reach: callers, tests, configs, and run records. If a protocol choice the code needs is still open in the research plan, name the blocker instead of picking a value.

## Write

Take the smallest change that fully solves the task. Put settings in `configs/`, share one evaluation path between both methods, pass seeds explicitly, and fail loudly on NaN or divergence. Add a small test for new logic.

Do not install packages, start training, or run energy trials as a side step. Those need the approvals in the [experiment-run skill](../experiment-run/SKILL.md).

## Check

Run the workspace checks and the tests for the changed code. Then read the diff once more and remove any line that is not needed. For changes that can affect a result, use the [research-review skill](../research-review/SKILL.md).

Report what ran, what passed, what failed, and what was not checked. A passing test shows the code does what the test checks; it does not prove the method is accurate or the comparison is fair.
