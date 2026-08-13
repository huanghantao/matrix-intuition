"""W1D4 图：数乘（拉伸、缩短、反向）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_RED, axes, save, vec

fig, ax = plt.subplots(figsize=(7, 5.5))
axes(ax, xlim=(-3.5, 5.5), ylim=(-3, 4.2))

u = (1.5, 1)
vec(ax, (0, 0), u, color=C_BLUE, label="u",
    label_at_tip=True, label_offset=(0.2, -0.25))
vec(ax, (0, 0), (2 * u[0], 2 * u[1]), color=C_RED, label="2u（伸长 2 倍）",
    label_at_tip=True, label_offset=(0.1, 0.15))
vec(ax, (0, 0), (-0.5 * u[0], -0.5 * u[1]), color=C_GREEN,
    label="-0.5u（反向、缩短一半）", label_at_tip=True, label_offset=(0.15, -0.2))
ax.set_title("数乘：拉伸、缩短、反向", fontsize=13, pad=10)
fig.suptitle("Week 1 · 数乘 = 拉橡皮筋", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.88)
save(fig, "w1d4_vector_scale.png")
