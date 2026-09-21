# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case09 fraction_split 图形分数等分拆分|无限细分感知
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def plot_split(n, idx):
    fig, ax = new_figure(width=6, height=3)
    W, H = 8, 2
    step = W / n
    for i in range(n):
        c = "#4078c0" if i%2==0 else "#b3d1f5"
        rect = patches.Rectangle((i*step, 0), step, H, color=c)
        ax.add_patch(rect)
    ax.text(W/2, -0.35, f"平均分成 {n} 份", ha="center", fontsize=12)
    ax.set_xlim(0,W)
    ax.set_ylim(-0.6, H+0.5)
    ax.set_aspect("equal")
    ax.set_title("图形不断等分切分", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")

if __name__ == "__main__":
    for idx,n in enumerate([2,8,32]):
        plot_split(n, idx)
