"""W1D4 图：向量加法（首尾相接，三角形法则）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_RED, axes, save, vec

fig, ax = plt.subplots(figsize=(7, 5.5))
axes(ax, xlim=(-1, 6.5), ylim=(-1, 5))

u = (3, 1)
v = (1, 2)
vec(ax, (0, 0), u, color=C_BLUE, label="u = (3,1)",
    label_at_tip=True, label_offset=(0.25, 0.15))
vec(ax, u, v, color=C_GREEN, label="v = (1,2)",
    label_at_tip=True, label_offset=(0.25, 0.1))
vec(ax, (0, 0), (u[0] + v[0], u[1] + v[1]), color=C_RED,
    label="u+v = (4,3)", label_at_tip=True, label_offset=(0.2, -0.35))
ax.set_title("向量加法：先走 u 再走 v，总位移 u+v", fontsize=13, pad=10)
ax.text(1.6, -0.6, "首尾相接（三角形法则）", color="#555555", fontsize=11,
        ha="center")
fig.suptitle("Week 1 · 向量加法", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.88)
save(fig, "w1d4_vector_add.png")
