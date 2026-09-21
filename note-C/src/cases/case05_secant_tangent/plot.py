"""case05 Secant to Tangent - 割线动态逼近切线全过程"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def f(x):
    return x ** 2


def plot_secant_tangent(dx, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2.5, 200)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)=x^2$")
    xp, yp = 1, f(1)
    xq, yq = xp + dx, f(xp + dx)
    k_sec = (yq - yp) / dx
    xline = np.linspace(0, 2.5, 100)
    y_sec = yp + k_sec * (xline - xp)
    ax.plot(xline, y_sec, color="#4078c0", lw=2, label=f"Secant, k={k_sec:.3f}")
    k_tan = 2
    y_tan = yp + k_tan * (xline - xp)
    ax.plot(xline, y_tan, color="#f08000", lw=2, linestyle="--", label="Tangent")
    draw_dot(ax, xp, yp, color="#e53935", label="$P(1,1)$")
    draw_dot(ax, xq, yq, color="#4078c0")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 6)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Secant -> Tangent, dx={dx:.3f}", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_dx{dx:.2f}.png")


def plot_final():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2.5, 200)
    ax.plot(xs, f(xs), color="#222", lw=2)
    xline = np.linspace(0, 2.5, 100)
    ax.plot(xline, 1 + 2 * (xline - 1), color="#f08000", lw=2, linestyle="--")
    draw_dot(ax, 1, 1, color="#e53935")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 6)
    ax.grid(True, alpha=0.3)
    add_watermark(ax)
    save_fig(fig, "tangent_final.png")


if __name__ == "__main__":
    for i, dx in enumerate([1.0, 0.5, 0.2, 0.1, 0.05]):
        plot_secant_tangent(dx, i)
    plot_final()
