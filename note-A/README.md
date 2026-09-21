# note-A 小学数理随笔

面向小学5-6年级，**只做图形化思维感知，不讲授微积分公式与计算**。
为 note-B 初中数理直觉做前置启蒙。

**四大核心直觉目标**
1. 分割-累加直觉：整体拆成细小单元，小块相加还原总量（积分原型）
2. 无限细分-逼近直觉：切分越细小，近似结果越接近真实
3. 变化快慢直觉：图形陡峭/平缓对应变化速度不同（导数原型）
4. 互逆直觉：变化快慢（微分）与总量累积（积分）可以来回转换

**完整学习链路：note-A → note-B → note-C**
> note-A（小学5-6）：启蒙四大底层直觉
> note-B（初中）：代数几何、Δ增量、割线、离散累积，微积分前置
> note-C（高中）：极限-导数-积分直观随笔

## case清单（共12个）

| # | Case | 主题 | 核心直觉 |
|---|------|------|----------|
| 01 | case01_area_accumulate | 矩形小块铺满 | 分割-累加（积分原型） |
| 02 | case02_circle_split | 圆分割拼接 | 化曲为直，逼近思想 |
| 03 | case03_irregular_grid | 不规则图形网格铺满 | 曲线图形累加 |
| 04 | case04_curve_trend | 曲线快慢变化 | 变化率雏形 |
| 05 | case05_wave_curve | 起伏波动曲线 | 忽快忽慢的变化 |
| 06 | case06_growth_compare | 匀速vs加速增长对比 | 不变与变快的区分 |
| 07 | case07_square_dot | 平方数点阵 | 离散单元累积 |
| 08 | case08_square_scale | 正方形边长缩放 | 变量连续改变 |
| 09 | case09_fraction_split | 图形分数等分拆分 | 无限细分感知 |
| 10 | case10_triangle_height | 三角形高变化 | 输入输出连续联动 |
| 11 | case11_unify_integral | 积分大一统 | 所有面积 = 小矩形累加 |
| 12 | case12_avg_inst_mutual | 平均-瞬时与互逆 | 微分积分来回转换 |

## 统一绘图规范（src下所有case的plot.py遵守）
1. 导入：`from calc_insight_kit import new_figure, save_fig, draw_dot, draw_segment, add_watermark`
2. 画布：浅灰色网格，适合讲义导出png/svg
3. 序列图命名规则：`frame_00.png, frame_01.png …`
4. 配色规范（沿用calc-insight-kit常量）
    - 基础曲线：#222222
    - 填充几何：#4078c0
    - 警示/误差：#e53935
    - 辅助线：#f08000
5. dpi=300，绘图完成调用`add_watermark(ax)`，水印`math-insight-lib`

## 学习使用建议
- 可单独选case；推荐按序号完整顺序学习
- tasks.md分为【基础任务】和【前瞻探究任务】；本阶段以看图思考为主，不需要复杂计算。

## License 协议区分
- `src/*.py`绘图源代码：**MIT License**，保留版权声明，可商用。
- Markdown讲义、tasks.md习题、dist目录全部图片素材：**CC BY-NC 4.0（署名-非商用）**。
图片右下角嵌入水印 `math-insight-lib`，未经许可禁止商用、去除水印后二次分发。
