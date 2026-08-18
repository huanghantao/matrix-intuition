"""W4D5 图 4：相似矩阵家族 —— 同一头猪的不同照片，"血型"相同（det 与迹不变）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_GRAY, C_RED, save
from figures._pig import draw_card, draw_pig

fig, ax = plt.subplots(figsize=(13, 7.2))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis("off")

draw_pig(ax, 7.0, 7.6, s=0.95, view="side")
ax.text(7.0, 9.3, "同一头猪：旋转变换 T（旋转 90°）",
        ha="center", fontsize=13.5, weight="bold")

cards = [
    ("镜头 = 标准尺子 I", "B = [[0, -1],\n     [1, 0]]"),
    ("镜头 = 尺子 P₁\n（x 轴拉长 2 倍）", "A₁ = [[0, -0.5],\n      [2, 0]]"),
    ("镜头 = 尺子 P₂\n（斜尺子）", "A₂ = [[-1, -2],\n      [1, 1]]"),
]
xs = [2.7, 7.0, 11.3]
for (title, mtxt), cx in zip(cards, xs):
    draw_card(ax, cx, 3.9, 3.8, 4.0)
    ax.text(cx, 5.25, title, ha="center", va="center", fontsize=10.5, color=C_GRAY)
    ax.text(cx, 3.95, mtxt, ha="center", va="center", fontsize=12, family="monospace")
    ax.text(cx, 2.55, "血型：det = 1 · tr = 0", ha="center", fontsize=11,
            color=C_RED, rotation=-4, weight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=C_RED, lw=1.6))
    ax.annotate("", xy=(cx, 6.15), xytext=(7.0, 6.55),
                arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=1.4))

ax.text(7.0, 0.75, "三张“照片”美丑各异，盖的血型章却完全一致 ——\n"
                   "det 和迹只是开胃菜，Week 7 揭晓终极指纹：特征值相同",
        ha="center", fontsize=12, color="#333333")

fig.suptitle("5.3 · 相似矩阵 = 同一头猪的不同照片（“相似照片”）", fontsize=15)
fig.subplots_adjust(top=0.9, bottom=0.03)
save(fig, "w4d5_similar_family.png")
