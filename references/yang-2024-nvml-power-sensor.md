# Yang, Adamek, Armour (2024): accuracy of NVIDIA's built-in power sensor

## Source

- Title: Accurate and Convenient Energy Measurements for GPUs: A Detailed Study of NVIDIA GPU's Built-In Power Sensor
- Authors: Zeyu Yang, Karel Adamek, Wesley Armour
- Year and publication or preprint version: 2024, SC24: International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 1-17; earlier preprint arXiv:2312.02741 ("Part-time Power Measurements: nvidia-smi's Lack of Attention")
- DOI or source URL: https://doi.org/10.1109/SC41406.2024.00028
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). No open-access copy of the SC24 version found; full text not read.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 77 (checked 2026-11-17). Previously listed in the shortlist as verified without a PDF; promoted to a note on 2026-11-17.

## Question and setting

How nvidia-smi derives its power readings and how accurate they are, tested on more than 70 GPUs across 12 architecture generations.

## Claims we may use

- The study found problems "that can lead to drastic under/overestimation of energy consumed"; for example, "on the A100 and H100 GPUs only 25% of the runtime is sampled". Abstract.
- The proposed mitigations "reduce the energy measurement error by an average of 35%" in the authors' test cases. Abstract.

## Relevance to this project

Our PINN training and queries will likely be measured through nvidia-smi or NVML. Short kernels and partial sampling can bias GPU joules, which would bias S_P and e_P and therefore N*. This paper is the reason to check the GPU model's sampling behavior in the pilot, use long enough query blocks, and apply its mitigations where they fit.

## Check status and gaps

Venue, pages, and DOI confirmed in Crossref. The specific mitigations, per-architecture behavior, and error figures were not read. A secondary source quoted the arXiv preprint as giving an error of ±5% rather than NVIDIA's ±5 W; that figure is not from the SC24 text we read, so do not cite it without checking. The "±5 W" GPU note in our Bengali review sits in its Henderson et al. section and is not from this paper.
