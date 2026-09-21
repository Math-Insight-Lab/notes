# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case02 circle_split 圆分割拼接|化曲为直，逼近思想
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark

def plot_circle_pack(n, idx):
    fig, (ax1, ax2) = new_figure(nrows=1, ncols=2, width=8, height=4)
    r = 2
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax1.fill(np.append(x,x[0]), np.append(y,y[0]), color="#4078c0", alpha=0.7)
    ax1.set_xlim(-r-1,r+1)
    ax1.set_ylim(-r-1,r+1)
    ax1.set_title(f"圆形分割 n={n}等分", fontsize=12)
    ax1.set_aspect("equal")
    ax1.axis("off")

    width = (2*np.pi*r)/2
    height = r
    rect_x = [0,width,width,0]
    rect_y = [0,0,height,height]
    ax2.fill(rect_x, rect_y, color="#f08000", alpha=0.6)
    ax2.set_xlim(0,width+1)
    ax2.set_ylim(0,height+1)
    ax2.set_title("拼接近似长方形", fontsize=12)
    ax2.set_aspect("equal")
    ax2.axis("off")
    add_watermark(ax1)
    add_watermark(ax2)
    save_fig(fig, f"frame_{idx:02d}_n{n}.png")

if __name__ == "__main__":
    for i,n in enumerate([4,10,20]):
        plot_circle_pack(n,i)
