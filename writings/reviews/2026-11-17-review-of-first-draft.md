# Review of the first conference draft

**Reviewed:** the first draft (`writings/paper/main.pdf`, 7 pages, since replaced by the conference and journal versions), on 2026-11-17.
**Method:** a pre-submission review (macro logic, writing, grammar, LaTeX, figures, banned words) plus the project's research review (fairness, cost accounting, evidence). The draft was also compared against the docs merged to `main` in PR #8 (`docs/training-pipeline.md`) and PR #9 (`docs/gap-evidence.md`), which are now the reference.
**Reviewer:** AI agent. A team member should check these findings.

Every finding below was fixed in the second drafts: `writings/conference/main.tex` (6 pages or less) and `writings/journal/main.tex` (10 to 12 pages). The "Fix" column says how.

## Summary

- CRITICAL: 4
- MAJOR: 9
- MINOR: 6
- First fixes: remove the claims that the study has measured anything; align the PINN and cost design with the merged docs; get the conference version to 6 pages.

## Macro logic and claims

| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | Overclaim. "Our contribution is that measurement, not a new model." No measurement exists. | CRITICAL | The contribution is now stated as the study design and the analysis rule. |
| 2 | Overclaim. Contribution 2 calls the design "a matched-accuracy benchmark ... with an efficient reusable finite-difference baseline". Nothing is built, and efficiency is not shown. | MAJOR | Now "a design for a matched-accuracy comparison". Efficiency is a pilot check, not a claim. |
| 3 | Mismatch with `training-pipeline.md` Sec. 4: the draft says "four to six hidden layers of 40 to 80 tanh units" and an "optional short L-BFGS stage". The merged plan proposes 3 or 4 layers, widths 32 and 64, Glorot init, FP64, and Adam then L-BFGS by default. | CRITICAL | PINN section rewritten from the merged plan, marked as candidates. |
| 4 | Mismatch with `training-pipeline.md` Sec. 5: validation reference solves and the classical grid study are not charged; no maximum retry count; seed selection cost not stated. | CRITICAL | Cost terms table and setup-cost section now follow Sec. 5. The crossover is reported with and without the cost of establishing accuracy. |
| 5 | Table I: Huang et al. listed as "Modeled cost". `gap-evidence.md` gives "solve units and time", finite volume with AMG-preconditioned CG, three seeds. Kapoor et al. and Zhang et al. are missing. | MAJOR | Table rebuilt from the evidence matrix. |
| 6 | Runtime ratios published by Markidis (about 69) and Chuang and Barba (over 5,700; over 28,000) are not used, though they show how far apart prior numbers are. | MAJOR | Added as arithmetic on published numbers, clearly labeled, with the note that those PINNs were single-problem. |
| 7 | Wang, Wang, Perdikaris speedup is described without saying it excludes training. | MAJOR | Now says the speedup is inference only. |
| 8 | Gate rule left vague ("an acceptance rule fixed before the gate"). The merged plan names the choice: worst case or a stated quantile, with box corners in the held-out set. | MAJOR | Stated as an open decision with both options. |
| 9 | The linear model assumes constant per-query cost. CG iterations can change with the parameters (`training-pipeline.md` C26). | MAJOR | Per-query classical cost is recorded across held-out parameters, and the linear check covers both methods. |
| 10 | GPU measurement rule is vague ("blocks long enough"). The merged plan gives at least 5 s blocks, four trials with random gaps, and training as one long window. | MAJOR | Protocol section now states these. |
| 11 | Precision of the two methods is not mentioned (C22). | MINOR | Both methods record dtype; FP64 preferred for both. |

## Writing details

| # | Finding | Severity | Fix |
|---|---|---|---|
| 12 | Long sentences. Example: "We ask how many new parameter queries a parametric PINN must answer before its cumulative electricity, and separately its cumulative runtime, falls to that of an efficient finite-difference solver at the same accuracy." Several intro sentences pass 35 words. | MAJOR | Rewritten as short sentences. Most are under 20 words. |
| 13 | "Results" section is only placeholder text, which reviewers read as missing work. | MAJOR | Renamed "Reporting Plan". It says what will be reported and shows the empty table format. |
| 14 | Vague topic sentence: "Two more problems make a fair answer hard to get." | MINOR | Replaced by specific statements. |
| 15 | Awkward phrase: "falls to that of". | MINOR | Rewritten. |

## LaTeX and format

| # | Finding | Severity | Fix |
|---|---|---|---|
| 16 | 7 pages; the conference target is 6. | CRITICAL | Conference version cut to 6 pages. The longer text moved to the journal version. |
| 17 | Last page holds three references in one column. | MINOR | Fixed by the new length. |
| 18 | Fig. 2 (conductivity) uses space without carrying a decision. | MINOR | Kept only in the journal version. |

## Figures

Both data-free figures are vector PDF, with fonts at 7 to 8 pt after scaling. Fig. 3 (outcome classes) is clearly labeled as a sketch. No issue beyond item 18.

## Banned words and dashes

Full scan of the first draft: no em dashes, none of delve, moreover, furthermore, underscore, leverage, utilize, pivotal, novel. Two soft phrases ("keeps the comparison honest", "keeps the cost ... visible") were already removed in the first polish.

## Score and recommendation

First draft: 5 of 10. Needs major revision before submission. The second drafts address every item above. They still report no measured results, so neither is a results paper yet.

## Second pass: overclaim and source audit of the new drafts

A separate reviewer checked every claim in `conference/main.tex` and `journal/main.tex` against the merged docs and the paper notes. All numbers matched their sources. Six wording problems were found and fixed:

1. The Henderson et al. R² value is about operation counts, not runtime. The text now says so, and the runtime point cites Wilson et al. (preprint).
2. Q3 credited Huang and Stuart with a training-cost claim they do not make. It now cites De Ryck et al. for training cost, in a linear model, and Huang and Stuart only for classical solvers gaining ground as the target tightens.
3. "Published work does not answer this question" is now limited to the search recorded for the project.
4. "A complete study design" became "a study design ... and its open decisions", since several decisions are still open.
5. Hardware: Grossmann et al. used one machine (GPU against CPU cores); Chuang and Barba used different machines. The text now says this.
6. "The PINN rows report no spread across training seeds" is now limited to the parts read.

Also aligned: failure counts are reported, not rates (training plan C23). Not checked by the second reviewer: the Zhang et al. row beyond the evidence matrix and training plan C26, and the bibliography metadata (checked in the first pass).
