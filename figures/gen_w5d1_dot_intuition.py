"""W5D1 图：点积 = 投影长度 × 对方长度。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.proj import dot, project_onto, project_scalar
from figures._common import C_BLUE, C_GREEN, C_RED, axes, save, vec

u = [3.0, 2.0]
v = [2.0, 0.0]

fig, ax = plt.subplots(figsize=(7, 6))
axes(ax, xlim=(-1, 5), ylim=(-1, 4))

vec(ax, (0, 0), u, color=C_BLUE, label="u = (3,2)",
    label_at_tip=True, label_offset=(0.15, 0.1))
vec(ax, (0, 0), v, color=C_GREEN, label="v = (2,0)",
    label_at_tip=True, label_offset=(0.1, -0.35))
p = project_onto(u, v)
ax.plot([u[0], p[0]], [u[1], p[1]], color=C_RED, lw=1.5, ls="--",
        label=f"u 在 v 上的投影（影子）长 {project_scalar(u, v):.0f}")
ax.plot([0, p[0]], [0, p[1]], color=C_RED, lw=3.5)

ax.text(1.55, -0.4, "投影长度 3", color=C_RED, fontsize=12, ha="center")
ax.text(3.0, 1.4, f"u·v = |u||v|cosθ = 3 × 2 = {dot(u, v):.0f}",
        color="#333333", fontsize=12,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
        zorder=6)
ax.legend(loc="upper left", fontsize=10)
ax.set_title("Week 5 · 点积的几何意义：影子的长度 × 对方长度", fontsize=13)
save(fig, "w5d1_dot_intuition.png")
