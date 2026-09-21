"""case02 Error Convergence - 细分数量递增误差收敛归零"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches


def f(x):
    return x ** 2


def plot_with_error(n, idx, a=0, b=2):
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
    true_area = b ** 3 / 3 - a ** 3 / 3
    err = true_area - approx_area
    for i in range(n):
        xi = x_rect[i]
        xr = np.linspace(xi, xi + dx, 50)
        yr = f(xi) * np.ones_like(xr)
        ax.fill_between(xr, yr, f(xr), color="#e53935", alpha=0.35)
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.set_ylim(0, f(b) + 0.2)
    ax.set_title(f"n={n}, error={err:.4f}", fontsize=12)
    ax.grid(True, alpha=0.3)
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")


def plot_error_curve():
    fig, ax = new_figure(width=6, height=4)
    ns = [2, 4, 8, 16, 32, 64, 128]
    a, b = 0, 2
    true_area = b ** 3 / 3 - a ** 3 / 3
    errs = []
    for n in ns:
        dx = (b - a) / n
        s = sum(f(a + i * dx) * dx for i in range(n))
        errs.append(true_area - s)
    ax.plot(ns, errs, marker="o", color="#e53935", lw=2)
    ax.set_xlabel("n")
    ax.set_ylabel("误差")
    ax.set_title("Error vs n")
    ax.grid(True, alpha=0.3)
    add_watermark(ax)
    save_fig(fig, "error_trend.png")


if __name__ == "__main__":
    for idx, n in enumerate([2, 4, 8, 16, 32]):
        plot_with_error(n, idx)
    plot_error_curve()
