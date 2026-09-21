# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case11 similar_triangle 相似三角形动态几何
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_triangle_scale(k, idx):
    fig, ax = new_figure(width=6, height=5)
    ax.set_xlim(0,8)
    ax.set_ylim(0,6)
    # 基准三角形
    p0 = (0,0)
    p1 = (4,0)
    p2 = (4,3)
    draw_segment(ax, p0[0],p0[1], p1[0],p1[1], color="#222222", lw=2)
    draw_segment(ax, p1[0],p1[1], p2[0],p2[1], color="#222222", lw=2)
    draw_segment(ax, p2[0],p2[1], p0[0],p0[1], color="#222222", lw=2)
    # 缩放相似三角形
    q0=(0,0)
    q1=(4*k,0)
    q2=(4*k,3*k)
    draw_segment(ax, q0[0],q0[1], q1[0],q1[1], color="#4078c0", lw=2, linestyle="--")
    draw_segment(ax, q1[0],q1[1], q2[0],q2[1], color="#4078c0", lw=2, linestyle="--")
    draw_segment(ax, q2[0],q2[1], q0[0],q0[1], color="#4078c0", lw=2, linestyle="--")
    ax.set_title(f"相似三角形，缩放系数 k={k:.1f}", fontsize=12)
    ax.text(5,2,f"直角边比例恒等于 $\\frac{{3}}{{4}}$（斜率）", fontsize=11)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_scale{k:.1f}.png")

if __name__ == "__main__":
    scale_list = [1.0,1.5,0.6]
    for i, k in enumerate(scale_list):
        plot_triangle_scale(k,i)