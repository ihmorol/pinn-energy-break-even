# Rathore et al. (2024): Challenges in training PINNs, a loss landscape perspective

## Source

- Title: Challenges in Training PINNs: A Loss Landscape Perspective
- Authors: Pratik Rathore, Weimu Lei, Zachary Frangella, Lu Lu, Madeleine Udell
- Year and publication or preprint version: 2024, Proceedings of the 41st International Conference on Machine Learning (ICML 2024), PMLR 235 (stated on p. 1 of the PDF); preprint arXiv:2402.01868v2
- DOI or source URL: https://arxiv.org/abs/2402.01868
- Date checked: 2026-11-17
- Reader: Claude Code AI agent (targeted full-text read); not yet independently read by a human member
- Access: full text; Sections 2 to 7 and Appendix E read; theory (Section 8, Appendix F, G) not checked
- Local file: `downloads/rathore-2024-loss-landscape/rathore-2024-loss-landscape.pdf`, SHA-256 2f94074f9451b22a6141478b4d25a01a57614e3e0231cac9412dbbc545244722

## Question and setting

Why PINN losses are hard to minimize, and which optimizer works. Convection, reaction, and wave problems; tanh MLPs with three hidden layers of width 50, 100, 200, or 400; Xavier normal init, zero biases; 5 seeds per setting; 41,000 total iterations.

## Claims we may use

- Section 2: Adam learning rate tuned over {1e-5, ..., 1e-1}; L-BFGS with learning rate 1.0, memory 100, strong Wolfe line search; Adam+L-BFGS switch tested after 1,000, 11,000, or 31,000 iterations.
- Section 4 and Figure 2: lower final loss generally goes with lower L2 relative error; good solutions need near-zero loss.
- Section 5: the loss is ill-conditioned, and the differential operator in the residual is the cause (proved in Section 8).
- Section 6 and Figure 8: Adam+L-BFGS beats Adam alone and L-BFGS alone across widths after tuning.
- Section 6, Figure 4, and Figure 9 (Appendix E): L-BFGS often stops early because the line search finds no step that satisfies the strong Wolfe conditions, while the gradient norm is still around 1e-2 to 1e-3. Section 7: the authors' NysNewton-CG optimizer continues from that point.

## Relevance to this project

Supports the Adam then L-BFGS schedule and makes the switch point a frozen setting, not a free knob. The early-stop finding means our training code must record why L-BFGS stopped, and a stop is not proof of convergence. The ill-conditioning result also predicts that high-contrast conductivity settings will be harder to train. NysNewton-CG is outside what we plan to build; cite it as a known option only.

## Check status and gaps

Identifier, title, and authors confirmed via the arXiv API; venue read from the PDF front page, not yet checked against the PMLR index. The test PDEs are not diffusion problems; transfer to our case is our inference.
