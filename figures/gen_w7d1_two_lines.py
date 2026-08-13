"""W7D1 图：方程组 = 两条直线的交点。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_ORANGE, C_RED, axes, save

fig, ax = plt.subplots(figsize=(7, 6))
axes(ax, xlim=(-1, 4.5), ylim=(-1, 4.5))

x = np.linspace(-1, 4.5, 50)
ax.plot(x, 3 - x, color=C_BLUE, lw=2, label="x + y = 3")
ax.plot(x, x - 1, color=C_ORANGE, lw=2, label="x - y = 1")
ax.scatter([2], [1], color=C_RED, s=70, zorder=6)
ax.text(2.15, 1.15, "(2, 1)：同时满足两个式子", color=C_RED, fontsize=12)
ax.legend(loc="upper right", fontsize=11)
ax.set_title("Ax = b：已知变换 A 和结果 b，找出“原来的点”\n（两条直线只有一个公共点 = 唯一解）", fontsize=13)
save(fig, "w7d1_two_lines.png")
