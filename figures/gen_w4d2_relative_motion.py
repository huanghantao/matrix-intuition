"""W4D2 图：运动是相对的 —— 点动 vs 尺子动。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_RED, axes, point, save

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    axes(ax, xlim=(-0.5, 5), ylim=(-0.5, 5))

# 左：点动（坐标系不动）
axes(ax1, xlim=(-0.5, 5), ylim=(-0.5, 5))
point(ax1, (1, 1), color=C_BLUE, label="(1,1)", label_offset=(0.15, 0.15))
point(ax1, (2, 3), color=C_RED, label="(2,3)", label_offset=(0.15, 0.15))
ax1.annotate("", xy=(2, 3), xytext=(1, 1),
             arrowprops=dict(arrowstyle="-|>", color=C_RED, lw=2))
ax1.set_title("方式一：点动\n把 (1,1) 挪到 (2,3)", fontsize=13)

# 右：尺子动（点不动）：x 轴刻度缩为 1/2、y 轴刻度缩为 1/3
# 孟岩原例：点物理上还在 (1,1)，但新刻度把"1"标成"2"、"3"，
# 于是同一个点的读数从 (1,1) 变成 (2,3)。
axes(ax2, xlim=(-0.5, 5), ylim=(-0.5, 5))
point(ax2, (1, 1), color=C_RED, label="点没动，物理位置还是 (1,1)",
      label_offset=(0.35, 0.35))
# 旧刻度（标准尺）淡色保留
for k in range(1, 5):
    ax2.plot([k, k], [-0.06, 0.06], color="#bbbbbb", lw=1)
    ax2.plot([-0.06, 0.06], [k, k], color="#bbbbbb", lw=1)
# 新刻度：原来标 1 的地方现在标 2（x 轴）、标 3（y 轴）
ax2.scatter([1], [0], color="#888888", s=40, zorder=6)
ax2.text(1, -0.45, "新刻度“2”", color="#888888", ha="center", fontsize=11,
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
ax2.scatter([0], [1], color="#888888", s=40, zorder=6)
ax2.text(-0.75, 1, "新刻度“3”", color="#888888", va="center", fontsize=11,
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
ax2.text(2.7, 1.4, "新尺子读数 = (2,3)\n（x 单位缩到 1/2，y 缩到 1/3）",
         color=C_RED, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
         zorder=6)
ax2.set_title("方式二：尺子动\n刻度变细，点的读数自然变成 (2,3)", fontsize=13)

fig.suptitle("Week 4 · 运动是相对的：变换对象 等价于 变换坐标系", fontsize=15)
save(fig, "w4d2_relative_motion.png")
