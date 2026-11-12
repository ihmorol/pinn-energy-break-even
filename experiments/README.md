# Experiment records

There are no research runs or measured results yet. The files here define how to record them. The [research plan](../docs/research-plan.md) holds the scope and the protocol decisions still to freeze.

## Before a run

Use the [experiment-run skill](../.agents/skills/experiment-run/SKILL.md). Confirm that the requested work has an approved machine, purpose, protocol, and compute budget. Do not start training or energy trials just because a run template exists. Full energy trials require usable measurements and both methods passing the accuracy target being tested.

Use a unique run ID in the form `YYYYMMDDTHHMMSSZ-short-task-tag`, based on the actual UTC start time and a short task label. Copy [run-template.json](run-template.json) into `experiments/records/<run-id>.json` when preparing a real run. Create `records/` with the first record. Set `is_template` to false and status to `planned`, then `running`, followed by `completed`, `failed`, or `stopped` as appropriate.

The blank values are unknown, not zero. Keep a missing reading as `null` with a reason. Do not run with unresolved settings that affect fairness or safety. Set the Git commit and record any uncommitted changes; a commit hash alone cannot reproduce a dirty tree.

## What a record needs

- The task, operator, start/end time, code commit, configuration path and hash, software versions, hardware, seeds, and device/thread settings.
- The protocol version, parameter sets, output grid, accuracy target, reference method, and error result. Use the same held-out workload for both methods.
- The allowed classical reuse, PINN model/checkpoint, query count, batch size, warm-up, repetition, and GPU synchronization policy.
- The common measurement boundary, counter coverage, idle/background policy, and sampling interval. Mark values as `counter`, `integrated_power`, `modeled`, or `unavailable` as appropriate.
- Setup and training totals, plus query-block energy and elapsed time. Derive per-query costs from the block totals and the number of queries. Keep units explicit: joules and seconds.
- Raw output locations and hashes, failures, warnings, retries, and the costs included in the deployment estimate. Never keep only the best seed.

Use the same meaning for a field across both methods. If a phase does not apply, record that reason; do not silently mix "not applicable" with a missing measurement. Note whether phases overlap so they are not summed twice. Record raw data before computing a crossover.

Write large generated files under `outputs/<run-id>/`. They are ignored by Git. Keep small metadata and evidence tables in tracked records or later report files. Before removing local outputs, copy them to approved shared storage and record a location and SHA-256 hash. Ignoring a file does not preserve it for another member.

After a run, keep raw readings and failures unchanged. Correct metadata through a recorded change that explains the correction. Do not reuse a run ID for another attempt. A stopped or failed run still consumed electricity and belongs in the study log.

## Study electricity ledger

[study-energy.csv](study-energy.csv) contains only a header until real work is measured. Add one row for each non-overlapping measured or estimated activity window, including pilots, validation, tuning, failures, and repeated trials. Each row links back to the run record.

| Column | Meaning |
|---|---|
| `entry_id`, `run_id` | Unique ledger entry and related run |
| `started_at_utc`, `ended_at_utc` | Actual UTC times for the accounted interval |
| `activity` | Work included in the interval |
| `energy_j` | Electricity in joules; blank if unavailable, never a made-up zero |
| `source_kind` | Counter, integrated power, modeled estimate, or unavailable |
| `measurement_boundary` | Components covered by the value |
| `overlap_group` | Shared identifier when intervals or devices overlap; explain how double counting is avoided |
| `record_path` | Repository-relative run record path |
| `notes` | Limits, missing readings, or the reason for an estimate |

Do not sum a whole-run total and its component phases. Do not double count overlapping CPU/GPU windows or overlapping telemetry sources. Mark and explain overlaps before computing the study total. Do not pool values with different coverage as if they measured the same system; report separate subtotals when a common total cannot be justified.

The deployment estimate answers the cost of using a solver/model under a stated retry policy. The study ledger reports electricity spent doing the research. Keep those accounts separate and state any unmeasured work.
