"""case12 Trapezoid Sum - 梯形求和比矩形更精确"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return x ** 2


def plot_trapezoid(n, idx, a=0, b=2):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(a, b, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    dx = (b - a) / n
    x_rect = np.linspace(a, b, n + 1)
    trapezoid_area = 0
    for i in range(n):
        xi = x_rect[i]
        xi_next = x_rect[i + 1]
        yi = f(xi)
        yi_next = f(xi_next)
        trap = patches.Polygon(
            [(xi, 0), (xi_next, 0), (xi_next, yi_next), (xi, yi)],
            color="#4078c0", alpha=0.4
        )
        ax.add_patch(trap)
        trapezoid_area += (yi + yi_next) * dx / 2
    true_area = 8 / 3
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.set_ylim(0, f(b) + 0.3)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"n={n}, trapezoid area={trapezoid_area:.4f}, error={abs(true_area-trapezoid_area):.4f}", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")


def plot_rect_vs_trap():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    n = 4
    dx = 0.5
    x_rect = np.linspace(0, 2, n + 1)
    # Rectangles (left sum)
    for i in range(n):
        xi = x_rect[i]
        yi = f(xi)
        rect = patches.Rectangle((xi, 0), dx, yi, color="#4078c0", alpha=0.4, label="Rectangles" if i == 0 else "")
        ax.add_patch(rect)
    # Trapezoids
    for i in range(n):
        xi = x_rect[i]
        yi = f(xi)
        yi_next = f(x_rect[i + 1])
        trap = patches.Polygon(
            [(xi, 0), (xi + dx, 0), (xi + dx, yi_next), (xi, yi)],
            color="#f08000", alpha=0.3, label="Trapezoids" if i == 0 else ""
        )
        ax.add_patch(trap)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 4.5)
    ax.grid(True, alpha=0.3)
    ax.set_title("Rectangles vs Trapezoids, n=4", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "rect_vs_trap.png")


if __name__ == "__main__":
    for i, n in enumerate([2, 4, 8]):
        plot_trapezoid(n, i)
    plot_rect_vs_trap()
