"""W4D5 图 0：把动作"冻结"成档案 —— 为什么变换也能当"猪"。

左：动作本身 —— 旋转 90° 把 e1=(1,0) 送到 (0,1)，把 e2=(0,1) 送到 (-1,0)。
    虚线是基向量原来的位置，实线是落点，灰色圆弧是它们的"旅程"。
右：冻结成的档案 —— 矩阵 B 的两列，就是两个落点的读数：
    第 1 列 = T(e1) = (0,1)，第 2 列 = T(e2) = (-1,0)。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_ORANGE, C_RED, axes, save, vec

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.2),
                               gridspec_kw={"width_ratios": [1, 1]})

# ---------- 左：动作本身 ----------
axes(ax1, xlim=(-2.4, 2.4), ylim=(-2.4, 2.4))

# 灰色圆弧：e1 与 e2 的"旅程"（半径 1，各转 90°）
for th_start in (0, 90):
    th = np.linspace(np.radians(th_start), np.radians(th_start + 90), 60)
    ax1.plot(np.cos(th), np.sin(th), color=C_GRAY, lw=1.6, alpha=0.85)
    th_end = np.radians(th_start + 90)
    ax1.annotate("",  # 弧线上的小箭头，指示方向
                 xy=(np.cos(th_end), np.sin(th_end)),
                 xytext=(np.cos(th_end - 0.12), np.sin(th_end - 0.12)),
                 arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=1.6))

# 基向量原来的位置（虚线，横向错开一点点以免和落点重叠）与落点（实线）
vec(ax1, (0, -0.07), (1, 0), color=C_BLUE, dashed=True, label="e₁ 原来在这",
    label_at_tip=True, label_offset=(0.1, -0.38))
vec(ax1, (0.07, 0), (0, 1), color=C_GREEN, dashed=True, label="e₂ 原来在这",
    label_at_tip=True, label_offset=(0.55, 0.1))
vec(ax1, (0, 0), (0, 1), color=C_RED, label="T(e₁) = (0,1)",
    label_at_tip=True, label_offset=(-2.15, 0.1))
vec(ax1, (0, 0), (-1, 0), color=C_ORANGE, label="T(e₂) = (−1,0)",
    label_at_tip=True, label_offset=(-0.75, 0.25))

ax1.text(0, -2.1, "e₁ 的落点恰好落在 e₂ 原来的位置", ha="center",
         fontsize=11, color=C_GRAY)
ax1.set_title("动作本身（猪）：把整把尺子转 90°", fontsize=13)

# ---------- 右：冻结成的档案 ----------
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis("off")

# 矩阵括号
bx0, bx1, by0, by1 = 3.6, 6.6, 3.9, 6.7
for x in (bx0, bx1):
    ax2.plot([x, x], [by0, by1], color="#333333", lw=2)
ax2.plot([bx0, bx0 + 0.35], [by1, by1], color="#333333", lw=2)
ax2.plot([bx0, bx0 + 0.35], [by0, by0], color="#333333", lw=2)
ax2.plot([bx1 - 0.35, bx1], [by1, by1], color="#333333", lw=2)
ax2.plot([bx1 - 0.35, bx1], [by0, by0], color="#333333", lw=2)
ax2.text(2.6, (by0 + by1) / 2, "B =", fontsize=17, va="center", ha="center")

# 四个元素
ex1, ex2, ey1, ey2 = 4.45, 5.85, 5.9, 4.7
for x, y, t in ((ex1, ey1, "0"), (ex1, ey2, "1"), (ex2, ey1, "−1"), (ex2, ey2, "0")):
    ax2.text(x, y, t, fontsize=17, ha="center", va="center", family="monospace")

# 两列的彩色框，与左图落点箭头同色
ax2.add_patch(FancyBboxPatch((ex1 - 0.52, by0 + 0.18), 1.04, by1 - by0 - 0.36,
                             boxstyle="round,pad=0.06", fill=False,
                             ec=C_RED, lw=2.4))
ax2.add_patch(FancyBboxPatch((ex2 - 0.62, by0 + 0.18), 1.24, by1 - by0 - 0.36,
                             boxstyle="round,pad=0.06", fill=False,
                             ec=C_ORANGE, lw=2.4))

# 列的出处标注
ax2.annotate("第 1 列 = T(e₁) 的读数", xy=(ex1, by0 + 0.1), xytext=(3.4, 2.4),
             fontsize=12, color=C_RED, ha="center",
             arrowprops=dict(arrowstyle="-|>", color=C_RED, lw=1.6))
ax2.annotate("第 2 列 = T(e₂) 的读数", xy=(ex2, by0 + 0.1), xytext=(7.3, 2.4),
             fontsize=12, color=C_ORANGE, ha="center",
             arrowprops=dict(arrowstyle="-|>", color=C_ORANGE, lw=1.6))

ax2.text(5.1, 0.9, "谁把 e₁、e₂ 送到了哪 ——\n一个变换的全部信息，就这 4 个数",
         ha="center", fontsize=11.5, color=C_GRAY)
ax2.set_title("冻结成的档案（照片）：两列 = 两个落点读数", fontsize=13)

# 两图之间的"冻结"箭头
fig.text(0.5, 0.48, "记录两个落点  →", ha="center", fontsize=13,
         color="#333333",
         bbox=dict(boxstyle="round,pad=0.35", fc="#fff7e6", ec=C_ORANGE))

fig.suptitle("把动作冻结成档案：一个变换 = 两根落点箭头；矩阵 = 它们并排站好",
             fontsize=14.5)
fig.subplots_adjust(top=0.82, wspace=0.1, bottom=0.06)
save(fig, "w4d5_freeze_transform.png")
