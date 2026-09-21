# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case03 irregular_grid 不规则图形网格铺满|曲线图形累加
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def f(x):
    return 2 + np.sin(x/2)

def plot_grid(grid_size, idx):
    fig, ax = new_figure(width=7, height=4.5)
    x = np.linspace(0,10,200)
    y = f(x)
    ax.plot(x,y,color="#222222",lw=2)
    ax.fill_between(x,y,0,alpha=0.2,color="#4078c0")
    for i in np.arange(0,10,grid_size):
        for j in np.arange(0,4,grid_size):
            if j < f(i):
                rect = patches.Rectangle((i,j),grid_size,grid_size,color="#4078c0",alpha=0.45)
                ax.add_patch(rect)
    ax.set_xlim(0,10)
    ax.set_ylim(0,4)
    ax.set_title(f"网格尺寸 {grid_size:.2f}", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_gs{grid_size:.2f}.png")

if __name__ == "__main__":
    for idx, gs in enumerate([0.8,0.4,0.2]):
        plot_grid(gs, idx)
