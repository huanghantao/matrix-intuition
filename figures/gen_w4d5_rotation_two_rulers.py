"""W4D5 图 3：同一个旋转，在两把尺子下的两张照片。

左：标准尺子看到的 —— 点绕原点转出干干净净的圆弧（例：点 (2,1) → (-1,2)）。
右：P 尺子（x 轴刻度拉长 2 倍）读出来的同一段物理运动 ——
    物理点 (x, y) 在 P 尺子里读作 (x/2, y)，整个圆被读成压扁的椭圆，
    例：读数 (1,1) → (-0.5,2)，对应 A = [[0,-0.5],[2,0]]。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, axes, point, save, vec

r = np.sqrt(5)                    # (2,1) 与 (-1,2) 到原点的距离
th1 = np.arctan2(1, 2)            # (2,1) 的极角
th2 = np.arctan2(2, -1)           # (-1,2) 的极角
full = np.linspace(0, 2 * np.pi, 200)
seg = np.linspace(th1, th2, 100)
th_mid = (th1 + th2) / 2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8))

# 左：标准尺子
axes(ax1, xlim=(-3.2, 3.2), ylim=(-3.2, 3.2))
ax1.plot(r * np.cos(full), r * np.sin(full), color="#cccccc", lw=1.2, ls="--")
ax1.plot(r * np.cos(seg), r * np.sin(seg), color=C_GRAY, lw=3.0)
ax1.annotate("", xy=(r * np.cos(th_mid + 0.22), r * np.sin(th_mid + 0.22)),
             xytext=(r * np.cos(th_mid - 0.22), r * np.sin(th_mid - 0.22)),
             arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=2.2,
                             connectionstyle="arc3,rad=-0.25"))
vec(ax1, (0, 0), (2, 1), color=C_BLUE, label="标准读数 (2,1)",
    label_at_tip=True, label_offset=(0.15, -0.35))
vec(ax1, (0, 0), (-1, 2), color=C_RED, label="B(Pu) = (-1,2)",
    label_at_tip=True, label_offset=(-0.1, 0.3))
point(ax1, (2, 1), color=C_BLUE)
point(ax1, (-1, 2), color=C_RED)
ax1.text(0, -2.75, "转一整圈，轨迹是圆", ha="center", fontsize=11, color=C_GRAY)
ax1.set_title("标准尺子看到的：干干净净的 90° 圆弧\nB = [[0, -1], [1, 0]]", fontsize=12.5)

# 右：P 尺子读数世界（物理点 (x,y) 在这里读作 (x/2, y)）
axes(ax2, xlim=(-3.2, 3.2), ylim=(-3.2, 3.2))
ax2.plot(r * np.cos(full) / 2, r * np.sin(full), color="#cccccc", lw=1.2, ls="--")
ax2.plot(r * np.cos(seg) / 2, r * np.sin(seg), color=C_GRAY, lw=3.0)
ax2.annotate("", xy=(r * np.cos(th_mid + 0.22) / 2, r * np.sin(th_mid + 0.22)),
             xytext=(r * np.cos(th_mid - 0.22) / 2, r * np.sin(th_mid - 0.22)),
             arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=2.2,
                             connectionstyle="arc3,rad=-0.25"))
vec(ax2, (0, 0), (1, 1), color=C_GREEN, label="新尺子读数 u = (1,1)",
    label_at_tip=True, label_offset=(0.2, -0.3))
vec(ax2, (0, 0), (-0.5, 2), color=C_RED, label="Au = (-0.5,2)",
    label_at_tip=True, label_offset=(-0.3, 0.3))
point(ax2, (1, 1), color=C_GREEN)
point(ax2, (-0.5, 2), color=C_RED)
ax2.text(0, -2.75, "同一个圆，被 P 尺子读成了椭圆", ha="center",
         fontsize=11, color=C_GRAY)
ax2.set_title("P 尺子看到的：同一段运动被拍成压扁的转身\nA = [[0, -0.5], [2, 0]]", fontsize=12.5)

fig.suptitle("同一个旋转，两把尺子，两张照片 —— 照片畸变了，动作没畸变\n"
             "（右图是 P 尺子自己的网格：x 方向 1 格 = 标准世界的 2 格）", fontsize=14)
fig.subplots_adjust(top=0.76, wspace=0.18)
save(fig, "w4d5_rotation_two_rulers.png")
