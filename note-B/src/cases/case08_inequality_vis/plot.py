# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case08 inequality_vis 不等式与解集可视化
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_gt(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-4,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-3,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08, c="#222222")
    # 空心圆
    ax.plot(2,0, marker="o", mfc="white", mec="#222222", markersize=8)
    ax.fill_between([2,5.8], -0.3,0.3, color="#4078c0", alpha=0.3)
    ax.text(4,0.4,"$x>2$",ha="center",fontsize=12)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("不等式解集：大于，空心圆圈不包含端点", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_gt.png")

def plot_le(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-6,4)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-5,4):
        ax.axvline(x=tick, ymin=0,ymax=0.08, c="#222222")
    draw_dot(ax, -1,0, color="#222222")
    ax.fill_between([-5.8,-1], -0.3,0.3, color="#e53935", alpha=0.3)
    ax.text(-3.5,0.4,r"$x \leq -1$",ha="center",fontsize=12)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("不等式解集：小于等于，实心圆点包含端点", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_le.png")

def plot_group(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-5,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-4,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08, c="#222222")
    ax.plot(1,0, marker="o", mfc="white", mec="#222222", markersize=8)
    draw_dot(ax,4,0,color="#222222")
    ax.fill_between([1,4], -0.3,0.3, color="#f08000", alpha=0.4)
    ax.text(2.5,0.4,r"$1 < x \leq 4$ 公共解集",ha="center",fontsize=12)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("不等式组，取区间重叠的公共部分", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_group.png")

if __name__ == "__main__":
    plot_gt(0)
    plot_le(1)
    plot_group(2)