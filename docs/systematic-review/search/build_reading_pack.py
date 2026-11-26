"""Build the team reading pack: one local HTML page with each shortlisted
study's title, abstract, verification facts and scoring buttons.

The page holds third-party abstracts, so it is written to the ignored
outputs/ folder and must not be committed.

Run from the repository root (isolated Python, because records.json holds
downloaded text):

    python -I docs/systematic-review/search/build_reading_pack.py

Inputs:
    docs/systematic-review/team-selection.csv     ranked list and verification columns
    outputs/systematic-review/sr_work/records.json abstracts and authors
    outputs/systematic-review/shortlist_meta.json  screening notes
Output:
    outputs/systematic-review/team-reading.html
"""
import csv
import html
import json
import os
import re
import sys

ROOT = os.getcwd()
SEL = os.path.join(ROOT, "docs", "systematic-review", "team-selection.csv")
REC = os.path.join(ROOT, "outputs", "systematic-review", "sr_work", "records.json")
META = os.path.join(ROOT, "outputs", "systematic-review", "shortlist_meta.json")
OUT = os.path.join(ROOT, "outputs", "systematic-review", "team-reading.html")

# Studies with a full-text note in references/ (path relative to the repo root).
NOTES = {
    "R00383": "references/li-2026-parametric-pinn-microfluidic.md",
    "R00627": "references/zhang-2026-breakeven-complexity.md",
    "R00504": "references/winkler-stoll-2026-flow-surrogates.md",
    "R00643": "references/sun-2026-fevessel.md",
    "R01555": "references/jediny-2025-pinn-fdm-plasma-thesis.md",
    "R01457": "references/tandale-2024-spiking-fem.md",
    "R03090": "references/xue-2026-geothermal-operator.md",
}

TAG = re.compile(r"<[^>]+>")
SPACE = re.compile(r"\s+")


def clean_abstract(text):
    """Strip markup such as JATS tags and collapse whitespace."""
    if not text:
        return ""
    return SPACE.sub(" ", TAG.sub(" ", html.unescape(text))).strip()


def author_line(authors):
    if not authors:
        return ""
    names = authors if isinstance(authors, list) else [a.strip() for a in str(authors).split(";")]
    names = [n for n in names if n]
    if not names:
        return ""
    return names[0] if len(names) == 1 else f"{names[0]} et al. ({len(names)} authors)"


def safe_json(obj):
    """JSON that can sit inside a <script> element."""
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def build_studies(sel_rows, records, meta):
    by_id = {}
    for r in records:
        rid = r.get("id")
        if rid:
            by_id[rid] = r
    meta_by_id = {m["id"]: m for m in meta}
    studies = []
    for row in sel_rows:
        rid = row["id"]
        rec = by_id.get(rid, {})
        m = meta_by_id.get(rid, {})
        link = row.get("link", "")
        studies.append({
            "list": row["list"],
            "rank": row["rank"],
            "id": rid,
            "year": row["year"],
            "title": row["title"],
            "authors": author_line(rec.get("authors")) or m.get("first_author", ""),
            "venue": row["venue"],
            "status": row["status"],
            "quality": row["quality_lists"],
            "identity": row["identity_check"],
            "published": row["published_version_note"],
            "fulltext": row["fulltext"],
            "cites": row["citations_openalex"],
            "link": link,
            "gaps": row["tests_gap"],
            "note": m.get("note", ""),
            "fulltext_note": NOTES.get(rid, ""),
            "abstract": clean_abstract(rec.get("abstract", "")),
            "venue_cited": row.get("venue_cited") or row["venue"],
            "citable": row.get("citable", ""),
            "reading_list": row.get("reading_list", ""),
            "stages": row.get("stages", ""),
            "ai": {c: row.get(c, "") for c in CRIT},
            "ai_reason": row.get("reason", ""),
        })
    studies.sort(key=list_order)
    return studies


CRIT = ["C1_relevance", "C2_cost_evidence", "C3_fairness", "C4_gap_value", "C5_source"]


def list_order(study):
    """Reading list first (1-12, then A-E, then optional), then by AI total."""
    rl = study["reading_list"]
    if rl.isdigit():
        group = int(rl)
    elif len(rl) == 1 and rl.isalpha():
        group = 100 + ord(rl.upper())
    elif rl == "opt":
        group = 300
    else:
        group = 400
    total = sum(int(v) for v in study["ai"].values() if str(v).isdigit())
    return (group, -total, study["id"])


def main():
    with open(SEL, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        sel_rows = list(reader)
    with open(REC, encoding="utf-8") as f:
        records = json.load(f)["unique"]
    with open(META, encoding="utf-8") as f:
        meta = json.load(f)
    studies = build_studies(sel_rows, records, meta)
    missing = [s["id"] for s in studies if not s["abstract"]]
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reading_pack_template.html")
    with open(template_path, encoding="utf-8") as f:
        page = f.read()
    page = page.replace("/*DATA*/null", safe_json({"columns": columns, "studies": studies}))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    print(f"Wrote {OUT}: {len(studies)} studies, {len(studies) - len(missing)} with abstracts")
    if missing:
        print("No abstract in any source:", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
