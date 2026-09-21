# case07 Derivative Sign -> Monotonicity 导数正负函数增减联动

## 专题简介
建立导数符号与函数单调性之间的直观关联。

## 前置依赖
- 前置学习：case06 Tangent Slope
- 后续依赖：case08 Derivative Magnitude

## 学习目标
看懂导数正负与函数增减的对应关系；识别驻点。

## 核心概念
1. f'(x)>0：函数递增
2. f'(x)<0：函数递减
3. f'(x)=0：驻点，可能是极值


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
1. $f(x)=x^2-2x$，$f'(x)=2x-2$
2. 同图绘制原函数和导函数
3. 多帧沿曲线移动切点，展示切线斜率变化

## 输出产物

### 第 1 组：各点切线斜率序列（5帧）

**说明：** f(x)=x²-2x，在 x=0, 0.5, 1.0, 2.0, 3.0 五点各画一条切线。x<1 时导数负、切线向右下倾斜；x=1 时导数为0、切线水平；x>1 时导数正、切线向右上倾斜。

**包含文件：**

- `frame_00_x0.0.png`
- `frame_01_x0.5.png`
- `frame_02_x1.0.png`
- `frame_03_x2.0.png`
- `frame_04_x3.0.png`

**关系/意义：** 5帧从左到右沿曲线移动，展示切线斜率从负→零→正的变化，建立"导数符号决定增减"的直觉。

### 第 2 组：单调性总览图

**说明：** 同时绘制 f(x) 和 f'(x)，用蓝色半透明标注递减区间 x<1，红色半透明标注递增区间 x>1。

**包含文件：**

- `monotonic_overview.png`

**关系/意义：** 将5帧的分散观察汇总为一图，同时看到函数曲线和导数曲线的对应关系。
