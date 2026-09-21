# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case03 balance_scale 天平动画｜等式性质与一元一次方程
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import matplotlib.patches as patches
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_balance_init(idx):
    fig, ax = new_figure(width=8, height=4)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,3)
    # 横梁支点
    draw_segment(ax,-5,2,5,2,color="#222222")
    draw_dot(ax,0,2,color="#222222")
    # 托盘吊线
    draw_segment(ax,-4.5,2,-4.5,1.2,color="#222222")
    draw_segment(ax,4.5,2,4.5,1.2,color="#222222")
    ax.add_patch(patches.Rectangle((-5.2, 0.9),1.4,0.3,ec="#222222",fill=False))
    ax.add_patch(patches.Rectangle((3.8, 0.9),1.4,0.3,ec="#222222",fill=False))
    # 方块代表x
    ax.add_patch(patches.Rectangle((-4.8,1.0),0.6,0.6,color="#4078c0",alpha=0.5))
    ax.text(-4.5,1.3,"$x$",ha="center",va="center")
    ax.add_patch(patches.Circle((4.4,1.2),0.25,color="#f08000",alpha=0.5))
    ax.text(4.4,1.4,"$3$",ha="center")
    ax.set_title("天平平衡：$x = 3$",fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_balance_init.png")

def plot_balance_add(idx):
    fig, ax = new_figure(width=8, height=4)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,3)
    draw_segment(ax,-5,2,5,2,color="#222222")
    draw_dot(ax,0,2,color="#222222")
    draw_segment(ax,-4.5,2,-4.5,1.2,color="#222222")
    draw_segment(ax,4.5,2,4.5,1.2,color="#222222")
    ax.add_patch(patches.Rectangle((-5.2, 0.9),1.4,0.3,ec="#222222",fill=False))
    ax.add_patch(patches.Rectangle((3.8, 0.9),1.4,0.3,ec="#222222",fill=False))
    ax.add_patch(patches.Rectangle((-4.8,1.0),0.6,0.6,color="#4078c0",alpha=0.5))
    ax.add_patch(patches.Circle((-4.0,1.2),0.22,color="#e53935",alpha=0.4))
    ax.text(-4.0,1.4,"$+2$",ha="center")
    ax.add_patch(patches.Circle((4.4,1.2),0.25,color="#f08000",alpha=0.5))
    ax.add_patch(patches.Circle((5.2,1.2),0.22,color="#e53935",alpha=0.4))
    ax.text(5.2,1.4,"$+2$",ha="center")
    ax.set_title("两边同时加2，等式依然成立 $x+2=3+2$",fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_balance_add.png")

def plot_balance_mul(idx):
    fig, ax = new_figure(width=8, height=4)
    ax.set_xlim(-6,6)
    ax.set_ylim(-1,3)
    draw_segment(ax,-5,2,5,2,color="#222222")
    draw_dot(ax,0,2,color="#222222")
    draw_segment(ax,-4.5,2,-4.5,1.2,color="#222222")
    draw_segment(ax,4.5,2,4.5,1.2,color="#222222")
    ax.add_patch(patches.Rectangle((-5.2, 0.9),1.4,0.3,ec="#222222",fill=False))
    ax.add_patch(patches.Rectangle((3.8, 0.9),1.4,0.3,ec="#222222",fill=False))
    ax.add_patch(patches.Rectangle((-4.8,1.0),0.6,0.6,color="#4078c0",alpha=0.5))
    ax.add_patch(patches.Rectangle((-4.1,1.0),0.6,0.6,color="#4078c0",alpha=0.5))
    ax.text(-4.4,1.3,"$2x$",ha="center",va="center")
    ax.add_patch(patches.Circle((4.2,1.2),0.25,color="#f08000",alpha=0.5))
    ax.add_patch(patches.Circle((5.0,1.2),0.25,color="#f08000",alpha=0.5))
    ax.text(4.6,1.4,"$2\\times3$",ha="center")
    ax.set_title("两边同时乘以2：$2x = 2\\times 3$",fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_balance_mul.png")

if __name__ == "__main__":
    plot_balance_init(0)
    plot_balance_add(1)
    plot_balance_mul(2)