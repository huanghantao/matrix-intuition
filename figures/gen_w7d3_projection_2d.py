"""W7D3 图（二维版）：最小二乘的投影本质 —— 列空间是一条直线，ŷ 是线上离 y 最近的点。

迷你例子：过原点直线 y = a·x 拟合两个点 (1,1)、(2,1)。
A 只有一列 (1,2)，列空间 = 这条过原点的直线；
y = (1,1) 悬在线外，投影 ŷ = 0.6·(1,2)，残差 (0.4,-0.2) 与直线垂直。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GREEN, C_GRAY, C_ORANGE, C_RED, save, vec

col = np.array([1.0, 2.0])          # A 的唯一一列
y = np.array([1.0, 1.0])            # 真实数据
a_hat = col @ y / (col @ col)       # 最小二乘解 = 0.6
y_hat = a_hat * col                 # 投影 (0.6, 1.2)
residual = y - y_hat                # (0.4, -0.2)，与 col 垂直
a_bad = 1.0                         # 落选者：a=1
y_bad = a_bad * col                 # (1, 2)

fig, ax = plt.subplots(figsize=(7.8, 6.8))

# 列空间：过原点的直线（A 的列张成）
t = np.array([-0.12, 1.16])
ax.plot(t * col[0], t * col[1], color=C_ORANGE, lw=7, alpha=0.30,
        solid_capstyle="round", zorder=1)

# 直角标记：在垂足 ŷ 处画一个小方角
d = col / np.linalg.norm(col)       # 沿线方向
n = residual / np.linalg.norm(residual)  # 残差方向
m = 0.09
corner = [y_hat + m * d, y_hat + m * d + m * n, y_hat + m * n]
ax.plot([p[0] for p in corner], [p[1] for p in corner],
        color=C_GRAY, lw=1.4, zorder=3)

# 各向量（带白底标签）
vec(ax, (0, 0), col, color=C_ORANGE, lw=2.5, label="A 的列 (1, 2)",
    label_offset=(-0.52, 0.10))
vec(ax, (0, 0), y_hat, color=C_GREEN, lw=2.5, label="$\\hat{y}$ = 投影（线上最近点）",
    label_offset=(0.28, -0.16))
vec(ax, (0, 0), y, color=C_BLUE, lw=2.5, label="y = 真实数据 (1, 1)",
    label_offset=(0.45, 0.30))

# 残差：从 ŷ 指向 y
ax.annotate("", xy=tuple(y), xytext=tuple(y_hat),
            arrowprops=dict(arrowstyle="-|>", color=C_RED, lw=3,
                            shrinkA=0, shrinkB=0, mutation_scale=18))
ax.text(0.86, 1.02, "残差 $y-\\hat{y}$\n垂直于列空间\n（所以才最短）",
        color=C_RED, fontsize=12,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88),
        zorder=6)

# 落选者：a=1 的预测 (1,2)，离 y 更远
ax.scatter(*y_bad, color=C_GRAY, s=45, zorder=5)
ax.plot([y_bad[0], y[0]], [y_bad[1], y[1]], color=C_GRAY, lw=1.6, ls="--", zorder=2)
ax.text(1.06, 1.92, "落选者：取 a=1\n得到 (1, 2)，\n离 y 明显更远", color=C_GRAY,
        fontsize=11,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88),
        zorder=6)

# 列空间的名字贴在左上空白区
ax.text(-0.38, 1.58, "列空间\n= 所有直线\n$y=a\\cdot x$\n能给出的预测",
        color="#b35a00", fontsize=11,
        bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88),
        zorder=6)

ax.axhline(0, color="#333333", lw=0.8)
ax.axvline(0, color="#333333", lw=0.8)
ax.set_xlim(-0.42, 1.85)
ax.set_ylim(-0.42, 2.55)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("点1的预测值", fontsize=11)
ax.set_ylabel("点2的预测值", fontsize=11)
ax.grid(True, color="#dddddd", lw=0.6)
ax.set_axisbelow(True)
ax.set_title("二维看懂投影：列空间是一条直线\nŷ 是线上离 y 最近的点，残差与直线垂直",
             fontsize=13)
save(fig, "w7d3_projection_2d.png")
