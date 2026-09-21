"""case01 Rectangular Approximation - 曲边图形矩形无限细分逼近"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches


def f(x):
    return x ** 2


def plot_riemann_approx(n, idx, a=0, b=2):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(a, b, 200)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)=x^2$")
    dx = (b - a) / n
    x_rect = np.linspace(a, b, n + 1)
    total_area = 0
    for i in range(n):
        xi = x_rect[i]
        yi = f(xi)
        rect = patches.Rectangle((xi, 0), dx, yi, color="#4078c0", alpha=0.4)
        ax.add_patch(rect)
        total_area += yi * dx
    true_area = b ** 3 / 3 - a ** 3 / 3
    ax.set_xlim(a - 0.1, b + 0.1)
    ax.set_ylim(0, f(b) + 0.2)
    ax.grid(True, alpha=0.3)
    ax.set_title(
        f"n={n}, area={total_area:.4f}, true={true_area:.4f}", fontsize=12
    )
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")


if __name__ == "__main__":
    for idx, n in enumerate([2, 4, 8, 16, 32]):
        plot_riemann_approx(n, idx)
