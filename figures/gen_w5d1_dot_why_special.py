"""W5D1 图：为什么点积 = 影子 × 长度（第一步，特例）。

v 躺在 x 轴上时：
- 代数侧：u·v = u₁·L + u₂·0 = u₁·L（y 方向那项被 0 杀掉）；
- 几何侧：影子右端点的刻度就是 u 的 x 坐标 u₁（坐标的定义本身）。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, axes, save, vec

u = [3.0, 2.0]
v = [3.5, 0.0]  # L = 3.5，影子 = u₁ = 3，u·v = 10.5

fig, ax = plt.subplots(figsize=(7.5, 5.5))
axes(ax, xlim=(-0.8, 5.6), ylim=(-1.4, 3.6))

# 两根向量
vec(ax, (0, 0), u, color=C_BLUE, label="u = (u₁, u₂) = (3, 2)",
    label_at_tip=True, label_offset=(0.15, 0.12))
vec(ax, (0, 0), v, color=C_GREEN, label="v = (L, 0) = (3.5, 0)",
    label_at_tip=True, label_offset=(-0.2, -0.45))

# 太阳正上方照下来：u 到 x 轴的落影虚线 + 直角符号
ax.plot([u[0], u[0]], [0, u[1]], color=C_GRAY, lw=1.2, ls="--", alpha=0.8)
ax.plot([2.8, 2.8, 3.0], [0, 0.2, 0.2], color=C_GRAY, lw=1.0)
ax.text(3.18, 1.0, "u₂ = 2", color=C_GRAY, fontsize=11, ha="left", va="center")

# 影子：x 轴上从 0 到 u₁ 的红色粗线
ax.plot([0, u[0]], [0, 0], color=C_RED, lw=3.5, zorder=4)
ax.text(1.5, -0.45, "影子 = u₁ = 3", color=C_RED, fontsize=12,
        ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
        zorder=6)

# 结论：两边算出来都是 u₁ × L
ax.text(0.15, 3.35, "代数：u·v = u₁·L + u₂·0 = u₁·L\n几何：影子 × L = u₁ × L",
        color="#333333", fontsize=12, ha="left", va="top",
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#bbbbbb", alpha=0.9),
        zorder=6)

ax.set_title("特例：v 躺在 x 轴上时，影子就是 u 的 x 坐标 u₁", fontsize=13)
save(fig, "w5d1_dot_why_special.png")
