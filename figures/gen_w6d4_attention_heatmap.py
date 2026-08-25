"""W6D4 图：迷你句子的注意力热力图（随机 2D 词向量）。"""
import random
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.attention import attention_scores, attention_weights
from figures._common import save

words = ["我", "爱", "吃", "苹果", "，", "很甜"]
random.seed(42)
X = [[round(random.uniform(-1, 1), 3), round(random.uniform(-1, 1), 3)]
     for _ in words]

scores = attention_scores(X, X)
weights = attention_weights(scores)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

im1 = ax1.imshow(scores, cmap="Blues")
ax1.set_xticks(range(len(words)), words)
ax1.set_yticks(range(len(words)), words)
ax1.set_title(r"亲密度分数 $Q\cdot K^{\mathsf{T}}$（未归一化）", fontsize=13)
for i in range(len(words)):
    for j in range(len(words)):
        ax1.text(j, i, f"{scores[i][j]:.2f}", ha="center", va="center",
                 fontsize=9, color="white" if scores[i][j] > 0.4 else "#333333")

im2 = ax2.imshow(weights, cmap="Oranges", vmin=0, vmax=1)
ax2.set_xticks(range(len(words)), words)
ax2.set_yticks(range(len(words)), words)
ax2.set_title("softmax 后：每行（每个查询）的总和 = 1", fontsize=13)
for i in range(len(words)):
    for j in range(len(words)):
        ax2.text(j, i, f"{weights[i][j]:.2f}", ha="center", va="center",
                 fontsize=9, color="white" if weights[i][j] > 0.5 else "#333333")

fig.suptitle("Week 6 · 注意力矩阵：第 i 行 = 第 i 个词“看”整句话的分配方案", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.82, wspace=0.28)
save(fig, "w6d4_attention_heatmap.png")
