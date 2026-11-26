# Jediný (2025): PINN against FDM for plasma reaction-diffusion, with estimated energy

## Source

- Title: Machine Learning Approach to the Solution of Reaction-Diffusion Equations in Low-Temperature Plasma
- Author: Filip Jediný. Supervisor: Štěpán Roučka. Opponent: František Němec.
- Year and type: 2025 bachelor's thesis, Charles University, Faculty of Mathematics and Physics. Defended 9 September 2025 (repository record).
- Source URL: http://hdl.handle.net/20.500.11956/202974
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown (energy method, results, discussion, conclusion). Not yet read by a human member.
- Access: full text (repository PDF, fetched through the app's built-in browser)
- Local file: `downloads/jediny-2025-thesis/jediny-2025-thesis.pdf`, SHA-256 fc41cbe0ab28428befd92714a28ca1c930ffd9c3e016dffbccb60ba8b2b975d3

## Question and setting

A 2D cylindrical reaction-diffusion equation for electron density in afterglow plasma (dimensionless form):

- **Methods compared:** a PINN (best: 3 layers of 128, GELU) and a finite-difference solver with Strang splitting and ADI half-steps (Thomas algorithm).
- **Hardware:** FDM on one core of an Intel Xeon E5-2650 v3 (105 W TDP), p28. PINN on an Nvidia T4 GPU (72 W TDP) in the same sandboxed cloud environment, p36.
- **Energy method:** CPU and GPU utilization multiplied by each device's TDP and integrated over time with the trapezoidal rule, because the author had no physical access to the machine (p25). The discussion calls both energy figures approximations from TDP; measuring at the wall socket was beyond the budget (p40-41).

## Claims we may use

- The best PINN trains in 1253 s and uses 117 kJ in total (CPU plus GPU, training and inference), p36 and p38.
- From polynomial fits, it "would break even with FDM at N = 1253 in terms of simulation time and N = 1303 in terms of energy use", where N is the number of points per spatial dimension, equal to the number of time steps (p38; Figs. 3.1 and 3.2).
- PINN output agrees with the FDM result at R² = 1 and MSE 2.12 × 10⁻⁷ (p40).
- Each hyperparameter setting was run once (p40).

## Relevance to this project

This is the closest study to GC1 and GC3. It reports an energy break-even and a time break-even separately, for a PINN against a classical solver. It does not meet our protocol:

- energy is estimated from utilization and TDP, not metered;
- the two methods run on different hardware (one CPU core against a GPU);
- the break-even axis is grid resolution for one problem, not repeated parameter queries;
- the FDM benchmark covers N = 100 to 300 (Table 3.1, p28-29), so the break-even near N = 1300 is an extrapolation;
- accuracy is agreement with the FDM solution, not both methods matched to a reference;
- one run per setting, and the energy of the hyperparameter sweep is not added to the 117 kJ in the passages read.

## Check status and gaps

- Confirmed in the cached text: the energy method, hardware, break-even values and limitations above.
- Our observation: the training time (1253 s) and the time break-even (N = 1253) are the same number. This may be a coincidence or a typo; check Fig. 3.1 before quoting the time figure.
- Not read: the full PINN result tables (Tables 3.2 to 3.4) beyond the best model.
