# case10 Right Riemann Sum 右矩形求和逼近曲边面积

## 专题简介
与case09对称：每个小区间取右端点函数值做矩形高度。

## 前置依赖
- 前置学习：case09 Left Riemann Sum
- 后续依赖：case11 Area Convergence

## 学习目标
理解右端点黎曼和；比较左右和差异；观察二者共同收敛。

## 核心概念
1. 右端点黎曼和：每个小区间用右端点函数值做高
2. 对递增函数：左和低估、右和高估
3. 共同收敛：左右和都逼近同一个真实面积


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
1. $f(x)=x^2$ 在 [0,2]
2. 多帧展示右和 n=4,8,16
3. 对比图 + 收敛折线图

## 输出产物

### 第 1 组：右矩形序列（3帧）

**说明：** f(x)=x² 在 [0,2] 上的右矩形黎曼和，n=4, 8, 16。红色矩形从曲线上方向下填充，每个矩形的顶边取右端点高度。

**包含文件：**

- `frame_00_n4.png`
- `frame_01_n8.png`
- `frame_02_n16.png`

**关系/意义：** 3帧展示右矩形如何从上方逼近真实面积，与case09的左矩形形成镜像对照。

### 第 2 组：左右对比总览图

**说明：** n=8 时左矩形（蓝色）和右矩形（红色）在同一图中叠加，同时标注红色区域（右矩形超出部分）和蓝色区域（左矩形不足部分）。

**包含文件：**

- `left_right_compare.png`

**关系/意义：** 将左右两种近似并列展示，让学生一眼看出"两种方法从上下两面包夹真实面积"。

### 第 3 组：左右收敛曲线

**说明：** n=4,8,16,32,64 时左和（蓝点）与右和（红点）的收敛路径，两条折线从两侧向真实值 8/3 ≈ 2.67 靠拢。

**包含文件：**

- `convergence.png`

**关系/意义：** 将左右对比从"单张图"升华为"收敛趋势"，展示两种方法都收敛于同一极限。
