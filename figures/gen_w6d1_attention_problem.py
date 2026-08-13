"""W6D1 图：Attention 要解决的问题 —— 该看谁。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import save

fig, ax = plt.subplots(figsize=(9, 4))
ax.axis("off")

words = ["我", "爱", "吃", "苹果"]
boxes = []
for i, w in enumerate(words):
    x = 0.12 + i * 0.24
    b = plt.Rectangle((x, 0.45), 0.16, 0.16, fill=True,
                      facecolor="#1f77b4", edgecolor="#333333", lw=1.5)
    ax.add_patch(b)
    ax.text(x + 0.08, 0.53, w, ha="center", va="center",
            color="white", fontsize=16)
    boxes.append((x + 0.08, 0.53))

# 从"吃"指向"苹果"的粗箭头
ax.annotate("", xy=(boxes[3][0], boxes[3][1] + 0.1),
            xytext=(boxes[2][0], boxes[2][1] + 0.1),
            arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=3))
ax.text(0.66, 0.86, "重点看它！", color="#d62728", fontsize=14)

# 其他词之间细虚线
for i in range(3):
    ax.annotate("", xy=(boxes[i + 1][0], boxes[i + 1][1] + 0.1),
                xytext=(boxes[i][0], boxes[i][1] + 0.1),
                arrowprops=dict(arrowstyle="-|>", color="#aaaaaa", lw=1,
                                linestyle="--"))

ax.text(0.5, 0.18, "“吃”这个位置的翻译/理解，需要知道吃的是什么\n→ 每个词都要学会：从整句话里挑重点、按重要程度汇总信息",
        ha="center", fontsize=13)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Week 6 · Attention 要解决的问题", fontsize=15)
save(fig, "w6d1_attention_problem.png")
