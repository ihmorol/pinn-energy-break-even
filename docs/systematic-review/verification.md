# Verification and full-text charting

**Checked:** 2026-11-26, by Claude Code (AI agent). Not yet checked by a team member.
**Covers:** all 55 studies in [team-shortlist.md](team-shortlist.md): the 45 ranked studies and the 10 reserves.

## 1. How each study was verified

1. **Identity.** Each DOI was resolved in Crossref, or in the arXiv API for arXiv DOIs. The registered title was compared with our record title (similarity 0 to 1). All 52 records with a Crossref or arXiv DOI matched exactly (similarity 1.0). The three theses were checked through their repository records only.
2. **Published versions of preprints.** Crossref was searched by title, and a match was accepted at similarity 0.9 or more. Two preprints were found to have journal versions, and four arXiv copies we read are the preprints of journal papers (table below).
3. **Venue quality.** Scopus and Web of Science could not be queried: no login, and SCImago answered with a bot check that was not bypassed. Instead we report two national expert-panel ratings, which OpenAlex lists for each venue:
   - the Finnish Publication Forum (JUFO): 1 basic, 2 leading, 3 top;
   - the Norwegian Register (NO): 1 standard, 2 high level.

   A journal on neither list is flagged. The OpenAlex "core source" flag was not used, because it also marks a low-quality journal in this set. Before the report, the team should confirm Scopus or Web of Science indexing for the studies it selects, in its own browser at https://www.scimagojr.com or https://mjl.clarivate.com.

## 2. What the check found

- **No fake or mis-cited records:** every DOI resolves to the title we hold.
- **Shortlist status (45):**
  - 19 journal papers, including three first found as preprints: R00637 and R00220, now in the Journal of Computational Physics 2026, and R00504, now in the Journal of Computational Science;
  - 5 conference papers;
  - 18 preprints, one of which (R00244) has a probable journal version in Chaos, Solitons & Fractals;
  - 3 theses.
- **Top-rated venues (JUFO 3):** Nature Communications, Science Advances, SIAM Journal on Scientific Computing, IEEE Transactions on Power Electronics, Medical Image Analysis, Materials & Design, and Water Research (reserve).
- **Leading (JUFO 2):** Journal of Computational Physics.
- **Weak or unrated venues to treat with care:**
  - AI Thermal Fluids (R02561): a new Elsevier journal, not yet rated.
  - Journal of Computing and Electronic Information Management (R02608, reserve): not on either list; small publisher.
  - PAMM (R01518): JUFO 1, but a proceedings-style journal with low citation rates.
  - The conference papers outside ISSCC (NO 1) and ICCAD: ICAIBD, CODS-COMAD, ECMOR, ICSPC, SBCAS and the PSE proceedings are on no list.
- **FEVessel (R00643) is not published yet.** Its PDF uses the International Journal for Numerical Methods in Engineering template with blank received and accepted dates. Treat it as a submitted manuscript.
- **Search sensitivity note.** Zhang et al. 2026 cites Sacchetti et al. 2022 (IEEE Access, DOI 10.1109/access.2022.3160186), a PINN-versus-FEM comparison across fidelities. Our searches did not retrieve it, because its title and abstract use "neural networks" without our cost or energy terms. It is a single-solve comparison (exclusion code E5), so it would not change a gap verdict. It is worth adding to the literature section as context.

## 3. Full texts read (targeted reading for cost, hardware, accuracy and break-even)

Full texts came only from legal open-access copies. Each was stored in its own folder under the ignored `downloads/`, with its SHA-256 in `outputs/systematic-review/fulltext_manifest.json`, then read through `scripts/to_markdown.py`. Page numbers are PDF pages of the arXiv copy. Check each number on the original page before the report quotes it.

| ID | Study (status, venue) | Model and training | Classical baseline and hardware | Cost and break-even (locator) | Energy | Accuracy basis | Effect on our gaps |
|---|---|---|---|---|---|---|---|
| R00383 | Li, Jiang, Song 2026 (preprint) | Parametric PINN with 4 geometry inputs, physics-only loss (p21) | COMSOL 6.3 FEM, 2.3 × 10^6 elements, 56 Xeon cores; PINN on one RTX 4090D (p13, p17) | Training 3 h 40 min; 9.3 ms against 122.53 s per design; break-even after about 108 designs by wall-clock, about 24 by rental price (p17, Fig. 8) | None | PINN error 8.1% / 5.6% against FEM reference; not matched | **Falsifies the broad GC2.** Narrowed GC2 holds: not matched accuracy, different hardware, no energy, no seeds |
| R00643 | Sun et al. 2026 (submitted manuscript) | Label-free Transolver trained on total potential energy | AMG-preconditioned CG at 1e-3; RTX 5090 against Ryzen 9 9950X (p5, Table 2) | Training 29.4 h; 0.0130 s against 2.30 s per case; warm start 9.2 times end-to-end (Table 2, abstract). No break-even stated; our arithmetic gives about 4.6 × 10^4 queries | None | 1.35% displacement error; baseline at stated tolerance | Supports narrowed GC2; efficient baseline example |
| R00692 | Cao et al. 2025 (EACFM journal; arXiv read) | Parametric TSONN, physics-trained, no labels | CFD timing not found by keyword search; RTX 4090 (p9) | Parametric training 4.6 days, about 40 single-flow solves (p1) | None | Lift and drag errors 1.7-4.4% | Gives S_P for parametric against single-problem training |
| R00504 | Winkler and Stoll 2026 (J. Comput. Sci., 2027 issue; arXiv read) | Eight supervised surrogates | FE solver on CPU against GPU surrogates (p11) | Q* = (N_train t_FEM + t_train)/(t_FEM - t_infer), Eqs. 26-27 (p11); configuration search "not charged" | None | Per-QoI errors; three seeds | Same cost model as ours; supervised; no energy |
| R00627 | Zhang et al. 2026 (preprint) | Four supervised and four foundation models | Error-matched lower-fidelity classical solver on the same GPU (p2-5) | Data, training and tuning counted (p1) | None; power suggested for CPU cases (p5) | Error-matched | Method standard for matched accuracy; no PINN |
| R00718 | Luo et al. 2025 (SIAM J. Sci. Comput.; arXiv read) | Derivative-informed reduced-basis operator (supervised) | PDE-based optimization on 48 CPU cores; network on an A100 GPU (p12, p22) | 1-2 orders more cost-efficient after construction costs (abstract) | None | Optimization solution accuracy | Supervised; offline cost counted |
| R00637 | Roohi 2026 (J. Comput. Phys.; arXiv read) | Supervised neural closure in a GPU particle solver | Cubic Fokker-Planck closure, GPU-native | Break-even about 20 runs (training only) and about 55 runs (data plus training) (Table 13, p31; p48) | None | Closure fidelity audits | Hybrid; break-even in runs |
| R01145 | Eivazi et al. 2026 (J. Comput. Phys.; arXiv read) | Physics-informed operator with hard equilibrium, trained on FE data | FE² multiscale simulations | Speedup over 8000-fold against FE² (abstract; Table 4, p19) | None | Against FE² reference | Per-simulation speedup; training cost not checked |
| R00220 | Garg et al. 2026 (J. Comput. Phys.; arXiv read) | Spiking PINN | No classical cost comparison | n/a | Modeled from synaptic-operation counts (Sec. 2.1, p5-7); not measured | PDE benchmarks | Does not touch GC1 (estimate, no classical side) |
| R01555 | Jediný 2025 (bachelor's thesis, Charles University; repository PDF) | Single-problem PINN, 3 × 128 GELU; one run per setting (p40) | Strang-split ADI FDM on one Xeon E5-2650 v3 core; PINN on a T4 GPU (p28, p36) | Training 1253 s, 117 kJ; break-even at N = 1253 (time) and N = 1303 (energy) grid points per dimension, from polynomial fits extrapolated beyond N = 300 (p38) | Estimated: utilization times TDP, integrated over time (p25) | Agreement with FDM, MSE 2.12 × 10⁻⁷ (p40) | GC1 holds only as "metered"; falsifies the broad GC3 |
| R01457 | Tandale and Stoffel 2024 (Engineering with Computers; publisher PDF) | Spiking network inside an in-house Python FE solver | Same FE solver without the network | 18-41% faster than classical FE, called conjectural by the authors (p21) | Per forward pass, modelled with KerasSpiking across CPU, GPU and Loihi (p27); no FEM energy | FE solution | Does not falsify GC1 (no network-against-FEM energy) |
| R03090 | Xue et al. 2026 (Nature Communications; publisher PDF) | Physics-constrained neural operator trained on 7350 CMG-STARS samples (p2-3) | CMG-STARS on a Ryzen 9 5950X; operator on an A100 (p9) | 1050 cases in about 310 s against about 7380 min; excludes "the effort to construct the model" (p9) | None | Test-set errors | Supports GC4: speedup without training or data cost |

Page numbers for R01555, R01457 and R03090 are PDF pages of the original documents.

Read earlier for the project (see the notes in `references/`): Huang et al. 2026 (R00670), Huang and Stuart 2026 (R00657), Kapoor et al. 2025 (R00177), Wilson et al. 2025 (R00810), Yoo et al. 2026 (R02174).

**Not read in full:**

- **Blocked:** the publisher refused automated access. On a second attempt through the app's built-in browser, each showed a "confirm you are human" check, which was not completed or bypassed:
  - R02880 Buoso et al. 2021, R01189 Wang et al. 2026 and R02939 Würth et al. 2023 (ScienceDirect);
  - R01850 Lee et al. 2026 (Wiley);
  - R00895 Srinivasan et al. 2025 (ACM).

  All are open access to a human reader. A team member can download the PDFs in a normal browser into `downloads/<name>/`, and they will be read the same way. R01555, R01457 and R03090, blocked on the first attempt, were fetched through the built-in browser on 2026-11-26 and read (table above).
- **Closed access, abstract only:** R03662 (ISSCC 2024), R01955 (ICAIBD 2026), R03609 (ICCAD 2023), R00993, R03325, R02483, R01247.

## 4. All 55 studies

The quality column lists JUFO and Norwegian levels. "n/a" means a preprint or thesis. The same data, with empty scoring columns, is in [team-selection.csv](team-selection.csv).

| List | ID | Year | Identity check | Status | Venue | Quality lists | Full text | Note |
|---|---|---|---|---|---|---|---|---|
| shortlist | [R00627](https://doi.org/10.48550/arxiv.2605.15399) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read (full text) |  |
| shortlist | [R00670](https://doi.org/10.48550/arxiv.2610.32911) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read earlier (project note) |  |
| shortlist | [R00657](https://doi.org/10.48550/arxiv.2609.24021) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read earlier (project note) |  |
| shortlist | [R00177](https://doi.org/10.48550/arxiv.2505.12556) | 2025 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read earlier (project note) |  |
| shortlist | [R00504](https://doi.org/10.48550/arxiv.2607.23667) | 2026 | arXiv ok (1.0) | journal (published version found) | arXiv | JUFO 1, NO 1 (journal version) | read (full text) | published: Journal of Computational Science (10.1016/j.jocs.2026.103075, 2027 issue) |
| shortlist | [R00383](https://doi.org/10.48550/arxiv.2611.10666) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read (full text) |  |
| shortlist | [R00692](https://doi.org/10.1080/19942060.2025.2559110) | 2025 | Crossref ok (1.0) | journal | Engineering Applications of Computational... | JUFO 1, NO 1 | read (full text) | published: Engineering Applications of Computational Fluid Mechanics 2025 (arXiv 2501.01165 read) |
| shortlist | [R01189](https://doi.org/10.1016/j.csite.2026.108226) | 2026 | Crossref ok (1.0) | journal | Case Studies in Thermal Engineering | JUFO 1, NO 1 | not retrievable (publisher block) |  |
| shortlist | [R01457](https://doi.org/10.1007/s00366-024-01967-3) | 2024 | Crossref ok (1.0) | journal | Engineering with Computers | JUFO 1, NO 1 | read (full text, publisher PDF) | [note](../../references/tandale-2024-spiking-fem.md) |
| shortlist | [R01555](https://openalex.org/W7135832291) | 2025 | repository record only | thesis | Digital Repository (National Repository of... | n/a (thesis) | read (full text, repository PDF) | bachelor thesis, Charles University 2025 (F. Jediný); [note](../../references/jediny-2025-pinn-fdm-plasma-thesis.md) |
| shortlist | [R02880](https://doi.org/10.1016/j.media.2021.102066) | 2021 | Crossref ok (1.0) | journal | Medical Image Analysis | JUFO 3, NO 1, CCF C | not retrievable (publisher block) |  |
| shortlist | [R03662](https://doi.org/10.1109/isscc49657.2024.10454502) | 2024 | Crossref ok (1.0) | conference | 2024 IEEE International Solid-State Circuits... | NO 1 (ISSCC) | closed access, abstract only |  |
| shortlist | [R00018](https://doi.org/10.1126/sciadv.abi8605) | 2021 | Crossref ok (1.0) | journal | Science Advances | JUFO 3, NO 2 | abstract only |  |
| shortlist | [R00244](https://doi.org/10.48550/arxiv.2512.24634) | 2025 | arXiv ok (1.0) | preprint (probable journal version) | arXiv | JUFO 1, NO 1 (probable journal version) | abstract only | probable published version: Chaos, Solitons & Fractals (10.1016/j.chaos.2026.118646; title differs slightly) |
| shortlist | [R00319](https://doi.org/10.48550/arxiv.2608.19209) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R00598](https://doi.org/10.48550/arxiv.2511.18260) | 2025 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only | also on SSRN (posted content), no journal version found |
| shortlist | [R00614](https://doi.org/10.48550/arxiv.2603.03211) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R00637](https://doi.org/10.1016/j.jcp.2026.115261) | 2026 | Crossref ok (1.0) | journal | Journal of Computational Physics | JUFO 2, NO 2 | read (full text) | published: Journal of Computational Physics 2026 (arXiv 2606.15622 read) |
| shortlist | [R00643](https://doi.org/10.48550/arxiv.2607.17318) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read (full text) | preprint in IJNME template, dates blank; no journal version found |
| shortlist | [R00649](https://doi.org/10.48550/arxiv.2608.23075) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R00718](https://doi.org/10.1137/23m157956x) | 2025 | Crossref ok (1.0) | journal | SIAM Journal on Scientific Computing | JUFO 3, NO 2 | read (full text) | published: SIAM J. Sci. Comput. 2025 (arXiv 2305.20053 read) |
| shortlist | [R00807](https://doi.org/10.31224/8628) | 2026 | Crossref ok (1.0) | preprint |  | n/a | abstract only | preprint, engrXiv (Crossref posted content) |
| shortlist | [R00810](https://doi.org/10.48550/arxiv.2509.24517) | 2025 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read earlier (project note) |  |
| shortlist | [R00895](https://doi.org/10.1145/3799830.3799865) | 2025 | Crossref ok (1.0) | conference | Proceedings of the 13th ACM IKDD... | not listed (ACM CODS-COMAD) | not retrievable (publisher block) |  |
| shortlist | [R00993](https://doi.org/10.1080/10407790.2024.2325648) | 2024 | Crossref ok (1.0) | journal | Numerical Heat Transfer, Part B: Fundamentals | JUFO 1, NO 1 | closed access, abstract only |  |
| shortlist | [R01247](https://doi.org/10.1063/5.0356861) | 2026 | Crossref ok (1.0) | journal | Physics of Fluids | JUFO 1, NO 1 | closed access, abstract only |  |
| shortlist | [R01850](https://doi.org/10.1002/aisy.202501108) | 2026 | Crossref ok (1.0) | journal | Advanced Intelligent Systems | JUFO 1, NO 1 | not retrievable (publisher block) |  |
| shortlist | [R01955](https://doi.org/10.1109/icaibd69640.2026.11637284) | 2026 | Crossref ok (1.0) | conference | 2026 9th International Conference on... | not listed (IEEE ICAIBD) | closed access, abstract only |  |
| shortlist | [R02174](https://doi.org/10.48550/arxiv.2609.30580) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | read earlier (project note) |  |
| shortlist | [R02483](https://doi.org/10.3997/2214-4609.202637152) | 2026 | Crossref ok (1.0) | conference | ECMOR 2026 | not listed (EAGE ECMOR) | closed access, abstract only |  |
| shortlist | [R03325](https://doi.org/10.1109/tpel.2025.3547390) | 2025 | Crossref ok (1.0) | journal | IEEE Transactions on Power Electronics | JUFO 3, NO 2 | closed access, abstract only |  |
| shortlist | [R03609](https://doi.org/10.1109/iccad57390.2023.10323696) | 2023 | Crossref ok (1.0) | conference | 2023 IEEE/ACM International Conference on... | no list data (IEEE/ACM ICCAD) | closed access, abstract only |  |
| shortlist | [R00092](https://doi.org/10.48550/arxiv.2401.00413) | 2023 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R00220](https://doi.org/10.1016/j.jcp.2026.115161) | 2025 | Crossref ok (1.0) | journal | Journal of Computational Physics | JUFO 2, NO 2 | read (full text) | published: Journal of Computational Physics 2026 (arXiv 2511.06081 read) |
| shortlist | [R00235](https://doi.org/10.48550/arxiv.2512.09202) | 2025 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R00275](https://doi.org/10.48550/arxiv.2603.21674) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R01518](https://doi.org/10.1002/pamm.202400066) | 2024 | Crossref ok (1.0) | journal | PAMM | JUFO 1, NO 1 | abstract only |  |
| shortlist | [R01786](https://openalex.org/W7162611103) | 2026 | repository record only | thesis | DR-NTU (Nanyang Technological University) | n/a (thesis) | abstract only | thesis, NTU repository; not verified beyond the record |
| shortlist | [R01799](https://doi.org/10.18419/opus-19222) | 2026 | repository record only | thesis |  | n/a (thesis) | abstract only | thesis, Univ. Stuttgart OPUS (DataCite DOI 10.18419/opus-19222) |
| shortlist | [R00370](https://doi.org/10.48550/arxiv.2609.33387) | 2026 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
| shortlist | [R03090](https://doi.org/10.1038/s41467-026-73183-0) | 2026 | Crossref ok (1.0) | journal | Nature Communications | JUFO 3, NO 2 | read (full text, publisher PDF) | [note](../../references/xue-2026-geothermal-operator.md) |
| shortlist | [R01145](https://doi.org/10.1016/j.jcp.2026.114745) | 2026 | Crossref ok (1.0) | journal | Journal of Computational Physics | JUFO 2, NO 2 | read (full text) | published: Journal of Computational Physics 2026 (arXiv 2504.07976 read) |
| shortlist | [R02939](https://doi.org/10.1016/j.matdes.2023.112034) | 2023 | Crossref ok (1.0) | journal | Materials & Design | JUFO 3, NO 1 | not retrievable (publisher block) |  |
| shortlist | [R02666](https://doi.org/10.1021/acs.iecr.6c02300) | 2026 | Crossref ok (1.0) | journal | Industrial & Engineering Chemistry Research | JUFO 1, NO 2 | abstract only |  |
| shortlist | [R02561](https://doi.org/10.1016/j.aitf.2026.100042) | 2026 | Crossref ok (1.0) | journal | AI Thermal Fluids | not on JUFO/NO lists | abstract only |  |
| reserve | [R00750](https://doi.org/10.1515/polyeng-2024-0228) | 2025 | Crossref ok (1.0) | journal | Journal of Polymer Engineering | JUFO 1, NO 1 | abstract only |  |
| reserve | [R00780](https://doi.org/10.1016/j.rineng.2026.110582) | 2026 | Crossref ok (1.0) | journal | Results in Engineering | JUFO 1, NO 1 | abstract only |  |
| reserve | [R02184](https://doi.org/10.1002/pamm.70245) | 2026 | Crossref ok (1.0) | journal | Proceedings in Applied Mathematics and Mechanics | JUFO 1, NO 1 | abstract only |  |
| reserve | [R02608](https://doi.org/10.54097/q4brzy12) | 2026 | Crossref ok (1.0) | journal | Journal of Computing and Electronic... | not on JUFO/NO lists | abstract only |  |
| reserve | [R02724](https://doi.org/10.1016/j.watres.2026.127290) | 2026 | Crossref ok (1.0) | journal | Water Research | JUFO 3, NO 2 | abstract only |  |
| reserve | [R02862](https://doi.org/10.69997/pse.127236) | 2026 | Crossref ok (1.0) | conference | Proceedings of the 3rd Foundations of... | not listed (PSE proceedings) | abstract only |  |
| reserve | [R03112](https://doi.org/10.4208/cicp.oa-2025-0152) | 2026 | Crossref ok (1.0) | journal | Communications in Computational Physics | JUFO 1, NO 1 | abstract only |  |
| reserve | [R03386](https://doi.org/10.1117/12.3077052) | 2025 | Crossref ok (1.0) | conference | International Conference on Signal... | not listed (SPIE ICSPC) | abstract only |  |
| reserve | [R03460](https://doi.org/10.5753/sbcas_estendido.2026.21588) | 2026 | Crossref ok (1.0) | conference | Anais Estendidos do XXVI Simpósio Brasileiro... | not listed (SBCAS extended) | abstract only |  |
| reserve | [R00218](https://doi.org/10.48550/arxiv.2511.04576) | 2025 | arXiv ok (1.0) | preprint | arXiv | n/a (preprint) | abstract only |  |
