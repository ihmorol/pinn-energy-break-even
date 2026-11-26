# Tandale and Stoffel (2024): spiking physics-based network inside an FE solver

## Source

- Title: Brain-inspired spiking neural networks in Engineering Mechanics: a new physics-based self-learning framework for sustainable Finite Element analysis
- Authors: Saurabh Balkrishna Tandale, Marcus Stoffel
- Year and publication: 2024, Engineering with Computers 40:2703-2738. Received 7 July 2023, accepted 4 March 2024, published online 12 April 2024.
- DOI: https://doi.org/10.1007/s00366-024-01967-3
- Date checked: 2026-11-26
- Reader: Claude Code AI agent; targeted read of the cached Markdown (abstract, Sections 6.4-6.5). Not yet read by a human member.
- Access: full text (Springer open-access PDF, fetched through the app's built-in browser)
- Local file: `downloads/tandale-2024-spiking-fem/tandale-2024-spiking-fem.pdf`, SHA-256 f86789865ed1f504c129c443769e2deb02e5578686c9e1b5de3315c580677d70

## Question and setting

A spiking recurrent network (SLMU) predicts plastic strain increments at Gauss points inside an in-house Python finite element solver for elasto-plastic plate structures.

## Claims we may use

- Runtime: the FE solution with the SLMU model was 41% faster, and with its non-spiking counterpart 29% faster, than the traditional FE solution for the first test case; about 33%, 30% and 18% for the later cases (p21). The authors call this speed comparison conjectural because it depends on their in-house solver (p21).
- Energy is per forward pass of the network, computed with KerasSpiking from published per-operation values for a CPU, a GPU and the Loihi chip, without deployment overhead. The authors say these values "should be held conjectural" (p27).
- Reduction factors: 1188 (Loihi against GPU) and 34,392 (Loihi against CPU) for the whole model (p27, Table 7); 111.55 and 3161.125 for the spiking layers on the Xylo-Av2 chip (p21-22, Tables 4-5).

## Relevance to this project

It doesn't falsify GC1. The energy comparison is between versions of the network on different hardware, not between the network-enhanced solver and classical FEM. The comparison with FEM is runtime only, and training cost is not part of it. It is useful context: an energy claim for a neural solver built on modelled per-operation energy.

## Check status and gaps

- Confirmed in the cached text: the runtime and energy statements above.
- Not settled: whether the Xylo-Av2 values in Tables 4-5 were measured on the chip or estimated; the passages read do not say.
