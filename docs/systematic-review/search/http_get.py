"""Polite JSON/text GET with spacing between calls and retry on HTTP 429."""
import json
import time
import urllib.error
import urllib.request

UA = {"User-Agent": "sr-scoping-review-client/0.1"}
_last = [0.0]


def get(url, gap=1.5, tries=8, as_json=True):
    for attempt in range(tries):
        wait = gap - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                body = r.read().decode("utf-8")
                cost = r.headers.get("X-RateLimit-Remaining-USD")
            if cost is not None:
                print(f"    [openalex budget left ${cost}]")
            return json.loads(body) if as_json else body
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or attempt == tries - 1:
                raise
            delay = float(e.headers.get("Retry-After") or 10 * (attempt + 1))
            print(f"    HTTP {e.code}, waiting {delay:.0f}s")
            time.sleep(min(delay, 120))
        except (TimeoutError, urllib.error.URLError, ConnectionError) as e:
            if attempt == tries - 1:
                raise
            print(f"    {type(e).__name__}, retrying")
            time.sleep(15 * (attempt + 1))
