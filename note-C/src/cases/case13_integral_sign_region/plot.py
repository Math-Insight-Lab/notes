"""case13 Integral Sign and Region - 积分符号与区域关系"""

import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches


def f1(x):
    return np.sin(x)


def f2(x):
    return np.sin(x) - 1.2


def plot_positive_region():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax.plot(xs, f1(xs), color="#222", lw=2)
    xs_pos = np.linspace(0, np.pi, 100)
    ax.fill_between(xs_pos, 0, f1(xs_pos), color="#4078c0", alpha=0.4)
    ax.text(
        np.pi / 2, 0.5, "+ area", fontsize=14, color="#4078c0"
    )
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-0.5, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    ax.set_title("Positive area: integral > 0", fontsize=12)
    add_watermark(ax)
    save_fig(fig, "positive_area.png")


def plot_negative_region():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax.plot(xs, f2(xs), color="#222", lw=2)
    ax.axhline(y=0, color="#222", lw=1)
    xs_neg = np.linspace(0, 2 * np.pi, 100)
    ax.fill_between(xs_neg, 0, f2(xs_neg), color="#e53935", alpha=0.4)
    ax.text(
        np.pi, -1.5, "- area", fontsize=14, color="#e53935"
    )
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-2, 0.5)
    ax.grid(True, alpha=0.3)
    ax.set_title("Negative area: integral < 0", fontsize=12)
    add_watermark(ax)
    save_fig(fig, "negative_area.png")


def plot_mixed_region():
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(0, 2 * np.pi, 300)
    ax.plot(xs, f1(xs), color="#222", lw=2)
    xs_pos = np.linspace(0, np.pi, 100)
    ax.fill_between(xs_pos, 0, f1(xs_pos), color="#4078c0", alpha=0.4)
    xs_neg = np.linspace(np.pi, 2 * np.pi, 100)
    ax.fill_between(xs_neg, 0, f1(xs_neg), color="#e53935", alpha=0.4)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-0.5, 1.5)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="#222", lw=1)
    ax.set_title("Mixed: net integral = 0", fontsize=12)
    add_watermark(ax)
    save_fig(fig, "mixed_area.png")


if __name__ == "__main__":
    plot_positive_region()
    plot_negative_region()
    plot_mixed_region()
