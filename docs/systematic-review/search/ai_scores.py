"""AI scores for the 55 shortlisted studies (2026-11-26), and the files built from them.

Scores follow the judging sheet in team-shortlist.md (C1-C5, 0-2 each). They come
from one AI reader's reading of each title and abstract, plus the full texts
where verification.md says one was read. The team can change any score in
team-selection.csv or on the reading page.

Run from the repository root:

    python -I docs/systematic-review/search/ai_scores.py

It fills the score columns of team-selection.csv and adds four columns:
citable, reading_list, stages and venue_cited.
"""
import csv
import io
import os

ROOT = os.getcwd()
SEL = os.path.join(ROOT, "docs", "systematic-review", "team-selection.csv")
REVIEWER = "Claude (AI), 2026-11-26"

# id: (C1, C2, C3, C4, C5, citable, reading_list, stages, reason)
# reading_list: "1".."12" = cite and read, "A".."E" = read only (not citable),
# "opt" = optional extra, "" = not on the list.
SCORES = {
    "R02724": (2, 2, 0, 2, 2, "yes", "1", "2, 12, 13", "Peer-reviewed parametric PINN break-even against COMSOL with offline training included; strongest citable prior for GC2"),
    "R00504": (2, 2, 1, 2, 2, "yes", "2", "5, 11, 12", "Break-even formula of our form; training charged but configuration search not charged (GC4)"),
    "R03609": (2, 2, 1, 2, 2, "yes", "3", "12, 13", "Parametric PINN against COMSOL over 3171 cases with training and inference time counted; closed access"),
    "R01189": (2, 2, 0, 2, 2, "yes", "4", "2, 12", "Parametric PINN training time against per-parameter classical solves (implied break-even about 7); different hardware"),
    "R02880": (2, 2, 0, 2, 2, "yes", "5", "2, 12", "Parametric PINN 30 times faster than FE including training; top-tier journal"),
    "R00637": (2, 2, 1, 1, 2, "yes", "6", "5, 11", "Break-even in runs with data and training charged; peer-reviewed J. Comput. Phys."),
    "R00718": (2, 2, 1, 1, 2, "yes", "7", "11", "Neural operator cost-efficiency after construction cost is counted; SIAM J. Sci. Comput."),
    "R00692": (1, 2, 0, 1, 2, "yes", "8", "4, 5", "Parametric physics-trained solver costs about 40 single solves to train; sizes S_P"),
    "R01247": (1, 1, 1, 1, 2, "yes", "9", "1, 2", "Parametric PINN with hard boundary conditions tested on unseen parameters against a finite-volume reference"),
    "R00018": (1, 1, 0, 1, 2, "yes", "10", "2, 3", "Method anchor: physics-informed parametric training without paired solver data (Science Advances); kept despite total 5"),
    "R01850": (1, 2, 0, 1, 2, "yes", "11", "10", "Measured power of a deployed surrogate against GPU and FE runtime; energy evidence, not against FE energy"),
    "R03325": (1, 1, 0, 1, 2, "yes", "12", "2", "Top-tier example of a parametric unsupervised PINN for design exploration against COMSOL; no break-even; kept despite total 5"),
    "R00383": (2, 2, 0, 2, 1, "no: preprint", "A", "2, 12, 13", "Explicit runtime break-even (about 108 designs) for a physics-only parametric PINN; must be known, cannot be cited"),
    "R01555": (2, 1, 1, 2, 1, "no: thesis", "B", "10, 13", "Separate energy and time break-even for a PINN against FDM, energy estimated from TDP; nearest prior for GC1 and GC3"),
    "R00627": (2, 2, 2, 2, 1, "no: preprint", "C", "5, 6, 12", "Method standard: error-matched classical solver and tuning cost counted; no PINN"),
    "R00643": (2, 2, 1, 2, 1, "no: preprint", "D", "9, 12", "Label-free model against a tuned multigrid solver at a stated tolerance, training time given"),
    "R00657": (1, 1, 2, 2, 1, "no: preprint", "E", "13", "Accuracy target decides which method is cheaper per query (GC5)"),
    "R02483": (2, 2, 1, 1, 2, "yes, weak venue", "opt", "9, 12", "Training amortized after a few queries against FD with AMG; conference not rated, closed access"),
    "R00895": (1, 1, 1, 1, 2, "yes, weak venue", "opt", "10", "Estimated (Green Algorithms) energy for a PINN variant; shows the estimate route we avoid"),
    "R02666": (1, 1, 1, 1, 2, "yes", "opt", "2", "Parametric PINN surrogates over 1000 times faster than a numerical solver; no training cost"),
    "R00670": (2, 2, 1, 2, 1, "no: preprint", "", "12, 13", "Amortization law (N* above 30,000 below 1% error); proposal reference 2, already summarised in a project note"),
    "R00177": (1, 1, 0, 1, 1, "no: preprint", "", "10", "Carbon metric for neural PDE solvers; modelled emissions"),
    "R01457": (1, 1, 0, 1, 2, "yes", "", "10", "Read in full: modelled per-pass energy across hardware, runtime only against FE"),
    "R03662": (1, 1, 0, 1, 2, "yes", "", "10", "Chip running PINN and FEM; energy compared with earlier chips; closed access"),
    "R00244": (1, 1, 1, 1, 1, "only the journal version", "", "", "PINN less efficient than classical schemes for single 1D problems"),
    "R00319": (1, 1, 1, 1, 1, "no: preprint", "", "", "Parametric PINN 5 times faster per query than FD; training not counted"),
    "R00598": (1, 1, 1, 1, 1, "no: preprint", "", "", "Reduced-basis operator trained label-free; relevant only if a classical surrogate is added"),
    "R00614": (2, 2, 1, 1, 1, "no: preprint", "", "", "Supervised operator cost counted with data generation; outside the PINN setting"),
    "R00649": (1, 2, 1, 1, 1, "no: preprint", "", "", "Negative result: surrogate cannot speed up a coupled solver"),
    "R00807": (1, 0, 0, 1, 1, "no: preprint", "", "", "Review with an analytic break-even condition"),
    "R00810": (0, 1, 0, 1, 1, "no: preprint", "", "10", "Runtime is an unreliable proxy for carbon cost"),
    "R00993": (1, 1, 0, 0, 2, "yes", "", "", "Per-query speedup of a PINN for a heat exchanger"),
    "R01955": (0, 1, 0, 1, 1, "yes, weak venue", "", "", "Hardware unit for PINN and FDM inference; no per-solve energy comparison"),
    "R02174": (0, 2, 0, 1, 1, "no: preprint", "", "10", "Measured operating energy with fixed clocks; no classical comparison"),
    "R00092": (0, 1, 0, 0, 1, "no: preprint", "", "", "Simulated optical PINN training energy"),
    "R00220": (0, 1, 0, 1, 2, "yes", "", "", "Spiking PINN with modelled energy; no classical comparison"),
    "R00235": (0, 1, 0, 0, 1, "no: preprint", "", "", "Accelerator energy for quantized PINN training"),
    "R00275": (0, 1, 0, 0, 1, "no: preprint", "", "", "Spiking operator; energy argued, not measured"),
    "R01518": (1, 1, 0, 0, 1, "yes, weak venue", "", "", "Spiking PINN inside an FE solver; energy on a neuromorphic chip"),
    "R01786": (0, 1, 0, 0, 1, "no: thesis", "", "", "Spiking solver costs at indicative neuromorphic energy"),
    "R01799": (0, 1, 0, 0, 1, "no: thesis", "", "", "Training energy of surrogate networks; no PDE solver comparison"),
    "R00370": (0, 1, 0, 1, 1, "no: preprint", "", "", "Training emissions to reach an error threshold; not a PDE solver"),
    "R03090": (1, 1, 0, 1, 2, "yes", "", "", "Read in full: 1,400-fold speedup that excludes model construction (GC4 example)"),
    "R01145": (1, 1, 1, 0, 2, "yes", "", "", "Per-simulation speedup of a physics-informed operator; training cost not compared"),
    "R02939": (1, 1, 0, 1, 2, "yes", "", "", "Data-free PINN surrogate inside an optimization loop"),
    "R02561": (1, 1, 0, 1, 1, "yes, weak venue", "", "", "Speedup with training excluded; new unrated journal"),
    "R00750": (1, 1, 0, 1, 2, "yes", "", "", "PINN pretraining costs more than FEM pretraining"),
    "R00780": (1, 0, 0, 1, 2, "yes", "", "", "Parametric PINN with finite-difference derivatives; no cost comparison"),
    "R02184": (1, 1, 0, 0, 1, "yes, weak venue", "", "", "FPGA inference inside an FE solver"),
    "R02608": (1, 1, 1, 0, 0, "weak venue: avoid", "", "", "Multi-fidelity PINN surrogate; journal on no quality list"),
    "R02862": (1, 1, 0, 1, 1, "yes, weak venue", "", "", "Hybrid PINN with CFD data; offline cost amortized"),
    "R03112": (0, 0, 0, 1, 2, "yes", "", "", "Reduced-basis PINN; no classical cost comparison"),
    "R03386": (1, 1, 1, 1, 1, "yes, weak venue", "", "", "Parametric PINN 52 times faster than COMSOL in sweeps"),
    "R03460": (1, 1, 1, 1, 1, "yes, weak venue", "", "", "PINN against GPU finite volume; inference speed only"),
    "R00218": (1, 0, 0, 0, 1, "no: preprint", "", "", "Review of PINNs and operators for parametric PDEs"),
}

# Venue to cite, where the index record shows only the preprint server or a repository.
VENUE_CITED = {
    "R00504": "Journal of Computational Science (2026)",
    "R00637": "Journal of Computational Physics (2026)",
    "R00718": "SIAM Journal on Scientific Computing (2025)",
    "R00692": "Engineering Applications of Computational Fluid Mechanics (2025)",
    "R00220": "Journal of Computational Physics (2026)",
    "R01145": "Journal of Computational Physics (2026)",
    "R01555": "Bachelor's thesis, Charles University (2025)",
    "R01786": "Thesis, Nanyang Technological University (2026)",
    "R01799": "Thesis, University of Stuttgart (2026)",
    "R00807": "engrXiv preprint (2026)",
    "R00244": "arXiv preprint; probable version in Chaos, Solitons & Fractals (2026)",
}
CRIT = ["C1_relevance", "C2_cost_evidence", "C3_fairness", "C4_gap_value", "C5_source"]
EXTRA = ["citable", "reading_list", "stages", "venue_cited"]


def decision(c, reading_list):
    total = sum(c)
    rule = c[3] == 2 or (total >= 6 and c[0] >= 1)
    return "yes" if (rule or reading_list) else "no"


def main():
    with open(SEL, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        cols = list(reader.fieldnames)
        rows = list(reader)
    for col in EXTRA:
        if col not in cols:
            cols.append(col)
    missing = [r["id"] for r in rows if r["id"] not in SCORES]
    if missing:
        raise SystemExit(f"No score for: {missing}")
    for r in rows:
        c1, c2, c3, c4, c5, cite, rl, stages, reason = SCORES[r["id"]]
        c = (c1, c2, c3, c4, c5)
        for name, value in zip(CRIT, c):
            r[name] = str(value)
        r["total"] = str(sum(c))
        r["select_yes_no"] = decision(c, rl)
        r["reason"] = reason
        r["reviewer"] = REVIEWER
        r["citable"] = cite
        r["reading_list"] = rl
        r["stages"] = stages
        r["venue_cited"] = VENUE_CITED.get(r["id"], r["venue"])
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    with open(SEL, "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())
    picked = sum(1 for r in rows if r["reading_list"] and r["reading_list"] != "opt")
    print(f"Scored {len(rows)} studies; {picked} on the reading list")


if __name__ == "__main__":
    main()
