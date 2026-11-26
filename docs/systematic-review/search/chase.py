"""Forward citation chasing in OpenAlex (filter-only requests). Usage:
python -I chase.py <script_dir> <raw_dir>
"""
import json
import os
import sys
import urllib.parse

sys.path.insert(0, sys.argv[1])
from http_get import get  # noqa: E402
from fetch_fields import OA_FIELDS  # noqa: E402

RAW = sys.argv[2]
DATES = "from_publication_date:2017-01-01,to_publication_date:2026-11-23"
TARGETS = {
    "wangwangperdikaris2021": "10.1126/sciadv.abi8605",
    "huang2026": "10.48550/arxiv.2610.32911",
    "kapoor2025": "10.48550/arxiv.2505.12556",
    "zhang2026": "10.48550/arxiv.2605.15399",
    "yoo2026": "10.48550/arxiv.2609.30580",
    "wilson2025": "10.48550/arxiv.2509.24517",
    "grossmann2024": "10.1093/imamat/hxae011",
    "markidis2021": "10.3389/fdata.2021.669097",
    "chuangbarba2022": "10.25080/majora-212e5952-005",
    "mcgreivyhakim2024": "10.1038/s42256-024-00897-5",
    "dehoop2022": "10.4208/jml.220509",
}

d = os.path.join(RAW, "chase")
os.makedirs(d, exist_ok=True)
url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
    {"filter": "doi:" + "|".join(TARGETS.values()), "per_page": 50, "select": "id,doi,cited_by_count,display_name"})
found = {w["doi"].replace("https://doi.org/", "").lower(): w for w in get(url)["results"]}
json.dump(found, open(os.path.join(d, "targets.json"), "w", encoding="utf-8"), indent=1)
for name, doi in TARGETS.items():
    w = found.get(doi)
    if not w:
        print(name, "NOT FOUND in OpenAlex", doi)
        continue
    wid = w["id"].rsplit("/", 1)[-1]
    n, pages = 1, 1
    while n <= pages:
        path = os.path.join(d, f"{name}_p{n:03d}.json")
        if os.path.exists(path):
            page = json.load(open(path, encoding="utf-8"))
        else:
            params = {"filter": f"cites:{wid},{DATES}", "per_page": 200, "page": n,
                      "sort": "publication_date:asc", "select": OA_FIELDS}
            page = get("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
            json.dump(page, open(path, "w", encoding="utf-8"))
        pages = min(50, -(-page["meta"]["count"] // 200))
        print(name, wid, "page", n, "of", pages, "citing", page["meta"]["count"], flush=True)
        n += 1
print("done chase")
