"""W3D3 图：变换的复合 —— 顺序不能换。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt

from reference.mat import matvec, rotation_matrix, scale_matrix
from figures._common import C_BLUE, C_GREEN, C_GRAY, C_RED, axes, save, vec

R = rotation_matrix(45)
S = scale_matrix(2, 1)

ANNOT = "#555555"  # 辅助线/辅助文字的深灰


def dashed_arrow(ax, p, q):
    """从 p 到 q 的细虚线箭头（表示"被拽过去"的辅助动作）。"""
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=ANNOT, lw=1.5,
                                linestyle="--", shrinkA=0, shrinkB=0,
                                mutation_scale=14))


def note(ax, x, y, text, ha="center", va="bottom", fontsize=11):
    """带白色衬底的辅助说明文字。"""
    ax.text(x, y, text, color=ANNOT, fontsize=fontsize, ha=ha, va=va,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
            zorder=6)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    axes(ax, xlim=(-0.5, 3), ylim=(-0.5, 2.5))

# 左：先旋转 45°，再横向拉伸 2 倍
v = (1, 0)
mid = matvec(R, v)
fin = matvec(S, mid)
vec(ax1, (0, 0), v, color=C_GRAY, label="v = (1,0)",
    label_at_tip=True, label_offset=(0.1, -0.3))
vec(ax1, (0, 0), mid, color=C_GREEN, label="旋转 45°",
    label_at_tip=True, label_offset=(-0.8, 0.32))
vec(ax1, (0, 0), fin, color=C_RED, label="再横向拉伸 ×2",
    label_at_tip=True, label_offset=(0.12, -0.25))
# 横向拉伸的"证据"：y 不变，只把 x 轴上的影子翻倍
ax1.plot([mid[0], mid[0]], [0, mid[1]], color=C_GREEN, lw=1.2, ls="--", alpha=0.8)
ax1.plot([fin[0], fin[0]], [0, fin[1]], color=C_RED, lw=1.2, ls="--", alpha=0.8)
dashed_arrow(ax1, mid, fin)
note(ax1, (mid[0] + fin[0]) / 2, mid[1] + 0.14, "x 翻倍，y 不变")
note(ax1, mid[0] - 0.06, 0.04, f"{mid[0]:.2f}", ha="right", fontsize=10)
note(ax1, fin[0] + 0.06, 0.04, f"{fin[0]:.2f}", ha="left", fontsize=10)
ax1.set_title("先旋转，再拉伸\n(R 后 S：S@R)", fontsize=13)

# 右：先横向拉伸 2 倍，再旋转 45°
mid2 = matvec(S, v)
fin2 = matvec(R, mid2)
vec(ax2, (0, 0), v, color=C_GRAY, label="v = (1,0)",
    label_at_tip=True, label_offset=(0.1, -0.3))
vec(ax2, (0, 0), mid2, color=C_BLUE, label="横向拉伸 ×2",
    label_at_tip=True, label_offset=(0.12, -0.3))
vec(ax2, (0, 0), fin2, color=C_RED, label="再旋转 45°",
    label_at_tip=True, label_offset=(0.05, 0.15))
# 旋转的"证据"：沿圆弧走，长度不变
theta = np.linspace(0, np.pi / 4, 60)
r = float(np.hypot(*mid2))
ax2.plot(r * np.cos(theta), r * np.sin(theta), color=ANNOT, lw=1.2, ls="--", alpha=0.8)
note(ax2, 1.95, 0.98, "沿圆弧：长度不变，只改方向", ha="center")
ax2.set_title("先拉伸，再旋转\n(S 后 R：R@S)", fontsize=13)

fig.suptitle("Week 3 · 穿袜子再穿鞋 ≠ 穿鞋再穿袜子\n矩阵乘法 A@B = “B 先动，A 后动”", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.78, wspace=0.22)
save(fig, "w3d3_compose.png")
