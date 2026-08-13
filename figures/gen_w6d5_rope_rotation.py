"""W6D5 图：RoPE —— 位置 = 旋转角度；分数只与相对位置有关。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from reference.rope import rope_score, rotate_2d
from figures._common import C_BLUE, C_ORANGE, C_RED, save

theta = 30.0
colors = ["#9ecae1", "#6baed6", "#3182bd", "#08519c"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 左：位置 m 的词向量被旋转 m*θ
ax1.set_aspect("equal", adjustable="box")
ax1.axhline(0, color="#333333", lw=1)
ax1.axvline(0, color="#333333", lw=1)
ax1.add_patch(plt.Circle((0, 0), 1, fill=False, color="#cccccc"))
for m in range(4):
    v = rotate_2d([1.0, 0.0], m * theta)
    ax1.annotate("", xy=(v[0], v[1]), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="-|>", color=colors[m], lw=2.5))
    ax1.text(v[0] * 1.22, v[1] * 1.22, f"位置 {m}\n转 {m * theta}°",
             color=colors[m], fontsize=11, ha="center", va="center")
ax1.set_xlim(-1.6, 1.6)
ax1.set_ylim(-1.6, 1.6)
ax1.set_title("每个位置转不同的角度（θ=30°）", fontsize=13)

# 右：q_m·k_n 只与 (m-n) 有关
q = [1.0, 0.0]
k = [1.0, 0.0]
diffs = list(range(-6, 7))
scores = []
for d in diffs:
    qm = rotate_2d(q, (d + 3) * theta)  # m = d+3, n = 3
    kn = rotate_2d(k, 3 * theta)
    scores.append(rope_score(qm, kn))

ax2.plot(diffs, scores, "o-", color=C_BLUE, lw=2)
ax2.axhline(0, color="#333333", lw=1)
ax2.set_xlabel("相对位置 m - n")
ax2.set_ylabel("q_m · k_n")
ax2.set_title("分数只与相对位置有关：cos((m-n)·30°)\n（m 和 n 一起平移，分数纹丝不动）", fontsize=13)
for d, s in zip(diffs, scores):
    if d in (-3, 0, 3, 6):
        ax2.annotate(f"{s:.2f}", (d, s), textcoords="offset points",
                     xytext=(0, 10), ha="center", fontsize=10)

fig.suptitle("Week 6 · RoPE：用旋转矩阵给词排队，位置信息藏进夹角里", fontsize=15)
save(fig, "w6d5_rope_rotation.png")
