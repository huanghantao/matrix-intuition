"""W5D1 图：为什么点积 = 影子 × 长度（第二步，旋转划归特例）。

左：一般位置 u = (1,3)、v = (3,4)，β = 53.13°（cosβ = 0.6，sinβ = 0.8）。
右：整张图旋转 −β，v' = (5,0) 躺平，u' = (3,1)，影子 = u' 的新 x 坐标 = 3。
旋转不改变长度和夹角，所以"影子 × 长度"旋转前后是同一个数。
"""
import sys, pathlib
import math

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from reference.proj import dot, norm, project_onto, project_scalar
from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, axes, save, vec

u = [1.0, 3.0]
v = [3.0, 4.0]  # |v| = 5
beta = math.atan2(v[1], v[0])  # 53.13°
c, s = math.cos(beta), math.sin(beta)  # 0.6, 0.8

# 旋转 −β：v' 躺到 x 轴上，u' = (u₁cosβ + u₂sinβ, −u₁sinβ + u₂cosβ)
u2 = [u[0] * c + u[1] * s, -u[0] * s + u[1] * c]  # (3, 1)
v2 = [norm(v), 0.0]  # (5, 0)

foot = project_onto(u, v)  # u 在 v 上的垂足 (1.8, 2.4)

XLIM = (-1.2, 6.4)
YLIM = (-1.8, 5.2)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5.4))

# ---------- 左：旋转前 ----------
axes(axL, xlim=XLIM, ylim=YLIM)
vec(axL, (0, 0), u, color=C_BLUE, label="u = (1, 3)",
    label_offset=(-0.85, 0.4))
vec(axL, (0, 0), v, color=C_GREEN, label="v = (3, 4)",
    label_at_tip=True, label_offset=(0.15, 0.08))

# β 角弧（x 轴 → v）
t = np.linspace(0, beta, 60)
axL.plot(0.9 * np.cos(t), 0.9 * np.sin(t), color=C_GRAY, lw=1.2)
axL.text(1.07, 0.54, "β", color=C_GRAY, fontsize=13, ha="center", va="center")

# 影子 + 落影虚线 + 直角符号
axL.plot([0, foot[0]], [0, foot[1]], color=C_RED, lw=3.5, zorder=4)
axL.plot([u[0], foot[0]], [u[1], foot[1]], color=C_GRAY, lw=1.2, ls="--", alpha=0.8)
a = (-0.6 * 0.16, -0.8 * 0.16)  # 沿 -v 方向
b = (-0.8 * 0.16, 0.6 * 0.16)   # 沿 垂足→u 方向
axL.plot([foot[0] + a[0], foot[0] + a[0] + b[0], foot[0] + b[0]],
         [foot[1] + a[1], foot[1] + a[1] + b[1], foot[1] + b[1]],
         color=C_GRAY, lw=1.0)
axL.text(1.62, 1.44, f"影子 = {project_scalar(u, v):.0f}", color=C_RED, fontsize=12,
         ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
         zorder=6)
axL.set_title("① 旋转前：v 斜放，影子不好直接读", fontsize=13)

# ---------- 右：整体旋转 −β 之后 ----------
axes(axR, xlim=XLIM, ylim=YLIM)
vec(axR, (0, 0), u2, color=C_BLUE, label="u' = (3, 1)",
    label_at_tip=True, label_offset=(0.13, 0.12))
vec(axR, (0, 0), v2, color=C_GREEN, label="v' = (5, 0)",
    label_at_tip=True, label_offset=(0.15, -0.45))

axR.plot([u2[0], u2[0]], [0, u2[1]], color=C_GRAY, lw=1.2, ls="--", alpha=0.8)
axR.plot([2.84, 2.84, 3.0], [0, 0.16, 0.16], color=C_GRAY, lw=1.0)

axR.plot([0, u2[0]], [0, 0], color=C_RED, lw=3.5, zorder=4)
axR.text(1.5, -0.45, "影子 = u' 的 x 坐标 = 3", color=C_RED, fontsize=12,
         ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
         zorder=6)

axR.text(-1.0, 4.95,
         "影子的刻度 = u' 的新 x 坐标\n"
         "= u₁cosβ + u₂sinβ\n"
         f"= 1×{c:.1f} + 3×{s:.1f} = {u2[0]:.0f}",
         color="#333333", fontsize=12, ha="left", va="top",
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#bbbbbb", alpha=0.9),
         zorder=6)
axR.set_title("② 整体旋转 −β：v 躺平，长度和影子都没变", fontsize=13)

fig.tight_layout()
save(fig, "w5d1_dot_why_rotate.png")
print(f"  校验: u·v = {dot(u, v):.1f}, 影子×|v| = {project_scalar(u, v) * norm(v):.1f}")
