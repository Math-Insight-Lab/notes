# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case01 number_line 数轴跳动｜有理数、绝对值几何意义
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_pos_frame(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0,color="#222222",lw=1.5)
    ax.axvline(x=0,color="#888888",lw=1,linestyle="--")
    for tick in range(-5,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08,color="#222222")
    draw_dot(ax, 3,0,color="#4078c0",label="x=3")
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("数轴：正数对应的点", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_pos.png")

def plot_neg_frame(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0,color="#222222",lw=1.5)
    ax.axvline(x=0,color="#888888",lw=1,linestyle="--")
    for tick in range(-5,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08,color="#222222")
    draw_dot(ax, -2,0,color="#e53935",label="x=-2")
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("数轴：负数对应的点", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_neg.png")

def plot_abs_origin(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0,color="#222222",lw=1.5)
    ax.axvline(x=0,color="#888888",lw=1,linestyle="--")
    for tick in range(-5,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08,color="#222222")
    draw_dot(ax,-4,0,color="#e53935")
    draw_segment(ax,-4,0,0,0,color="#f08000")
    ax.text(-2,0.2,"$|-4|=4$",ha="center",fontsize=11)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("绝对值：点到原点的距离", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_abs0.png")

def plot_abs_dist(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0,color="#222222",lw=1.5)
    ax.axvline(x=0,color="#888888",lw=1,linestyle="--")
    for tick in range(-5,6):
        ax.axvline(x=tick, ymin=0,ymax=0.08,color="#222222")
    draw_dot(ax,1,0,color="#4078c0")
    draw_dot(ax,4,0,color="#4078c0")
    draw_segment(ax,1,0,4,0,color="#f08000")
    ax.text(2.5,0.2,"$|4-1|=3$两点距离",ha="center",fontsize=11)
    ax.set_yticks([])
    ax.grid(False)
    ax.set_title("$|x-a|$代表两点之间距离", fontsize=12)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_abs_dist.png")

if __name__ == "__main__":
    plot_pos_frame(0)
    plot_neg_frame(1)
    plot_abs_origin(2)
    plot_abs_dist(3)