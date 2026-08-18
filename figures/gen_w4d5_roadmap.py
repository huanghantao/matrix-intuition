"""W4D5 图 2：A = P⁻¹BP 的路线图 —— 老路（P→B→P⁻¹）绕一圈 = 新路（A）一步直达。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, save

fig, ax = plt.subplots(figsize=(11, 7.5))
ax.set_xlim(0, 12.6)
ax.set_ylim(0, 9)
ax.axis("off")

# 两个世界的底色
ax.add_patch(Rectangle((0.15, 0.3), 5.9, 7.6, fc="#f0faf0", ec="none", zorder=0))
ax.add_patch(Rectangle((6.35, 0.3), 6.1, 7.6, fc="#eef4ff", ec="none", zorder=0))
ax.text(3.1, 8.2, "新尺子世界（P 尺子）", ha="center", fontsize=12.5,
        color=C_GREEN, weight="bold")
ax.text(9.4, 8.2, "标准世界", ha="center", fontsize=12.5, color=C_BLUE, weight="bold")


def node(cx, cy, text, color):
    ax.add_patch(FancyBboxPatch((cx - 2.0, cy - 0.85), 4.0, 1.7,
                                boxstyle="round,pad=0.1,rounding_size=0.18",
                                fc="white", ec=color, lw=2, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=12,
            color=color, zorder=4, weight="bold")


N1 = (3.1, 6.5)   # u：新尺子读数
N2 = (9.4, 6.5)   # Pu：标准读数
N3 = (9.4, 1.9)   # B(Pu)：干完活
N4 = (3.1, 1.9)   # P⁻¹B(Pu)：翻译回新尺子
node(*N1, "新尺子读数\nu = (1, 1)", C_GREEN)
node(*N2, "翻译成标准读数\nPu = (2, 1)", C_BLUE)
node(*N3, "标准世界里干完活\nB(Pu) = (-1, 2)", C_BLUE)
node(*N4, "翻译回新尺子读数\nP⁻¹B(Pu) = (-0.5, 2)", C_GREEN)


def arrow(p, q, label, color, lx=0.0, ly=0.0, lw=2.2, fs=11.5):
    ax.annotate("", xy=q, xytext=p,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=32, shrinkB=32, mutation_scale=20),
                zorder=2)
    mx, my = (p[0] + q[0]) / 2 + lx, (p[1] + q[1]) / 2 + ly
    ax.text(mx, my, label, ha="center", va="center", fontsize=fs,
            color=color, weight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.92),
            zorder=5)


arrow(N1, N2, "① 乘 P\n翻译成标准读数", C_GRAY, ly=0.85)
arrow(N2, N3, "② 乘 B\n干活：旋转 90°", C_GRAY, lx=2.15)
arrow(N3, N4, "③ 乘 P⁻¹\n翻译回新尺子", C_GRAY, ly=-0.95)
arrow(N1, N4, "照片 A = P⁻¹BP\n一步直达", C_RED, lx=-2.35, lw=3.2)

ax.text(6.25, 4.2, "老路 ①②③ 绕一圈  =  新路（A）一步直达\n对任意 u 都成立 —— 这就是 A = P⁻¹BP 的全部含义",
        ha="center", va="center", fontsize=12.5, color="#333333",
        bbox=dict(boxstyle="round,pad=0.4", fc="#fffbe8", ec="#e0d090", lw=1.2))

fig.suptitle("5.2 · 路线图：先翻译成标准读数 → 干活 → 再翻译回新尺子", fontsize=15)
fig.subplots_adjust(top=0.9, bottom=0.03, left=0.02, right=0.98)
save(fig, "w4d5_roadmap.png")
