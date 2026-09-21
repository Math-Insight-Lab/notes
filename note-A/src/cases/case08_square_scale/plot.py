# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case08 square_scale 正方形边长缩放|变量连续改变
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def plot_square(size, idx):
    fig, ax = new_figure(width=5, height=5)
    rect = patches.Rectangle((0,0), size, size, color="#4078c0", alpha=0.45)
    ax.add_patch(rect)
    ax.text(size/2, -0.35, f"边长 = {size:.1f}", ha="center", fontsize=12)
    ax.set_xlim(0,5)
    ax.set_ylim(-0.6,5)
    ax.set_aspect("equal")
    ax.set_title("正方形边长连续改变", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_s{size:.1f}.png")

if __name__ == "__main__":
    for idx,s in enumerate([1.0,2.0,3.5]):
        plot_square(s, idx)
