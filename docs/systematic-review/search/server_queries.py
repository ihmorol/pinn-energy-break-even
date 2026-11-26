"""Server-side superset queries (search v1, 2026-11-23). The local filter (local_filter.py) is applied afterwards."""

# OpenAlex title_and_abstract.search syntax. Plurals are written out because phrase stemming
# is not applied inside combined boolean queries (seen in search development).
OA_A = ('("physics-informed" OR "physics informed" OR "physics-constrained" OR "physics constrained" OR PINN OR PINNs '
        'OR "deep Ritz" OR "deep Galerkin" OR PINO OR VPINN OR VPINNs OR XPINN OR XPINNs OR PIKAN OR PIKANs)')
OA_N = ('("neural operator" OR "neural operators" OR DeepONet OR DeepONets OR FNO OR "operator learning" '
        'OR surrogate OR surrogates OR emulator OR emulators)')
OA_NN = '("neural network" OR "neural networks" OR "deep learning" OR "machine learning")'
OA_P = ('("partial differential equation" OR "partial differential equations" OR PDE OR PDEs OR CFD OR fluid OR flow '
        'OR flows OR weather OR climate OR "finite element" OR "finite difference" OR "finite volume")')
OA_E = ('("energy consumption" OR "energy efficiency" OR "energy efficient" OR "energy-efficient" OR "energy usage" '
        'OR "energy cost" OR "energy costs" OR "power consumption" OR "carbon footprint" OR "carbon emissions" '
        'OR "carbon emission" OR CO2 OR joule OR joules OR electricity OR sustainability OR sustainable OR "green AI" '
        'OR "green computing" OR kWh OR watts OR "less energy" OR "lower energy")')
OA_B = ('("break-even" OR breakeven OR "break even" OR amortized OR amortised OR amortization OR amortisation '
        'OR "many-query" OR "multi-query" OR queries OR offline OR payback OR "training cost" OR "training costs")')
OA_C = ('(solver OR solvers OR "finite element" OR "finite elements" OR "finite difference" OR "finite volume" OR FEM '
        'OR FDM OR FVM OR numerical OR spectral OR multigrid OR CFD OR COMSOL OR OpenFOAM OR ANSYS OR Abaqus OR PETSc)')
OA_T = ('(cost OR costs OR time OR faster OR speed OR speedup OR speedups OR "speed-up" OR runtime OR runtimes '
        'OR efficient OR efficiency OR FLOPs OR expensive OR seconds OR hours OR minutes)')
OA_R = ('(parametric OR parameterized OR parametrized OR parameterised OR parametrised OR surrogate OR surrogates '
        'OR "real-time" OR "real time" OR "many-query" OR queries OR optimization OR optimisation '
        'OR "uncertainty quantification" OR unseen OR "different parameters" OR "new parameters")')
OA_HW = ('(GPU OR GPUs OR CPU OR CPUs OR hardware OR accelerator OR accelerators OR "computational cost" '
         'OR "computational costs" OR "computational energy" OR "energy per" OR joules OR "power draw" '
         'OR "carbon footprint" OR inference OR "training cost" OR "training costs")')
OA_OP = ('("neural operator" OR "neural operators" OR DeepONet OR DeepONets OR FNO OR "operator learning" '
         'OR emulator OR emulators)')
OA_E2 = ('("energy consumption" OR "energy efficiency" OR "energy efficient" OR "energy-efficient" OR "energy usage" '
         'OR "energy cost" OR "energy costs" OR "power consumption" OR "carbon footprint" OR "carbon emissions" '
         'OR joules OR kWh OR "green AI" OR "green computing" OR "less energy" OR "computational energy")')
NS = f"({OA_A} OR {OA_N} OR ({OA_NN} AND {OA_P}))"

OPENALEX = {
    "OA-Q1-energy": f"(({OA_A} OR {OA_OP}) AND {OA_E2}) OR ({OA_NN} AND {OA_P} AND {OA_E2} AND {OA_HW})",
    "OA-Q2-breakeven": f"({OA_A} OR {OA_N}) AND {OA_B}",
    "OA-Q3-parametric": f"{OA_A} AND {OA_C} AND {OA_T} AND {OA_R}",
}

# Semantic Scholar bulk search syntax: | OR, + AND, "phrase", ( ) grouping.
S2_A = ('("physics-informed" | "physics informed" | "physics-constrained" | "physics constrained" | PINN | PINNs '
        '| "deep Ritz" | "deep Galerkin" | PINO | VPINN | XPINN | PIKAN)')
S2_N = ('("neural operator" | "neural operators" | DeepONet | DeepONets | FNO | "operator learning" | surrogate '
        '| surrogates | emulator | emulators | "neural network" | "neural networks" | "deep learning" | "machine learning")')
S2_P = ('("partial differential equation" | "partial differential equations" | PDE | PDEs | CFD | fluid | flow '
        '| weather | climate | "finite element" | "finite difference" | "finite volume" | solver | solvers)')
S2_E = ('("energy consumption" | "energy efficiency" | "energy efficient" | "energy usage" | "energy cost" '
        '| "power consumption" | "carbon footprint" | "carbon emissions" | CO2 | joules | electricity | sustainability '
        '| "green AI" | "green computing" | kWh | "less energy")')
S2_B = ('("break-even" | breakeven | "break even" | amortized | amortised | amortization | amortisation | "many-query" '
        '| "multi-query" | queries | offline | payback | "training cost")')

S2_A2 = ('("physics-informed" | "physics informed" | PINN | PINNs | "neural operator" | "neural operators" | DeepONet '
         '| DeepONets | FNO | "operator learning" | emulator | emulators)')
S2_NN = '("neural network" | "neural networks" | "deep learning" | "machine learning")'
S2_HW = ('(GPU | GPUs | CPU | CPUs | hardware | accelerator | "computational cost" | "computational energy" '
         '| "energy per" | joules | "power draw" | "carbon footprint" | inference | "training cost")')

SEMANTIC_SCHOLAR = {
    "S2-Q0-pinn-family": S2_A,
    "S2-Q1a-energy": f"{S2_A2} + {S2_E}",
    "S2-Q1b-energy": f"{S2_NN} + {S2_P} + {S2_E} + {S2_HW}",
    "S2-Q2-breakeven": f"{S2_N} + {S2_P} + {S2_B}",
}

# arXiv API syntax (abs: searches the abstract field; ti: the title).
AX_A = ('(abs:"physics-informed" OR abs:"physics informed" OR abs:PINN OR abs:PINNs OR abs:"physics-constrained" '
        'OR abs:"deep Ritz" OR abs:"deep Galerkin")')
AX_N = ('(abs:"neural operator" OR abs:"neural operators" OR abs:DeepONet OR abs:FNO OR abs:"operator learning" '
        'OR abs:surrogate OR abs:emulator OR abs:"neural network" OR abs:"deep learning" OR abs:"machine learning")')
AX_P = ('(abs:"partial differential" OR abs:PDE OR abs:PDEs OR abs:CFD OR abs:fluid OR abs:weather OR abs:climate '
        'OR abs:"finite element" OR abs:solver OR abs:solvers)')
AX_E = ('(abs:"energy consumption" OR abs:"energy efficiency" OR abs:"energy efficient" OR abs:"energy usage" '
        'OR abs:"energy cost" OR abs:"power consumption" OR abs:"carbon footprint" OR abs:"carbon emissions" '
        'OR abs:CO2 OR abs:joules OR abs:electricity OR abs:sustainability OR abs:"green AI" OR abs:"less energy")')
AX_B = ('(abs:"break-even" OR abs:breakeven OR abs:"break even" OR abs:amortized OR abs:amortised OR abs:amortization '
        'OR abs:"many-query" OR abs:queries OR abs:offline OR abs:"training cost")')

ARXIV = {
    "AX-Q0-pinn-family": AX_A,
    "AX-Q1-energy": f"{AX_N} AND {AX_P} AND {AX_E}",
    "AX-Q2-breakeven": f"{AX_N} AND {AX_P} AND {AX_B}",
}
