# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case04 curve_trend 曲线快慢变化|变化率雏形
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark

def plot_curve(label, y_func, idx):
    fig, ax = new_figure(width=7, height=4.5)
    x = np.linspace(0,10,200)
    y = y_func(x)
    ax.plot(x,y,color="#222222",lw=2)
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)
    ax.set_title(label, fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}.png")

if __name__ == "__main__":
    plot_curve("匀速变化", lambda x:0.5*x, 0)
    plot_curve("加速变化", lambda x:0.15*x**1.8, 1)
    plot_curve("增速逐渐放缓", lambda x:8-0.3*(x-8)**2, 2)
