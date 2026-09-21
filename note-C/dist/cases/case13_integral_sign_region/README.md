# case13 Integral Sign and Region 积分符号与区域关系

## 专题简介
积分不仅仅是面积，而是"有符号面积"。曲线在轴上方贡献正面积，在下方贡献负面积。

## 前置依赖
- 前置学习：case12 Trapezoid Sum
- 后续依赖：case14 Interval Flip

## 学习目标
理解积分的符号含义；看到正负区域互相抵消。

## 核心概念
1. 正面积：曲线在x轴上方，积分>0
2. 负面积：曲线在x轴下方，积分<0
3. 净面积：正负区域代数和


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
1. $f(x)=sin(x)$ 在 [0,2pi]
2. 上图：正面积蓝色填充
3. 中图：负面积红色填充
4. 下图：正负混合，净积分为0

## 输出产物

### 第 1 组：正面积图

**说明：** f(x)=sin(x) 在 [0,π] 上，曲线与x轴之间的区域用蓝色填充，标注 "+ area"，展示正面积对应正积分。

**包含文件：**

- `positive_area.png`

**关系/意义：** 三组图的第一个：展示"曲线在x轴上方时积分为正"。

### 第 2 组：负面积图

**说明：** f(x)=sin(x)-1.2 在 [0,2π] 上，整个曲线在x轴下方，区域用红色填充，标注 "- area"，展示负面积对应负积分。

**包含文件：**

- `negative_area.png`

**关系/意义：** 三组图中的第二个：与正面积图对照，展示"曲线在x轴下方时积分为负"。

### 第 3 组：混合区域图

**说明：** f(x)=sin(x) 在 [0,2π] 上，[0,π] 蓝色正面积与 [π,2π] 红色负面积叠加。两者相等，净积分 = 0。

**包含文件：**

- `mixed_area.png`

**关系/意义：** 三组图的综合：正负面积相互抵消，说明定积分是"有符号的面积"而非简单的总面积。
