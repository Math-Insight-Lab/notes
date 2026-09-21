# case05 Secant to Tangent 割线动态逼近切线全过程

## 专题简介
正式进入导数模块。曲线上两个点不断靠近，两点连成的割线逐步旋转逼近切线。

## 前置依赖
- 前置学习：case04 Series Convergence
- 后续依赖：case06 Tangent Slope

## 学习目标
认识割线、切线；观察两点不断靠近，割线逐渐逼近切线。

## 核心概念
1. 割线：曲线上两个不同点相连的直线，代表平均变化率
2. 切线：曲线在单点处的直线，由割线取极限得到
3. dx趋近0，割线逐步趋近切线


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
1. $f(x)=x^2$，定点 $P(1,1)$，动点Q向P靠近
2. 生成多帧：Q从x=2逐步靠近1
3. 黑色：原曲线；蓝色：割线；橙色：切线

## 输出产物

### 第 1 组：割线逼近切线序列（5帧）

**说明：** 在 f(x)=x² 的 P(1,1) 点，割线另一端 Q 从 dx=1.0 逐步靠近 P（dx=0.5→0.2→0.1→0.05）。每帧显示割线（蓝色实线，标注斜率）和切线（橙色虚线），直观展示割线如何"旋转"到切线位置。

**包含文件：**

- `frame_00_dx1.00.png`
- `frame_01_dx0.50.png`
- `frame_02_dx0.20.png`
- `frame_03_dx0.10.png`
- `frame_04_dx0.05.png`

**关系/意义：** 5帧是"从粗到精"的逼近过程：dx 越大割线与切线差异明显，dx 越小割线越贴近切线，直观理解导数是"割线斜率的极限"。

### 第 2 组：最终切线图

**说明：** 仅显示 f(x)=x² 及其在 x=1 处的切线，作为动画的终点/结论图。

**包含文件：**

- `tangent_final.png`

**关系/意义：** 动画的终点——去掉割线、只留切线，回答"切线到底是什么"。
