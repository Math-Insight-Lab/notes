# case16 Accumulation Function 累积函数积分上限函数

## 专题简介
从定面积过渡到变上限积分：F(x) = integral_a^x f(t)dt。累积函数本身也是一个函数，且 F'(x) = f(x)。

## 前置依赖
- 前置学习：case15 Piecewise Integral
- 后续依赖：无（最后一个case）

## 学习目标
理解变上限积分函数；看到面积函数本身可微。

## 核心概念
1. 累积函数 F(x)：从固定起点到x的面积
2. 基本定理：F'(x) = f(x)，积分和导数互为逆运算
3. 面积函数从曲线本身演化而来


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
1. 双轴图：上轴f(x)，下轴F(x)
2. 动画帧：逐步展开积分区域，观察累积面积增长
3. 展示F(x)与f(x)的对应关系

## 输出产物

### 第 1 组：累积动画序列（5帧）

**说明：** F(x) = ∫₀ˣ sin(t)dt 的逐步构造过程。a 从 0 逐步增大到 2π（a=0, π/2≈1.6, π≈3.1, 3π/2≈4.7, 2π≈6.3），每帧显示从0到a的积分区域（蓝色填充）和当前累积面积值。

**包含文件：**

- `accum_00_a0.0.png`
- `accum_01_a1.6.png`
- `accum_02_a3.1.png`
- `accum_03_a4.7.png`
- `accum_04_a6.3.png`

**关系/意义：** 5帧构成动画序列：蓝色填充区域从左向右"生长"，累积面积值随a变化——先增后减再增，直观展示变上限积分函数 F(x) 的"面积函数"本质。

### 第 2 组：原函数与累积函数对比

**说明：** 双轴图：上轴 f(x)=sin(x)，下轴 F(x)=∫₀ˣ sin(t)dt。展示 F'(x)=f(x) 的关系——F(x) 的斜率恰好是 f(x) 的高度。

**包含文件：**

- `f_and_F.png`

**关系/意义：** 将5帧动画的结论提炼为一张图："F是f的积分（累积面积）"，"f是F的导数（变化率）"。这是微积分基本定理的核心。
