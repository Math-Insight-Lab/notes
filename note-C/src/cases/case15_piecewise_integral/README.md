# case15 Piecewise Integral 分段函数分段积分

## 专题简介
处理分段函数或多区域情况，正负面积分别计算、累加。

## 前置依赖
- 前置学习：case14 Interval Flip
- 后续依赖：case16 Accumulation Function

## 学习目标
理解分段区域积分；正负面积独立累加。

## 核心概念
1. 分段积分：每段独立计算
2. 区域合并：按符号分别处理
3. 净面积：正负区域的代数和


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
1. $f(x)=sin(x)$ 在 [0,2pi]，天然分段
2. 正区域蓝、负区域红
3. 累积积分曲线

## 输出产物

### 第 1 组：分段区域图

**说明：** f(x)=sin(x) 在 [0,2π] 上，[0,π] 正面积蓝色填充（+），[π,2π] 负面积红色填充（-），橙色虚线标注分界点 x=π。

**包含文件：**

- `piecewise_regions.png`

**关系/意义：** 展示"分段处理"：将积分区间在正负分界处切开，分别计算正负面积。

### 第 2 组：累积示意图

**说明：** f(x) 曲线与x轴围成的区域整体展示，蓝色半透明填充正负区域，帮助学生理解分段积分如何"累加"。

**包含文件：**

- `cumulative.png`

**关系/意义：** 将分段图转化为"累积"视角，为case16的变上限积分函数做铺垫。
