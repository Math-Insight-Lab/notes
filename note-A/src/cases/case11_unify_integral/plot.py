# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case11 unify_integral 积分大一统|所有面积 = 小矩形累加
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches

def f(x):
    return 0.3 * x**2

def plot_riemann(n_rects, idx):
    fig, ax = new_figure(width=7, height=4.5)
    x = np.linspace(0,4,200)
    y = f(x)
    ax.plot(x,y,color="#222222",lw=2)
    ax.fill_between(x,y,0,alpha=0.15,color="#4078c0")
    dx = 4.0 / n_rects
    for i in range(n_rects):
        xi = i * dx
        yi = f(xi)
        rect = patches.Rectangle((xi,0), dx-0.05, yi, color="#4078c0", alpha=0.45)
        ax.add_patch(rect)
    ax.set_xlim(0,4)
    ax.set_ylim(0,5)
    ax.set_title(f"小矩形数量 {n_rects}", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n_rects}.png")

if __name__ == "__main__":
    for idx,n in enumerate([4,10,20]):
        plot_riemann(n, idx)
