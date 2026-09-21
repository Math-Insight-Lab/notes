# note-C 高中数理随笔｜微积分直觉篇

高中数学可视化教学案例集，共 16 个独立 case，覆盖极限、导数、积分三大模块。

## 快速开始

### 1. 安装 Python

确保已安装 Python 3.9 或更高版本。如未安装，请访问 <https://www.python.org/downloads/> 下载安装。

### 2. 安装依赖

```bash
pip install numpy matplotlib sympy
```

### 3. 安装 calc-insight-kit 工具库（可选）

```bash
# 方法 A：直接安装 GitHub 最新版
pip install git+https://github.com/Math-Insight-Lab/calc-insight-kit.git

# 方法 B：克隆本地后安装
git clone https://github.com/Math-Insight-Lab/calc-insight-kit.git
cd calc-insight-kit
pip install -e .
```

### 4. 验证安装

```bash
python -c "import matplotlib; import numpy; import sympy; print('所有依赖已就绪')"
```

### 5. 运行示例

```bash
cd src/cases/case01_riemann_rect_approx
python plot.py
```

## 模块划分

### 模块1：极限 (Limit) — Case 01-04

| Case | 主题 |
|------|------|
| case01 | 曲边图形矩形无限细分逼近 |
| case02 | 细分数量递增误差收敛归零 |
| case03 | 函数趋近定点极限 |
| case04 | 数列无穷累积极限收敛 |

### 模块2：导数 (Derivative) — Case 05-08

| Case | 主题 |
|------|------|
| case05 | 割线动态逼近切线全过程 |
| case06 | 切线斜率瞬时变化率原理 |
| case07 | 导数正负函数增减联动 |
| case08 | 导数大小变化快慢匹配 |

### 模块3：积分 (Integral) — Case 09-16

| Case | 主题 |
|------|------|
| case09 | 左矩形求和逼近曲边面积 |
| case10 | 右矩形求和逼近曲边面积 |
| case11 | 不同n下黎曼和面积收敛可视化 |
| case12 | 梯形求和比矩形更精确 |
| case13 | 积分符号与区域关系 |
| case14 | 积分上下限翻转符号变化 |
| case15 | 分段函数分段积分 |
| case16 | 累积函数积分上限函数 |

## 目录结构

```
note-C/
├── src/cases/          # 源码：每个 case 包含 plot.py、README.md、tasks.md
│   ├── case01_riemann_rect_approx/
│   ├── case02_error_convergence/
│   ├── ...
│   └── case16_accumulation_function/
├── dist/cases/         # 产物：每个 case 包含 assets/（渲染图片）、README.md、tasks.md
│   ├── case01_riemann_rect_approx/
│   ├── case02_error_convergence/
│   ├── ...
│   └── case16_accumulation_function/
├── pyproject.toml      # Python 包配置
├── .gitignore
└── README.md
```

## 许可证

- 源码：MIT
- 文档与图片素材：CC BY-NC 4.0
