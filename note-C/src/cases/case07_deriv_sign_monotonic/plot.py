"""case07 Derivative Sign -> Monotonicity - 导数正负函数增减联动"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark


def f(x):
    return x ** 2 - 2 * x


def df(x):
    return 2 * x - 2


def plot_tangent_frame(x0, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-0.5, 3.5, 300)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)=x^2-2x$")
    ax.plot(xs, df(xs), color="#f08000", lw=2, linestyle="--", label="$f'(x)=2x-2$")
    y0 = f(x0)
    k = df(x0)
    xtan = np.linspace(x0 - 1, x0 + 1, 100)
    ax.plot(xtan, y0 + k * (xtan - x0), color="#4078c0", lw=2)
    draw_dot(ax, x0, y0, color="#e53935", label=f"x={x0:.1f}")
    ax.set_title(f"切线斜率 f'({x0:.1f})={k:.2f}", fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_x{x0:.1f}.png")


def plot_overview():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-0.5, 3.5, 300)
    ax.plot(xs, f(xs), color="#222", lw=2, label="$f(x)$")
    ax.plot(xs, df(xs), color="#f08000", lw=2, linestyle="--", label="$f'(x)$")
    ax.fill_between(xs, f(xs), where=xs < 1, color="#4078c0", alpha=0.2, label="Decreasing")
    ax.fill_between(xs, f(xs), where=xs > 1, color="#e53935", alpha=0.2, label="Increasing")
    ax.set_title("Derivative sign and monotonicity", fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, "monotonic_overview.png")


if __name__ == "__main__":
    for i, x0 in enumerate([0.0, 0.5, 1.0, 2.0, 3.0]):
        plot_tangent_frame(x0, i)
    plot_overview()
