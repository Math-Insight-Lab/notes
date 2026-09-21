# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case13 stat_prob 初中统计与概率直观模拟
import numpy as np
from calc_insight_kit import new_figure, save_fig, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_stat_bar(idx):
    fig, ax = new_figure(width=7, height=4.5)
    data = [3,5,4,6,2]
    xs = np.arange(len(data))
    mean_val = np.mean(data)
    ax.bar(xs, data, color="#4078c0", alpha=0.6)
    ax.axhline(y=mean_val, color="#f08000", lw=2, linestyle="--", label=f"平均数 = {mean_val:.2f}")
    ax.set_xticks(xs)
    ax.set_ylabel("数值")
    ax.set_title("离散数据柱状图与平均数参考线", fontsize=12)
    ax.grid(True, alpha=0.25)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_stat_bar_mean.png")

if __name__ == "__main__":
    plot_stat_bar(0)