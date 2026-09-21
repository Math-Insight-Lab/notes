"""case11 Area Convergence - 不同n下黎曼和面积收敛可视化"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return np.sin(x)


def plot_riemann_series(ns, a=0, b=3, idx=""):
    fig, axs = new_figure(nrows=1, ncols=len(ns), width=5*len(ns), height=5)
    if len(ns) == 1:
        axs = [axs]
    for ax, n in zip(axs, ns):
        xs = np.linspace(a, b, 200)
        ax.plot(xs, f(xs), color="#222", lw=2)
        dx = (b - a) / n
        x_rect = np.linspace(a, b, n + 1)
        for i in range(n):
            xi = x_rect[i]
            yi = f(xi)
            rect = patches.Rectangle((xi, 0), dx, yi, color="#4078c0", alpha=0.4)
            ax.add_patch(rect)
        area = sum(f(a + i * dx) * dx for i in range(n))
        ax.set_xlim(a - 0.2, b + 0.2)
        ax.set_ylim(-0.2, 1.2)
        ax.grid(True, alpha=0.3)
        ax.set_title(f"n={n}, area={area:.3f}", fontsize=12)
    for ax in axs:
        add_watermark(ax)
    save_fig(fig, f"convergence_series{idx}.png")


def plot_convergence_curve():
    fig, ax = new_figure(width=7, height=4)
    ns = [2, 4, 8, 16, 32, 64, 128, 256]
    sums = [sum(np.sin(i * 3 / n) * 3 / n for i in range(n)) for n in ns]
    true_val = 1 - np.cos(3)
    ax.plot(ns, sums, marker="o", color="#4078c0", lw=2, label="Left sum")
    ax.axhline(y=true_val, linestyle="--", color="#f08000", label=f"True = {true_val:.3f}")
    ax.set_xlabel("n")
    ax.set_ylabel("Sum")
    ax.set_title("Convergence of Left Riemann Sum")
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "conv_curve.png")


if __name__ == "__main__":
    plot_riemann_series([2, 4, 8, 16], idx="_4panel.png")
    plot_convergence_curve()
