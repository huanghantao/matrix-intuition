"""W7D3 图：最小二乘的投影本质 —— y 悬在列空间平面外，投影是最近的平面点，残差垂直于平面。

用 3 个点的小例子：3 个方程 = 三维空间里的一个向量 y；
A 的两列张出一个真·平面（列空间）；拟合 = 把 y 拍到平面上。
坐标刻意做了置换（x,y,z)←(点3,点1,点2)，让残差方向接近竖直：
同一视角下平面能"打开"、残差向量又立得起来。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from reference.lstsq import fit_line
from figures._common import C_BLUE, C_GREEN, C_ORANGE, C_RED, save

# 3 个点的小例子（点太多的话列空间是高维平面，画不出来）。
# 数据刻意散：残差向量大，投影结构才看得清。
xs = [0.0, 1.0, 2.0]
ys = [0.2, 2.8, 0.6]
a, b = fit_line(xs, ys)

col1 = np.array(xs, dtype=float)          # 各点的 x
col2 = np.ones(3)                         # 全 1
y = np.array(ys)
y_hat = a * col1 + b * col2               # 投影 = A x̂
residual = y - y_hat                      # 残差向量（垂直于平面）

# 坐标置换 (显示 x, y, z) ← (点3, 点1, 点2)：让残差近似指向 z 正方向
perm = [2, 0, 1]
P = lambda v: np.array([v[perm[0]], v[perm[1]], v[perm[2]]])
col1_p, col2_p, y_p, y_hat_p, r_p = map(P, (col1, col2, y, y_hat, residual))

fig = plt.figure(figsize=(8.5, 7))
ax = fig.add_subplot(111, projection="3d")

# 列空间平面：s·列1 + t·列2
s = np.linspace(0.0, 1.15, 10)
t = np.linspace(0.0, 1.55, 10)
S, T = np.meshgrid(s, t)
Pl = S[..., None] * col1_p + T[..., None] * col2_p
ax.plot_surface(Pl[..., 0], Pl[..., 1], Pl[..., 2], color=C_ORANGE, alpha=0.20,
                linewidth=0, antialiased=True)

def arrow(v, color, lw=2.5):
    ax.quiver(0, 0, 0, *v, color=color, lw=lw, arrow_length_ratio=0.07)

def label(pos, text, color, off):
    ax.text(pos[0] + off[0], pos[1] + off[1], pos[2] + off[2], text,
            color=color, fontsize=11,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.88))

# A 的两列（直线的两个"原料"）
arrow(col1_p, C_ORANGE, lw=2)
arrow(col2_p, C_ORANGE, lw=2)
label(col1_p, "列1：各点的 x", C_ORANGE, (0.1, -0.55, 0.05))
label(col2_p, "列2：全是 1", C_ORANGE, (0.05, 0.25, -0.35))

# 真实数据 y（蓝）、投影 ŷ（绿）、残差（红，从 ŷ 指向 y）
arrow(y_p, C_BLUE)
arrow(y_hat_p, C_GREEN)
label(y_p, "y：真实数据", C_BLUE, (0.35, 0.1, 0.15))
label(y_hat_p, "$\\hat{y}$：投影", C_GREEN, (0.2, 0.9, 0.42))

# 残差向量：从 ŷ 指向 y（画成虚线感：先粗线再箭头）
ax.quiver(*(list(y_hat_p) + list(r_p)), color=C_RED, lw=3.5,
          arrow_length_ratio=0.08)
mid = y_hat_p + r_p * 0.55
label(mid, "残差 $y-\\hat{y}$\n垂直于平面\n（所以才最短）", C_RED, (0.42, 0.05, 0.28))
ax.scatter(*y_hat_p, color=C_GREEN, s=45, depthshade=False)

# 平面名字贴在平面远角
label(1.15 * col1_p + 1.55 * col2_p, "列空间平面\n（所有直线预测的落脚地）", "#b35a00",
      (0.1, 0.15, 0.12))

ax.set_xlim(0, 3.9)
ax.set_ylim(0, 3.0)
ax.set_zlim(0, 3.4)
ax.set_box_aspect((1.25, 1, 1))
ax.set_xlabel("点3的 y", fontsize=10)
ax.set_ylabel("点1的 y", fontsize=10)
ax.set_zlabel("点2的 y", fontsize=10)
ax.tick_params(labelsize=8)
ax.view_init(elev=42, azim=-20)
ax.set_title("最小二乘的几何本质：把 y 投影到列空间平面上\n（残差向量垂直于平面 = 平方和最小）",
             fontsize=13, pad=2)
save(fig, "w7d3_projection.png")
