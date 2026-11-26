"""Download open-access full texts, one new folder per paper, recording source and SHA-256.
Usage: python -I download_fulltexts.py <downloads_dir> <manifest_out.json>
A file that is not a PDF (for example a bot-check page) is deleted and recorded as not retrieved.
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

ROOT, OUT = sys.argv[1], sys.argv[2]
UA = {"User-Agent": "Mozilla/5.0 (compatible; literature-check)", "Accept": "application/pdf,*/*"}
SD = "https://www.sciencedirect.com/science/article/pii/{}/pdfft?isDTMRedir=true&download=true"
PAPERS = [
    ("R01457", "tandale-2024-spiking-fem", ["https://link.springer.com/content/pdf/10.1007/s00366-024-01967-3.pdf"]),
    ("R02880", "buoso-2021-parametric-pinn-heart", [SD.format("S1361841521001122")]),
    ("R01189", "wang-2026-eppinns", [SD.format("S2214157X26005897")]),
    ("R02939", "wurth-2023-pinn-composite", [SD.format("S0264127523004495")]),
    ("R00383", "li-2026-parametric-pinn-microfluidic", ["https://arxiv.org/pdf/2611.10666"]),
    ("R00643", "sun-2026-fevessel", ["https://arxiv.org/pdf/2607.17318"]),
    ("R00692", "cao-2025-tsonn-aerofoil", ["https://arxiv.org/pdf/2501.01165"]),
    ("R00718", "luo-2025-mr-dino", ["https://arxiv.org/pdf/2305.20053"]),
    ("R01145", "eivazi-2026-equino", ["https://arxiv.org/pdf/2504.07976"]),
    ("R00637", "roohi-2026-fp-surrogate", ["https://arxiv.org/pdf/2606.15622"]),
    ("R00220", "garg-2026-neuropinns", ["https://arxiv.org/pdf/2511.06081"]),
    ("R03090", "xue-2026-geothermal-operator", ["https://pmc.ncbi.nlm.nih.gov/articles/PMC13389401/pdf/"]),
    ("R01850", "lee-2026-fem-ml-fpga", ["https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/aisy.202501108"]),
    ("R00895", "srinivasan-2025-rbf-pielm", ["https://dl.acm.org/doi/pdf/10.1145/3799830.3799865"]),
    ("R00504", "flow-surrogates-2026-no-free-lunch", ["https://arxiv.org/pdf/2607.23667"]),
    ("R00627", "zhang-2026-breakeven-complexity", ["https://arxiv.org/pdf/2605.15399"]),
]
manifest = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for rid, slug, urls in PAPERS:
    d = os.path.join(ROOT, slug)
    path = os.path.join(d, slug + ".pdf")
    if manifest.get(rid, {}).get("status") == "ok" and os.path.exists(path):
        continue
    os.makedirs(d, exist_ok=True)
    rec = dict(id=rid, slug=slug, status="not retrieved", tried=[])
    for url in urls:
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
                body = r.read()
                final = r.geturl()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            rec["tried"].append([url, f"{type(e).__name__}: {getattr(e, 'code', '')}"])
            continue
        if body[:5] != b"%PDF-":
            rec["tried"].append([url, f"not a PDF ({len(body)} bytes, starts {body[:30]!r})"])
            continue
        open(path, "wb").write(body)
        rec.update(status="ok", url=url, final_url=final, bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                   retrieved="2026-11-26")
        break
    if rec["status"] != "ok" and not os.listdir(d):
        os.rmdir(d)
    manifest[rid] = rec
    print(rid, slug, rec["status"], rec.get("bytes", ""), rec["tried"][-1:] if rec["status"] != "ok" else "", flush=True)
    time.sleep(3)
json.dump(manifest, open(OUT, "w", encoding="utf-8"), indent=1)
