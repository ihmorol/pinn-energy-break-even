# Strubell, Ganesh, McCallum (2019): Energy and policy considerations for deep learning in NLP

## Source

- Title: Energy and Policy Considerations for Deep Learning in NLP
- Authors: Emma Strubell, Ananya Ganesh, Andrew McCallum
- Year and publication or preprint version: 2019, Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL 2019), Florence, pp. 3645-3650
- DOI or source URL: https://doi.org/10.18653/v1/P19-1355 ; PDF at https://aclanthology.org/P19-1355.pdf
- Date checked: 2026-11-12
- Reader: ZCode AI agent (full text read via the ACL Anthology PDF during the automated literature check); not yet independently read by a human member
- Access: full text read
- Local file: `downloads/strubell-2019-energy-policy/strubell-2019-energy-policy.pdf`, SHA-256 184c42b148a3db99f4a59ed8336c403dc2229bf3100bbc934212116acd8c61d9

OpenAlex cited_by_count 5,005 (checked 2026-11-12). ACL Anthology ID is P19-1355; an earlier guess of D19-3003 was wrong (that ID is a different paper).

## Question and setting

The paper that made training cost a research-policy issue in NLP: it measures power draw during one-day trainings (nvidia-smi for GPU, Intel RAPL for CPU) and estimates total energy and CO2 for training and running common NLP models, using published training times, PUE 1.58, and an EPA grid factor of 0.954 lbs CO2e/kWh.

## Claims we may use

- The often-quoted 626,155 lbs CO2e figure (Table 3) is for a full neural architecture search (8x P100, 274,120 GPU hours, 656,347 kWh with PUE), a search over architectures, not a single training run; the five-car comparison comes from Table 1 (average car lifetime, 126,000 lbs).
- Single-run figures from the same table: about 192 lbs CO2e for one Transformer-big training, about 1,438 lbs for BERT-base on GPU.
- Its totals are modeled estimates: sampled power plus published training times, not whole-run integrated measurement. This is the canonical example of the measured-power-then-extrapolate pattern that our labeling rules distinguish from counter readings.

## Relevance to this project

Anchors the motivation section (energy became a reported cost in ML research) and supplies the canonical example of a modeled estimate built on sampled power, which is exactly the category our measurement boundary must label separately from counter readings.

## Check status and gaps

Anthology ID and DOI verified; full text read (tables transcribed as above). Gaps: none blocking. When quoting numbers, cite the specific table row, because the paper's figures are frequently misquoted without the search-versus-single-run distinction.
