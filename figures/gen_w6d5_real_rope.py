"""W6D5 图：真实 RoPE 的三张图解。

图 A w6d5_real_rope_pairs.png  —— 完整例子：d=8 切成 4 对，位置 m=2 各转各的。
图 B w6d5_real_rope_matrix.png —— 8×8 块对角旋转矩阵 R(m)：4 个 2×2 小旋转沿对角线排开。
图 C w6d5_real_rope_waves.png  —— 每对是一只转速不同的时钟 + 相对距离越远分数越衰减。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Patch, Rectangle

from figures._common import C_BLUE, C_ORANGE, C_PURPLE, C_RED, save

D = 8                 # 词向量维度（真实模型里是 64/128，这里用 8 演示）
BASE = 10000
M = 2                 # 演示用位置
PAIR_COLORS = [C_RED, C_ORANGE, C_BLUE, C_PURPLE]

theta = BASE ** (-np.arange(0, D, 2) / D)   # [1, 0.1, 0.01, 0.001]
theta_str = ["1", "0.1", "0.01", "0.001"]
angles = M * theta                          # 每对在位置 m 要转的角度（弧度）


def rot(pair, ang):
    """rotate_2d 的 NumPy 版：2D 向量逆时针转 ang 弧度。"""
    c, s = np.cos(ang), np.sin(ang)
    return np.array([c * pair[0] - s * pair[1], s * pair[0] + c * pair[1]])


x = np.array([1.0, 0.0] * (D // 2))         # [1,0,1,0,1,0,1,0]
pairs = x.reshape(-1, 2)
rotated = np.array([rot(p, a) for p, a in zip(pairs, angles)])

# 打印 markdown 里要引用的数字，保证图文一致
np.set_printoptions(precision=4, suppress=True)
print("theta =", theta)
print("m*theta (deg) =", np.degrees(angles))
print("rotated x' =", rotated.reshape(-1))
print("len before/after =", np.linalg.norm(x), np.linalg.norm(rotated))
for (m, n) in [(2, 5), (10, 13)]:
    s = sum(np.cos((m - n) * theta))
    print(f"score({m},{n}) = Σcos((m-n)·θ_i) = {s:.6f}")

# ---------------------------------------------------------------- 图 A：完整例子
fig, axs = plt.subplots(1, 4, figsize=(14, 4.2))
for i, ax in enumerate(axs):
    deg = np.degrees(angles[i])
    tip = rotated[i]
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#333333", lw=0.8)
    ax.axvline(0, color="#333333", lw=0.8)
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="#cccccc", ls="--"))
    # 原向量（灰虚线）→ 旋转后（彩色实线）
    ax.annotate("", xy=(pairs[i][0], pairs[i][1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#999999", lw=2, ls="--"))
    ax.annotate("", xy=(tip[0], tip[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=PAIR_COLORS[i], lw=2.5))
    if deg >= 3:    # 角度够大才画弧线，太小的只写数字
        ax.add_patch(Arc((0, 0), 0.9, 0.9, theta1=0, theta2=deg,
                         color=PAIR_COLORS[i], lw=1.5))
    ax.text(tip[0] * 1.28, tip[1] * 1.28,
            f"({tip[0]:.2f}, {tip[1]:.2f})", color=PAIR_COLORS[i],
            fontsize=10.5, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
            zorder=6)
    ax.text(0.5, -0.28, f"转 m·θ{i} = 2×{theta_str[i]}\n= {deg:.1f}°",
            color=PAIR_COLORS[i], fontsize=10, ha="center", va="top",
            transform=ax.transAxes)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_title(f"第 {i} 对 (x{2*i}, x{2*i+1})\nθ{i} = {theta_str[i]} rad/位",
                 fontsize=11.5)
fig.suptitle("真实 RoPE 完整例子：d=8 → 4 对，位置 m=2，x=[1,0,1,0,1,0,1,0]\n"
             "同一个 m，四只指针各转各的角度（灰虚线 = 转之前）",
             fontsize=13.5, y=1.02)
fig.subplots_adjust(top=0.76, wspace=0.3)
save(fig, "w6d5_real_rope_pairs.png")

# ---------------------------------------------------------------- 图 B：块对角矩阵
fig, ax = plt.subplots(figsize=(8.6, 6.4))
ax.imshow(np.ones((D, D, 3)))                # 白底
ax.set_xticks(np.arange(-0.5, D, 1), minor=True)
ax.set_yticks(np.arange(-0.5, D, 1), minor=True)
ax.grid(which="minor", color="#bbbbbb", lw=0.8)
ax.tick_params(which="minor", length=0)
ax.set_xticks(range(D), [f"x{c}" for c in range(D)])
ax.set_yticks(range(D), [f"x{r}" for r in range(D)])
for i in range(D // 2):
    c, s = np.cos(angles[i]), np.sin(angles[i])
    block = np.array([[c, -s], [s, c]])
    for r in range(2):
        for cc in range(2):
            row, col = 2 * i + r, 2 * i + cc
            ax.add_patch(Rectangle((col - 0.5, row - 0.5), 1, 1,
                                   facecolor=PAIR_COLORS[i], alpha=0.22))
            ax.text(col, row, f"{block[r, cc]:.2f}", ha="center", va="center",
                    fontsize=10, color="#222222")
    ax.add_patch(Rectangle((2 * i - 0.5, 2 * i - 0.5), 2, 2, fill=False,
                           edgecolor=PAIR_COLORS[i], lw=2.5))
# 非块对角格子写 0
for r in range(D):
    for cc in range(D):
        if r // 2 != cc // 2:
            ax.text(cc, r, "0", ha="center", va="center",
                    fontsize=8, color="#bbbbbb")
handles = [Patch(facecolor=PAIR_COLORS[i], alpha=0.25, edgecolor=PAIR_COLORS[i],
                 label=f"第 {i} 对：转 m·θ{i} = {np.degrees(angles[i]):.1f}°")
           for i in range(D // 2)]
ax.legend(handles=handles, loc="center left", bbox_to_anchor=(1.03, 0.5),
          fontsize=10.5, frameon=False)
ax.set_title("R(m)：8×8 的真实旋转矩阵 = 4 个 2×2 小旋转沿对角线排开\n"
             "（图示 m=2；空白处全是 0，所以真实代码只存 cos/sin 两张表，不建矩阵）",
             fontsize=12.5)
save(fig, "w6d5_real_rope_matrix.png")

# ---------------------------------------------------------------- 图 C：时钟 + 衰减
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 4.6))

# 左：每只时钟指针的横坐标 cos(m·θ_i) 随位置 m 的波动
ms = np.linspace(0, 60, 2000)
period_txt = ["周期≈6.3 位", "≈63 位", "≈628 位", "≈6283 位"]
label_y = [None, 1.05, 0.66, 1.35]           # 右端标签的固定高度（防重叠）
for i in range(D // 2):
    ax1.plot(ms, np.cos(ms * theta[i]), color=PAIR_COLORS[i], lw=2)
    y = np.cos(60 * theta[i]) if label_y[i] is None else label_y[i]
    ax1.text(61.5, y, f"第{i}对 θ={theta_str[i]}\n{period_txt[i]}",
             color=PAIR_COLORS[i], fontsize=9.5, va="center",
             bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85),
             zorder=6)
ax1.axhline(0, color="#333333", lw=0.8)
ax1.set_xlim(0, 82)
ax1.set_ylim(-1.25, 1.5)
ax1.set_xlabel("位置 m")
ax1.set_ylabel("cos(m·θ_i)")
ax1.set_title("每对是一只转速不同的时钟\n（快针管近处，慢针管远处）", fontsize=12.5)

# 右：q=k=[1,0,...] 时分数 = 各对 cos((m-n)·θ_i) 之和，随相对距离衰减
ds = np.arange(0, 301)
theta64 = BASE ** (-np.arange(0, 64, 2) / 64)        # 真实头维 64 对，曲线更平滑
score64 = np.cos(np.outer(ds, theta64)).sum(axis=1)
score8 = np.cos(np.outer(ds, theta)).sum(axis=1)
ax2.plot(ds, score64 / (64 / 2), color=C_BLUE, lw=2,
         label="d=128（64 对，真实尺度）")
ax2.plot(ds, score8 / (D / 2), color=C_ORANGE, lw=1.5, alpha=0.9,
         label="d=8（本节的 4 对）")
ax2.axhline(0, color="#333333", lw=0.8)
ax2.annotate("距离 0：所有余弦对齐\n分数 = 满分 1.0", xy=(0, 1), xytext=(30, 0.82),
             fontsize=10, color=C_BLUE,
             arrowprops=dict(arrowstyle="->", color=C_BLUE))
ax2.text(150, -0.47, "距离拉大：各频率互相抵消\n→ 总体衰减（远程衰减）",
         fontsize=10, color="#444444", ha="center",
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
         zorder=6)
ax2.set_ylim(-0.62, 1.08)
ax2.set_xlabel("相对距离 |m − n|")
ax2.set_ylabel("q_m·k_n（归一化）")
ax2.set_title("附赠性质：分数总体随相对距离衰减\n（q=k 时分数 = Σ cos((m−n)·θ_i)）",
              fontsize=12.5)
ax2.legend(fontsize=10, loc="upper right")
fig.subplots_adjust(wspace=0.25)
save(fig, "w6d5_real_rope_waves.png")
