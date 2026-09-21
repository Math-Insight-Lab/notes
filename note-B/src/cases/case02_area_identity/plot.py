# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case02 area_identity 面积拼图｜完全平方、平方差公式
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches
import os

A = 3
B = 1.2


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_sq_sum(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(0, A+B+0.3)
    ax.set_ylim(0, A+B+0.3)
    # (a+b)^2
    ax.add_patch(patches.Rectangle((0,0), A+B, A+B, fill=False, ec="#222222", lw=2))
    # a²
    ax.add_patch(patches.Rectangle((0,0), A, A, color="#4078c0", alpha=0.4))
    # b²
    ax.add_patch(patches.Rectangle((A,A), B, B, color="#e53935", alpha=0.4))
    # ab 两块
    ax.add_patch(patches.Rectangle((A,0), B, A, color="#f08000", alpha=0.3))
    ax.add_patch(patches.Rectangle((0,A), A, B, color="#f08000", alpha=0.3))
    ax.text(A/2, A/2, "$a^2$", ha="center", va="center", fontsize=12)
    ax.text(A+B/2, A+B/2, "$b^2$", ha="center", va="center", fontsize=12)
    ax.text(A+B/2, A/2, "$ab$", ha="center", va="center", fontsize=11)
    ax.text(A/2, A+B/2, "$ab$", ha="center", va="center", fontsize=11)
    ax.set_title("$(a+b)^2 = a^2+2ab+b^2$", fontsize=13)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_sq_sum.png")

def plot_sq_diff_sub(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(0, A+0.3)
    ax.set_ylim(0, A+0.3)
    ax.add_patch(patches.Rectangle((0,0), A, A, fill=False, ec="#222222", lw=2))
    ax.add_patch(patches.Rectangle((0,0), A-B, A-B, color="#4078c0", alpha=0.4))
    ax.add_patch(patches.Rectangle((A-B,0), B, A-B, color="#f08000", alpha=0.3))
    ax.add_patch(patches.Rectangle((0,A-B), A-B, B, color="#f08000", alpha=0.3))
    ax.add_patch(patches.Rectangle((A-B,A-B), B, B, color="#e53935", alpha=0.4))
    ax.text((A-B)/2,(A-B)/2,"$(a-b)^2$",ha="center",va="center",fontsize=12)
    ax.set_title("$(a-b)^2 = a^2-2ab+b^2$", fontsize=13)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_sq_diff_sub.png")

def plot_sq_diff_factor(idx):
    fig, ax = new_figure(width=7, height=4.5)
    ax.set_xlim(0, (A+B)+0.4)
    ax.set_ylim(0, (A-B)+0.4)
    ax.add_patch(patches.Rectangle((0,0), A+B, A-B, color="#4078c0", alpha=0.4, ec="#222222"))
    ax.text((A+B)/2, (A-B)/2, "$a^2-b^2=(a+b)(a-b)$", ha="center", va="center", fontsize=13)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_sq_diff_factor.png")

if __name__ == "__main__":
    plot_sq_sum(0)
    plot_sq_diff_sub(1)
    plot_sq_diff_factor(2)