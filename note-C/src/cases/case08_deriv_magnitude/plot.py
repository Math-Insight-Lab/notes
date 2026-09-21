"""case08 Derivative Magnitude - 导数大小变化快慢匹配"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def f(x):
    return np.sin(x)


def df(x):
    return np.cos(x)


def plot_tangent_frame(x0, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)=sin(x)$")
    ax.plot(xs, df(xs), color="#f08000", lw=2, linestyle="--", label="$f'(x)=cos(x)$")
    y0, k = f(x0), df(x0)
    xtan = np.linspace(x0 - 0.8, x0 + 0.8, 100)
    ax.plot(xtan, y0 + k * (xtan - x0), color="#4078c0", lw=2)
    draw_dot(ax, x0, y0, color="#e53935",
             label=f"x={x0:.2f}, |f'|={abs(k):.2f}")
    ax.set_title(f"Steepness: |f'|={abs(k):.2f}", fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_x{x0:.1f}.png")


def plot_overview():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax.plot(xs, f(xs), color="#222", lw=2)
    ax.plot(xs, df(xs), color="#f08000", lw=2, linestyle="--")
    ax.set_title("Steepness and derivative magnitude", fontsize=12)
    ax.grid(True, alpha=0.3)
    add_watermark(ax)
    save_fig(fig, "steepness_overview.png")


if __name__ == "__main__":
    for i, x0 in enumerate([0.0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]):
        plot_tangent_frame(x0, i)
    plot_overview()
