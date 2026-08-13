"""W8D1 图：导数 = 切线的斜率 = 变化率。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GRAY, C_ORANGE, C_RED, save

fig, ax = plt.subplots(figsize=(7.5, 5.5))
x = np.linspace(-0.5, 4.5, 200)
f = lambda x: (x - 2) ** 2 + 1
ax.plot(x, f(x), color=C_BLUE, lw=2.5, label="f(x) = (x-2)² + 1")

x0 = 1.0
y0 = f(x0)
# 切线：f'(x0) = 2(x0-2) = -2
slope = 2 * (x0 - 2)
tx = np.array([x0 - 1.2, x0 + 1.2])
ax.plot(tx, y0 + slope * (tx - x0), color=C_RED, lw=2, ls="--",
        label=f"切线斜率 = -2")

# 割线：从 x0 到 x1
x1 = 3.2
ax.plot([x0, x1], [f(x0), f(x1)], color=C_ORANGE, lw=1.5, ls=":",
        label="割线（两个点连起来）")

ax.scatter([x0], [y0], color=C_RED, s=70, zorder=6)
ax.text(x0 + 0.1, y0 - 0.5, f"在 x={x0} 处：往右走，f 在下降\n导数 < 0 → 该往正方向走，才能下山", fontsize=11,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
        zorder=7)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Week 8 · 导数 = 变化率 = “往哪个方向走函数会变小”", fontsize=13)
ax.legend(loc="upper left", fontsize=10)
ax.set_ylim(0, 8)
save(fig, "w8d1_slope.png")
