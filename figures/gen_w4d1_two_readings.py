"""W4D1 图：一个矩阵，两种读法 —— 变换 vs 坐标系。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_PURPLE, C_RED, axes, point, save, vec

M = [[2, 0], [0, 3]]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    axes(ax, xlim=(-0.5, 6), ylim=(-0.5, 6))

# 左：变换读法 —— M 把 v 搬到 Mv
axes(ax1, xlim=(-0.5, 6), ylim=(-0.5, 6))
v = (1, 1)
vec(ax1, (0, 0), v, color=C_BLUE, label="v = (1,1)",
    label_at_tip=True, label_offset=(0.15, -0.3))
vec(ax1, (0, 0), (2, 3), color=C_RED, label="Mv = (2,3)",
    label_at_tip=True, label_offset=(0.2, -0.2))
ax1.set_title("读法 1：变换\nv 被 M 搬到 Mv", fontsize=13)

# 右：坐标系读法 —— M 的列是两根新坐标轴
axes(ax2, xlim=(-0.5, 6), ylim=(-0.5, 6))
vec(ax2, (0, 0), (M[0][0], M[1][0]), color=C_GREEN, label="新 x 轴（刻度=2）",
    label_at_tip=True, label_offset=(0.15, -0.35))
vec(ax2, (0, 0), (M[0][1], M[1][1]), color=C_PURPLE,
    label="新 y 轴（刻度=3）", label_at_tip=True, label_offset=(-0.25, 0.2))
# 新尺子下的网格
for s in (1, 2):
    ax2.plot([s * 2, s * 2], [0, 6], color="#c8b5e0", lw=0.8, ls="--")
    ax2.plot([0, 6], [s * 3, s * 3], color="#c8b5e0", lw=0.8, ls="--")
point(ax2, (2, 3), color=C_RED, label="新尺子读数 (1,1)\n= 标准读数 (2,3)",
      label_offset=(0.3, 0.3))
ax2.set_title("读法 2：坐标系\nM 的列向量 = 两根新坐标轴", fontsize=13)

fig.suptitle("Week 4 · 变换点，还是变换尺子？—— 结果一样", fontsize=15)
save(fig, "w4d1_two_readings.png")
