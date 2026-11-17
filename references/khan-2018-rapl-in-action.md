# Khan et al. (2018): RAPL in Action

## Source

- Title: RAPL in Action (as listed in Crossref)
- Authors: Kashif Nizam Khan, Mikael Hirki, Tapio Niemi, Jukka K. Nurminen, Zhonghong Ou
- Year and publication or preprint version: 2018, ACM Transactions on Modeling and Performance Evaluation of Computing Systems 3(2):1-26 (online 2018-03-22)
- DOI or source URL: https://doi.org/10.1145/3177754 ; open copy http://hdl.handle.net/10138/321707
- Date checked: 2026-11-17
- Reader: Claude (AI agent, automated literature check); not yet independently read by a human member
- Access: Crossref metadata and abstract (via OpenAlex). Full text not read. A subtitle may exist on the published PDF; confirm the full title before the report.
- Local file or approved storage location and SHA-256, if downloaded: not downloaded

OpenAlex cited_by_count 472 (checked 2026-11-17).

## Question and setting

Strengths and weaknesses of Intel's RAPL interface for CPU and DRAM energy, using microbenchmarks, three application benchmarks (Stream, Stress-ng, ParFullCMS), production power data from the Taito cluster, and replication on Amazon EC2.

## Claims we may use

- RAPL readings "are highly correlated with plug power, promisingly accurate enough, and have negligible performance overhead". Abstract.
- RAPL provides "accurate energy readings for CPUs and DRAM". Abstract.

## Relevance to this project

Peer-reviewed support for using RAPL as the CPU and DRAM counter inside our measurement boundary, for both the classical solver and the CPU side of the PINN. "Correlated with plug power" is not "equal to whole-machine power", so our rule stands: RAPL readings are labeled as CPU package and DRAM, not machine electricity.

## Check status and gaps

Venue, volume, issue, pages, and DOI confirmed in Crossref. The paper's documented weaknesses (update interval, overflow, platform differences) were not read; read them before the pilot energy check, since they set how we sample and integrate RAPL counters.
