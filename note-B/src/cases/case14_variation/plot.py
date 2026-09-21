# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case14 variation 变量与变化关系专题【核心内嵌：离散累积】
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_sum_blocks(idx):
    fig, ax = new_figure(width=6, height=4.5)
    ax.set_xlim(0,5)
    ax.set_ylim(0,3)
    widths = [1,1,1,1]
    x_pos = 0
    for w in widths:
        ax.add_patch(patches.Rectangle((x_pos,0), w, 2, color="#4078c0", alpha=0.4))
        x_pos += w
    ax.text(2.5,2.3,"多个小块相加得到整体总面积",ha="center",fontsize=11)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_sum_blocks.png")

def plot_approx_curve(idx):
    def f(x):
        return 0.4*x**2
    fig, ax = new_figure(width=6, height=4.5)
    xs = np.linspace(0,4,200)
    ys = f(xs)
    ax.plot(xs, ys, color="#222222", lw=2)
    n=4
    a,b=0,4
    dx=(b-a)/n
    x_nodes = np.linspace(a,b,n+1)
    for i in range(n):
        xi = x_nodes[i]
        hi = f(xi)
        ax.add_patch(patches.Rectangle((xi,0), dx, hi, color="#4078c0", alpha=0.35))
    ax.set_xlim(-0.2,4.2)
    ax.set_ylim(0,7)
    ax.set_title("用小矩形小块之和近似曲线下方的面积",fontsize=12)
    ax.grid(True, alpha=0.25)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_approx_curve.png")

if __name__ == "__main__":
    plot_sum_blocks(0)
    plot_approx_curve(1)