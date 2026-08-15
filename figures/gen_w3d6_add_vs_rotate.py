"""W3D6 彩蛋图：为什么用"旋转"而不是"加一个大数"编码位置？

两张图：
1. w3d6_add_vs_rotate.png —— 几何对比：加法让向量越来越长、方向趋同（语义被淹没）；
   旋转长度不变，位置写进方向。
2. w3d6_dot_compare.png —— 点积对比：加法编码下"同样相邻"的词对得分差约 800 倍；
   旋转编码下完全相同。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GRAY, C_RED, save

# 同一个词向量、同一组位置，两种编码方案
v = np.array([1.0, 0.0])          # 词向量（语义）
c = np.array([1.0, 0.8])          # 加法方案：每个位置要加的"大数"方向
theta = 30.0                      # 旋转方案：每个位置转 30°
M = 5                             # 位置 0..4
colors = ["#9ecae1", "#6baed6", "#3182bd", "#08519c", "#08306b"]


def rotate(vec, deg):
    t = np.radians(deg)
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    return R @ vec


def arrow(ax, tip, color, lw=2.5):
    ax.annotate("", xy=tip, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=16))


# ============ 图 1：几何对比 ============
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6))

# 左：加法编码 —— v + m·c
ax1.set_aspect("equal", adjustable="box")
ax1.axhline(0, color="#333333", lw=1)
ax1.axvline(0, color="#333333", lw=1)
# c 的方向（所有向量的"吸引子"）
cu = c / np.linalg.norm(c)
ax1.plot([0, cu[0] * 6.4], [0, cu[1] * 6.4], ls="--", color=C_GRAY, lw=1.2)
ax1.annotate("c 的方向：\n所有向量都被拉向它", xy=(cu[0] * 4.6, cu[1] * 4.6),
             xytext=(4.3, 1.0), color=C_GRAY, fontsize=10, ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color=C_GRAY, lw=1.0))
# 先画长的、后画短的：加法方案里各向量几乎共线，短的压在最上面才都看得见
for m in reversed(range(M)):
    enc = v + m * c
    arrow(ax1, enc, colors[m])
    ax1.text(enc[0] + 0.12, enc[1] + 0.22, f"位置 {m}\n长 {np.linalg.norm(enc):.1f}",
             color=colors[m], fontsize=9.5, ha="left", va="bottom",
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax1.set_xlim(-0.6, 7.6)
ax1.set_ylim(-0.6, 5.2)
ax1.set_title("加法编码：位置 m → 向量加 m·c\n越来越长、方向趋同 —— 语义被淹没",
              fontsize=12.5, color=C_RED)

# 右：旋转编码 —— 转 m·θ
ax2.set_aspect("equal", adjustable="box")
ax2.axhline(0, color="#333333", lw=1)
ax2.axvline(0, color="#333333", lw=1)
r = np.linalg.norm(v)
ax2.add_patch(plt.Circle((0, 0), r, fill=False, color="#cccccc", lw=1.2))
for m in range(M):
    enc = rotate(v, m * theta)
    arrow(ax2, enc, colors[m])
    ax2.text(enc[0] * 1.38, enc[1] * 1.38, f"位置 {m}\n转 {m * theta:.0f}°",
             color=colors[m], fontsize=9.5, ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax2.text(0, -r * 1.45, f"长度永远是 {r:.2f}（= 原向量长度）", color=C_BLUE,
         fontsize=10.5, ha="center", va="top")
ax2.set_xlim(-2.0, 2.0)
ax2.set_ylim(-2.0, 2.0)
ax2.set_title("旋转编码：位置 m → 转 m·θ\n长度纹丝不动，位置写进方向",
              fontsize=12.5, color=C_BLUE)

fig.suptitle("同一个词、同样的 5 个位置：两种位置编码的几何对比", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.82, wspace=0.25)
save(fig, "w3d6_add_vs_rotate.png")

# ============ 图 2：点积对比 ============
# 加法（1 维简化：词向量=1，c=10）：enc(x, m) = x + 10m
def add_enc(x, m):
    return x + 10 * m

add_pairs = [("位置 (3, 4)", add_enc(1, 3) * add_enc(1, 4)),
             ("位置 (100, 101)", add_enc(1, 100) * add_enc(1, 101))]
# 旋转（2 维单位向量，θ=30°）：q_m·k_n = cos((m-n)·θ)
rot_pairs = [("位置 (0, 1)", np.cos(np.radians(1 * theta))),
             ("位置 (3, 4)", np.cos(np.radians(1 * theta))),
             ("位置 (100, 101)", np.cos(np.radians(1 * theta)))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8))

xs = range(len(add_pairs))
ax1.bar(xs, [s for _, s in add_pairs], width=0.45, color=[C_RED, C_RED])
for x, (name, s) in zip(xs, add_pairs):
    ax1.annotate(f"{s:,.0f}", (x, s), textcoords="offset points",
                 xytext=(0, 8), ha="center", fontsize=12, color=C_RED)
ax1.set_xticks(list(xs), [name for name, _ in add_pairs])
ax1.set_ylabel("q · k")
ax1.set_ylim(0, 1.2e6)
ax1.set_title("加法编码：两对都是「相邻」，\n点积却差了约 800 倍", fontsize=12.5,
              color=C_RED)

xs = range(len(rot_pairs))
ax2.bar(xs, [s for _, s in rot_pairs], width=0.45, color=[C_BLUE] * 3)
for x, (name, s) in zip(xs, rot_pairs):
    ax2.annotate(f"{s:.3f}", (x, s), textcoords="offset points",
                 xytext=(0, 8), ha="center", fontsize=12, color=C_BLUE)
ax2.set_xticks(list(xs), [name for name, _ in rot_pairs])
ax2.set_ylim(0, 1.0)
ax2.set_title("旋转编码：相对位置相同，\n三对得分一模一样 = cos(30°)", fontsize=12.5,
              color=C_BLUE)

fig.suptitle("attention 靠点积打分：两种编码给「相邻词对」的分数", fontsize=15, y=1.0)
fig.subplots_adjust(top=0.78, wspace=0.25)
save(fig, "w3d6_dot_compare.png")
