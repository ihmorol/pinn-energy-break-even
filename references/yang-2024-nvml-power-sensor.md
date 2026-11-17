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

## Preprint full-text check, 2026-11-17

Reader: Claude Code AI agent; targeted read of the methods, setup, and cost passages through the Markdown cache (`scripts/to_markdown.py`). Not yet read by a human member. Source: arXiv:2312.02741v3, "Part-time Power Measurements: nvidia-smi's Lack of Attention", stored at `downloads/yang-2024-nvml-power-sensor/yang-2024-nvml-power-sensor.pdf`, SHA-256 b7d0013de1acc92094426e42377387f5cd9d4296f4dd9cf405cb044a609813a0. This is the preprint, not the SC24 text; wording and numbers may differ in the published version.

- Section 4: measured power update periods were mostly about 20 ms on a V100 and about 100 ms on an A100; nvidia-smi follows a load change one update later, with delays up to about 100 ms.
- Section 4.3: the reported value is a boxcar average whose window can be shorter than the update period on some GPUs, which is why part of the runtime goes unsampled.
- Section 5 good practice: run the target for 32 consecutive iterations or at least 5 seconds; insert controlled delays if the averaging window is short; run four trials with random delays between them; discard repetitions during the power rise time and shift the data to line up with GPU activity.
- Section 5: on nine benchmarks this practice cut the average energy error from 39.27% to 4.89% against an external power-measurement device.

Use for us: GPU query blocks must last at least 5 s and be repeated; short training phases (for example the Adam to L-BFGS switch) are hard to resolve on their own and are better measured inside the whole training window.
