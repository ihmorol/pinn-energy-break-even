# Reddi et al. (2024): MLPerf Power benchmarking methodology

## Source

- Title: MLPerf Power: Benchmarking the Energy Efficiency of Machine Learning Systems from Microwatts to Megawatts for Sustainable AI
- Authors: Vijay Janapa Reddi and the MLPerf Power working group (industry consortium; confirm the full author list from the PDF before citing)
- Year and publication or preprint version: preprint arXiv:2410.12032v2 (2024-10-15); published at IEEE International Symposium on High-Performance Computer Architecture (HPCA) 2025
- DOI or source URL: https://arxiv.org/abs/2410.12032
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: abstract and verified metadata; preprint PDF stored locally
- Local file: `downloads/mlperf-power-2024/mlperf-power-2024.pdf`, SHA-256 865ab1673906550ab1500f93132c4761666581c94bc96e84ab75664f27598ec2

OpenAlex: 103 citing works; venue recorded as HPCA 2025 (checked 2026-11-12).

## Question and setting

Benchmarking methodology for ML energy efficiency across system scales, developed by more than 20 organizations. Establishes rules and best practices so energy measurements are comparable across architectures; reports 1,841 reproducible measurements from 60 systems using MLPerf workloads.

## Claims we may use

- Standardized power-measurement rules (defined measurement points, procedures, and reporting) are what make energy numbers comparable across systems; MLPerf Power codifies them. Abstract.
- Energy efficiency is treated as a key metric alongside performance. Abstract framing.

## Relevance to this project

A recent, industry-backed reference for measurement discipline. We will not run MLPerf workloads, but its rule structure supports our protocol choices: fixed measurement boundary, stated sampling, warm-up, repetition, and reporting of units and counter coverage in every run record.

## Check status and gaps

Preprint verified via the arXiv API; venue verified via OpenAlex. Gaps: abstract-level access only; the author list and the exact HPCA citation details must be transcribed from the PDF before the final report. Note in the report that this is methodology context, not a PDE result.
