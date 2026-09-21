# note-B 初中数理随笔

初中数学可视化随笔，共 16 个独立 case，覆盖代数、几何、统计概率三大模块。

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

运行单个 case：

```bash
cd src/cases/case01_number_line
python plot.py
```

批量运行所有 case：

```bash
for d in src/cases/case*; do echo "=== Running $d ===" && cd "$d" && python plot.py && cd ../../..; done
```

### 6. 查看渲染素材

所有 case 的渲染图片已生成至 `dist/cases/case*/assets/` 目录：

```bash
# 查看某个 case 的素材
ls dist/cases/case01_number_line/assets/

# 查看全部素材统计
find dist/cases -name "*.png" | wc -l
```

## 模块表

| Case | 专题 | 前置依赖 |
|------|------|----------|
| case01 | 数轴跳动 | 小学整数/分数基础 |
| case02 | 面积拼图 | case01 |
| case03 | 天平动画 | case01 |
| case04 | 坐标系点行走平移 | case01 |
| case05 | 负数与绝对值拓展 | case01 |
| case06 | 多项式乘法几何拼图 | case01, case02 |
| case07 | 二元一次方程组 | case03, case04 |
| case08 | 不等式与解集可视化 | case05 |
| case09 | 一次函数深度专题 | case04, case07 |
| case10 | 二次函数几何直观 | case02, case06 |
| case11 | 相似三角形动态几何 | case04 |
| case12 | 圆基础动态演示 | case11 |
| case13 | 初中统计与概率直观模拟 | 无 |
| case14 | 变量与变化关系专题 | case09 |
| case15 | 简单实际问题数学建模 | case09, case14 |
| case16 | 初中常见概念易错边界 | case01~case15 回顾 |

## 目录结构

```
note-B/
├── src/cases/          # 源码：每个 case 包含 plot.py、README.md、tasks.md
│   ├── case01_number_line/
│   ├── case02_area_identity/
│   ├── ...
│   └── case16_boundary_mistake/
├── dist/cases/         # 产物：每个 case 包含 assets/（渲染图片）、README.md、tasks.md
│   ├── case01_number_line/
│   ├── case02_area_identity/
│   ├── ...
│   └── case16_boundary_mistake/
├── pyproject.toml      # Python 包配置
├── .gitignore
└── README.md
```

## 许可

- `src/*.py` 绘图源代码：**MIT License**
- Markdown 讲义、`tasks.md` 习题、`dist/` 生成图片素材：**CC BY-NC 4.0（署名‑非商用）**
