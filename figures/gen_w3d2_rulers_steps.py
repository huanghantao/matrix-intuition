"""W3D2 图：变换搬走的是尺子，不是步数 —— 同一句导航指令，在新尺子体系里重走一遍。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.mat import matvec, scale_matrix
from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, axes, save, vec

M = scale_matrix(2, 3)           # 拉伸：横 ×2、纵 ×3
v = [2.0, 1.0]                   # 导航指令：向东 2 步、向北 1 步
c1 = [M[0][0], M[1][0]]          # e1 的新家（第一列）= (2, 0)
c2 = [M[0][1], M[1][1]]          # e2 的新家（第二列）= (0, 3)
Mv = matvec(M, v)                # = (4, 3)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2))
for ax in (ax1, ax2):
    axes(ax, xlim=(-0.7, 4.9), ylim=(-0.7, 3.9))

# ---------- 左：旧尺子体系 ----------
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
ax1.text(2.55, 2.45, "导航指令：\n“向东 2 步，向北 1 步”", color="#333333",
         fontsize=12, ha="left", va="center",
         bbox=dict(boxstyle="round,pad=0.4", fc="#f5f5f5", ec="#cccccc"))
ax1.set_title("变换前：沿旧尺子走 → v = (2, 1)", fontsize=12)

# ---------- 右：新尺子体系，同一句指令 ----------
vec(ax2, (0, 0), c1, color=C_BLUE, label="c1 = e1 的新家",
    label_at_tip=True, label_offset=(0.1, -0.42))
vec(ax2, (0, 0), c2, color=C_GREEN, label="c2 = e2 的新家",
    label_at_tip=True, label_offset=(0.12, -0.05))
# 新尺子的 "1 步" 变长了
ax2.text(1.0, -0.42, "新 1 步 = 2 格", color=C_BLUE, fontsize=10.5,
         ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
ax2.text(0.15, 1.5, "新 1 步 = 3 格", color=C_GREEN, fontsize=10.5,
         ha="left", va="center",
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
# 同样的 2 步 + 1 步，只是沿新尺子走
ax2.scatter([2, 4], [0, 0], color=C_BLUE, s=28, zorder=5)
ax2.plot([0, Mv[0], Mv[0], 0, 0], [0, 0, Mv[1], Mv[1], 0],
         color=C_GRAY, lw=1, ls=":", alpha=0.9)
vec(ax2, (0, 0), Mv, color=C_RED, label="M·v = (4, 3)",
    label_at_tip=True, label_offset=(0.15, 0.12))
ax2.text(2.85, 0.9, "同一句指令：\n“向东 2 步，向北 1 步”", color="#333333",
         fontsize=12, ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.4", fc="#f5f5f5", ec="#cccccc"))
ax2.set_title("变换后：尺子搬了家，步数不变 → M·v = (4, 3)", fontsize=12)

fig.suptitle("Week 3 · 变换搬走的是尺子，不是步数", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.80, wspace=0.22)
save(fig, "w3d2_rulers_steps.png")
