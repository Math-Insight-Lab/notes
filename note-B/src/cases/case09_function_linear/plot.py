# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case09 function_linear 一次函数深度专题【核心内嵌：平均变化率】
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def f(x):
    return 1.5*x + 1

def plot_two_points(idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-1,4,200)
    ys = f(xs)
    ax.plot(xs, ys, color="#222222", lw=2, label="$y=1.5x+1$")
    x1,y1 = 0, f(0)
    x2,y2 = 2, f(2)
    draw_dot(ax, x1,y1, color="#4078c0", label="$P_1(x_1,y_1)$")
    draw_dot(ax, x2,y2, color="#e53935", label="$P_2(x_2,y_2)$")
    # 增量辅助线
    draw_segment(ax, x1,y1, x2,y1, color="#f08000", linestyle="--")
    draw_segment(ax, x2,y1, x2,y2, color="#f08000", linestyle="--")
    ax.text((x1+x2)/2, y1-0.4, "$\Delta x$", ha="center")
    ax.text(x2+0.15, (y1+y2)/2, "$\Delta y$", va="center")
    k = (y2-y1)/(x2-x1)
    ax.text(0.2,6.0,f"平均变化率 $\\frac{{\Delta y}}{{\Delta x}}={k:.2f}$", fontsize=12)
    ax.grid(True, alpha=0.25)
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,8)
    ax.set_title("一次函数：两点之间增量与平均变化率", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_linear_two_points.png")

def plot_diff_points(idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-1,4,200)
    ys = f(xs)
    ax.plot(xs, ys, color="#222222", lw=2, label="$y=1.5x+1$")
    pts = [(0, f(0)), (1, f(1)), (3, f(3))]
    for px,py in pts:
        draw_dot(ax, px,py, color="#4078c0")
    ax.text(0.2,6.0,"直线任意两点，平均变化率恒定不变",fontsize=12)
    ax.grid(True, alpha=0.25)
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,8)
    ax.set_title("直线：更换不同取样点，斜率保持不变", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_diff_points.png")

if __name__ == "__main__":
    plot_two_points(0)
    plot_diff_points(1)