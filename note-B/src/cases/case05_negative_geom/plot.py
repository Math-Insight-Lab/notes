# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case05 negative_geom 负数与绝对值拓展｜负数运算的几何图景
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_dir_plus(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-7,7)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-6,7):
        ax.axvline(x=tick, ymin=0, ymax=0.08, c="#222222")
    draw_dot(ax,0,0,color="#222222")
    draw_segment(ax,0,0,3,0,color="#4078c0")
    draw_segment(ax,3,0,5,0,color="#f08000")
    ax.text(1.5,0.2,"$+3$",ha="center")
    ax.text(4.0,0.2,"$+2$",ha="center")
    ax.text(5.3,0.2,"$3+2=5$",ha="left")
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("有向线段：正数相加", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_dir_plus.png")

def plot_dir_minus(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-7,7)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-6,7):
        ax.axvline(x=tick, ymin=0, ymax=0.08, c="#222222")
    draw_dot(ax,0,0,color="#222222")
    draw_segment(ax,0,0,4,0,color="#4078c0")
    draw_segment(ax,4,0,1,0,color="#e53935")
    ax.text(2,0.2,"$+4$",ha="center")
    ax.text(2.5,0.2,"$-3$",ha="center")
    ax.text(1.3,0.2,"$4-3=1$",ha="left")
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("减法等价于加上反向有向线段", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_dir_minus.png")

def plot_delta_x(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-7,7)
    ax.set_ylim(-1,1)
    ax.axhline(y=0, color="#222222", lw=1.5)
    for tick in range(-6,7):
        ax.axvline(x=tick, ymin=0, ymax=0.08, c="#222222")
    draw_dot(ax, 2, 0, color="#4078c0", label="$x_1=2$")
    draw_dot(ax, 5, 0, color="#e53935", label="$x_2=5$")
    draw_segment(ax,2,0,5,0,color="#f08000")
    ax.text(3.5,0.2,"$\Delta x=x_2-x_1=3$",ha="center")
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("增量 $\Delta x$：两点之间带方向的变化量", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_delta_x.png")

if __name__ == "__main__":
    plot_dir_plus(0)
    plot_dir_minus(1)
    plot_delta_x(2)