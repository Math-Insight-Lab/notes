# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case04 coord_walk 坐标系点行走平移｜平面直角坐标系
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_quad(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.axhline(y=0,c="#222222",lw=1.2)
    ax.axvline(x=0,c="#222222",lw=1.2)
    ax.text(2.5,2.5,"第一象限",ha="center")
    ax.text(-2.5,2.5,"第二象限",ha="center")
    ax.text(-2.5,-2.5,"第三象限",ha="center")
    ax.text(2.5,-2.5,"第四象限",ha="center")
    draw_dot(ax,0,0,color="#222222",label="原点 O(0,0)")
    ax.grid(True,alpha=0.25)
    ax.set_title("平面直角坐标系与四个象限",fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_origin_quad.png")

def plot_walk_x(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.axhline(y=0,c="#222222",lw=1.2)
    ax.axvline(x=0,c="#222222",lw=1.2)
    draw_dot(ax,1,2,color="#4078c0",label="$P(1,2)$")
    draw_dot(ax,4,2,color="#e53935",label="$P'(4,2)$ 向右移动")
    draw_segment(ax,1,2,4,2,color="#f08000",linestyle="--")
    ax.grid(True,alpha=0.25)
    ax.set_title("横坐标变化，点沿水平方向行走",fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_walk_x.png")

def plot_walk_y(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.axhline(y=0,c="#222222",lw=1.2)
    ax.axvline(x=0,c="#222222",lw=1.2)
    draw_dot(ax,2,1,color="#4078c0",label="$P(2,1)$")
    draw_dot(ax,2,4,color="#e53935",label="$P'(2,4)$ 向上移动")
    draw_segment(ax,2,1,2,4,color="#f08000",linestyle="--")
    ax.grid(True,alpha=0.25)
    ax.set_title("纵坐标变化，点沿竖直方向行走",fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_walk_y.png")

def plot_sym_xy(idx):
    fig, ax = new_figure(width=6, height=6)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.axhline(y=0,c="#222222",lw=1.2)
    ax.axvline(x=0,c="#222222",lw=1.2)
    draw_dot(ax,3,2,color="#4078c0",label="$P(3,2)$")
    draw_dot(ax,3,-2,color="#e53935",label="关于x轴对称 $(3,-2)$")
    draw_dot(ax,-3,2,color="#f08000",label="关于y轴对称 $(-3,2)$")
    ax.grid(True,alpha=0.25)
    ax.set_title("点关于坐标轴的对称变换",fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_sym_xy.png")

if __name__ == "__main__":
    plot_quad(0)
    plot_walk_x(1)
    plot_walk_y(2)
    plot_sym_xy(3)