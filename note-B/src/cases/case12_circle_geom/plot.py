# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case12 circle_geom 圆基础动态演示【内嵌：切线直观】
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import matplotlib.patches as patches
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_circle_tangent(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    # 圆
    circle = patches.Circle((0,0), radius=2, fill=False, ec="#222222", lw=2)
    ax.add_patch(circle)
    draw_dot(ax,0,0,color="#222222",label="圆心 O")
    # 切点
    px,py = 2,0
    draw_dot(ax, px,py, color="#e53935", label="切点 P")
    draw_segment(ax,0,0, px,py, color="#4078c0", lw=2, label="半径 OP")
    # 切线，垂直于半径（竖直直线 x=2）
    ax.axvline(x=2, color="#f08000", lw=2, linestyle="--", label="切线")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    ax.set_title("圆的切线垂直于过切点的半径", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_circle_tangent.png")

if __name__ == "__main__":
    plot_circle_tangent(0)