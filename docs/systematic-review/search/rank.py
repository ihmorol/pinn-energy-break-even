"""Zone 1: scripted ranking of deduplicated records (no model reads any record here). Usage:
python -I rank.py <script_dir> <records.json> <out.json>
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import local_filter as L  # noqa: E402

BE_STRONG = re.compile(r"break ?even|amorti[sz]|pays? off|payback")
BE_WEAK = re.compile(r"many query|multi query|multiple queries|number of (queries|evaluations|simulations|solves)|"
                     r"offline (cost|phase|stage|training)|offline online|training cost|total (computational )?cost")
# Energy of the computation, not of the modelled system: a cost noun plus a computing noun nearby.
_E = (r"((energy|power|electricity) (consumption|usage|use|cost|costs|draw|footprint|efficiency|budget|savings?|requirements?)|"
      r"carbon (footprint|emissions?|cost)|co2 emissions?|\bjoules?\b|\bkwh\b|(less|lower|reduced) energy)")
_C = (r"(training|inference|gpus?|cpus?|hardware|computation|computational|computing|accelerators?|clusters?|"
      r"data cent(er|re)s?|solvers?|simulations?|neural networks?|deep learning|machine learning|\bai\b|surrogates?|"
      r"neural operators?|pinns?)")
CE_STRONG = re.compile(rf"{_E}\W+(?:\w+\W+){{0,5}}?{_C}|{_C}\W+(?:\w+\W+){{0,5}}?{_E}|codecarbon|carbontracker|\brapl\b|"
                       r"\bnvml\b|nvidia smi|power meter|wattmeter|green (ai|computing)|"
                       r"energy efficient (computing|hardware|inference|training|ai|neural|deep learning)|"
                       r"(fixed|locked) clocks?|power (mode|cap|capping|limit)s?|\d+ ?w mode|"
                       r"(operating|measured|metered) energy|energy (measurement|meter|metering|per (query|request|inference|prediction|update))")
DOMAIN_ENERGY = re.compile(r"\bbuildings?\b|\bhvac\b|batter(y|ies)|state of charge|power (grid|system|plant|flow|network|distribution)s?|"
                           r"smart grid|microgrid|wind (turbine|farm|power|energy)|\bsolar\b|photovoltaic|load forecast|"
                           r"electricity (price|demand|load|market)|energy (management|storage|system)s?|demand response|heat pump|"
                           r"thermal comfort|district heating|fuel cell|lithium|electric vehicle")
TITLE_CUE = re.compile(r"energy|carbon|power consumption|break ?even|amorti|\bcost|efficien|speed|faster|compar|versus|\bvs\b|"
                       r"benchmark|surrogate|parametri|parameteri")


def score(r):
    title, ab = r.get("title", ""), r.get("abstract", "")
    t = L.norm(f"{title} . {ab}")
    tt = L.norm(title)
    a1, a2 = bool(L.A1.search(t)), bool(L.A2.search(t))
    ns = a1 or a2 or (bool(L.NN.search(t)) and bool(L.PDE.search(t)))
    be_s, be_w, ce_s = bool(BE_STRONG.search(t)), bool(BE_WEAK.search(t)), bool(CE_STRONG.search(t))
    de = bool(DOMAIN_ENERGY.search(t))
    s = 3 if a1 else 1 if a2 else 0.5 if ns else 0
    s += 6 * be_s + 2 * (be_w and not be_s)
    s += 5 * ce_s + 1 * (bool(L.EN.search(t)) and not ce_s)
    cl, co, pa = bool(L.CL.search(t)), bool(L.CO.search(t)), bool(L.PA.search(t))
    param_pinn = a1 and cl and co and pa
    s += 2 * cl + co + pa + 3 * param_pinn
    s += 2 * bool(TITLE_CUE.search(tt))
    s -= 5 * (de and not ce_s)
    y = int(r.get("year") or 0) if str(r.get("year", "")).isdigit() else 0
    s += 1.5 if y >= 2025 else 0.75 if y >= 2023 else 0
    s += 0.5 * ("preprint" not in (r.get("type") or "").lower())
    strong = ns and (be_s or ce_s) and not (de and not ce_s)
    return round(s, 2), dict(a1=a1, a2=a2, ns=ns, be_strong=be_s, be_weak=be_w, compute_energy=ce_s,
                             domain_energy=de, param_pinn=param_pinn, no_abstract=not ab, strong=strong)


if __name__ == "__main__":
    recs = json.load(open(sys.argv[2], encoding="utf-8"))
    recs = recs if isinstance(recs, list) else recs["unique"]
    out = []
    for r in recs:
        s, f = score(r)
        out.append(dict(id=r["id"], score=s, **f, year=r.get("year"), type=r.get("type"), doi=r.get("doi"),
                        title=r.get("title"), journal=r.get("journal"), sources=r.get("sources")))
    out.sort(key=lambda x: (-x["strong"], -x["score"], x["id"]))
    json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), indent=0)
    n_strong = sum(x["strong"] for x in out)
    print("records", len(out), "strong", n_strong)
    for cut in (8, 10, 12, 14):
        print("score >=", cut, sum(x["score"] >= cut for x in out), "| strong or >=", cut, sum(x["strong"] or x["score"] >= cut for x in out))
