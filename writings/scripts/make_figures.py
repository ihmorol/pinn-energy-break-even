"""Build the paper figures that need no measured data.

breakeven-outcomes.pdf shows the four outcome classes with made-up shapes and
no axis values, so it cannot be read as a result. conductivity-family.pdf
plots the candidate k = 1 + mu1*x + mu2*y, which is a definition, not a solve.
Measured-result figures will be added only after the energy trials.

Run from the repository root:
    python -B -X utf8 writings/scripts/make_figures.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "shared" / "figures"
COL_W = 3.5  # IEEE two-column width in inches
PINN, FD = "#1f5fa8", "#c0392b"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "legend.fontsize": 7,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.2,
    "pdf.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})


def outcome_panel(ax, title, s_p, e_p, s_c, e_c, band=0.0, n_max=None):
    n = np.linspace(0, 1, 200)
    for s, e, color, name in ((s_p, e_p, PINN, "PINN"), (s_c, e_c, FD, "Classical")):
        y = s + e * n
        ax.plot(n, y, color=color, label=name)
        if band:
            ax.fill_between(n, y - band * (0.3 + n), y + band * (0.3 + n), color=color, alpha=0.15, lw=0)
    if n_max is not None:
        ax.axvspan(n_max, 1, color="0.88", lw=0)
        ax.text((n_max + 1) / 2, 0.06, "beyond\nmeasured\nrange", ha="center", va="bottom", fontsize=6, color="0.35")
    if e_c != e_p:
        n_star = (s_p - s_c) / (e_c - e_p)
        if 0 < n_star < 1:
            ax.plot([n_star], [s_p + e_p * n_star], "o", ms=3.5, mfc="white", mec="k", mew=0.8)
            ax.annotate(r"$N^\ast$", (n_star, s_p + e_p * n_star), xytext=(-12, 8),
                        textcoords="offset points", fontsize=8)
    ax.set_title(title, pad=3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([])
    ax.set_yticks([])


def fig_outcomes():
    fig, axes = plt.subplots(2, 2, figsize=(COL_W, 2.55), sharex=True, sharey=True)
    outcome_panel(axes[0, 0], "(a) Crossing in measured range", 0.45, 0.25, 0.05, 0.85)
    outcome_panel(axes[0, 1], "(b) One method cheaper throughout", 0.45, 0.45, 0.05, 0.40)
    outcome_panel(axes[1, 0], "(c) Uncertain crossing", 0.45, 0.30, 0.10, 0.75, band=0.08)
    outcome_panel(axes[1, 1], "(d) Extrapolated crossing", 0.55, 0.20, 0.05, 0.75, n_max=0.62)
    for ax in axes[1]:
        ax.set_xlabel("New parameter queries, $N$")
    for ax in axes[:, 0]:
        ax.set_ylabel("Cumulative energy")
    axes[0, 0].legend(loc="upper left", frameon=False, handlelength=1.5)
    fig.tight_layout(pad=0.3, h_pad=0.6, w_pad=0.4)
    fig.savefig(OUT / "breakeven-outcomes.pdf")
    plt.close(fig)


def fig_conductivity():
    x = np.linspace(0, 1, 201)
    xx, yy = np.meshgrid(x, x)
    cases = (((0.25, 0.25), "(a)"), ((-0.25, 0.25), "(b)"))
    fig, axes = plt.subplots(1, 2, figsize=(COL_W, 1.75), sharey=True)
    grid = np.linspace(0, 1, 9)[1:-1]
    gx, gy = np.meshgrid(grid, grid)
    for ax, ((m1, m2), tag) in zip(axes, cases):
        k = 1 + m1 * xx + m2 * yy
        im = ax.pcolormesh(xx, yy, k, cmap="viridis", vmin=0.5, vmax=1.5, shading="auto", rasterized=True)
        ax.plot(gx, gy, ".", color="white", ms=1.6)
        ax.set_title(f"{tag} $\\mu$ = ({m1:+.2f}, {m2:+.2f})".replace("-", "−"), pad=3)
        ax.set_aspect("equal")
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xlabel("$x$", labelpad=-6)
    axes[0].set_ylabel("$y$", labelpad=-4)
    cbar = fig.colorbar(im, ax=axes, fraction=0.046, pad=0.03)
    cbar.set_label("Conductivity, $k$")
    cbar.set_ticks([0.5, 1.0, 1.5])
    fig.savefig(OUT / "conductivity-family.pdf", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    fig_outcomes()
    fig_conductivity()
    print("wrote", *sorted(p.name for p in OUT.glob("*.pdf")))
