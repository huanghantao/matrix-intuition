"""W1D5 图：颜色 = 三维向量 —— 词变成向量的雏形。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import save

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection="3d")

# 三个基向量：红、绿、蓝（标签带白底 + 偏移，避免压住箭头和坐标轴）
basis = [
    ((1, 0, 0), "#d62728", "红 (1,0,0)", (0.35, 0.0, -0.02)),
    ((0, 1, 0), "#2ca02c", "绿 (0,1,0)", (-0.02, 0.35, -0.02)),
    ((0, 0, 1), "#1f77b4", "蓝 (0,0,1)", (-0.05, 0.0, 0.32)),
]
for v, color, label, off in basis:
    ax.quiver(0, 0, 0, *v, color=color, lw=3, arrow_length_ratio=0.08)
    ax.text(v[0] + off[0], v[1] + off[1], v[2] + off[2], label,
            color=color, fontsize=11,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))

# 混合色：橙 = 红 + 一半绿；黄 = 红 + 绿（标签错开，避免互相压着）
for v, color, label, off in [
    ((1, 0.5, 0), "#ff9f43", "橙 = 红+半绿", (0.1, -0.05, -0.18)),
    ((1, 1, 0), "#e6c229", "黄 = 红+绿", (0.1, 0.0, -0.32)),
]:
    ax.quiver(0, 0, 0, *v, color=color, lw=2.5, arrow_length_ratio=0.08)
    ax.text(v[0] + off[0], v[1] + off[1], v[2] + off[2], label,
            color=color, fontsize=11,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))

ax.set_xlim(0, 1.4)
ax.set_ylim(0, 1.4)
ax.set_zlim(0, 1.4)
ax.set_xlabel("红分量 R", fontsize=11)
ax.set_ylabel("绿分量 G", fontsize=11)
ax.set_zlabel("蓝分量 B", fontsize=11)
ax.set_title("Week 1 · 颜色是三维向量：混合 = 向量相加", fontsize=13, pad=14)
fig.tight_layout()
save(fig, "w1d5_color_vectors.png")
