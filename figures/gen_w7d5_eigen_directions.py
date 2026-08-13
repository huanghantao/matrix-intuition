"""W7D5 图：特征向量 = 变换后方向不变的"主轴"。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GREEN, C_GRAY, C_RED, axes, save

A = np.array([[3.0, 1.0], [1.0, 2.0]])
# 特征值/特征向量（手工给定，与 reference.eigen 的幂迭代结果一致）
lam1, v1 = 3.618033988749895, np.array([0.8506508084, 0.5257311121])
lam2, v2 = 1.381966011250105, np.array([-0.5257311121, 0.8506508084])

fig, ax = plt.subplots(figsize=(7.5, 6.5))
axes(ax, xlim=(-5, 5), ylim=(-4.5, 4.5))

# 单位圆（变换前）
t = np.linspace(0, 2 * np.pi, 120)
ax.plot(np.cos(t), np.sin(t), color=C_GRAY, lw=1.5, ls="--", label="单位圆（变换前）")

# 变换后的椭圆
pts = A @ np.vstack([np.cos(t), np.sin(t)])
ax.plot(pts[0], pts[1], color=C_BLUE, lw=2, label="A 变换后的椭圆")

# 特征方向（主轴）
ax.plot([0, lam1 * v1[0]], [0, lam1 * v1[1]], color=C_RED, lw=3,
        label=f"特征方向 1：A 只把它拉长 λ₁={lam1:.2f} 倍")
ax.plot([0, lam2 * v2[0]], [0, lam2 * v2[1]], color=C_GREEN, lw=3,
        label=f"特征方向 2：A 只把它拉长 λ₂={lam2:.2f} 倍")

ax.legend(loc="lower left", fontsize=10)
ax.set_title("特征向量 Ax = λx：矩阵作用后方向不变，只是伸缩\n椭圆的长短轴正是两个特征方向", fontsize=13)
save(fig, "w7d5_eigen_directions.png")
