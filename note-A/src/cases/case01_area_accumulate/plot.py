# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case01 area_accumulate 矩形小块铺满|分割-累加（积分原型）
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def plot_tile(n_col, idx):
    fig, ax = new_figure(width=7, height=4.5)
    ax.set_xlim(0,10)
    ax.set_ylim(0,6)
    cell_w = 10.0 / n_col
    cell_h = 0.6
    for i_col in range(n_col):
        for i_row in range(int(6 / cell_h)):
            x = i_col * cell_w
            y = i_row * cell_h
            rect = patches.Rectangle((x,y), cell_w-0.02, cell_h-0.02, color="#4078c0", alpha=0.45)
            ax.add_patch(rect)
    ax.set_title(f"矩形小块铺满，分割数量 {n_col}", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n_col}.png")

if __name__ == "__main__":
    for idx,n in enumerate([4,10,20]):
        plot_tile(n, idx)
