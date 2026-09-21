# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case07 square_dot 平方数点阵|离散单元累积
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark

def plot_dot_grid(n, idx):
    fig, ax = new_figure(width=5, height=5)
    for i in range(n):
        for j in range(n):
            draw_dot(ax, i, j, color="#4078c0")
    ax.set_xlim(-1,6)
    ax.set_ylim(-1,6)
    ax.set_title(f"点阵 n={n}，总点数 {n*n}", fontsize=12)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")

if __name__ == "__main__":
    for idx,n in enumerate([2,3,5]):
        plot_dot_grid(n, idx)
