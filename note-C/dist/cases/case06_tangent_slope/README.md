# case06 Tangent Slope 切线斜率瞬时变化率原理

## 专题简介
割线斜率代表平均变化率；dx趋近0时，割线斜率的极限就是切线斜率（导数）。

## 前置依赖
- 前置学习：case05 Secant to Tangent
- 后续依赖：case07 Derivative Sign -> Monotonicity

## 学习目标
区分平均变化率和瞬时变化率；理解导数的几何含义就是切线斜率。

## 核心概念
1. 平均变化率：dy/dx，割线斜率
2. 瞬时变化率：在一点处的变化速率，由极限得到
3. 导数 f'(a)：等于该点切线斜率


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
1. $f(x)=x^2$，定点 $a=1$
2. 多帧图不断缩小dx
3. 汇总图：横轴dx，纵轴割线斜率，看到收敛曲线

## 输出产物

### 第 1 组：平均变化率收敛序列（5帧）

**说明：** 与case05相同图形设置（f(x)=x², dx从1.0到0.05），但每帧标题强调"平均变化率"，突出斜率数值的收敛。

**包含文件：**

- `frame_00_dx1.00.png`
- `frame_01_dx0.50.png`
- `frame_02_dx0.20.png`
- `frame_03_dx0.10.png`
- `frame_04_dx0.05.png`

**关系/意义：** 与case05的关系：case05侧重"几何"（割线变切线），case06侧重"代数"（斜率数值收敛到2）。同一组dx序列，不同教学视角。

### 第 2 组：斜率收敛散点图

**说明：** 将 dx=1.0, 0.5, 0.2, 0.1, 0.05, 0.01 对应的割线斜率绘制为散点，蓝色散点收敛到水平虚线 y=2。

**包含文件：**

- `slope_convergence.png`

**关系/意义：** 将5帧的斜率数值抽取出来做成散点图，从"看线"变为"看数"。
