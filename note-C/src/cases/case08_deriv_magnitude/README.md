# case08 Derivative Magnitude 导数大小变化快慢匹配

## 专题简介
导数的符号决定增减；绝对值大小决定变化快慢。

## 前置依赖
- 前置学习：case07 Derivative Sign -> Monotonicity
- 后续依赖：case09 Left Riemann Sum

## 学习目标
区分导数符号（增减方向）与导数绝对值（变化快慢）。

## 核心概念
1. |f'(x)| 越大：切线越陡，函数变化越快
2. |f'(x)| 越小：切线越平缓，函数变化越慢


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
1. $f(x)=sin(x)$，区间 $[0,2\pi]$
2. 多帧移动切点，展示切线倾斜程度变化

## 输出产物

### 第 1 组：各点切线倾斜度序列（5帧）

**说明：** f(x)=sin(x)，在 x=0, π/2, π, 3π/2, 2π 五点各画一条切线。切线越陡峭处 |f'(x)| 越大（x=0和π处最陡），切线水平处 |f'(x)| 越小（x=π/2和3π/2处为0）。

**包含文件：**

- `frame_00_x0.0.png`
- `frame_01_x1.6.png`
- `frame_02_x3.1.png`
- `frame_03_x4.7.png`
- `frame_04_x6.3.png`

**关系/意义：** 5帧沿正弦波从左到右移动，展示切线陡度与导数大小的对应关系。

### 第 2 组：陡度总览图

**说明：** 同时绘制 f(x)=sin(x) 和 f'(x)=cos(x)，展示函数最陡处对应导数绝对值最大。

**包含文件：**

- `steepness_overview.png`

**关系/意义：** 将5帧的观察汇总为一图，让学生理解"导数的大小 = 曲线的陡峭程度"。
