"""case04 Series Convergence - 数列无穷累积极限收敛"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def partial_sum(n):
    return 1 - 1 / (2 ** n)


def plot_series_frame(max_n, idx):
    fig, ax = new_figure(width=7, height=5)
    ns = np.arange(1, max_n + 1)
    sns = np.array([partial_sum(k) for k in ns])
    ax.scatter(ns, sns, color="#4078c0", zorder=3)
    ax.axhline(y=1, linestyle="--", color="#f08000", label="收敛值 = 1")
    ax.set_xlim(0, max(max_n + 1, 33))
    ax.set_ylim(0, 1.1)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Series partial sum, n up to {max_n}", fontsize=12)
    ax.set_xlabel("n")
    ax.set_ylabel("$S_n$")
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{max_n}.png")


def plot_bar():
    fig, ax = new_figure(width=7, height=5)
    n = 8
    xs = np.arange(1, n + 1)
    terms = 1 / (2 ** xs)
    ax.bar(xs, terms, color="#4078c0", alpha=0.6)
    ax.set_xlim(0, n + 1)
    ax.set_ylim(0, 0.6)
    ax.grid(True, alpha=0.3)
    ax.set_title("Individual term sizes")
    add_watermark(ax)
    save_fig(fig, "series_bar.png")


if __name__ == "__main__":
    for i, nv in enumerate([1, 2, 4, 8, 16, 32]):
        plot_series_frame(nv, i)
    plot_bar()
