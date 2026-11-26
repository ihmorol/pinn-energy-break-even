"""Turn raw downloads into filtered RIS exports plus counts. Usage:
python -I build_candidates.py <script_dir> <raw_dir> <out_dir> [--enrich]
"""
import collections
import glob
import html
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, sys.argv[1])
from local_filter import routes, chase_keep, title_keep  # noqa: E402

RAW, OUT = sys.argv[2], sys.argv[3]
ENRICH = "--enrich" in sys.argv
os.makedirs(OUT, exist_ok=True)
ARX = "10.48550/arxiv."


def clean_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    return d if d.startswith("10.") else ""


def strip_v(a):
    return re.sub(r"v\d+$", "", (a or "").strip().lower())


def inv_abstract(inv):
    if not inv:
        return ""
    return " ".join(t for _, t in sorted((p, t) for t, ps in inv.items() for p in ps))


recs = []


def oa_rec(w, src, qkey):
    loc = w.get("primary_location") or {}
    s = loc.get("source") or {}
    doi = clean_doi(w.get("doi"))
    return dict(src=src, qkey=qkey, title=w.get("display_name") or "", abstract=inv_abstract(w.get("abstract_inverted_index")),
                year=str(w.get("publication_year") or ""), doi=doi, arxiv=doi[len(ARX):] if doi.startswith(ARX) else "",
                venue=s.get("display_name") or "", vtype=s.get("type") or "", ptype=w.get("type") or "",
                lang=w.get("language") or "", ext=w.get("id") or "")


for path in sorted(glob.glob(os.path.join(RAW, "openalex", "*", "p*.json"))):
    qkey = os.path.basename(os.path.dirname(path))
    for w in json.load(open(path, encoding="utf-8"))["results"]:
        recs.append(oa_rec(w, "OpenAlex", qkey))

for path in sorted(glob.glob(os.path.join(RAW, "chase", "*_p*.json"))):
    qkey = "CH-" + os.path.basename(path).rsplit("_p", 1)[0]
    for w in json.load(open(path, encoding="utf-8"))["results"]:
        recs.append(oa_rec(w, "Citation chasing (OpenAlex)", qkey))

for path in sorted(glob.glob(os.path.join(RAW, "s2", "*", "p*.json"))):
    qkey = os.path.basename(os.path.dirname(path))
    for p in json.load(open(path, encoding="utf-8")).get("data", []):
        ext = p.get("externalIds") or {}
        types = p.get("publicationTypes") or []
        recs.append(dict(src="Semantic Scholar", qkey=qkey, title=p.get("title") or "", abstract=p.get("abstract") or "",
                         year=str(p.get("year") or ""), doi=clean_doi(ext.get("DOI")), arxiv=strip_v(ext.get("ArXiv")),
                         venue=(p.get("journal") or {}).get("name") or p.get("venue") or "", vtype="",
                         ptype=";".join(types), lang="", ext=p.get("paperId") or ""))

ENTRY = re.compile(r"<entry>(.*?)</entry>", re.S)


def tag(block, name):
    m = re.search(rf"<{name}[^>]*>(.*?)</{name}>", block, re.S)
    return html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""


for path in sorted(glob.glob(os.path.join(RAW, "arxiv", "*", "s*.xml"))):
    qkey = os.path.basename(os.path.dirname(path))
    for b in ENTRY.findall(open(path, encoding="utf-8").read()):
        aid = strip_v(tag(b, "id").rsplit("/abs/", 1)[-1])
        recs.append(dict(src="arXiv", qkey=qkey, title=tag(b, "title"), abstract=tag(b, "summary"),
                         year=tag(b, "published")[:4], doi=clean_doi(tag(b, "arxiv:doi")), arxiv=aid,
                         venue=tag(b, "arxiv:journal_ref"), vtype="repository", ptype="preprint", lang="en",
                         ext="arXiv:" + aid))

# Link preprint and published versions where a source states both identifiers.
alias = {}
for r in recs:
    if r["arxiv"] and r["doi"] and not r["doi"].startswith(ARX):
        alias.setdefault(r["arxiv"], r["doi"])
for r in recs:
    if r["doi"].startswith(ARX) and not r["arxiv"]:
        r["arxiv"] = strip_v(r["doi"][len(ARX):])
    if r["arxiv"] and (not r["doi"] or r["doi"].startswith(ARX)):
        r["doi"] = alias.get(r["arxiv"], ARX + r["arxiv"])

# Fill missing abstracts from other records with the same DOI, then (optionally) from OpenAlex.
best = {}
for r in recs:
    if r["doi"] and len(r["abstract"]) > len(best.get(r["doi"], "")):
        best[r["doi"]] = r["abstract"]
missing = sorted({r["doi"] for r in recs if r["doi"] and not best.get(r["doi"])})
enrich_dir = os.path.join(RAW, "enrich")
os.makedirs(enrich_dir, exist_ok=True)
if ENRICH:
    from http_get import get  # noqa: E402
    for i in range(0, len(missing), 50):
        path = os.path.join(enrich_dir, f"b{i // 50:04d}.json")
        if not os.path.exists(path):
            chunk = [d for d in missing[i:i + 50] if "," not in d and "|" not in d]
            url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
                {"filter": "doi:" + "|".join(chunk), "per_page": 50, "select": "doi,abstract_inverted_index"})
            json.dump(get(url), open(path, "w", encoding="utf-8"))
def load_enrich(pattern):
    for path in glob.glob(os.path.join(enrich_dir, pattern)):
        data = json.load(open(path, encoding="utf-8"))
        for w in data.get("response", data).get("results", []):
            ab = inv_abstract(w.get("abstract_inverted_index"))
            d = clean_doi(w.get("doi"))
            if ab and len(ab) > len(best.get(d, "")):
                best[d] = ab


load_enrich("b*.json")
# Some sources give a one-line teaser instead of the abstract; look those up too (second pass, own cache files).
short = sorted(d for d, ab in best.items() if 0 < len(ab) < 200 and d not in set(missing) and "," not in d and "|" not in d)
print("short abstracts to look up:", len(short))
if "--enrich-short" in sys.argv:
    from http_get import get  # noqa: E402
    for i in range(0, len(short), 50):
        path = os.path.join(enrich_dir, f"c{i // 50:04d}.json")
        if not os.path.exists(path):
            chunk = short[i:i + 50]
            url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
                {"filter": "doi:" + "|".join(chunk), "per_page": 50, "select": "doi,abstract_inverted_index"})
            json.dump({"requested": chunk, "response": get(url)}, open(path, "w", encoding="utf-8"))
load_enrich("c*.json")
for r in recs:
    if r["doi"] and len(best.get(r["doi"], "")) > len(r["abstract"]):
        r["abstract"] = best[r["doi"]]

# Apply the local filter.
for r in recs:
    if not r["abstract"]:
        r["routes"] = ["T"] if title_keep(r["title"]) else []
    elif r["src"].startswith("Citation"):
        r["routes"] = ["CH"] if chase_keep(r["title"], r["abstract"]) else []
    else:
        r["routes"] = routes(r["title"], r["abstract"])


def m3(r):
    p, v = r["ptype"].lower(), r["vtype"].lower()
    if "review" in p:
        return "Review"
    if p in ("erratum", "retraction", "editorial", "letter", "paratext", "dataset", "dissertation", "book-chapter", "book"):
        return {"book-chapter": "Book chapter", "paratext": "Front matter or other"}.get(p, p.capitalize())
    if "preprint" in p or v == "repository" or (r["doi"].startswith(ARX) and not r["venue"]):
        return "Preprint"
    if "conference" in p or v == "conference":
        return "Conference paper"
    if "journalarticle" in p or p == "article":
        return "Journal article"
    return r["ptype"] or "Other"


def ris(r, qkeys, rts):
    ty = {"Journal article": "JOUR", "Conference paper": "CONF", "Preprint": "UNPB", "Review": "JOUR"}.get(m3(r), "GEN")
    lines = [f"TY  - {ty}", f"TI  - {r['title']}", f"AB  - {r['abstract']}", f"PY  - {r['year']}"]
    lines += [f"DO  - {r['doi']}"] if r["doi"] else []
    lines += [f"T2  - {r['venue']}"] if r["venue"] else []
    lines += [f"M3  - {m3(r)}", f"DB  - {r['src']}", f"UR  - {r['ext']}"]
    lines += [f"LA  - {r['lang']}"] if r["lang"] else []
    lines += [f"N1  - search queries: {', '.join(qkeys)}; filter routes: {', '.join(rts)}", "ER  - ", ""]
    return "\n".join(x.replace("\r", " ").replace("\n", " ") if not x.startswith("ER") else x for x in lines)


counts = collections.defaultdict(lambda: dict(raw=0, with_abstract=0, kept=0, routes=collections.Counter()))
by_src = collections.defaultdict(dict)
for r in recs:
    c = counts[r["qkey"]]
    c["raw"] += 1
    c["with_abstract"] += bool(r["abstract"])
    c["kept"] += bool(r["routes"])
    c["routes"].update(r["routes"])
    key = r["doi"] or r["ext"]
    e = by_src[r["src"]].setdefault(key, dict(r=r, q=set(), rt=set()))
    e["q"].add(r["qkey"])
    e["rt"].update(r["routes"])
    if len(r["abstract"]) > len(e["r"]["abstract"]):
        e["r"] = r

summary = {"queries": {k: dict(v, routes=dict(v["routes"])) for k, v in sorted(counts.items())},
           "sources": {}, "missing_abstract_dois_looked_up": len(missing) if ENRICH else 0}
for src, entries in by_src.items():
    kept = [e for e in entries.values() if e["rt"]]
    fname = re.sub(r"[^a-z0-9]+", "-", src.lower()).strip("-") + ".ris"
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        for e in kept:
            f.write(ris(e["r"], sorted(e["q"]), sorted(e["rt"])) + "\n")
    summary["sources"][src] = dict(unique_records=len(entries), kept=len(kept),
                                   no_abstract=sum(not e["r"]["abstract"] for e in entries.values()), file=fname)
json.dump(summary, open(os.path.join(OUT, "search_counts.json"), "w", encoding="utf-8"), indent=1)
print(json.dumps(summary["sources"], indent=1))
