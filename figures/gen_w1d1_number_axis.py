"""W1D1 图：数轴与平面坐标 —— 位置就是"地址"。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_RED, C_ORANGE, axes, point, save

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8))

# 左：数轴
ax1.axhline(0, color="#333333", lw=1.5)
for x in range(-6, 7):
    ax1.plot([x, x], [-0.12, 0.12], color="#333333", lw=1)
ax1.set_xlim(-6, 6)
ax1.set_ylim(-1.7, 1.7)
ax1.set_yticks([])
ax1.set_title("数轴：一个数 = 一个地址", fontsize=13, pad=10)
# 三个点上下交错标注，避免 0 与 2.5 靠太近互压；统一加白底
point_labels = [
    (-3, -3, "-3", 0.42),
    (0, 0, "0", 0.42),
    (2.5, 2.5, "2.5", -0.55),  # 2.5 离 0 近，标签往下放，避开 0 的标签
]
for x, px, label, dy in point_labels:
    ax1.scatter([px], [0], color=C_RED, s=50, zorder=5)
    ax1.text(px, dy, label, ha="center", va="center", color=C_RED, fontsize=12,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax1.text(4.2, 1.25, "往右走 2.5 步，就是 2.5", color=C_BLUE, fontsize=11,
         ha="center")

# 右：平面坐标
axes(ax2, xlim=(-1, 6), ylim=(-1, 5))
point(ax2, [3, 2], color=C_ORANGE, label="(3, 2)：\n向右 3 步\n向上 2 步",
      label_offset=(0.35, 0.35))
ax2.plot([3, 3], [0, 2], color=C_GRAY if False else "#888888", lw=1, ls="--")
ax2.plot([0, 3], [2, 2], color="#888888", lw=1, ls="--")
ax2.set_title("平面坐标：两个数 = 一个地址", fontsize=13, pad=10)
fig.suptitle("Week 1 · 位置就是“地址”", fontsize=15, y=0.99)
fig.subplots_adjust(wspace=0.32, top=0.83)
save(fig, "w1d1_number_axis.png")
