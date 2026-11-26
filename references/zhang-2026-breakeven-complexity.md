# Zhang et al. (2026): breakeven complexity of neural PDE solvers

## Source

- Title: Breakeven complexity: A new perspective on neural partial differential equation solvers
- Authors: Yijing Zhang (University of Wisconsin-Madison), Nicholas Roberts (Princeton University), and co-authors (full list in the PDF)
- Year and publication or preprint version: 2026 preprint, arXiv:2605.15399. No published version found in Crossref on 2026-11-26.
- DOI or source URL: https://doi.org/10.48550/arxiv.2605.15399
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown. An earlier read through arXiv HTML is cited in [gap-evidence.md](../docs/gap-evidence.md). Not yet read by a human member.
- Access: full text (arXiv PDF)
- Local file: `downloads/zhang-2026-breakeven-complexity/zhang-2026-breakeven-complexity.pdf`, SHA-256 7476b72fdb19c7972079d150744b3bdc8bb2029b27f893905afdcb5e2b55cc03

## Question and setting

The paper defines "breakeven complexity": the number of forward solves before a learned solver is cheaper than an error-matched classical solver (abstract; p2).

- **Classical comparator:** a lower-fidelity classical solver run at the same error as the learned model (p3-4).
- **Models:** eight, four supervised solvers and four foundation models (p2).
- **Benchmarks:** three APEBench PDEs and a PyFR multi-obstacle flow benchmark.
- **Up-front cost counted:** data generation, training and tuning (p1).
- **Hardware:** the same GPU hardware for both sides (p5). The authors suggest a monetary or power-usage comparison when the classical side must run on CPU (p5).

## Claims we may use

- Neural solver cost must include up-front costs for data generation, training and tuning (p1).
- The comparison uses an error-matched classical solver, not a fixed high-fidelity reference (p2-4).
- Both sides run on the same hardware with high GPU utilization (p5).
- Breakeven complexity depends on hardware and on how good the classical solver is (p10, limitations).
- Varying-fidelity classical comparisons "has been done for PINNs [26, 10]". These are Sacchetti et al. 2022 (IEEE Access) and Grossmann et al. 2024, both single-solve studies (p2; references [10] and [26]).

## Relevance to this project

This is the methodological standard closest to our plan: matched accuracy by an error-matched classical solver, the same hardware, and tuning counted. It does not test a physics-trained PINN, and it measures no energy. Our study adds both.

## Check status and gaps

- Full author list and per-benchmark break-even values not yet recorded; read Section 5 before citing numbers.
