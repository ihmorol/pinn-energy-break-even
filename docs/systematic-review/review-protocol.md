# Review protocol: scoping review for gap validation

**Project:** Reaching the energy and computational break-even point between PINNs, and classical solvers.
**Version:** 0.1 draft, 2026-11-23. Not yet confirmed by the team.
**Prepared by:** Claude Code (AI agent) at the request of a team member. Every step below is AI-run unless marked otherwise; see Section 9 for the human checks this needs.

## 1. Purpose and review type

We want to know whether the gap our study claims is real, and to narrow it if it is not. The design is a **scoping review with targeted appraisal**: a documented search of open bibliographic indexes, dual screening against fixed rules, charting of every included study, and an appraisal of the studies closest to our design.

Reporting follows the PRISMA extension for scoping reviews (PRISMA-ScR) and PRISMA-S for the search, as guidance only. The review is not registered, screening is AI-assisted, and Scopus and Web of Science could not be searched directly (Section 4). We will not describe it as PRISMA-compliant or as a full systematic review.

## 2. Questions

- **RQ1.** Which studies report the energy, power or carbon of a neural PDE solver, and is it measured (hardware counter or meter) or estimated? For which of them is a classical solver measured the same way?
- **RQ2.** Which studies compare a neural PDE solver with a classical solver under repeated use (break-even, amortization, or offline plus online cost), and what break-even counts do they report?
- **RQ3.** Among those, which use a physics-informed model trained across a parameter family, and how do they handle accuracy matching, baseline strength, hardware, seeds and failed runs?
- **RQ4.** Does any included study meet the conditions of one of our gap claims (Section 3)?

## 3. Gap claims under test

Each claim comes from [gap-analysis.md](../gap-analysis.md) Section 4. A claim is **falsified** if at least one included study meets every condition listed. It is **partly met** if a study meets all but one condition; we then narrow the claim by naming the missing condition. Otherwise it **holds within this review's search**, which is not proof that no such study exists.

| ID | Claim (from gap-analysis) | Conditions a study must meet to falsify it |
|---|---|---|
| GC1 | No metered-energy comparison of a PINN against a classical solver at matched accuracy | physics-informed model; classical solver; energy reported for both; measured by counter or meter (not only estimated); same problem; accuracy matched or stated for both |
| GC2 | No break-even count for a parametric PINN against a classical solver | physics-informed model trained across a parameter family; classical solver; a break-even or amortization query count reported in any cost unit |
| GC3 | Energy and runtime break-even never reported separately | any neural PDE solver; classical solver; break-even reported in energy and, separately, in runtime |
| GC4 | Tuning, failed runs and uncertainty not carried into a break-even estimate | physics-informed model; classical solver; break-even or cumulative cost with seed or trial variability and with failed or tuning runs counted |
| GC5 | No PINN evidence on how the accuracy target moves the break-even point | physics-informed model; classical solver; break-even reported at two or more accuracy targets |

The narrow combined claim (gap-analysis, "Narrow statement of the gap") is tested as GC1 and GC2 together.

## 4. Information sources

| Source | Use | Access |
|---|---|---|
| OpenAlex | Main multidisciplinary index; covers most journals indexed in Scopus and Web of Science, plus arXiv | Public API, no key (shared daily budget) |
| Semantic Scholar | Second multidisciplinary index with strong computer science and arXiv coverage | Public bulk-search API |
| arXiv | Preprints, where most 2025-2026 work in this area first appears | Public API |
| Citation chasing | Forward citations (OpenAlex) of the seed studies and of key context papers (Grossmann et al. 2024; Markidis 2021; Chuang and Barba 2022; McGreivy and Hakim 2024; de Hoop et al. 2022); backward references of included studies | OpenAlex API |
| OpenAlex full-text search | Check for break-even or amortization terms that appear only in full texts | Works with indexed full text only |
| Scopus, Web of Science | Not searchable: no login available to the team | Venue indexing of each included study checked on public lists (SCImago Journal Rank, which uses Scopus data, and the Clarivate Master Journal List) |
| DBLP | Not used: the site returned a bot-check page, which we do not bypass | None |
| Google Scholar | Not used: no stable scriptable access | None |

## 5. Search strategy

Search dates: records published 2017-01-01 to 2026-11-23 (PINNs were introduced in 2017 preprints). No language limit at search; non-English records are flagged at screening.

The search runs in two steps:

1. **Server-side supersets** ([search/server_queries.py](search/server_queries.py)). These are broad queries in each source's syntax, kept simple because OpenAlex drops phrase stemming inside combined boolean queries. This was found when the first strings missed seed studies.
2. **Local filter** ([search/local_filter.py](search/local_filter.py)). This is one fixed set of regular expressions applied to every downloaded title and abstract, so every source is filtered by the same rules. A record is kept if it meets any of three routes:
   - **F1:** neural PDE solver plus an energy, power or carbon term.
   - **F2:** neural PDE solver plus a break-even, amortization or offline-cost term.
   - **F3:** physics-informed model plus a classical-solver term, a cost term and a parametric or many-query term.

Records with no abstract in the source get the abstract from OpenAlex by DOI where possible; otherwise only the title is filtered.

Search development used the seed studies (Section 6) to find missing terms. Seed recall therefore checks the final strings but is not an independent test of sensitivity. Citation chasing is the independent check. Every query, date, raw count and post-filter count goes into [search-log.md](search-log.md).

## 6. Selection

Rules: [screening_protocol.md](screening_protocol.md) and [screening_config.json](screening_config.json), applied with the sr-screener workflow.

- **Seed studies** (known eligible): Wang, Wang, Perdikaris 2021; Huang et al. 2026; Kapoor et al. 2025; Zhang et al. 2026; Yoo et al. 2026; Wilson et al. 2025. Grossmann et al. 2024, Markidis 2021, and Chuang and Barba 2022 are not seeds. They compare single solves on runtime only, which is exclusion code E5. They stay in the report as context.
Selection runs in three zones and a team stage (amendment 1):

1. **Zone 1, scripted ranking.** Every deduplicated record gets a score from fixed title and abstract terms: break-even, amortization, computational energy, classical comparator, physics-informed model, parametric use. Terms marking energy as a physical quantity of the modelled system (buildings, batteries, power grids) lower the score unless computational energy terms are also present. Recency and peer-review status add small amounts. Records above the cutoff, plus every record with a strong gap signal, go to Zone 2. Records below are reported in PRISMA as "marked ineligible by automation tools".
2. **Zone 2, titles.** One AI reader (Claude, main session) applies the screening rules to the titles and keeps any record that could be eligible.
3. **Zone 3, abstracts.** The same reader applies the rules to the abstracts of the Zone 2 records. It ranks the eligible ones by how closely they test a gap claim, and uses venue strength, citations and recency only to order similar records. The output is a ranked list of 40-50.
4. **Team stage.** Team members read the 40-50 titles and abstracts with the judging sheet and select the studies to chart (expected 20-30).
5. **Full text.** Only the selected studies that could falsify a gap claim are read in full, to settle the gap decisions.

**Stage counts:** reported in a PRISMA 2020 flow diagram. One AI reader is not dual screening, and the methods text will say so.

## 7. Charting and appraisal

**Charting form, per included study:**
- identity, version and peer-review status;
- venue and its Scopus or Web of Science indexing;
- route (F1, F2, F3);
- model type and training mode (physics-only, data, or both);
- PDE and parameter family;
- classical solver and any evidence that it is efficient (preconditioner, multigrid, direct factorization, tuning);
- query definition;
- accuracy metric and target, and whether accuracy was matched;
- costs reported (setup or training, per query, total) and their units (runtime, energy, FLOPs, carbon);
- energy method (counter, meter, or estimate tool) and declared measurement boundary;
- hardware for each method;
- break-even value and its units;
- number of accuracy targets;
- seeds or repeats;
- failed or tuning runs counted;
- main result, and the limits the authors state.

**Appraisal**, for studies that meet three or more conditions of any gap claim. This is a project checklist, not a validated tool:

| Item | Basis |
|---|---|
| Q1 Equal accuracy or equal runtime | McGreivy and Hakim 2024, rule 1 |
| Q2 Efficient classical baseline | McGreivy and Hakim 2024, rule 2 |
| Q3 Training or offline cost counted | Huang et al. 2026, Eq. 1 |
| Q4 Energy measured, not only estimated, with a declared boundary | Henderson et al. 2020 |
| Q5 Same hardware, or a matched measurement boundary | project plan Section 4 |
| Q6 Seed or trial variability reported | project plan Section 4 |
| Q7 Failed or tuning runs reported | McGreivy and Hakim 2024 (reporting bias) |

Each item is rated yes, partial, no, or not reported, with the page or section.

## 8. Synthesis

- An evidence map: tables by route, model family, cost unit and energy method.
- A decision for each gap claim (falsified, partly met, holds within the search), with the deciding studies.
- If a claim is falsified or partly met, a narrowed wording that adds the missing condition. The narrowing stays within the fixed project scope (research plan Section 2); no new benchmark family is added.

## 9. Known limits and human checks

- No direct Scopus or Web of Science search. Coverage of those indexes is approximated through OpenAlex and Semantic Scholar.
- The search is limited to titles and abstracts. A break-even analysis mentioned only in a full text can be missed, which the full-text search check reduces but does not remove.
- AI screening is decision support. A team member should check every included study, a sample of exclusions, and the gap decisions before the report uses them.
- Two runs of one model family are not independent human reviewers. The methods text will say so.

## Appendix A. Boundary cases (synthetic records, not real papers)

These test the screening rules. If the team disagrees with an expected decision, the rule wording changes before the pilot.

| # | Synthetic title and abstract | Expected | Tests |
|---|---|---|---|
| 1 | Parametric PINN for steady heat conduction with variable conductivity. Training cost is recovered after about 400 queries compared with a finite element solver. | include | Route (ii) with an explicit break-even |
| 2 | PINN surrogate for heat sink design optimization; computational efficiency compared with a CFD-based optimization loop. No details of what was timed. | unclear | Many-query use is plausible; the full text must show cost accounting |
| 3 | PINN versus FEM for 2D Poisson: the PINN trains 100 times slower and is less accurate. | exclude E5 | Single problem, runtime only, no repeated use |
| 4 | PINN predicts the energy consumption of a building from a heat-transfer PDE. | exclude E3 | "Energy" is a physical quantity, not the cost of computation |
| 5 | Adaptive sampling speeds up PINN training threefold compared with a vanilla PINN. | exclude E4 | Cost only against another neural model, no energy |
| 6 | Carbon footprint of training Fourier neural operators for weather forecasting, measured with CodeCarbon. | include | Route (i): energy or carbon, no classical comparator needed |
| 7 | FNO for Navier-Stokes: inference 1000 times faster than a pseudo-spectral solver. | exclude E5 | Non-physics-informed model with a plain speed-up claim |
| 8 | Title only, no abstract: "Break-even analysis of neural operator surrogates versus multigrid solvers". | unclear | No-abstract rule: the title suggests both core criteria |

## Amendment log

| Date | Change | Reason |
|------|--------|--------|
| 2026-11-23 | Eligibility rules confirmed (screening protocol v1.0). | Team confirmation. |
| 2026-11-23 | Selection changed from dual AI screening to three zones plus team selection: scripted ranking of all records (Zone 1), single AI reader on titles (Zone 2) and abstracts (Zone 3) to a ranked 40-50, then the team reads those and selects 20-30. Venue strength and recency only order records; they never remove a record that carries a strong gap signal. | Team request to limit token use. A single AI reader is not dual screening, and the methods text will say so. |
| 2026-11-23 | OpenAlex query OA-Q3-parametric (about 6,200 records) not run. | The OpenAlex free daily budget ran out; the team chose to rely on Semantic Scholar and arXiv for that route. |
