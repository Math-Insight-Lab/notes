"""case15 Piecewise Integral - 分段函数分段积分"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f_piecewise(x):
    result = np.zeros_like(x)
    mask1 = x <= np.pi
    mask2 = (x > np.pi) & (x <= 2 * np.pi)
    result[mask1] = np.sin(x[mask1])
    result[mask2] = np.sin(x[mask2])
    return result


def plot_piecewise_regions():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ys = f_piecewise(xs)
    ax.plot(xs, ys, color="#222", lw=2)
    ax.fill_between(xs[xs <= np.pi], 0, ys[xs <= np.pi], color="#4078c0", alpha=0.4, label="Region 1 (+)")
    ax.fill_between(xs[(xs > np.pi) & (xs <= 2 * np.pi)], 0, ys[(xs > np.pi) & (xs <= 2 * np.pi)], color="#e53935", alpha=0.4, label="Region 2 (-)")
    ax.set_xlim(-0.2, 2 * np.pi + 0.2)
    ax.set_ylim(-0.5, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    ax.axvline(x=np.pi, color="#f08000", lw=1, linestyle="--")
    ax.legend()
    ax.set_title("Piecewise integral with sign", fontsize=14)
    add_watermark(ax)
    save_fig(fig, "piecewise_regions.png")


def plot_cumulative():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ys = f_piecewise(xs)
    ax.plot(xs, ys, color="#222", lw=2, label="f(x)")
    ax.fill_between(xs, 0, ys, color="#4078c0", alpha=0.3)
    ax.set_xlim(-0.2, 2 * np.pi + 0.2)
    ax.set_ylim(-0.5, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    ax.set_title("Positive and negative regions", fontsize=14)
    add_watermark(ax)
    save_fig(fig, "cumulative.png")


if __name__ == "__main__":
    plot_piecewise_regions()
    plot_cumulative()
