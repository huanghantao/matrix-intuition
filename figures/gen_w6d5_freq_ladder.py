"""W6D5 图：频率梯子为什么"长短通吃"——单一频率的两个失败实验 + 梯子分工图。

图 A w6d5_freq_trap.png      —— 单一频率两头都顾不上：
     左 快针 θ=1 的 cos(m) 曲线：位置 62 与 106（相距 44 词）读数几乎一样（撞针）；
     中 两只钟面并排：转过 62 rad 和 106 rad 之后，针指在同一个地方；
     右 慢针 θ=0.001 的 cos(m·θ) 曲线：500 个位置近乎直线，近处分不开。
图 B w6d5_ladder_division.png —— 频率梯子的分工：
     左 每根针自己的"分数-距离"曲线 cos(r·θ_i)，色带标出各自的最佳工作区；
     右 撞针对 62 vs 106 在四根针上的读数差：第 0 对撞了，第 1 对一票否决。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
from matplotlib.patches import Circle

from figures._common import C_BLUE, C_ORANGE, C_PURPLE, C_RED, save

THETAS = np.array([1.0, 0.1, 0.01, 0.001])       # d=8 时的四根针
THETA_STR = ["1", "0.1", "0.01", "0.001"]
PAIR_COLORS = [C_RED, C_ORANGE, C_BLUE, C_PURPLE]
TWO_PI = 2 * np.pi


def reading(m, theta):
    """位置 m 的钟面读数 (cos mθ, sin mθ)。"""
    return np.array([np.cos(m * theta), np.sin(m * theta)])


def reading_dist(a, b, theta):
    """两个位置的钟面读数差（2D 欧氏距离），0 = 撞针。"""
    return float(np.linalg.norm(reading(a, theta) - reading(b, theta)))


# ------------------------------------------------ 打印 markdown 里要引用的数字
print("== 实验①：快针 θ=1 找撞针（前 300 个位置、相距 30 词以上的最像一对）==")
best = None
for m1 in range(300):
    for m2 in range(m1 + 30, 300):
        d = reading_dist(m1, m2, THETAS[0])
        if best is None or d < best[0]:
            best = (d, m1, m2)
d, m1, m2 = best
gap = m2 - m1
print(f"  撞针对：位置 {m1} 和 {m2}，相距 {gap} 词，钟面读数差 {d:.3f}")
print(f"  {gap} 个词转过 {gap} rad = {int(gap // TWO_PI)} 整圈再多 {gap % TWO_PI:.3f} rad")

print("== 实验②：慢针 θ=0.001 ==")
ms = np.arange(500)
diffs = [reading_dist(m, m + 1, THETAS[3]) for m in range(499)]
print(f"  相邻位置读数差最大 {max(diffs):.6f}")
print(f"  500 个位置总共只挪了 {1 - np.cos(499 * THETAS[3]):.3f}")
cos_f16 = [float(np.float16(np.cos(m * THETAS[3]))) for m in range(500)]
collapse16 = sum(1 for k in range(499) if cos_f16[k] == cos_f16[k + 1])
print(f"  float16 下相邻 cos 完全相同的相邻对：{collapse16}/499")

print("== 梯子验证：三组位置对、四根针的钟面读数差 ==")
rows = [(62, 106, "相距 44 词，快针撞针"), (100, 101, "相邻两词，慢针没劲"), (0, 2000, "句首 vs 句中")]
for a, b, _ in rows:
    ds = [reading_dist(a, b, t) for t in THETAS]
    print(f"  {a} vs {b}: " + "  ".join(f"{x:.3f}" for x in ds))

# ================================================================ 图 A：失败实验
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.7))

# 左：快针曲线 + 撞针对
tt = np.linspace(0, 120, 4000)
ax1.plot(tt, np.cos(tt), color=C_RED, lw=1.8)
cy1, cy2 = np.cos(m1), np.cos(m2)
ax1.plot([m1, m2], [cy1, cy2], ls="--", color="#888888", lw=1)
ax1.scatter([m1, m2], [cy1, cy2], color=C_RED, s=45, zorder=5)
ax1.annotate(f"位置 {m1} 和 {m2}：相距 {gap} 个词\n钟面读数只差 {d:.3f} —— 撞针！",
             xy=((m1 + m2) / 2, cy1), xytext=(60, -0.9), color=C_RED, fontsize=10,
             ha="center", arrowprops=dict(arrowstyle="->", color=C_RED),
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax1.text(60, 1.14, "每 6.3 个词转满一圈", color="#666666", fontsize=9, ha="center")
ax1.axhline(0, color="#333333", lw=0.8)
ax1.set_xlim(0, 120)
ax1.set_ylim(-1.3, 1.32)
ax1.set_xlabel("位置 m")
ax1.set_ylabel("cos(m·θ)")
ax1.set_title("快针 θ=1（6.3 个词转一圈）\n远处的位置\u201c撞针\u201d", fontsize=12)

# 中：两只钟面并排
ax2.set_aspect("equal", adjustable="box")
ax2.axis("off")
for cx, m in [(-1.15, m1), (1.15, m2)]:
    ang = m % TWO_PI
    ax2.add_patch(Circle((cx, 0.05), 0.85, fill=False, edgecolor="#aaaaaa", lw=1.2))
    ax2.plot([cx], [0.05], marker="o", ms=3, color="#888888")
    ax2.plot([cx, cx], [0.9, 0.9], marker="|", ms=6, color="#aaaaaa")  # 12 点刻度
    ax2.annotate("", xy=(cx + 0.70 * np.cos(ang), 0.05 + 0.70 * np.sin(ang)),
                 xytext=(cx, 0.05),
                 arrowprops=dict(arrowstyle="-|>", color=C_RED, lw=2.5,
                                 shrinkA=0, shrinkB=0, mutation_scale=16))
    ax2.text(cx, -1.02, f"位置 {m} 的钟面", color="#333333", fontsize=10.5,
             ha="center", va="top")
    ax2.text(cx, -1.24,
             f"转过 {m} rad = {int(m // TWO_PI)} 圈 + {np.degrees(ang):.1f}°",
             color="#666666", fontsize=9, ha="center", va="top")
ax2.text(0, 1.08, "两个相距 44 个词的位置，钟面几乎一样\n—— 模型分不清",
         color="#333333", fontsize=10.5, ha="center")
ax2.set_xlim(-2.4, 2.4)
ax2.set_ylim(-1.55, 1.4)
ax2.set_title("转完之后的钟面：针指同一个地方", fontsize=12)

# 右：慢针曲线 + 放大插图
ax3.plot(ms, np.cos(ms * THETAS[3]), color=C_PURPLE, lw=2)
ax3.annotate("500 个位置只挪了 0.12\n整条曲线看上去就是一条直线",
             xy=(200, np.cos(0.2)), xytext=(360, 0.45), color="#444444", fontsize=9.5,
             ha="center", arrowprops=dict(arrowstyle="->", color="#888888"),
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax3.annotate("相邻读数差 ≤ 0.001\nfloat16 下 499 个相邻对里 249 个完全相同\n（bfloat16 更糟：全糊）",
             xy=(390, np.cos(0.39)), xytext=(355, -0.60), color=C_PURPLE, fontsize=9.5,
             ha="center", arrowprops=dict(arrowstyle="->", color=C_PURPLE),
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
axin = ax3.inset_axes([0.10, 0.12, 0.44, 0.30])
axin.plot(np.arange(31), np.cos(np.arange(31) * THETAS[3]), color=C_PURPLE, lw=1.8)
axin.set_ylim(0.9994, 1.0001)
axin.tick_params(labelsize=7)
axin.set_title("放大前 30 个词：还是不动", fontsize=8.5)
ax3.axhline(0, color="#333333", lw=0.8)
ax3.set_xlim(0, 500)
ax3.set_ylim(-1.3, 1.32)
ax3.set_xlabel("位置 m")
ax3.set_ylabel("cos(m·θ)")
ax3.set_title("慢针 θ=0.001（6283 个词转一圈）\n相邻位置\u201c分不开\u201d", fontsize=12)

fig.suptitle("单一频率实验：快针 θ=1 远处\u201c撞针\u201d，慢针 θ=0.001 近处\u201c分不开\u201d",
             fontsize=13.5, y=1.02)
fig.subplots_adjust(wspace=0.28)
save(fig, "w6d5_freq_trap.png")

# ================================================================ 图 B：梯子分工
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 4.9))

# 左：每根针的 cos(r·θ_i) 曲线 + 最佳工作区色带
rr = np.logspace(np.log10(0.5), np.log10(TWO_PI / THETAS[3]), 30000)
for i, t in enumerate(THETAS):
    ax1.plot(rr, np.cos(rr * t), color=PAIR_COLORS[i], lw=1.3)
for i, t in enumerate(THETAS):
    lo, hi = 0.5 / t, np.pi / t          # 最佳工作区：转过 0.5~π 弧度
    ax1.axvspan(lo, hi, color=PAIR_COLORS[i], alpha=0.10, zorder=0)
    label = f"第{i}对管\n0.5~{hi:.0f} 词" if i == 0 else f"第{i}对管\n{lo:.0f}~{hi:.0f} 词"
    ax1.text(np.sqrt(lo * hi), 1.38, label, color=PAIR_COLORS[i], fontsize=9,
             ha="center", va="center")
ax1.annotate("快针转了太多圈：读数已经\n乱成一团，远处指望不上",
             xy=(700, -0.3), xytext=(700, -0.85), color=C_RED, fontsize=9,
             ha="center", arrowprops=dict(arrowstyle="->", color=C_RED),
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax1.text(4300, 1.12, "r 再大，最慢的针也开始回卷\n（更长上下文：调大 base）",
         color="#666666", fontsize=8.5, ha="center",
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
         zorder=6)
ax1.set_xscale("log")
ax1.set_xlim(0.5, TWO_PI / THETAS[3])
ax1.set_ylim(-1.15, 1.55)
ax1.set_xticks([1, 10, 100, 1000])
ax1.xaxis.set_major_formatter(mticker.ScalarFormatter())
ax1.set_xlabel("相对距离 r（log 轴）")
ax1.set_ylabel("第 i 对的读数 cos(r·θ_i)")
ax1.set_title("每根针自己的\u201c分数-距离\u201d曲线：\n色带 = 最佳工作区（转过 0.5~π 弧度，一段接一段）",
              fontsize=12)

# 右：撞针对在四根针上的读数差（一票否决）
a, b = m1, m2
ds = [reading_dist(a, b, t) for t in THETAS]
bars = ax2.bar(range(4), ds, color=PAIR_COLORS, width=0.62)
for i, (bar, val) in enumerate(zip(bars, ds)):
    ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.05, f"{val:.3f}",
             ha="center", fontsize=10.5, color=PAIR_COLORS[i])
ax2.text(0, 0.16, "撞针！\n读数一样", color=C_RED, fontsize=9.5, ha="center")
ax2.annotate("一票否决：读数差 1.617\n两个位置明明白白分开",
             xy=(1, ds[1] + 0.02), xytext=(1.75, 1.85), color=C_ORANGE, fontsize=9.5,
             ha="center", arrowprops=dict(arrowstyle="->", color=C_ORANGE),
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax2.set_xticks(range(4), [f"第 {i} 对\nθ={THETA_STR[i]}" for i in range(4)])
ax2.set_ylim(0, 2.1)
ax2.set_ylabel("钟面读数差（0 = 分不清）")
ax2.set_title(f"位置 {a} vs {b}（相距 {gap} 词）：第 0 对撞了，别的针没撞\n—— 撞针必须所有针一起撞才算数",
              fontsize=12)

fig.suptitle("频率梯子的分工：每个距离尺度，都有一根针\u201c既灵敏又不撞针\u201d",
             fontsize=13.5, y=1.0)
fig.subplots_adjust(wspace=0.25)
save(fig, "w6d5_ladder_division.png")
