# Reaching the energy and computational break-even point between PINNs, and classical solvers.

**Course:** Green Computing

**Status:** Proposal submitted; research implementation has not started.

**Repository:** [pinn-energy-break-even](https://github.com/ihmorol/pinn-energy-break-even)

## Research question

For a defined family of heat-diffusion problems, how many new parameter queries are needed before a physics-informed neural network (PINN) uses less cumulative energy than an efficient classical solver at matched accuracy? How does that threshold change with the required accuracy?

We will measure both **energy break-even** and **computational break-even**, with computational cost defined as runtime. Setup and training count alongside repeated-query costs. A crossover is not guaranteed: an absent, uncertain, or impractically distant crossover is a valid result.

## Fixed scope

| Item | Scope |
|---|---|
| Pilot | A one-dimensional heat problem with a known solution; validate both implementations and the energy-measurement approach. |
| Main experiment | Steady diffusion on a two-dimensional square, with two bounded parameters controlling spatially varying conductivity. Geometry and boundary conditions remain fixed. |
| Neural method | A small parametric PINN in PyTorch, taking coordinates and the two parameters as inputs. |
| Classical baseline | Finite differences with SciPy sparse solvers, retaining meshes, sparsity patterns, and any valid factorization or preconditioner reuse. |
| One query | Return the solution on a fixed output grid for a previously unseen parameter setting—not repeatedly recompute an identical cached answer. |
| Accuracy | Relative L2 error targets of **1%** and **0.1%**; **0.01%** only as a stretch target within a fixed training budget. |
| Measurement | One controlled machine, a common measurement boundary, separate setup/training/query costs, repeated trials, and at least three training seeds. |
| Duration | Twelve weeks, with full energy trials gated on usable measurements and matched accuracy. |

## Project documents

- [Research plan](RESEARCH_PLAN.md): the active scope, comparison protocol, decision points, and work plan.
- [Submitted two-page proposal (PDF)](ENERGY_CROSSOVER_PROPOSAL.pdf): the submission baseline.
- [Proposal source (Word)](ENERGY_CROSSOVER_PROPOSAL.docx): the accompanying editable source, preserved unchanged.

The submitted files retain their original heading, *The energy crossover*. They are not being retroactively retitled; the title at the top of this README is the current project name.

## Start here

1. Confirm the machine, available energy telemetry, and compute budget.
2. Specify and validate the 1D pilot, including reference accuracy and measurement stability.
3. Freeze the main problem specification, parameter ranges, data splits, output grid, accuracy acceptance rule, and timing/energy protocol after the pilot.
4. Build the reusable classical baseline and parametric PINN, then proceed through the accuracy gate before full energy trials.

There is no solver code, dependency setup, or experiment data yet. The next work is the pilot and protocol—not further topic selection. Results will be limited to the tested workload and hardware, and the electricity used by the study itself will be reported separately.
