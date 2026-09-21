# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case05 wave_curve 起伏波动曲线|忽快忽慢的变化
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark

def plot_wave(scale, idx):
    fig, ax = new_figure(width=7, height=4.5)
    x = np.linspace(0,20,300)
    y = np.sin(x / scale)*2 + 3
    ax.plot(x,y,color="#222222",lw=2)
    ax.set_xlim(0,20)
    ax.set_ylim(0,6)
    ax.set_title(f"波动周期缩放 {scale:.1f}", fontsize=12)
    ax.axis("off")
    add_watermark(ax)
    save_fig(fig, f"frame_{idx:02d}_s{scale:.1f}.png")

if __name__ == "__main__":
    for idx,s in enumerate([3.5,2.5,1.5]):
        plot_wave(s, idx)
