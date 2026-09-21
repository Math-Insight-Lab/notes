# Copyright © Math‑Insight‑Lab
# SPDX‑License‑Identifier: MIT
# plot.py case15 model_scenario 简单实际问题数学建模
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark
import os


# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def plot_motion_model(idx):
    fig, ax = new_figure(width=7, height=5)
    t = np.linspace(0,5,200)
    v_const = 2
    s = v_const * t
    ax.plot(t,s,color="#222222",lw=2,label="$s=2t$ 路程（累积总量）")
    ax.text(1,8,"速率=2（变化快慢恒定）",fontsize=11)
    ax.set_xlabel("时间 t")
    ax.set_ylabel("路程 s")
    ax.set_title("运动建模：变化快慢（速率）与累积得到总路程",fontsize=12)
    ax.grid(True, alpha=0.25)
    ax.legend()
    add_watermark(ax)
    save_fig(fig, f"assets/frame_{idx:02d}_model_motion.png")

if __name__ == "__main__":
    plot_motion_model(0)