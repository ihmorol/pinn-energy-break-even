# Scoping review for gap validation

This folder records a documented search and screening run on 2026-11-23. Its purpose is to test whether the gaps our study claims hold, and to narrow them where needed. It is AI-assisted and not yet checked by a team member.

| File | Contents |
|---|---|
| [review-protocol.md](review-protocol.md) | Question, gap claims under test, sources, search method, selection zones, charting and appraisal plan, amendment log |
| [screening_protocol.md](screening_protocol.md) | Eligibility rules and exclusion codes (v1.0, confirmed 2026-11-23) |
| [screening_config.json](screening_config.json) | Codes, seeds and keyword groups for the sr-screener scripts |
| [search-log.md](search-log.md) | Queries, dates, counts per source and the PRISMA-style flow |
| [screening-decisions.csv](screening-decisions.csv) | Decision, code and note for each of the 109 abstracts read in Zone 3 |
| [team-shortlist.md](team-shortlist.md) | Ranked 45 studies plus 10 reserves, the judging sheet, and context papers |
| [team-selection.csv](team-selection.csv) | Sheet for the team to score and select 20-30 studies |
| [reading-list.md](reading-list.md) | The 17 studies to read (12 to cite, 5 read-only preprints or theses), AI scores for all 55, and the map from each methodology stage to its sources |
| [verification.md](verification.md) | Identity check, publication status and venue quality for all 55 studies; facts from the full texts read |
| [gap-validation.md](gap-validation.md) | Provisional verdict for each gap claim, narrowed gap wording, full-text checks needed |
| [search/](search/) | The scripts that ran the search, filter and ranking (tests in `tests/test_sr_search_filter.py`) |

**Next steps:**

1. The team reads the 17 studies in [reading-list.md](reading-list.md), using `outputs/systematic-review/team-reading.html` (opens on those 17, with abstracts and the AI scores), and changes any score it disagrees with.
2. A team member downloads the five open-access papers that still show a human-verification check (list in verification.md Section 3), so they can be read. None of them decides GC1 or GC3, which are now settled from full text.
3. The team confirms Scopus or Web of Science indexing for the selected studies.
4. The gap statement in `docs/gap-analysis.md` is updated from the confirmed verdicts.
