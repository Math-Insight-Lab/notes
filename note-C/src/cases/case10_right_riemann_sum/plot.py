"""case10 Right Riemann Sum - 右矩形求和逼近曲边面积"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return x ** 2


def plot_right_riemann(n, idx, a=0, b=2):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(a, b, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    dx = (b - a) / n
    x_rect = np.linspace(a, b, n + 1)
    approx_area = 0
    for i in range(n):
        xi = x_rect[i + 1]
        yi = f(xi)
        rect = patches.Rectangle((xi - dx, 0), dx, yi, color="#e53935", alpha=0.4)
        ax.add_patch(rect)
        approx_area += yi * dx
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.set_ylim(0, f(b) + 0.2)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Right Riemann Sum, n={n}, area={approx_area:.3f}", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")


def plot_left_vs_right():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    n = 8
    dx = 2 / n
    x_rect = np.linspace(0, 2, n + 1)
    for i in range(n):
        xi = x_rect[i]
        yi_left = f(xi)
        rect = patches.Rectangle((xi, 0), dx, yi_left, color="#4078c0", alpha=0.3, label="Left" if i == 0 else "")
        ax.add_patch(rect)
    for i in range(n):
        xi = x_rect[i + 1]
        yi_right = f(xi)
        rect = patches.Rectangle((xi - dx, 0), dx, yi_right, color="#e53935", alpha=0.3, label="Right" if i == 0 else "")
        ax.add_patch(rect)
    true_area = 8 / 3
    ax.axhline(y=0, color="none")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 4.5)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Left vs Right Riemann, n={n}", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "left_right_compare.png")


def plot_convergence():
    fig, ax = new_figure(width=6, height=4)
    ns = [4, 8, 16, 32, 64]
    left_sums, right_sums = [], []
    for n in ns:
        dx = 2 / n
        lr = sum(f(2 * i / n) * dx for i in range(n))
        rr = sum(f(2 * (i + 1) / n) * dx for i in range(n))
        left_sums.append(lr)
        right_sums.append(rr)
    ax.plot(ns, left_sums, marker="o", color="#4078c0", label="Left", lw=2)
    ax.plot(ns, right_sums, marker="s", color="#e53935", label="Right", lw=2)
    ax.axhline(y=8/3, linestyle="--", color="#f08000", label="True = 2.67")
    ax.set_xlabel("n")
    ax.set_ylabel("Sum")
    ax.set_title("Left vs Right convergence")
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "convergence.png")


if __name__ == "__main__":
    for i, n in enumerate([4, 8, 16]):
        plot_right_riemann(n, i)
    plot_left_vs_right()
    plot_convergence()
