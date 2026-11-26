"""Verify shortlist records: Crossref or arXiv identity, published versions of preprints, venue quality lists.
Usage: python -I verify.py <shortlist_meta.json> <out.json>
"""
import difflib
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from http_get import get  # noqa: E402

meta = json.load(open(sys.argv[1], encoding="utf-8"))


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", re.sub(r"<[^>]+>|\$[^$]*\$", " ", (t or "").lower())).strip()


def sim(a, b):
    return round(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio(), 3)


def crossref(doi):
    try:
        return get("https://api.crossref.org/works/" + urllib.parse.quote(doi), gap=1.0)["message"]
    except Exception as e:  # noqa: BLE001 - record the failure, keep going
        return {"error": str(e)}


def crossref_title_search(title):
    q = urllib.parse.urlencode({"query.title": title, "rows": 5, "select": "DOI,title,type,container-title,published,ISSN"})
    try:
        items = get("https://api.crossref.org/works?" + q, gap=1.0)["message"]["items"]
    except Exception:  # noqa: BLE001
        return []
    out = []
    for it in items:
        s = sim(title, (it.get("title") or [""])[0])
        if s >= 0.9 and it.get("type") in ("journal-article", "proceedings-article", "book-chapter", "posted-content", "dissertation"):
            out.append(dict(doi=it["DOI"].lower(), type=it.get("type"), venue=(it.get("container-title") or [""])[0],
                            date=(it.get("published") or {}).get("date-parts"), issn=it.get("ISSN"), sim=s))
    return out


def arxiv(aid):
    x = get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": aid}), gap=4, as_json=False)
    t = re.search(r"<entry>.*?<title>(.*?)</title>", x, re.S)
    jr = re.search(r"<arxiv:journal_ref[^>]*>(.*?)</arxiv:journal_ref>", x, re.S)
    dd = re.search(r"<arxiv:doi[^>]*>(.*?)</arxiv:doi>", x, re.S)
    pub = re.search(r"<published>(.*?)</published>", x)
    return dict(title=re.sub(r"\s+", " ", t.group(1)).strip() if t else None, journal_ref=jr.group(1).strip() if jr else None,
                doi=dd.group(1).strip().lower() if dd else None, published=pub.group(1)[:10] if pub else None)


def sources_by_issn(issns):
    issns = [i for i in issns if i]
    if not issns:
        return []
    q = urllib.parse.urlencode({"filter": "issn:" + "|".join(issns[:50]), "per_page": 50,
                                "select": "display_name,issn,listed_in,is_core,summary_stats,host_organization_name,is_in_doaj,type"})
    return get("https://api.openalex.org/sources?" + q)["results"]


out = []
for o in meta:
    r = dict(id=o["id"], tier=o["tier"], title=o["title"], doi=o["doi"])
    doi = (o["doi"] or "").lower()
    if doi.startswith("10.48550/arxiv."):
        a = arxiv(doi.split("arxiv.", 1)[1])
        r["arxiv"] = a
        r["identity_ok"] = bool(a["title"]) and sim(a["title"], o["title"]) >= 0.85
        r["identity_sim"] = sim(a["title"] or "", o["title"])
        r["published_versions"] = crossref_title_search(o["title"])
    elif doi:
        m = crossref(doi)
        if "error" in m:
            r["identity_ok"] = None
            r["crossref_error"] = m["error"]
            if doi.startswith("10.31224") or doi.startswith("10.18419"):
                r["note"] = "DOI registered outside Crossref (engrXiv/DataCite); checked via OpenAlex record only"
        else:
            ct = (m.get("title") or [""])[0]
            r.update(identity_ok=sim(ct, o["title"]) >= 0.85, identity_sim=sim(ct, o["title"]), cr_type=m.get("type"),
                     cr_venue=(m.get("container-title") or [""])[0], cr_publisher=m.get("publisher"), cr_issn=m.get("ISSN"),
                     cr_date=(m.get("published") or m.get("issued") or {}).get("date-parts"),
                     cr_update=[u.get("type") for u in m.get("update-to", [])] if m.get("update-to") else None,
                     cr_relation=list((m.get("relation") or {}).keys()))
            if m.get("type") == "posted-content":
                r["published_versions"] = crossref_title_search(o["title"])
    else:
        r["identity_ok"] = None
        r["note"] = "no DOI; repository record only"
    out.append(r)
    print(r["id"], r.get("identity_ok"), r.get("cr_type") or ("arXiv" if "arxiv" in r else ""), r.get("cr_venue", "")[:40],
          [v["venue"][:30] for v in r.get("published_versions", [])], flush=True)

issns = sorted({i for r in out for i in (r.get("cr_issn") or [])} | {i for r in out for v in r.get("published_versions", []) for i in (v.get("issn") or [])})
src = []
for k in range(0, len(issns), 50):
    src += sources_by_issn(issns[k:k + 50])
json.dump({"records": out, "sources": src}, open(sys.argv[2], "w", encoding="utf-8"), indent=1)
print("done", len(out), "sources", len(src))
