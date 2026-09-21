# case02 Error Convergence 细分数量递增误差收敛归零

## 专题简介
承接case01。单独可视化**近似误差**：矩形面积与真实曲边面积的差值。随着n不断增大，误差区域不断缩小，直观看到误差不断向0靠近。

## 前置依赖
- 前置学习：case01
- 后续依赖：case03 Function Limit

## 学习目标
【基础目标】理解近似存在误差；n增大，误差不断减小；观察误差区域的几何形态。
【前瞻目标】建立核心直觉：可以无限逼近，但不一定等于；误差可以无限趋近于0。

## 核心概念
1. 误差 = 真实曲边面积 - 矩形近似面积
2. 收敛：随着细分n增大，误差不断变小，无限趋近于0


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
1. 沿用 $f(x)=x^2$，区间[0,2]
2. 绘制多帧图 n=2,4,8,16,32
3. 蓝色矩形是近似面积；红色填充绘制误差区域
4. 额外绘制折线图：横轴n，纵轴误差，直观看到误差曲线不断下降靠近0

## 输出产物

### 第 1 组：误差可视化逐步细分（5帧动画组）

**说明：** 与case01相同图形设置（f(x)=x², [0,2]），但每帧用红色区域标注左矩形与曲线之间的误差面积，并显示当前误差值。从 n=2 到 n=32，误差面积逐渐缩小。

**包含文件：**

- `frame_00_n2.png`
- `frame_01_n4.png`
- `frame_02_n8.png`
- `frame_03_n16.png`
- `frame_04_n32.png`

**关系/意义：** 这5帧与case01的5帧是一组对照：case01展示"近似值"，case02展示"误差"。两者结合让学生同时理解"逼近了"和"误差在减小"。

### 第 2 组：误差收敛曲线

**说明：** 将 n=2,4,8,16,32,64,128 对应的误差值绘制为折线图，直观显示误差随 n 增大而快速下降（对 x² 左矩形误差为 O(1/n) 速率）。

**包含文件：**

- `error_trend.png`

**关系/意义：** 将5帧离散观察升华为连续趋势图，展示误差收敛的规律性。
