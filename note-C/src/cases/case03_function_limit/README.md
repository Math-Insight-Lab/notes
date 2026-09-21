# case03 Function Limit 函数趋近定点极限

## 专题简介
从面积极限过渡到通用函数极限。当自变量 $x$ 不断靠近 $a$，函数值 $f(x)$ 无限靠近某个常数 $L$。

## 前置依赖
- 前置学习：case02 Error Convergence
- 后续依赖：case04 Series Convergence

## 学习目标
理解自变量趋近定点的含义；看懂左右两侧趋近；分清极限和函数值。

## 核心概念
1. 函数极限：$x$ 无限靠近 $a$ 时，$f(x)$ 无限靠近常数 $L$
2. 左极限：x从左侧向a逼近
3. 可去间断点：x=a处无定义但左右极限相等


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
1. 选用 $f(x)=(x^2-1)/(x-1)$，在 $x=1$ 处无定义，极限为2
2. 生成多帧展示x从左右两侧趋近1
3. 标记空心圆圈表示无定义；绘制水平虚线代表L=2

## 输出产物

### 第 1 组：左侧逼近序列（4帧）

**说明：** f(x) = (x²-1)/(x-1)，x 从左侧趋近于1（x=0→0.5→0.9→0.99）。每帧用红点标记当前 x 值对应的函数值，显示函数值趋近于2。

**包含文件：**

- `frame_left_00.png`
- `frame_left_01.png`
- `frame_left_02.png`
- `frame_left_03.png`

**关系/意义：** 展示"从左边无限接近"的过程。

### 第 2 组：右侧逼近序列（4帧）

**说明：** x 从右侧趋近于1（x=2→1.5→1.1→1.01）。同样用红点标记函数值，显示函数值趋近于2。

**包含文件：**

- `frame_right_00.png`
- `frame_right_01.png`
- `frame_right_02.png`
- `frame_right_03.png`

**关系/意义：** 展示"从右边无限接近"的过程。与左侧序列对比，理解"左右极限相等"的含义。

### 第 3 组：左右极限总览

**说明：** 完整函数图像，用空心圆圈标出 x=1 处的极限点 L=2（函数本身在此无定义），用橙色虚线标注极限值 y=2。

**包含文件：**

- `limit_overview.png`

**关系/意义：** 将左右逼近两序列合并为一幅总览图，展示"无论从哪边趋近，都到达同一个点"的极限本质。
