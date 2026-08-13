"""W1D4 图：向量加法（首尾相接）与数乘（伸缩）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_ORANGE, C_RED, axes, save, vec

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

# 左：加法 u + v = w（三角形法则）
axes(ax1, xlim=(-1, 6.5), ylim=(-1, 5))
u = (3, 1)
v = (1, 2)
vec(ax1, (0, 0), u, color=C_BLUE, label="u = (3,1)",
    label_at_tip=True, label_offset=(0.25, 0.15))
vec(ax1, u, v, color=C_GREEN, label="v = (1,2)",
    label_at_tip=True, label_offset=(0.25, 0.1))
vec(ax1, (0, 0), (u[0] + v[0], u[1] + v[1]), color=C_RED,
    label="u+v = (4,3)", label_at_tip=True, label_offset=(0.2, -0.35))
ax1.set_title("加法：先走 u 再走 v，总位移 u+v", fontsize=13, pad=10)
ax1.text(1.6, -0.6, "首尾相接", color="#555555", fontsize=11,
         ha="center")

# 右：数乘
axes(ax2, xlim=(-3.5, 5.5), ylim=(-3, 4.2))
u2 = (1.5, 1)
vec(ax2, (0, 0), u2, color=C_BLUE, label="u",
    label_at_tip=True, label_offset=(0.2, -0.25))
vec(ax2, (0, 0), (2 * u2[0], 2 * u2[1]), color=C_RED, label="2u（伸长 2 倍）",
    label_at_tip=True, label_offset=(0.1, 0.15))
vec(ax2, (0, 0), (-0.5 * u2[0], -0.5 * u2[1]), color=C_GREEN,
    label="-0.5u（反向、缩短一半）", label_at_tip=True, label_offset=(0.15, -0.2))
ax2.set_title("数乘：拉伸、缩短、反向", fontsize=13, pad=10)
fig.suptitle("Week 1 · 向量 = 有方向有长度的箭头", fontsize=15, y=0.99)
fig.subplots_adjust(wspace=0.2, top=0.83)
save(fig, "w1d4_vector_add.png")
