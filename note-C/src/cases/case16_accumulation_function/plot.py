"""case16 Accumulation Function - 累积函数积分上限函数"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return np.sin(x)


def F(x):
    """Antiderivative: F(x) = -cos(x) + 1"""
    return -np.cos(x) + 1


def plot_f_and_F():
    fig, ax1 = new_figure(width=8, height=6)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax1.plot(xs, f(xs), color="#222", lw=2, label="f(x) = sin(x)")
    ax2 = ax1.twinx()
    ax2.plot(xs, F(xs), color="#4078c0", lw=2, label="F(x) = integral_0^x sin(t)dt")
    ax1.set_xlim(0, 2 * np.pi)
    ax1.set_ylim(-0.5, 1.5)
    ax2.set_ylim(-0.2, 2.2)
    ax1.grid(True, alpha=0.3)
    ax1.set_title("Original function and its integral (accumulation)", fontsize=14)
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)", color="#222")
    ax2.set_ylabel("F(x)", color="#4078c0")
    add_watermark(ax1)
    save_fig(fig, "f_and_F.png")


def plot_accumulation_animation_frames():
    for idx, a in enumerate([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]):
        fig, ax = new_figure(width=7, height=5)
        xs = np.linspace(0, 2 * np.pi, 300)
        ax.plot(xs, f(xs), color="#222", lw=2)
        fill_xs = np.linspace(0, a, max(int(a * 50), 1))
        ax.fill_between(fill_xs, 0, f(fill_xs), color="#4078c0", alpha=0.4)
        area_val = F(a) - F(0)
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-0.5, 1.5)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color="#222", lw=1)
        ax.text(
            a * 0.5, 0.3,
            f"A = {area_val:.3f}", fontsize=12, color="#4078c0"
        )
        ax.set_title(f"Accumulation from 0 to {a:.2f}", fontsize=14)
        add_watermark(ax)
        save_fig(fig, f"accum_{idx:02d}_a{a:.1f}.png")


if __name__ == "__main__":
    plot_f_and_F()
    plot_accumulation_animation_frames()
