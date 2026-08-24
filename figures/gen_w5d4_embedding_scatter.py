"""W5D4 图：二维"词向量"散点 —— 相似度 = 夹角。

右上角"猫/狗/老虎/小猫"挤成一团，直接挨点标注必然互相遮挡，
所以密集簇的标签全部拉到人群外（左侧 / 右侧），用细引线指回各自的点；
分散的词（汽车/火车/自行车/苹果/香蕉）仍然挨点标注。
"""
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

fig, ax = plt.subplots(figsize=(8.5, 7))
axes(ax, xlim=(-4, 4), ylim=(-3.5, 4.5))

BBOX = dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9)


def lead(color, lw=0.9):
    """细灰引线：从标签连到目标点，不压任何文字。"""
    return dict(arrowstyle="-", color=color, lw=lw, shrinkA=2, shrinkB=3)


def tag(text, xy, xytext, color="#444444", fontsize=12, ha="left"):
    """带引线的标签：文字放在 xytext，引线指到 xy。"""
    ax.annotate(text, xy=xy, xytext=xytext, color=color, fontsize=fontsize,
                ha=ha, bbox=BBOX, zorder=8, arrowprops=lead(color))


def plain(text, xy, dx=0.14, dy=0.14, color="#444444", fontsize=12):
    """挨点标注（只用于周围空旷的词）。"""
    ax.text(xy[0] + dx, xy[1] + dy, text, fontsize=fontsize, color=color,
            bbox=BBOX, zorder=6)


# ---- 所有词向量点 ----
for w, p in words.items():
    ax.scatter([p[0]], [p[1]], color=C_GRAY, s=60, zorder=5)

# 周围空旷的词：挨点标注
plain("汽车", words["汽车"])
plain("火车", words["火车"])
plain("自行车", words["自行车"])
plain("苹果", words["苹果"])
plain("香蕉", words["香蕉"])

# ---- 右上角密集簇：标签拉到人群外 + 引线 ----
# 右侧一列：老虎（挨点即可）、猫、狗
plain("老虎", words["老虎"], dx=0.14, dy=0.08)
tag("猫", words["猫"], (3.15, 2.90))
tag("狗", words["狗"], (3.15, 2.25))

# 查询点：红色星星，标签放左侧
ax.scatter([q[0]], [q[1]], color=C_RED, s=110, zorder=6, marker="*")
tag(f"{query}（查询）", q, (0.4, 3.45), color=C_RED)

# ---- 最近邻连线（橙）与对照连线（蓝） ----
names = list(words.keys())
vecs = list(words.values())
best = names[nearest_index(q, vecs)]
p = words[best]
ax.plot([q[0], p[0]], [q[1], p[1]], color=C_ORANGE, lw=2.5, ls="--", zorder=4)
tag(f"cos = {cosine_similarity(q, p):.2f}",
    ((q[0] + p[0]) / 2, (q[1] + p[1]) / 2), (0.4, 4.25), color=C_ORANGE, fontsize=11)

# 对照：与"汽车"的夹角大得多
p2 = words["汽车"]
ax.plot([q[0], p2[0]], [q[1], p2[1]], color=C_BLUE, lw=1.5, ls=":", zorder=3)
tag(f"cos = {cosine_similarity(q, p2):.2f}",
    ((q[0] + p2[0]) / 2, (q[1] + p2[1]) / 2), (-2.15, 2.45), color=C_BLUE, fontsize=11)

ax.set_title(f"Week 5 · “{query}”与“{best}”夹角最小 → 最相似\n相似度不看距离长短，只看方向（夹角）", fontsize=13)
save(fig, "w5d4_embedding_scatter.png")
