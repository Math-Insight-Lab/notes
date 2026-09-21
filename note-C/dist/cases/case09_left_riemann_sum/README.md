# case09 Left Riemann Sum 左矩形求和逼近曲边面积

## 专题简介
将黎曼和具体化为左端点矩形：每个小区间取左端点函数值作为矩形高度。

## 前置依赖
- 前置学习：case05 Secant to Tangent (极限直觉)
- 后续依赖：case10 Right Riemann Sum

## 学习目标
理解左端点黎曼和的构造方式；观察n增大时逼近效果；比较左右差异。

## 核心概念
1. 左端点黎曼和：每个小区间用左端点函数值做高
2. 逼近：n越大，矩形和越接近真实面积
3. 左右差异：单调函数左右和存在上下界差异


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
1. $f(x)=x^2$ 在 [0,2]，单调递增
2. 多帧展示 n=4,8,16 的左和
3. 对比图：左和(蓝) vs 右和(红)

## 输出产物

### 第 1 组：左矩形序列（3帧）

**说明：** f(x)=x² 在 [0,2] 上的左矩形黎曼和，n=4, 8, 16。蓝色矩形从曲线下方向上填充，每个矩形的顶边取左端点高度。

**包含文件：**

- `frame_00_n4.png`
- `frame_01_n8.png`
- `frame_02_n16.png`

**关系/意义：** 3帧展示n增大时左矩形总和如何逼近真实面积。

### 第 2 组：左右矩形对比（2帧）

**说明：** n=4 和 n=8 时左矩形（蓝色，低估）与右矩形（红色，高估）在同一图中叠加对比。

**包含文件：**

- `compare_n4.png`
- `compare_n8.png`

**关系/意义：** 对比展示"左矩形偏小、右矩形偏大"的原因：f(x)=x² 单调递增时，左端点总是取较小值，右端点总是取较大值。n 增大时左右差距缩小。
