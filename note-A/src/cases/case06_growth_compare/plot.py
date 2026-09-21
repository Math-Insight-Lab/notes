# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case06 growth_compare 匀速vs加速增长对比
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark

def plot_growth(end_x, idx):
    fig, ax = new_figure(width=7, height=4.5)
    x_full = np.linspace(0,10,100)
    mask = x_full <= end_x
    x = x_full[mask]
    y1 = 0.8 * x
    y2 = 0.12 * x**2
    ax.plot(x,y1,label="匀速变化",color="#4078c0",lw=2)
    ax.plot(x,y2,label="加速变化",color="#f08000",lw=2)
    ax.set_xlim(0,10)
    ax.set_ylim(0,12)
    ax.legend(loc="upper left")
    ax.set_title("匀速与加速增长对比", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_ex{end_x}.png")

if __name__ == "__main__":
    for idx,ex in enumerate([3,6,10]):
        plot_growth(ex, idx)
