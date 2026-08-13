"""W3D1 图：三个开胃变换 —— 拉伸、旋转、剪切。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.mat import apply_to_points, rotation_matrix, scale_matrix, shear_matrix
from figures._common import C_BLUE, C_GRAY, save

house = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.5, 1.6], [0.0, 1.0]]

transforms = [
    ("拉伸 scale(2, 0.5)", scale_matrix(2, 0.5), (-1, 3.5, -1, 3.5)),
    ("旋转 rotation(45°)", rotation_matrix(45), (-1.6, 1.6, -1.6, 1.6)),
    ("剪切 shear(0.8)", shear_matrix(0.8), (-1, 3.5, -1, 2.2)),
]

fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.5))
for ax, (title, M, lim) in zip(axs, transforms):
    ax.axhline(0, color="#333333", lw=1)
    ax.axvline(0, color="#333333", lw=1)
    ax.set_xlim(*lim[:2])
    ax.set_ylim(*lim[2:])
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, color="#dddddd", lw=0.6)
    # 原图（灰）
    ax.fill(*zip(*(house + [house[0]])), color=C_GRAY, alpha=0.25)
    ax.text(0.5, 1.85, "原图", color=C_GRAY, ha="center", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))
    # 变换后（蓝）
    new_house = apply_to_points(M, house)
    ax.fill(*zip(*(new_house + [new_house[0]])), color=C_BLUE, alpha=0.35)
    ax.text(sum(p[0] for p in new_house) / 5, sum(p[1] for p in new_house) / 5 + 0.55,
            "变换后", color=C_BLUE, ha="center", fontsize=11,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))
    ax.set_title(title, fontsize=13)

fig.suptitle("Week 3 · 矩阵乘向量 = 对整个图形施加一次变换", fontsize=15)
save(fig, "w3d1_transforms.png")
