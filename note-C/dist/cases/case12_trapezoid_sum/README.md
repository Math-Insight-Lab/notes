# case12 Trapezoid Sum 梯形求和比矩形更精确

## 专题简介
梯形近似比矩形更接近曲线：每个小区间用梯形代替矩形。

## 前置依赖
- 前置学习：case11 Area Convergence
- 后续依赖：case13 Integral Sign and Region

## 学习目标
理解梯形求和法；比较梯形与矩形精度差异。

## 核心概念
1. 梯形求和：每个小区间用梯形（斜顶）代替矩形（平顶）
2. 精度提升：梯形更贴合曲线，误差更小
3. 梯形公式：(上底+下底)*高/2


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
1. $f(x)=x^2$ 在 [0,2]
2. 多帧 n=2,4,8 的梯形近似
3. 对比图：矩形(蓝) vs 梯形(橙)

## 输出产物

### 第 1 组：梯形求和序列（3帧）

**说明：** f(x)=x² 在 [0,2] 上，n=2, 4, 8 时的梯形近似。每个小区间用梯形（蓝色）代替矩形，顶边沿曲线倾斜。

**包含文件：**

- `frame_00_n2.png`
- `frame_01_n4.png`
- `frame_02_n8.png`

**关系/意义：** 3帧展示梯形法随n增大的逼近过程。

### 第 2 组：矩形 vs 梯形对比

**说明：** n=4 时，蓝色矩形（左和）与橙色梯形叠加对比。梯形紧密贴合曲线，矩形在曲线下方或上方留有空隙。

**包含文件：**

- `rect_vs_trap.png`

**关系/意义：** 直观展示"为什么梯形比矩形更精确"：梯形顶边沿曲线倾斜，减少了一阶误差。
