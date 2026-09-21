# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case07 linear_system 二元一次方程组｜直线相交几何视角
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_intersect(idx):
    fig, ax = new_figure(width=6, height=5)
    xs = np.linspace(-4,4,200)
    # y = -x+3
    y1 = -xs + 3
    # y = 2*x
    y2 = 2*xs
    ax.plot(xs,y1,color="#4078c0",lw=2,label="$y=-x+3$")
    ax.plot(xs,y2,color="#f08000",lw=2,label="$y=2x$")
    draw_dot(ax,1,2,color="#e53935",label="交点 $(1,2)$")
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.grid(True, alpha=0.25)
    ax.set_title("两直线相交，唯一一组解", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_intersect.png")

def plot_parallel(idx):
    fig, ax = new_figure(width=6, height=5)
    xs = np.linspace(-4,4,200)
    y1 = xs +1
    y2 = xs -2
    ax.plot(xs,y1,color="#4078c0",lw=2,label="$y=x+1$")
    ax.plot(xs,y2,color="#f08000",lw=2,label="$y=x-2$")
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.grid(True, alpha=0.25)
    ax.set_title("两直线平行，方程组无解", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_parallel.png")

def plot_coincide(idx):
    fig, ax = new_figure(width=6, height=5)
    xs = np.linspace(-4,4,200)
    y1 = 2*xs +1
    ax.plot(xs,y1,color="#4078c0",lw=2,label="$y=2x+1$（两条直线完全重合）")
    ax.set_xlim(-4,4)
    ax.set_ylim(-4,4)
    ax.grid(True, alpha=0.25)
    ax.set_title("直线重合，有无穷多组解", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_coincide.png")

if __name__ == "__main__":
    plot_intersect(0)
    plot_parallel(1)
    plot_coincide(2)