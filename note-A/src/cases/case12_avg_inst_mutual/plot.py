# Copyright © Math-Insight-Lab
# SPDX-License-Identifier: MIT
# plot.py case12 avg_inst_mutual 平均-瞬时与互逆|微分积分来回转换
import numpy as np
from calc_insight_kit import new_figure, save_fig, draw_dot, add_watermark
import matplotlib.patches as patches

def s(t):
    r"""路程 s = t^2"""
    return t**2

def v(t):
    r"""对应瞬时速度 v=2*t"""
    return 2*t

def plot_mutual_frame(dt, idx):
    fig, (ax_left, ax_right) = new_figure(nrows=1, ncols=2, width=10, height=4.8)
    t0 = 1.5
    t1 = t0 + dt
    t_range = np.linspace(0,3,200)
    # -------- 左图：微分视角 路程曲线，割线逼近瞬时速度 --------
    s_arr = s(t_range)
    ax_left.plot(t_range, s_arr, color="#222222", lw=2, label="s(t)=t^2 路程")
    draw_dot(ax_left, t0, s(t0), color="#4078c0")
    draw_dot(ax_left, t1, s(t1), color="#e53935")
    ax_left.plot([t0,t1],[s(t0),s(t1)], color="#f08000", lw=2)
    v_avg = (s(t1)-s(t0)) / dt
    ax_left.set_title(f"【微分视角】Δt={dt:.3f}，平均速度={v_avg:.2f}", fontsize=11)
    ax_left.set_xlim(0,3)
    ax_left.set_ylim(0,9)
    ax_left.grid(True, alpha=0.25)
    ax_left.legend(fontsize=9)

    # -------- 右图：积分视角 速度小块累加得到总路程 --------
    v_arr = v(t_range)
    ax_right.plot(t_range, v_arr, color="#222222", lw=2, label="v(t)=2t 速度")
    n_seg = int(3.0 / dt)
    total_sum = 0.0
    for i in range(n_seg):
        ti = i*dt
        vi = v(ti)
        rect = patches.Rectangle((ti,0), dt, vi, color="#4078c0", alpha=0.35)
        ax_right.add_patch(rect)
        total_sum += vi*dt
    ax_right.set_title(f"【积分视角】小段速度累加，估算总路程≈{total_sum:.2f}", fontsize=11)
    ax_right.set_xlim(0,3)
    ax_right.set_ylim(0,7)
    ax_right.grid(True, alpha=0.25)
    ax_right.legend(fontsize=9)

    add_watermark(ax_left)
    add_watermark(ax_right)
    save_fig(fig, f"frame_{idx:02d}_dt{dt:.3f}.png")

if __name__ == "__main__":
    for i,dt in enumerate([0.8,0.3,0.08]):
        plot_mutual_frame(dt,i)
