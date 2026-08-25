"""W6D2 图：Attention 流水线的四站直觉分工图。

四站：投影（运动直觉 W3）→ 配对（亲密度直觉 W5）→ softmax（百分比 D3）→ 汇总（配方直觉 W2）。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_ORANGE, C_PURPLE, save

DARK = "#333333"
Y = 1.9          # 流水线高度
BW, BH = 2.35, 1.15


def station(ax, x, title, sub, color):
    box = FancyBboxPatch((x - BW / 2, Y - BH / 2), BW, BH,
                         boxstyle="round,pad=0.09",
                         fc="white", ec=color, lw=2.2, zorder=3)
    ax.add_patch(box)
    ax.text(x, Y + 0.18, title, ha="center", va="center",
            fontsize=12.5, color=color, weight="bold", zorder=4)
    ax.text(x, Y - 0.28, sub, ha="center", va="center",
            fontsize=11, color=color, zorder=4)


def flow(ax, x_from, x_to, label=None):
    ax.annotate("", xy=(x_to, Y), xytext=(x_from, Y),
                arrowprops=dict(arrowstyle="-|>", color=C_GRAY, lw=2,
                                shrinkA=0, shrinkB=0, mutation_scale=18))
    if label:
        ax.text((x_from + x_to) / 2, Y + 0.42, label, ha="center", va="center",
                fontsize=11.5, color=DARK,
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.9),
                zorder=5)


def caption(ax, x, text):
    ax.text(x, Y - 1.05, text, ha="center", va="center", fontsize=10.5, color=C_GRAY)


fig, ax = plt.subplots(figsize=(13, 3.6))
ax.set_xlim(-0.4, 13.2)
ax.set_ylim(0.3, 3.1)
ax.axis("off")

X1, X2, X3, X4 = 2.35, 5.35, 8.05, 10.75

ax.text(0.15, Y, "X\n（每个词一行）", ha="center", va="center",
        fontsize=11.5, color=DARK, weight="bold")
flow(ax, 0.85, X1 - BW / 2 - 0.05)

station(ax, X1, "① 投影  ×Wq/Wk/Wv", "运动直觉（Week 3）", C_BLUE)
caption(ax, X1, "进一个出一个：\n同一个词，换个空间")
flow(ax, X1 + BW / 2 + 0.05, X2 - BW / 2 - 0.05, "Q, K, V")

station(ax, X2, r"② 配对  $Q\cdot K^T$", "亲密度直觉（Week 5）", C_GREEN)
caption(ax, X2, "一堆点积堆成表：\n每个格子测一次合拍")
flow(ax, X2 + BW / 2 + 0.05, X3 - BW / 2 - 0.05, "scores")

station(ax, X3, "③ 归一  softmax", "百分比（Day 3）", C_ORANGE)
caption(ax, X3, "分数翻译成权重：\n每行加起来恰好 100%")
flow(ax, X3 + BW / 2 + 0.05, X4 - BW / 2 - 0.05, "weights")

station(ax, X4, "④ 汇总  ×V", "配方直觉（Week 2）", C_PURPLE)
caption(ax, X4, "进多个出一个：\n按关注度揉合干货")
flow(ax, X4 + BW / 2 + 0.05, 12.55)
ax.text(12.85, Y, "out\n（新词向量）", ha="center", va="center",
        fontsize=11.5, color=DARK, weight="bold")

save(fig, "w6d2_intuition_stations.png")
