"""W5D4 图：二维"词向量"散点 —— 相似度 = 夹角。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.similarity import cosine_similarity, nearest_index
from figures._common import C_BLUE, C_GRAY, C_ORANGE, C_RED, axes, save

words = {
    "猫": (2.0, 3.0),
    "狗": (2.2, 2.6),
    "老虎": (2.9, 3.2),
    "汽车": (-3.0, 1.0),
    "火车": (-2.7, 1.6),
    "自行车": (-2.3, 0.7),
    "苹果": (0.5, -2.4),
    "香蕉": (0.2, -2.0),
}
query = "小猫"
q = (2.1, 2.9)

fig, ax = plt.subplots(figsize=(7.5, 6.5))
axes(ax, xlim=(-4, 4), ylim=(-3.5, 4.5))

for w, p in words.items():
    ax.scatter([p[0]], [p[1]], color=C_GRAY, s=60, zorder=5)
    ax.text(p[0] + 0.12, p[1] + 0.12, w, fontsize=12, color="#444444")

ax.scatter([q[0]], [q[1]], color=C_RED, s=90, zorder=6, marker="*")
ax.text(q[0] + 0.15, q[1] + 0.15, f"{query}（查询）", color=C_RED, fontsize=12)

# 找最近邻
names = list(words.keys())
vecs = list(words.values())
best = names[nearest_index(q, vecs)]
p = words[best]
ax.plot([q[0], p[0]], [q[1], p[1]], color=C_ORANGE, lw=2, ls="--")
ax.text((q[0] + p[0]) / 2 + 0.2, (q[1] + p[1]) / 2,
        f"cos = {cosine_similarity(q, p):.2f}", color=C_ORANGE, fontsize=11)

# 对照：与"汽车"的夹角大得多
p2 = words["汽车"]
ax.plot([q[0], p2[0]], [q[1], p2[1]], color=C_BLUE, lw=1.5, ls=":")
ax.text((q[0] + p2[0]) / 2 - 1.6, (q[1] + p2[1]) / 2,
        f"cos = {cosine_similarity(q, p2):.2f}", color=C_BLUE, fontsize=11)

ax.set_title(f"Week 5 · “{query}”与“{best}”夹角最小 → 最相似\n相似度不看距离长短，只看方向（夹角）", fontsize=13)
save(fig, "w5d4_embedding_scatter.png")
