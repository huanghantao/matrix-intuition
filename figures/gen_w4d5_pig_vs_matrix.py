"""W4D5 图 1：对象 vs 描述 —— 一头猪的多张照片 = 一个变换的多个矩阵。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from figures._common import C_BLUE, C_GRAY, C_RED, save
from figures._pig import draw_card, draw_pig

fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 6.8))
for ax in (axL, axR):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

# ---------- 左：猪与照片 ----------
draw_pig(axL, 3.0, 4.6, s=1.15, view="side")
axL.text(3.0, 7.2, "那头猪\n（对象本身）", ha="center", fontsize=13, weight="bold")

shots = [("side", "侧面照 · 镜头 1"), ("front", "正面照 · 镜头 2"), ("back", "背影照 · 镜头 3")]
for i, (view, name) in enumerate(shots):
    cy = 8.0 - i * 2.85
    draw_card(axL, 7.7, cy, 3.4, 2.3)
    draw_pig(axL, 7.5, cy - 0.3, s=0.5, view=view)
    axL.text(7.7, cy + 0.85, name, ha="center", fontsize=10.5, color=C_GRAY)
    axL.annotate("", xy=(6.1, cy), xytext=(4.7, 4.7),
                 arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=1.4))

axL.text(5.0, 0.35, "所有照片都是这同一头猪的描述，\n但又都不是这头猪本身",
         ha="center", fontsize=11.5, color=C_RED)

# ---------- 右：变换与矩阵 ----------
axR.add_patch(Circle((3.0, 4.6), 1.4, fc="#eaf3ff", ec=C_BLUE, lw=1.8))
axR.text(3.0, 4.6, "同一个变换 T\n（旋转 90°）", ha="center", va="center",
         fontsize=12, weight="bold", color=C_BLUE)
axR.text(3.0, 7.2, "那个动作\n（对象本身）", ha="center", fontsize=13, weight="bold")

mats = [("标准尺子 I 下", "B = [[0, -1],\n     [1, 0]]"),
        ("尺子 P₁（x 拉长 2 倍）下", "A₁ = [[0, -0.5],\n      [2, 0]]"),
        ("尺子 P₂（斜尺子）下", "A₂ = [[-1, -2],\n      [1, 1]]")]
for i, (name, mtxt) in enumerate(mats):
    cy = 8.0 - i * 2.85
    draw_card(axR, 7.7, cy, 3.7, 2.3)
    axR.text(7.7, cy + 0.83, name, ha="center", fontsize=10, color=C_GRAY)
    axR.text(7.7, cy - 0.3, mtxt, ha="center", va="center",
             fontsize=10.5, family="monospace")
    axR.annotate("", xy=(5.95, cy), xytext=(4.4, 4.7),
                 arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=1.4))

axR.text(5.0, 0.35, "所有矩阵都是这同一个变换的描述，\n但又都不是变换本身",
         ha="center", fontsize=11.5, color=C_RED)

fig.suptitle("5.1 · 对象 vs 描述：猪只有一头，照片可以拍无数张", fontsize=15)
fig.subplots_adjust(top=0.86, wspace=0.05, bottom=0.04)
save(fig, "w4d5_pig_vs_matrix.png")
