"""W6D3 图：softmax —— 把分数变成百分比。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.attention import softmax
from figures._common import C_BLUE, C_ORANGE, save

scores = [-2.0, -0.5, 2.5]
weights = softmax(scores)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
labels = ["词 A", "词 B", "词 C"]

bars1 = ax1.bar(labels, scores, color=C_BLUE, alpha=0.8)
ax1.axhline(0, color="#333333", lw=1)
ax1.set_title("原始分数 Q·K：可正可负，加起来不是 1", fontsize=13)
ax1.set_ylabel("分数")
# 给负柱也留出底部空间，避免数值标签压到 x 轴刻度
ax1.set_ylim(-2.6, 3.0)
for b, s in zip(bars1, scores):
    ax1.text(b.get_x() + b.get_width() / 2, s + (0.08 if s >= 0 else -0.18),
             f"{s}", ha="center", fontsize=12, color="#333333")

bars2 = ax2.bar(labels, weights, color=C_ORANGE, alpha=0.85)
ax2.set_ylim(0, 1.05)
ax2.set_title("softmax 之后：都是正数，加起来 = 1\n（“总注意力 100%”的分配方案）", fontsize=13)
ax2.set_ylabel("权重")
for b, w in zip(bars2, weights):
    ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.02,
             f"{w:.2f}", ha="center", fontsize=12, color="#333333")
# 求和说明放在左上角空白处（词 A、词 B 的柱子很矮，上方是空的），
# 避免压住右侧 0.94 高柱和它的数值标签
ax2.text(0.03, 0.95, "0.01 + 0.05 + 0.94 = 1.00", transform=ax2.transAxes,
         fontsize=12, color="#333333", ha="left", va="top")

fig.suptitle("Week 6 · softmax：分数最大的分到几乎全部注意力", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.82, wspace=0.28)
save(fig, "w6d3_softmax.png")
