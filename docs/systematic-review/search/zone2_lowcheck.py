"""Zone 2 scripted check for low-tier titles: keep a record only if its abstract names a classical
solver and has a break-even, computational-energy or quantitative speed-comparison term. Usage:
python -I zone2_lowcheck.py <records.json> <decisions.txt> [<decisions.txt> ...]
Each decisions file has lines "H <ids>" and "L <ids>" (ids without the leading R).
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import local_filter as L  # noqa: E402
from rank import BE_STRONG, CE_STRONG  # noqa: E402

CMP = re.compile(r"(faster|slower|cheaper) than|times faster|orders? of magnitude|speed ?ups?|"
                 r"compared (to|with) (the )?(fem|finite|numerical|classical|traditional|conventional|cfd|standard|high fidelity)")


def passes(title, abstract):
    t = L.norm(f"{title} . {abstract}")
    return bool(L.CL.search(t) and (BE_STRONG.search(t) or CE_STRONG.search(t) or CMP.search(t)))


if __name__ == "__main__":
    recs = {r["id"]: r for r in json.load(open(sys.argv[1], encoding="utf-8"))["unique"]}
    high, low = set(), set()
    for path in sys.argv[2:]:
        for line in open(path, encoding="utf-8"):
            tag, *ids = line.split()
            (high if tag == "H" else low).update("R" + i for i in ids)
    passed = sorted(i for i in low if passes(recs[i]["title"], recs[i]["abstract"]))
    print(json.dumps({"high": sorted(high), "low": sorted(low), "low_passed": passed,
                      "zone3": sorted(high | set(passed))}, indent=1))
