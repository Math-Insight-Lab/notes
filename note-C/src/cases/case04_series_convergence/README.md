# case04 Series Convergence 数列无穷累积极限收敛

## 专题简介
从连续函数极限转向离散无穷过程：无穷级数。可视化部分和序列，直观看到不断累加，总和趋近固定常数。

## 前置依赖
- 前置学习：case03 Function Limit
- 后续依赖：case05 Secant to Tangent

## 学习目标
理解无穷级数是无穷多项相加；部分和 $S_n$ 是前n项累加；观察部分和逐步靠近收敛值。

## 核心概念
1. 部分和 $S_n$：级数前n项相加
2. 级数收敛：n趋向无穷时，部分和趋近一个固定常数


## 环境配置

运行本例需要 Python 3.8+，以下安装命令跨平台兼容（Windows / macOS / Linux 均适用）：

### 1. 安装 Python 依赖

安装 matplotlib、numpy 和 sympy（三选一即可）：

```bash
pip install numpy matplotlib sympy
```

如果尚未安装 Python，请访问 <https://www.python.org/downloads/> 下载安装。

### 2. 安装 calc-insight-kit 工具库（可选）

本例使用的 `calc_insight_kit` 可视化库可从 GitHub 获取：

```bash
# 方法 A：直接安装 GitHub 最新版
pip install git+https://github.com/Math-Insight-Lab/calc-insight-kit.git

# 方法 B：克隆本地后安装
git clone https://github.com/Math-Insight-Lab/calc-insight-kit.git
cd calc-insight-kit
pip install -e .
```

### 3. 验证安装

运行以下命令确认一切正常：

```bash
python -c "import matplotlib; import numpy; import sympy; print('所有依赖已就绪')"
```

如输出 `所有依赖已就绪` 即表示安装成功。

### 4. 可选：安装 Maxima（高级用户）

如需使用 Maxima 作为额外 CAS 后端，请参考 [calc-insight-kit 安装文档](https://github.com/Math-Insight-Lab/calc-insight-kit) 中的 Maxima 安装指南。默认使用 SymPy 后端，无需安装 Maxima 即可运行所有示例。

---

## 运行方法

```bash
python plot.py
```

运行后生成的图片保存在 `assets/` 目录中。

## 可视化绘图要点
1. 选用等比级数 $\sum 1/2^n$，收敛到1
2. 绘制散点图横轴n纵轴$S_n$
3. 画水平虚线标记收敛值1

## 输出产物

### 第 1 组：部分和逐步展开序列（6帧）

**说明：** 展示级数 S_n = 1 - 1/2^n 的部分和如何逐步逼近收敛值1。帧中 n 的上限依次为 1, 2, 4, 8, 16, 32，蓝色散点逐渐密集地挤向 y=1 的橙色虚线。

**包含文件：**

- `frame_00_n1.png`
- `frame_01_n2.png`
- `frame_02_n4.png`
- `frame_03_n8.png`
- `frame_04_n16.png`
- `frame_05_n32.png`

**关系/意义：** 6帧构成一个递进序列：每增加一帧，显示的项数翻倍，直观显示"项越多，部分和越稳定"。

### 第 2 组：各项大小柱状图

**说明：** 展示级数的前8项 1/2, 1/4, 1/8, ... 的各自大小，直观显示每项越来越小。

**包含文件：**

- `series_bar.png`

**关系/意义：** 解释"为什么能收敛"：因为各项快速趋近于0，累加不会发散。
