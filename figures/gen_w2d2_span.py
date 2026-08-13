"""W2D2 图：两个不共线的向量张成整个平面（斜网格）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_ORANGE, C_BLUE, C_GREEN, axes, save, vec

fig, ax = plt.subplots(figsize=(7, 6))
axes(ax, xlim=(-8, 8), ylim=(-8, 8))

b1 = np.array([2.0, 1.0])
b2 = np.array([-1.0, 1.0])

# 斜网格：s*b1 + t*b2，s、t 取整数
for s in range(-6, 7):
    for t in range(-6, 7):
        p = s * b1 + t * b2
        ax.plot([p[0] - 4 * b2[0], p[0] + 4 * b2[0]],
                [p[1] - 4 * b2[1], p[1] + 4 * b2[1]],
                color="#cccccc", lw=0.6, zorder=1)
        ax.plot([p[0] - 4 * b1[0], p[0] + 4 * b1[0]],
                [p[1] - 4 * b1[1], p[1] + 4 * b1[1]],
                color="#cccccc", lw=0.6, zorder=1)

vec(ax, (0, 0), b1, color=C_BLUE, label="b1 = (2,1)",
    label_at_tip=True, label_offset=(0.15, -0.35))
vec(ax, (0, 0), b2, color=C_GREEN, label="b2 = (-1,1)",
    label_at_tip=True, label_offset=(-0.4, 0.1))

# 示例：2*b1 + 1*b2
p = 2 * b1 + 1 * b2
ax.scatter([p[0]], [p[1]], color=C_ORANGE, s=50, zorder=5)
ax.text(p[0] + 0.3, p[1] - 0.4, "2·b1 + 1·b2", color=C_ORANGE, fontsize=12,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
        zorder=6)

ax.set_title("张成：用 b1、b2 伸缩相加，能铺满整个平面\n（网格上每个交叉点都是一个线性组合）", fontsize=13)
save(fig, "w2d2_span.png")
