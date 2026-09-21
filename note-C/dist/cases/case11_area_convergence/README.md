# case11 Area Convergence 不同n下黎曼和面积收敛可视化

## 专题简介
将多帧黎曼和并排展示，直观对比n变化带来的逼近效果改善。

## 前置依赖
- 前置学习：case09, case10
- 后续依赖：case12 Trapezoid Sum

## 学习目标
对比不同n值的逼近效果；观察收敛趋势。

## 核心概念
1. 并排对比：直观展示逼近改进
2. 收敛曲线：数值上量化收敛速度


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
1. $f(x)=sin(x)$ 在 [0,3]
2. 四宫格 n=2,4,8,16
3. 收敛折线图

## 输出产物

### 第 1 组：四宫格对比图

**说明：** f(x)=sin(x) 在 [0,3] 上（注意：实际代码中 b=3，不是 π），将 n=2, 4, 8, 16 四种矩形数并列展示在同一张图中（四宫格），每格显示当前矩形数和左矩形黎曼和面积近似值。注意 sin(x) 在 [0,3] 上始终非负（3<π≈3.14），因此所有矩形都在 x 轴上方。

**包含文件：**

- `convergence_series_4panel.png.png`

**关系/意义：** 四宫格将case01的5帧压缩为一张图——但注意：case01用 f(x)=x²，case11用 f(x)=sin(x)，函数不同。四宫格适合做讲义插图或PPT展示，横向对比不同n的效果。

### 第 2 组：收敛曲线图

**说明：** n=2,4,8,...,256 时左矩形黎曼和的收敛路径（横轴n，纵轴和值），蓝色折线逼近真实值 1-cos(3) ≈ 1.879。注意：这个横坐标是 n 值，不是 x 值，因此它显示的是一条从左到右上升的折线，与frame图中的函数曲线形态完全不同。

**包含文件：**

- `conv_curve.png`

**关系/意义：** 与四宫格的关系：四宫格展示"图形变化"（每格内函数曲线+矩形），收敛曲线展示"数值变化"（横轴是n，纵轴是面积值）。两者互补，一个看形一个看数。
