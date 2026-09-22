# Math‑Insight‑Lab · notes

> **数理直觉随笔集** | note‑A · note‑B · note‑C

[![license‑code](https://img.shields.io/badge/code‑MIT‑blue.svg)](https://opensource.org/licenses/MIT)
[![license‑content](https://img.shields.io/badge/content‑CC_BY_NC_4.0‑orange.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

这不是成套正规教材，是一整套**数理直觉随笔集**。
核心理念：**先看图建立直观感受，之后再去啃课本上的定义、符号、刷题。**

阅读参考顺序：`note‑A（小学5‑6） → note‑B（初中） → note‑C（高中）`
> 也可以随便挑感兴趣的篇章跳读，不用死板按顺序。

> ⚠️ 协议说明
> - ✅ `src/**/*.py` 绘图源码：MIT，可以商用，保留版权声明即可
> - 🚫 所有 md 讲义、习题、dist 下生成的图片素材：CC BY‑NC 4.0（署名‑非商用）
>
> 图片自带水印 `math‑insight‑lib`，禁止商用、禁止去水印后二次分发。

## 外部依赖

- `calc‑insight‑kit`：统一绘图、水印工具库，独立仓库。
  安装方式：`pip install git+https://github.com/Math-Insight-Lab/calc-insight-kit.git`
- `logic‑opt‑kit`：预留习题、符号计算工具，尚在规划。

## 仓库目录

```
notes/
├── README.md
├── pyproject.toml
├── .gitignore
├── note-A/
│   ├── README.md
│   ├── src/cases/      # plot.py 绘图源码 (MIT)
│   └── dist/cases/     # 对外阅读：讲义、图片素材 (CC-BY-NC 4.0)
├── note-B/
│   ├── README.md
│   ├── src/cases/
│   └── dist/cases/
└── note-C/
    ├── README.md
    ├── src/cases/
    └── dist/cases/
```

## 📖 各分册随笔简介

### note‑A｜小学数理随笔

面向五六年级。不讲复杂公式，重在思维感受。
一组小随笔，种下底层直觉：分割累加、无限细分、变化快慢、快慢与总量的互相转换。
以看图思考为主，不需要大量刷题。

包含 12 篇随笔小专题：

01 area_accumulate｜矩形小块铺满｜分割累加的朴素感觉
02 circle_split｜圆分割拼接｜体会化曲为直
03 irregular_grid｜不规则图形网格铺满｜曲线也可以小块拼出来
04 curve_trend｜曲线快慢变化｜看懂陡和缓
05 wave_curve｜起伏波动曲线｜感受时快时慢
06 growth_compare｜匀速 vs 加速增长
07 square_dot｜平方数点阵｜离散的累加
08 square_scale｜正方形边长缩放｜一个量带动另一个量变
09 fraction_split｜图形等分拆分｜越切越细小
10 triangle_height｜三角形高变化｜几何量的连续联动
11 unify_integral｜积分大一统｜不管什么曲线，都可以切小块累加
12 avg_inst_mutual｜平均‑瞬时与互逆｜快慢 ↔ 总量，本册随笔收官

> 读完大概收获：脑子里建立图像感，对"分割、逼近、变化"有直观体会，给初中做思维铺垫。

---

### note‑B｜初中数理随笔

贴合初中课内知识，随笔里顺带埋好微积分前置直觉。
跟着课本知识点走，悄悄引入增量 Δ、平均变化率、割线、离散累加、"无限靠近但不等于"这些想法。
不超纲，不提前硬塞高中公式，只是多一层几何视角。

一共 16 篇随笔小专题

**七上基础**
01 number_line 数轴跳动｜有理数、绝对值几何感受
02 area_identity 面积拼图｜完全平方、平方差
03 balance_scale 天平动画｜等式和一元一次方程
04 coord_walk 坐标系点行走｜平面直角坐标系

**七下~九年级拓展**
05 negative_geom 负数与绝对值拓展｜带方向的增量
06 polynomial_geom 多项式拼图｜整式与因式分解
07 linear_system 二元一次方程组｜直线相交看解
08 inequality_vis 不等式可视化｜看懂区间和边界
09 function_linear 一次函数｜重点感受平均变化率
10 quadratic_geom 二次函数｜非线性、割线一点点靠近
11 similar_triangle 相似三角形｜比例与局部近似
12 circle_geom 圆｜切线的直观感受
13 stat_prob 统计概率｜离散数据的累加平均
14 variation 变量专题｜把整体拆成小块再求和
15 model_scenario 现实小建模｜变化快慢 vs 累积总量
16 boundary_mistake 易错边界梳理｜专门理清"趋近不等于等于"

> 读完大概收获：掌握初中课内知识的同时，心里已经备好了可以衔接高中微积分的直觉。

---

### note‑C｜高中数理随笔｜微积分直觉篇

> 本随笔集的核心篇章，不完全照搬教材刷题顺序。
> 阅读路径：几何面积感受极限 → 抽象极限 → 导数（变化快慢） → 积分（累积总量）→ 抛出 FRC 互逆猜想。
> 注意：这只是随笔，重在建立直观，不等同于严谨高中教科书。

16 篇随笔小专题

**几何具象极限（先用面积感受极限）**
01 Rectangular Approximation｜矩形细分逼近曲边面积
02 Error Convergence｜细分越多误差越小

**抽象极限**
03 Function Limit｜函数趋近某个点
04 Series Convergence｜数列无穷累加

**导数专题：瞬时变化快慢**
05 Secant to Tangent｜割线一点点逼近切线
06 Tangent Slope｜切线斜率就是瞬时变化
07 Derivative Sign → Monotonicity｜导数正负看增减
08 Derivative Magnitude｜导数大小看变化有多猛

**积分专题：累积总量 + FTC 猜想收尾**
09 Left Riemann Sum｜左黎曼矩形
10 Right Riemann Sum｜右黎曼矩形
11 Area Convergence｜细分之后面积收敛
12 Trapezoid Approximation｜梯形近似
13 Integral Sign Regions｜积分正负，上下面积抵消
14 Interval Flip｜积分区间翻转
15 Piecewise Integration｜分段积分
16 Accumulation Function｜累积函数，抛出微积分互逆猜想（本册随笔收官）

> 读完大概收获：在脑海建立极限、导数、积分的几何画面；埋下互逆猜想，之后再去学习高中教材的严格定义。

## 📂 工作流

1. 在 `src/cases/xxx` 修改随笔文档和绘图脚本
2. 运行 `python plot.py` 生成带水印图片（直接输出到 `src/cases/xxx/` 目录）
3. 将 `src/cases/xxx/README.md` 和 `src/cases/xxx/tasks.md` 复制到 `dist/cases/xxx/` 对应目录
4. 将生成的 `frame_*.png` 图片复制到 `dist/cases/xxx/assets/`
5. 提交 src 和 dist；`src/cases/*/assets/` 下的临时构建图片不会被 git 跟踪

> 本地临时生成图片被 `.gitignore` 过滤，只提交 dist 下的最终产物。

## 🧭 使用小提示

- 不必从头读到尾，感兴趣的随笔专题可以直接跳过去看。
- 每个专题分为基础任务 + 前瞻思考；**前瞻只需要想一想，不用严格证明、不用追求标准答案。**
- 两种打开方式：
  - 看成品：直接打开 `dist/`，看图片 + 文字，不需要运行代码
  - 动手玩：运行 `src/` 下面 `plot.py`，改参数，自己观察图形变化

## 🔗 相关链接

- calc‑insight‑kit：https://github.com/Math-Insight-Lab/calc-insight-kit

> 纯属个人随手写的**数理直觉随笔集**，无答疑服务。
