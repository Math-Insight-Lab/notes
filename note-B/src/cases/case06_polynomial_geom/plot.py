# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case06 polynomial_geom 多项式乘法几何拼图｜从整式到因式分解
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import matplotlib.patches as patches
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_poly_mul(idx):
    a = 2.2
    m = 1.0
    b = 1.8
    n = 1.2
    fig, ax = new_figure(width=6.2, height=5.5)
    ax.set_xlim(0, a+m+0.3)
    ax.set_ylim(0, b+n+0.3)
    ax.add_patch(patches.Rectangle((0,0), a+m, b+n, fill=False, ec="#222222", lw=2))
    ax.axvline(x=a, c="#888888", lw=1)
    ax.axhline(y=b, c="#888888", lw=1)

    ax.add_patch(patches.Rectangle((0,0),a,b,color="#4078c0",alpha=0.4))
    ax.add_patch(patches.Rectangle((a,0),m,b,color="#f08000",alpha=0.35))
    ax.add_patch(patches.Rectangle((0,b),a,n,color="#e53935",alpha=0.35))
    ax.add_patch(patches.Rectangle((a,b),m,n,color="#70b850",alpha=0.35))

    ax.text(a/2, b/2, "$ab$", ha="center", va="center", fontsize=12)
    ax.text(a+m/2, b/2, "$mb$", ha="center", va="center", fontsize=11)
    ax.text(a/2, b+n/2, "$an$", ha="center", va="center", fontsize=11)
    ax.text(a+m/2, b+n/2, "$mn$", ha="center", va="center", fontsize=11)

    ax.set_title("$(a+m)(b+n)=ab+an+mb+mn$", fontsize=13)
    ax.set_aspect("equal")
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_poly_mul.png")

if __name__ == "__main__":
    plot_poly_mul(0)