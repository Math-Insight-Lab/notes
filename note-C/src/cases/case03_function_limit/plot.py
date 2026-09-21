"""case03 Function Limit - 函数趋近定点极限"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def f(x):
    if np.isclose(x, 1):
        return np.nan
    return (x ** 2 - 1) / (x - 1)


def plot_limit_frame(x_val, side_name, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-0.5, 2.5, 300)
    ys = np.array([f(t) for t in xs])
    ax.plot(xs, ys, color="#222", lw=2)
    ax.axhline(y=2, linestyle="--", color="#f08000", label="L=2")
    ax.plot(1, 2, marker="o", mfc="white", mec="#222", markersize=8)
    y_val = f(x_val)
    draw_dot(
        ax, x_val, y_val, color="#e53935", label=f"$x={x_val:.3f}$"
    )
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 4)
    ax.grid(True, alpha=0.3)
    ax.set_title(
        f"Limit: x approaching 1 from {side_name}", fontsize=12
    )
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{side_name}_{idx:02d}.png")


def plot_overview():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-0.5, 2.5, 300)
    ys = np.array([f(t) for t in xs])
    ax.plot(xs, ys, color="#222", lw=2)
    ax.axhline(y=2, linestyle="--", color="#f08000", label="L=2")
    ax.plot(1, 2, marker="o", mfc="white", mec="#222", markersize=8)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 4)
    ax.grid(True, alpha=0.3)
    ax.set_title("Left and Right Limits", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "limit_overview.png")


if __name__ == "__main__":
    for i, xv in enumerate([0, 0.5, 0.9, 0.99]):
        plot_limit_frame(xv, "left", i)
    for i, xv in enumerate([2, 1.5, 1.1, 1.01]):
        plot_limit_frame(xv, "right", i)
    plot_overview()
