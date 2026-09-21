"""case06 Tangent Slope - 切线斜率瞬时变化率原理"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def f(x):
    return x ** 2


def plot_slope_frame(dx, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2.5, 200)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)=x^2$")
    a = 1
    ya = f(a)
    ya2 = f(a + dx)
    k_sec = (ya2 - ya) / dx
    xline = np.linspace(0, 2.5, 100)
    y_sec = ya + k_sec * (xline - a)
    ax.plot(xline, y_sec, color="#4078c0", lw=2, label=f"Secant, k={k_sec:.3f}")
    y_tan = ya + 2 * (xline - a)
    ax.plot(xline, y_tan, color="#f08000", lw=2, linestyle="--", label="Tangent, k=2")
    draw_dot(ax, a, ya, color="#e53935")
    draw_dot(ax, a + dx, ya2, color="#4078c0")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 6)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Average rate, dx={dx:.3f}", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_dx{dx:.2f}.png")


def plot_convergence():
    fig, ax = new_figure(width=6, height=4)
    dx_list = [1.0, 0.5, 0.2, 0.1, 0.05, 0.01]
    slopes = [(f(1 + dx) - f(1)) / dx for dx in dx_list]
    ax.scatter(dx_list, slopes, color="#4078c0", zorder=3)
    ax.axhline(y=2, linestyle="--", color="#f08000", label="f'(1)=2")
    ax.set_xlabel("dx")
    ax.set_ylabel("Secant slope")
    ax.set_title("Convergence of secant slope")
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "slope_convergence.png")


if __name__ == "__main__":
    for i, dx in enumerate([1.0, 0.5, 0.2, 0.1, 0.05]):
        plot_slope_frame(dx, i)
    plot_convergence()
