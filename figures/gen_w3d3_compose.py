"""W3D3 图：变换的复合 —— 顺序不能换。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.mat import matmul, matvec, rotation_matrix, scale_matrix
from figures._common import C_BLUE, C_GREEN, C_GRAY, C_RED, axes, save, vec

R = rotation_matrix(45)
S = scale_matrix(2, 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    axes(ax, xlim=(-0.5, 3), ylim=(-0.5, 2.5))

# 左：先旋转 45°，再横向拉伸 2 倍
v = (1, 0)
mid = matvec(R, v)
fin = matvec(S, mid)
vec(ax1, (0, 0), v, color=C_GRAY, label="v = (1,0)")
vec(ax1, (0, 0), mid, color=C_GREEN, label="旋转 45°")
vec(ax1, (0, 0), fin, color=C_RED, label="再拉伸 ×2")
ax1.set_title("先旋转，再拉伸\n(R 后 S：S@R)", fontsize=13)

# 右：先横向拉伸 2 倍，再旋转 45°
mid2 = matvec(S, v)
fin2 = matvec(R, mid2)
vec(ax2, (0, 0), v, color=C_GRAY, label="v = (1,0)")
vec(ax2, (0, 0), mid2, color=C_BLUE, label="拉伸 ×2")
vec(ax2, (0, 0), fin2, color=C_RED, label="再旋转 45°")
ax2.set_title("先拉伸，再旋转\n(S 后 R：R@S)", fontsize=13)

fig.suptitle("Week 3 · 穿袜子再穿鞋 ≠ 穿鞋再穿袜子\n矩阵乘法 A@B = “B 先动，A 后动”", fontsize=15)
save(fig, "w3d3_compose.png")
