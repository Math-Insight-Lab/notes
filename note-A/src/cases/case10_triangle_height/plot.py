# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case10 triangle_height 三角形高变化|输入输出连续联动
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def plot_triangle(height, idx):
    fig, ax = new_figure(width=5, height=5)
    base = 4.0
    triangle = patches.Polygon([(0,0),(base,0),(base/2,height)], color="#4078c0", alpha=0.45)
    ax.add_patch(triangle)
    ax.text(base/2, -0.35, f"底={base:.1f}, 高={height:.1f}", ha="center", fontsize=12)
    ax.set_xlim(-0.5, base+0.5)
    ax.set_ylim(-0.6, height+0.5)
    ax.set_aspect("equal")
    ax.set_title("三角形高度连续变化", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_h{height:.1f}.png")

if __name__ == "__main__":
    for idx,h in enumerate([1.0,2.0,4.0]):
        plot_triangle(h, idx)
