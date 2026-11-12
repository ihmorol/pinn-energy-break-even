# Henderson et al. (2020): Systematic reporting of energy and carbon footprints

## Source

- Title: Towards the Systematic Reporting of the Energy and Carbon Footprints of Machine Learning
- Authors: Peter Henderson, Jieru Hu, Joshua Romoff, Emma Brunskill, Dan Jurafsky, Joelle Pineau
- Year and publication or preprint version: 2020, Journal of Machine Learning Research 21(248):1-43; preprint arXiv:2002.05651v2
- DOI or source URL: https://www.jmlr.org/papers/v21/20-312.html (JMLR assigns no DOI)
- Date checked: 2026-11-12
- Reader: ZCode AI agent (automated literature check); not yet independently read by a human member
- Access: full text read via ar5iv HTML
- Local file: `downloads/henderson-2020-energy-reporting/henderson-2020-energy-reporting.pdf`, SHA-256 798ac1ea89ea43b4db1e44d5e4306b80b4cab1db54421236402630f31de08411

OpenAlex cited_by_count 484 (checked 2026-11-12).

## Question and setting

A framework and tooling paper for measuring and reporting ML energy use and carbon emissions, demonstrated on NLP, RL, and speech workloads. It distinguishes direct per-component power measurement (Intel RAPL with the powercap interface or Intel PowerGadget for CPU/DRAM, nvidia-smi for GPU, psutil for per-process CPU utilization), per-process attribution on shared machines, PUE adjustment for facility overhead, and conversion to carbon with grid intensity data.

## Claims we may use

- Measurement tooling anchor: "We currently use Intel's RAPL tool with the powercap interface ... or Intel's PowerGadget Tool (depending on availability) to gather CPU/DRAM power draw and Nvidia's nvidia-smi ... for GPU power draw." Section 4.3.1.
- Estimates from partial information are unreliable: "without detailed accounting, it is easy to severely over- or underestimate carbon or energy emissions by extrapolating from partial information." Sections 5.2 and 6.
- FLOPs are a poor proxy: energy is essentially uncorrelated with FLOPs-based efficiency across architectures (R^2 = 0.083), though ordering holds within one architecture family. Section 5.1.
- Reporting protocol: log hardware, package versions, tool version, grid region, start and end times, keep raw data, and publish a Carbon Impact Statement. Section 7.5.
- Region choice can change emissions by up to about 30x for the same compute. Section 6.2.

## Relevance to this project

This paper is the template for our measurement section. It justifies our rules that readings come from hardware counters where available, that device readings are not whole-machine electricity without stated coverage, that modeled values are labeled, and that setup, training, and query phases are logged separately with units and sources. Our experiment records and study-energy ledger mirror its logging list.

## Check status and gaps

JMLR volume and article verified from the JMLR page (21(248):1-43, 2020). Full text read in HTML form. Gaps: none blocking. When writing our protocol, re-check the exact RAPL coverage statement (CPU package versus DRAM versus whole socket) before claiming counter coverage.
