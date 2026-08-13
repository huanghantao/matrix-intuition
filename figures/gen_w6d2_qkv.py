"""W6D2 图：Q、K、V 流水线 —— 三个变换，三种角色。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GREEN, C_ORANGE, C_RED, save

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.axis("off")


def box(x, y, w, h, text, color="#ffffff", fs=12):
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=True, facecolor=color,
                               edgecolor="#333333", lw=1.5))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)


def arrow(x1, y1, x2, y2, color="#333333", label=None, lx=0, ly=0.03):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    if label:
        ax.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label,
                ha="center", va="bottom", fontsize=11, color=color)


# 左侧：X（词向量矩阵）
box(0.02, 0.30, 0.16, 0.30, "X\n每个词一行\n（Week 1 的词向量）", "#eaf2fb")
# 三个投影
box(0.32, 0.66, 0.16, 0.22, "×Wq 投影", "#d5e8f7")
box(0.32, 0.38, 0.16, 0.22, "×Wk 投影", "#d5e8f7")
box(0.32, 0.10, 0.16, 0.22, "×Wv 投影", "#d5e8f7")
box(0.58, 0.66, 0.12, 0.22, "Q\n“我在找谁”", "#fdeadd")
box(0.58, 0.38, 0.12, 0.22, "K\n“我是谁”", "#fdeadd")
box(0.58, 0.10, 0.12, 0.22, "V\n“我装了啥”", "#fdeadd")
# 分数、权重、输出
box(0.80, 0.54, 0.17, 0.22, "Q·K 点积\n= 亲密度分数", "#fef0d9")
box(0.80, 0.26, 0.17, 0.22, "softmax\n= 注意力权重\n（行和为 1）", "#fef0d9")
box(0.80, 0.02, 0.17, 0.18, "加权求和 Σw·V\n= 上下文融合后的新词向量", "#f7e3c5")

arrow(0.18, 0.45, 0.32, 0.77, label="Week 3 的变换")
arrow(0.18, 0.45, 0.32, 0.49)
arrow(0.18, 0.45, 0.32, 0.21)
arrow(0.48, 0.77, 0.58, 0.77)
arrow(0.48, 0.49, 0.58, 0.49)
arrow(0.48, 0.21, 0.58, 0.21)
arrow(0.70, 0.71, 0.80, 0.61, label="Week 5 的点积")
arrow(0.88, 0.54, 0.88, 0.48)
arrow(0.88, 0.26, 0.86, 0.20, label="Week 2 的线性组合")
arrow(0.70, 0.15, 0.80, 0.10)

ax.text(0.5, 0.97, "Week 6 · Attention = 变换(3) + 点积(5) + softmax + 加权求和(2)，括号里是它用到的周数",
        ha="center", fontsize=13)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.02)
save(fig, "w6d2_qkv.png")
