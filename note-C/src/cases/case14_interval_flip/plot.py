"""case14 Interval Flip - 积分上下限翻转符号变化"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f(x):
    return np.sin(x)


def plot_forward():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, np.pi, 300)
    ax.plot(xs, f(xs), color="#222", lw=2)
    ax.fill_between(xs, 0, f(xs), color="#4078c0", alpha=0.4)
    ax.set_xlim(-0.2, np.pi + 0.2)
    ax.set_ylim(-0.3, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    ax.text(
        np.pi / 2, 0.3,
        "integral = 2", fontsize=14, ha="center", color="#4078c0"
    )
    ax.set_title(r"$\int_0^\pi \sin(x)dx = 2$", fontsize=14)
    add_watermark(ax)
    save_fig(fig, "forward.png")


def plot_reversed():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, np.pi, 300)
    ax.plot(xs, f(xs), color="#222", lw=2)
    ax.fill_between(xs, 0, f(xs), color="#e53935", alpha=0.4)
    ax.set_xlim(-0.2, np.pi + 0.2)
    ax.set_ylim(-0.3, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    # Arrow showing reversed direction
    ax.annotate("", xy=(0.1, 1.3), xytext=(np.pi - 0.1, 1.3),
                arrowprops=dict(arrowstyle="<-", color="#e53935", lw=2))
    ax.text(
        np.pi / 2, 0.5,
        "integral = -2", fontsize=14, ha="center", color="#e53935"
    )
    ax.set_title(r"$\int_\pi^0 \sin(x)dx = -2$", fontsize=14)
    add_watermark(ax)
    save_fig(fig, "reversed.png")


def plot_comparison():
    fig, (ax1, ax2) = new_figure(nrows=1, ncols=2, width=12, height=5)
    xs = np.linspace(0, np.pi, 300)
    # Forward
    ax1.plot(xs, f(xs), color="#222", lw=2)
    ax1.fill_between(xs, 0, f(xs), color="#4078c0", alpha=0.4)
    ax1.axhline(y=0, color="#222", lw=1)
    ax1.text(np.pi / 2, 0.3, "2", fontsize=16, ha="center", color="#4078c0")
    ax1.set_xlim(-0.2, np.pi + 0.2)
    ax1.set_ylim(-0.3, 1.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_title(r"$\int_0^\pi \sin(x)dx = 2$")
    # Reversed
    ax2.plot(xs, f(xs), color="#222", lw=2)
    ax2.fill_between(xs, 0, f(xs), color="#e53935", alpha=0.4)
    ax2.axhline(y=0, color="#222", lw=1)
    ax2.text(np.pi / 2, 0.5, "-2", fontsize=16, ha="center", color="#e53935")
    ax2.set_xlim(-0.2, np.pi + 0.2)
    ax2.set_ylim(-0.3, 1.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_title(r"$\int_\pi^0 \sin(x)dx = -2$")
    add_watermark(ax1, ax2)
    save_fig(fig, "comparison.png")


if __name__ == "__main__":
    plot_forward()
    plot_reversed()
    plot_comparison()
