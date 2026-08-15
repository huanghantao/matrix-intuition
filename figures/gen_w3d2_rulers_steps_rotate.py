"""W3D2 图（旋转版）：变换搬走的是尺子，不是步数 —— 旋转 90°，尺子不变长，只是转了向。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.mat import matvec, rotation_matrix
from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, axes, save, vec

M = rotation_matrix(90)            # 旋转：逆时针 90°，R(90) = [[0,-1],[1,0]]
v = [2.0, 1.0]                     # 导航指令：向东 2 步、向北 1 步（和拉伸版同一句）
c1 = [M[0][0], M[1][0]]            # e1 的新家（第一列）≈ (0, 1)：东尺子转到北
c2 = [M[0][1], M[1][1]]            # e2 的新家（第二列）≈ (-1, 0)：北尺子转到西
Mv = matvec(M, v)                  # ≈ (-1, 2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))
axes(ax1, xlim=(-0.7, 3.4), ylim=(-0.9, 2.7))
axes(ax2, xlim=(-2.3, 2.1), ylim=(-0.9, 2.9))

# ---------- 左：旧尺子体系（和拉伸版完全一样） ----------
vec(ax1, (0, 0), (1, 0), color=C_BLUE, label="e1（东尺子）",
    label_at_tip=True, label_offset=(0.08, -0.42))
vec(ax1, (0, 0), (0, 1), color=C_GREEN, label="e2（北尺子）",
    label_at_tip=True, label_offset=(-0.62, 0.06))
# 步数刻度：沿 e1 走的 2 步，每步 1 格
ax1.scatter([1, 2], [0, 0], color=C_BLUE, s=28, zorder=5)
# 指令走出来的矩形（2 步 × 1 步）
ax1.plot([0, v[0], v[0], 0, 0], [0, 0, v[1], v[1], 0],
         color=C_GRAY, lw=1, ls=":", alpha=0.9)
vec(ax1, (0, 0), v, color=C_RED, label="v = (2, 1)",
    label_at_tip=True, label_offset=(0.15, 0.12))
ax1.text(2.45, 2.05, "导航指令：\n“向东 2 步，向北 1 步”", color="#333333",
         fontsize=12, ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.4", fc="#f5f5f5", ec="#cccccc"))
ax1.set_title("变换前：沿旧尺子走 → v = (2, 1)", fontsize=12)

# ---------- 右：旋转 90° 后的新尺子体系，同一句指令 ----------
vec(ax2, (0, 0), c1, color=C_BLUE, label="c1 = e1 的新家",
    label_at_tip=True, label_offset=(0.12, 0.05))
vec(ax2, (0, 0), c2, color=C_GREEN, label="c2 = e2 的新家",
    label_at_tip=True, label_offset=(-1.0, -0.45))
# 和拉伸的本质区别：新尺子的 "1 步" 还是 1 格，只是方向转了
ax2.text(0.95, 0.55, "新 1 步还是 1 格，\n只是尺子整体转了 90°", color="#333333",
         fontsize=11, ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))
# 同样的 2 步 + 1 步，只是沿转了向的新尺子走
ax2.scatter([0, 0], [1, 2], color=C_BLUE, s=28, zorder=5)
ax2.plot([0, 2 * c1[0], Mv[0], c2[0], 0],
         [0, 2 * c1[1], Mv[1], c2[1], 0],
         color=C_GRAY, lw=1, ls=":", alpha=0.9)
vec(ax2, (0, 0), Mv, color=C_RED, label="M·v = (-1, 2)",
    label_at_tip=True, label_offset=(0.12, 0.14))
ax2.text(0.95, 2.35, "同一句指令：\n“向东 2 步，向北 1 步”", color="#333333",
         fontsize=12, ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.4", fc="#f5f5f5", ec="#cccccc"))
ax2.set_title("变换后：尺子转了向，步数不变 → M·v = (-1, 2)", fontsize=12)

fig.suptitle("Week 3 · 旋转也是“尺子搬家”：步长不变，方向跟着转", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.80, wspace=0.22)
save(fig, "w3d2_rulers_steps_rotate.png")
