"""Download raw search results page by page (resumable). Usage:
python -I fetch.py <script_dir> <raw_dir> <source> <query_key> [<query_key> ...]
source: s2 | arxiv | openalex
"""
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, sys.argv[1])
from http_get import get  # noqa: E402
import server_queries as Q  # noqa: E402

RAW, SOURCE, KEYS = sys.argv[2], sys.argv[3], sys.argv[4:]
OA_DATES = "from_publication_date:2017-01-01,to_publication_date:2026-11-23"
OA_FIELDS = "id,doi,display_name,publication_year,publication_date,type,language,primary_location,abstract_inverted_index,ids"
S2_FIELDS = "title,abstract,year,publicationDate,externalIds,venue,publicationTypes,journal"


def save(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def fetch_s2(key):
    d = os.path.join(RAW, "s2", key)
    os.makedirs(d, exist_ok=True)
    n, token = 0, None
    while True:
        path = os.path.join(d, f"p{n:03d}.json")
        if os.path.exists(path):
            page = json.load(open(path, encoding="utf-8"))
        else:
            params = {"query": Q.SEMANTIC_SCHOLAR[key], "fields": S2_FIELDS, "year": "2017-2026"}
            if token:
                params["token"] = token
            page = get("https://api.semanticscholar.org/graph/v1/paper/search/bulk?" + urllib.parse.urlencode(params), gap=4)
            save(path, json.dumps(page))
            print(key, "page", n, "records", len(page.get("data", [])), "total", page.get("total"), flush=True)
        token = page.get("token")
        n += 1
        if not token:
            break


def fetch_arxiv(key):
    d = os.path.join(RAW, "arxiv", key)
    os.makedirs(d, exist_ok=True)
    q = f"({Q.ARXIV[key]}) AND submittedDate:[201701010000 TO 202611232359]"
    start, step, total = 0, 500, None
    while total is None or start < total:
        path = os.path.join(d, f"s{start:06d}.xml")
        if os.path.exists(path):
            xml = open(path, encoding="utf-8").read()
        else:
            params = {"search_query": q, "start": start, "max_results": step, "sortBy": "submittedDate", "sortOrder": "ascending"}
            xml = get("https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params), gap=4, as_json=False)
            save(path, xml)
            print(key, "start", start, "entries", xml.count("<entry>"), flush=True)
        total = int(re.search(r"totalResults[^>]*>(\d+)<", xml).group(1))
        start += step


def fetch_openalex(key):
    d = os.path.join(RAW, "openalex", key)
    os.makedirs(d, exist_ok=True)
    # Cursor paging needs an API key; basic page paging works up to 10,000 results.
    n, pages = 1, 1
    while n <= pages:
        path = os.path.join(d, f"p{n:03d}.json")
        if os.path.exists(path):
            page = json.load(open(path, encoding="utf-8"))
        else:
            params = {"filter": f"title_and_abstract.search:{Q.OPENALEX[key]},{OA_DATES}", "per_page": 200,
                      "page": n, "sort": "publication_date:asc", "select": OA_FIELDS}
            page = get("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
            save(path, json.dumps(page))
            print(key, "page", n, "records", len(page["results"]), "count", page["meta"]["count"], flush=True)
        pages = min(50, -(-page["meta"]["count"] // 200))
        n += 1


for k in KEYS:
    {"s2": fetch_s2, "arxiv": fetch_arxiv, "openalex": fetch_openalex}[SOURCE](k)
print("done", SOURCE, KEYS)
