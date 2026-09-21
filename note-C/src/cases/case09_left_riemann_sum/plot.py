"""case09 Left Riemann Sum - 左矩形求和逼近曲边面积"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return x ** 2


def plot_left_riemann(n, idx, a=0, b=2):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(a, b, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    dx = (b - a) / n
    x_rect = np.linspace(a, b, n + 1)
    approx_area = 0
    for i in range(n):
        xi = x_rect[i]
        yi = f(xi)
        rect = patches.Rectangle((xi, 0), dx, yi, color="#4078c0", alpha=0.4)
        ax.add_patch(rect)
        approx_area += yi * dx
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.set_ylim(0, f(b) + 0.2)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Left Riemann Sum, n={n}, area={approx_area:.3f}", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")


def plot_compare(n):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    dx = (2 - 0) / n
    x_rect = np.linspace(0, 2, n + 1)
    # Left sum
    for i in range(n):
        xi = x_rect[i]
        yi = f(xi)
        rect = patches.Rectangle((xi, 0), dx, yi, color="#4078c0", alpha=0.4, label="Left" if i == 0 else "")
        ax.add_patch(rect)
    # Right sum
    for i in range(n):
        xi = x_rect[i + 1]
        yi = f(xi)
        rect = patches.Rectangle((xi - dx, 0), dx, yi, color="#e53935", alpha=0.3, label="Right" if i == 0 else "")
        ax.add_patch(rect)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 4.5)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Left vs Right Riemann Sum, n={n}", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"compare_n{n}.png")


if __name__ == "__main__":
    for i, n in enumerate([4, 8, 16]):
        plot_left_riemann(n, i)
    for i, n in enumerate([4, 8]):
        plot_compare(n)
