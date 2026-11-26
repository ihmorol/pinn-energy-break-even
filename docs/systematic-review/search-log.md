# Search and selection log

**Review:** scoping review for gap validation ([review-protocol.md](review-protocol.md)).
**Run:** 2026-11-23, by Claude Code (AI agent) for the team. Not yet checked by a team member.
**Scripts:** [search/](search/). They ran with Python 3.12 using only the standard library. Raw downloads are kept under the ignored `downloads/sr-search-2026-11-23/`, and working files under the ignored `outputs/systematic-review/`.

## 1. Sources and access

| Source | Accessed | Access used | Notes |
|---|---|---|---|
| OpenAlex | 2026-11-23 | Public API, no key | Shared free budget of $0.10 a day per IP. Cursor paging needs a key, so basic page paging was used (fine under 10,000 results). |
| Semantic Scholar | 2026-11-23 | Public bulk-search API | Frequent HTTP 429 replies; handled by waiting and retrying. |
| arXiv | 2026-11-23 | Public API | 500 results per page. |
| Citation chasing | 2026-11-23 | OpenAlex `cites:` filter | Forward citations of 11 target papers (Section 3). |
| Scopus, Web of Science | not searched | No login | Venue indexing will be checked for the studies the team selects. |
| DBLP | not searched | Bot-check page | Not bypassed. |
| OpenAlex query OA-Q3-parametric | not run | Budget ran out | About 6,200 records. The team chose to rely on Semantic Scholar and arXiv for this route (amendment, 2026-11-23). |

## 2. Search development

- The first OpenAlex strings found none of the four core comparison papers. Their abstracts use words such as "computational costs", "solution time", "performance benchmark" and "conventional PDE solvers", so the comparator and cost terms were widened.
- OpenAlex drops plural and phrase matching inside long combined boolean queries. For example, each block found the physics-informed DeepONet paper alone, but the AND of the blocks did not. So server queries were kept broad, and one local filter ([search/local_filter.py](search/local_filter.py)) was applied to every record from every source.
- A bug in the local filter missed the word "parametric" itself. It was found when the seed study Wang, Wang, Perdikaris (2021) was missing after the first deduplication, and fixed before any screening. [tests/test_sr_search_filter.py](../../tests/test_sr_search_filter.py) guards against it.
- Semantic Scholar sometimes stores a one-line teaser instead of the abstract. Such records got the longest abstract available for the same DOI from another source. In addition, 10,146 DOIs with no abstract and 104 with a teaser were looked up in OpenAlex.
- The seed studies were used to find missing terms, so finding all six seeds checks the final strings. It is not an independent test of sensitivity.

## 3. Queries and counts

Server queries are in [search/server_queries.py](search/server_queries.py). Dates: published 2017-01-01 to 2026-11-23. "Kept" means the record passed the local filter. Routes F1 (energy), F2 (break-even), F3 (parametric physics-informed versus classical) and T (title only, no abstract) are defined in the filter. Citation-chasing records used a looser rule (CH): a neural PDE solver with any energy, break-even or cost term.

| Query | Raw records | With abstract | Kept |
|---|---:|---:|---:|
| OA-Q1-energy | 7,449 | 6,252 | 1,086 |
| OA-Q2-breakeven | 5,799 | 4,766 | 688 |
| S2-Q0-pinn-family (all physics-informed records) | 31,067 | 25,201 | 2,095 |
| S2-Q1a-energy | 6,277 | 5,596 | 899 |
| S2-Q1b-energy | 3,482 | 3,142 | 431 |
| S2-Q2-breakeven | 5,290 | 4,623 | 497 |
| AX-Q0-pinn-family | 6,970 | 6,970 | 389 |
| AX-Q1-energy | 842 | 842 | 157 |
| AX-Q2-breakeven | 647 | 647 | 247 |
| Citation chasing, 11 targets | 2,613 | 1,949 | 729 |

Citation-chasing targets and the number of citing records found: Wang, Wang, Perdikaris 2021 (1,425); Grossmann et al. 2024 (382); Markidis 2021 (337); McGreivy and Hakim 2024 (265); de Hoop et al. 2022 (132); Chuang and Barba 2022 (66); Kapoor et al. 2025 (4); Zhang et al. 2026 (1); Yoo et al. 2026 (1); Huang et al. 2026 (0); Wilson et al. 2025 (0).

Unique records within each source, then kept: OpenAlex 13,128 then 1,750; Semantic Scholar 43,859 then 2,917; arXiv 8,264 then 681; citation chasing 2,395 then 660.

## 4. Selection flow (PRISMA 2020 terms)

| Step | Records |
|---|---:|
| Records identified after the full search strategy (4 sources) | 6,008 |
| Duplicates removed (sr-screener `prepare_records.py`: DOI, then title and year) | 1,807 |
| Unique records | 4,201 |
| Marked ineligible by automation tools: Zone 1 rank below cutoff ([search/rank.py](search/rank.py)) | 3,278 |
| Titles screened (Zone 2) | 923 |
| Excluded at title | 761 |
| Low-priority titles removed by the scripted check ([search/zone2_lowcheck.py](search/zone2_lowcheck.py)) | 53 |
| Abstracts screened (Zone 3) | 109 |
| Excluded at abstract (E1 7, E2 5, E3 1, E4 12, E5 11) | 36 |
| Eligible at title and abstract stage (49 include, 24 unclear) | 73 |
| Ranked list for the team ([team-shortlist.md](team-shortlist.md)), plus 10 reserves | 45 |
| Full-text assessment | pending team selection |

Zone 1 cutoff: every record with a strong gap signal (412) plus every record with a score of 12 or more. All six seeds passed the cutoff. Decisions for all 109 Zone 3 records are in [screening-decisions.csv](screening-decisions.csv).

## 5. Verification and full texts (2026-11-26)

- **Identity.** All 52 shortlist and reserve records with a DOI resolved in Crossref or arXiv with an exact title match. The three theses were checked as repository records only. Details and venue ratings are in [verification.md](verification.md).
- **Full texts.** 17 open-access PDFs were attempted, each into its own folder under `downloads/`. Nine came from arXiv. The publisher copies (Springer, ScienceDirect, Wiley, ACM, Nature/PMC) and the Charles University repository refused automated access with HTTP 403 or 429, a login redirect, or a Cloudflare check. The check was not completed or bypassed. A second attempt the same day used the Claude desktop app's built-in browser, which a person can also operate. It fetched three more: the Charles University thesis (R01555), Tandale and Stoffel 2024 (R01457) and Xue et al. 2026 (R03090). ScienceDirect, Wiley and ACM showed a "confirm you are human" check, which was left for a team member. Hashes are in `outputs/systematic-review/fulltext_manifest.json`. The scripts are [search/verify.py](search/verify.py) and [search/download_fulltexts.py](search/download_fulltexts.py).
- **Sensitivity miss.** Sacchetti et al. 2022 (IEEE Access), cited by Zhang et al. 2026 as a varying-fidelity PINN-versus-FEM comparison, was not retrieved by any query. It is a single-solve study (code E5), so the gap verdicts do not change.

## 6. Known limits of this run

- **Single AI reader.** One AI reader (Claude, main session) screened titles and abstracts. There was no second reviewer and no human pilot. A team member should check the excluded Zone 3 records and a sample of Zone 2 title exclusions.
- **Title and abstract search only.** A break-even analysis mentioned only in a full text can be missed. About 7% of the unique records (318) have no abstract in any source, mostly Elsevier journals; those were searched by title only.
- **Ranking weakness.** A model name right next to "energy consumption" (for example "PINN for building energy consumption") counts as a computational-energy signal. Some building-energy records were therefore ranked high and then dropped at the title stage. This widened Zone 2 rather than narrowing it.
- **Index coverage.** No Scopus or Web of Science search. Coverage of their journals relies on OpenAlex and Semantic Scholar, and OpenAlex query OA-Q3 was not run.
