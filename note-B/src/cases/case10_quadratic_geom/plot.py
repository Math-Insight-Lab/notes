# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case10 quadratic_geom 二次函数几何直观【核心内嵌：非线性变化与趋近】
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def f(x):
    return x**2

def plot_secant_frame(dx, idx):
    fig, ax = new_figure(width=7, height=5)
    xs = np.linspace(-0.5, 2.5, 200)
    ys = f(xs)
    ax.plot(xs, ys, color="#222222", lw=2, label="$y=x^2$")
    xp = 1
    yp = f(xp)
    xq = xp + dx
    yq = f(xq)
    # 割线
    k_sec = (yq - yp)/dx
    xl = np.linspace(-0.2, 2.7,100)
    yl = yp + k_sec*(xl - xp)
    ax.plot(xl, yl, color="#4078c0", lw=2, label=f"割线，斜率={k_sec:.2f}")
    draw_dot(ax, xp, yp, color="#e53935", label="$P(1,1)$")
    draw_dot(ax, xq, yq, color="#4078c0", label=f"Q({xq:.2f},{yq:.2f})")
    ax.set_xlim(-0.5,2.5)
    ax.set_ylim(0,6)
    ax.grid(True, alpha=0.25)
    ax.set_title(f"二次函数，Q向P靠近，$\Delta x={dx:.2f}$", fontsize=12)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_dx{dx}.png")

if __name__ == "__main__":
    for i,dx in enumerate([1.0, 0.4, 0.1]):
        plot_secant_frame(dx,i)