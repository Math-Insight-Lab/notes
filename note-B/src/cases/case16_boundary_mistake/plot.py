# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case16 boundary_mistake 初中常见概念易错边界合集
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_divzero(idx):
    fig, ax = new_figure(width=7, height=4)
    ax.text(0.5,0.5,"$\\dfrac{1}{x}$，当 $x=0$ 表达式无意义（除零禁忌）", fontsize=14,ha="center",va="center",transform=ax.transAxes)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_divzero.png")

def plot_approach_not_eq(idx):
    fig, ax = new_figure(width=8, height=3.5)
    ax.set_xlim(-1,6)
    ax.set_ylim(-1,1)
    ax.axhline(y=0,color="#222222",lw=1.5)
    for tick in range(0,6):
        ax.axvline(x=tick,ymin=0,ymax=0.08,c="#222222")
    ax.plot(3,0,marker="o",mfc="white",mec="#222222",markersize=8)
    draw_dot(ax,1,0,color="#4078c0")
    draw_dot(ax,2,0,color="#4078c0")
    draw_dot(ax,2.6,0,color="#4078c0")
    draw_dot(ax,2.9,0,color="#4078c0")
    ax.text(4,0.2,"点不断靠近3，但不等于3",ha="left",fontsize=12)
    ax.set_yticks([])
    ax.grid(False)
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_approach_not_eq.png")

if __name__ == "__main__":
    plot_divzero(0)
    plot_approach_not_eq(1)