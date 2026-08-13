"""W2D1 图：线性组合 2·e1 + 3·e2 —— 伸缩再相加。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_RED, axes, dashed_line, point, save, vec

fig, ax = plt.subplots(figsize=(6.5, 5.5))
axes(ax, xlim=(-1, 5), ylim=(-1, 5))

e1 = (1, 0)
e2 = (0, 1)
s, t = 2, 3
vec(ax, (0, 0), (s, 0), color=C_BLUE, label="2·e1",
    label_at_tip=True, label_offset=(0.1, -0.4))
vec(ax, (0, 0), (0, t), color=C_GREEN, label="3·e2",
    label_at_tip=True, label_offset=(-0.35, 0.2))
vec(ax, (0, 0), (s, t), color=C_RED, label="2·e1 + 3·e2 = (2,3)",
    label_at_tip=True, label_offset=(0.15, 0.1))

# 平行四边形虚线
ax.plot([s, s], [0, t], color="#888888", lw=1, ls="--")
ax.plot([0, s], [t, t], color="#888888", lw=1, ls="--")
point(ax, (s, t), color=C_RED)
dashed_line(ax, (s, t))
ax.text(0.45, -0.35, "e1", color=C_BLUE, fontsize=12, ha="center")
ax.text(-0.4, 1.55, "e2", color=C_GREEN, fontsize=12, ha="center", va="center")
ax.set_title("线性组合：先伸缩，再相加\n2·(1,0) + 3·(0,1) = (2,3)", fontsize=13)
save(fig, "w2d1_lincomb.png")
