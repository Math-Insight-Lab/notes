# case14 Interval Flip 积分上下限翻转符号变化

## 专题简介
积分上下限互换，结果反号。可视化展示为什么交换上下限会改变符号。

## 前置依赖
- 前置学习：case13 Integral Sign and Region
- 后续依赖：case15 Piecewise Integral

## 学习目标
理解上下限与积分符号的关系；直观看到方向与正负的关联。

## 核心概念
1. 积分方向：从a到b为正方向，从b到a为负方向
2. 上下限互换：积分结果变号
3. 方向性与物理运动类比


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
1. 同图展示正向积分（蓝，结果为正）和反向积分（红，结果为负）
2. 用箭头标示积分方向

## 输出产物

### 第 1 组：正向积分图

**说明：** ∫₀ᵖⁱ sin(x)dx = 2，蓝色填充区域，积分从左到右（下限0→上限π）。

**包含文件：**

- `forward.png`

**关系/意义：** 三组图中的第一个：展示正常方向的积分。

### 第 2 组：反向积分图

**说明：** ∫ᵖⁱ⁰ sin(x)dx = -2，红色填充区域，上方红色双向箭头表示方向反转（从π到0），积分结果为负。

**包含文件：**

- `reversed.png`

**关系/意义：** 三组图中的第二个：与正向图对照，面积相同但符号相反，说明"交换上下限改变积分符号"。

### 第 3 组：正反向对比图

**说明：** 左右并排展示正向积分（=2，蓝色）和反向积分（=-2，红色），两张图共享同一曲线但方向相反。

**包含文件：**

- `comparison.png`

**关系/意义：** 将前两张图合并对比，让学生一眼看到"同一块面积，方向不同符号不同"。
