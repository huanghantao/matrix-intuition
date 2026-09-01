"""W7D3 图（二维版·双联）：同一件事的两个空间。

左：数据平面（横轴 x、纵轴 y）——逐点残差是竖直小线段（3.2 的图）。
右：成绩单空间（每根轴管一个点的分数）——同样的残差打包成一支箭头：
   每个坐标 = 一个点的残差，箭头长度的平方 = RSS = 两张成绩单距离的平方。

迷你例子：过原点直线 y = a·x 拟合两个点 (1,1)、(2,1)。
候选成绩单 (a, 2a) 排成一条过原点、斜率 2 的直线（= 列空间，A 只有一列 (1,2)）；
最优 a = 0.6 → ŷ = (0.6, 1.2)，残差向量 y − ŷ = (0.4, −0.2) 与直线垂直。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GREEN, C_GRAY, C_ORANGE, C_RED, save

col = np.array([1.0, 2.0])            # A 的唯一一列（两个点的 x）
y = np.array([1.0, 1.0])              # 真实成绩单
a_hat = float(col @ y / (col @ col))  # 最小二乘解 = 0.6
y_hat = a_hat * col                   # 最优成绩单 ŷ = (0.6, 1.2)
res = y - y_hat                       # (0.4, -0.2)，与列垂直
y_bad = 1.0 * col                     # 落选者 a=1 → (1, 2)

G_DARK = "#1e7b1e"
O_DARK = "#b35a00"
WHITE = dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88)


def note(ax, x, yy, s, color, ha="left", fs=11):
    ax.text(x, yy, s, color=color, fontsize=fs, ha=ha, va="center",
            bbox=WHITE, zorder=7)


def check_overlaps(fig, tag):
    """目检替身：把所有文本的两两包围盒算一遍，报告重叠（附数据坐标，便于调整）。"""
    fig.canvas.draw()
    ren = fig.canvas.get_renderer()
    items = []
    for ax in fig.axes:
        inv = ax.transData.inverted()
        for t in ax.texts:
            s = t.get_text().strip()
            if not s:
                continue
            try:
                bb = t.get_window_extent(renderer=ren)
                (x0, y0), (x1, y1) = inv.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
                items.append((id(ax), s.splitlines()[0][:16], (x0, y0, x1, y1), bb))
            except Exception:
                pass
    fx = fig.transFigure.inverted()
    for t in fig.texts:
        s = t.get_text().strip()
        if not s:
            continue
        try:
            bb = t.get_window_extent(renderer=ren)
            (x0, y0), (x1, y1) = fx.transform([(bb.x0, bb.y0), (bb.x1, bb.y1)])
            items.append(("fig", s.splitlines()[0][:16], (round(x0, 3), round(y0, 3),
                                                          round(x1, 3), round(y1, 3)), bb))
        except Exception:
            pass
    bad = [(items[i][1], items[j][1])
           for i in range(len(items)) for j in range(i + 1, len(items))
           if items[i][0] == items[j][0] and items[i][3].overlaps(items[j][3])]
    for axid, label, box, _ in items:
        print(f"    [{axid}] {label!r} bbox={tuple(round(v, 2) for v in box)}")
    if bad:
        print(f"  [warn] {tag} 文本重叠: {bad}")
    else:
        print(f"  [ok] {tag} 文本无重叠（{len(items)} 条）")


fig, (axL, axR) = plt.subplots(1, 2, figsize=(14.2, 6.4))
fig.subplots_adjust(left=0.05, right=0.98, top=0.84, bottom=0.10, wspace=0.22)
fig.suptitle("最小二乘的几何本质：在“成绩单空间”里找离真实成绩单最近的预测", fontsize=15)

# 中央的“打包”提示（画在两栏之间的缝隙里）
fig.text(0.5, 0.56, "同样的残差\n打包成一支箭头", ha="center", va="center",
         fontsize=11.5, color="#555555", bbox=WHITE, zorder=8)
from matplotlib.patches import FancyArrowPatch
fig.add_artist(FancyArrowPatch((0.455, 0.47), (0.545, 0.47),
                               transform=fig.transFigure, arrowstyle="-|>",
                               mutation_scale=16, color="#888888", lw=2))

# ================= 左：数据平面 =================
axL.set_title("左：数据平面（横轴 x，纵轴 y）\n逐点残差 = 红色竖线段", fontsize=12.5)
axL.axhline(0, color="#333333", lw=0.8)
axL.axvline(0, color="#333333", lw=0.8)
axL.set_xlim(-0.15, 2.95)
axL.set_ylim(-0.15, 1.85)
axL.set_aspect("equal", adjustable="box")
axL.grid(True, color="#dddddd", lw=0.6)
axL.set_axisbelow(True)
axL.set_xlabel("x")
axL.set_ylabel("y（分数）")

t = np.array([-0.05, 2.5])
axL.plot(t, a_hat * t, color=C_GREEN, lw=2.6, zorder=2)          # 最优直线
pts = [(1.0, 1.0), (2.0, 1.0)]
axL.scatter([p[0] for p in pts], [p[1] for p in pts], color=C_BLUE, s=80, zorder=5)
for xi, yi in pts:                                               # 残差竖线段
    yh = a_hat * xi
    axL.plot([xi, xi], [yi, yh], color=C_RED, lw=3.4, zorder=4,
             solid_capstyle="round")

note(axL, 2.15, 1.64, "最优直线 y = 0.6x", G_DARK, ha="center", fs=11)
note(axL, 1.02, 1.16, "点 1 (1, 1)", C_BLUE, ha="center", fs=11)
note(axL, 1.78, 0.80, "点 2 (2, 1)", C_BLUE, ha="center", fs=11)
note(axL, 0.90, 0.66, "残差1 = 0.4\n（预测 0.6，实际 1）", C_RED, ha="right", fs=10.5)
note(axL, 2.08, 1.00, "残差2 = 0.2\n（预测 1.2，实际 1）", C_RED, ha="left", fs=10.5)
note(axL, 0.06, 1.62, "残差 = 预测 − 实际\n（正负号无所谓，平方后一样）",
     "#444444", fs=10.5)

# ================= 右：成绩单空间 =================
axR.set_title("右：成绩单空间（每根轴管一个点的分数）\n同样的残差 = 一支箭头的两个坐标",
              fontsize=12.5)
axR.axhline(0, color="#333333", lw=0.8)
axR.axvline(0, color="#333333", lw=0.8)
axR.set_xlim(-0.32, 1.82)
axR.set_ylim(-0.32, 2.5)
axR.set_aspect("equal", adjustable="box")
axR.grid(True, color="#dddddd", lw=0.6)
axR.set_axisbelow(True)
axR.set_xlabel("点 1 的分数")
axR.set_ylabel("点 2 的分数")

tt = np.array([-0.1, 1.1])
axR.plot(tt * col[0], tt * col[1], color=C_ORANGE, lw=6, alpha=0.32,
         solid_capstyle="round", zorder=1)                       # 候选成绩单直线（列空间）

# ŷ 的坐标虚线（把成绩单的两个值读出来）
axR.plot([0, y_hat[0]], [y_hat[1], y_hat[1]], color=C_GRAY, lw=1, ls="--", alpha=0.7)
axR.plot([y_hat[0], y_hat[0]], [0, y_hat[1]], color=C_GRAY, lw=1, ls="--", alpha=0.7)

# 残差的“阶梯分解”：横向 0.4 + 纵向 −0.2
axR.plot([y_hat[0], y[0]], [y_hat[1], y_hat[1]], color=C_RED, lw=1.8, ls="--", zorder=3)
axR.plot([y[0], y[0]], [y_hat[1], y[1]], color=C_RED, lw=1.8, ls="--", zorder=3)
axR.text(0.8, 1.27, "0.4", color=C_RED, fontsize=10, ha="center", va="bottom", zorder=7)
axR.text(1.05, 1.1, "0.2", color=C_RED, fontsize=10, ha="left", va="center", zorder=7)

# 直角标记：残差 ⊥ 候选线
d = col / np.linalg.norm(col)
n = res / np.linalg.norm(res)
m = 0.09
corner = [y_hat + m * d, y_hat + m * d + m * n, y_hat + m * n]
axR.plot([p[0] for p in corner], [p[1] for p in corner], color=C_GRAY, lw=1.4, zorder=3)

# 两个成绩单画成点（一张成绩单 = 空间里的一个点），残差画成箭头
axR.scatter(*y_hat, color=C_GREEN, s=70, zorder=6)
axR.scatter(*y, color=C_BLUE, s=70, zorder=6)
axR.scatter(*y_bad, color=C_GRAY, s=55, zorder=6)
axR.plot([y_bad[0], y[0]], [y_bad[1], y[1]], color=C_GRAY, lw=1.6, ls="--", zorder=2)
axR.annotate("", xy=tuple(y), xytext=tuple(y_hat),
             arrowprops=dict(arrowstyle="-|>", color=C_RED, lw=3,
                             shrinkA=0, shrinkB=0, mutation_scale=18))

note(axR, 0.64, 0.38, "RSS = 0.4² + 0.2² = 0.20\n　　 = ‖y − ŷ‖² = 距离的平方",
     "#333333", fs=11)
note(axR, 0.62, 0.62, "ŷ = 最优成绩单 (0.6, 1.2)", G_DARK, fs=11)
note(axR, 1.03, 0.88, "y = 真实成绩单 (1, 1)", C_BLUE, fs=10.5)
note(axR, 0.62, 0.76, "残差向量 y − ŷ = (0.4, −0.2)", C_RED, fs=11)
note(axR, 0.03, 2.32, "候选成绩单：(a, 2a)\n= 列空间（A 的列的所有倍数）",
     O_DARK, fs=11)
note(axR, 1.13, 1.62, "落选者 a=1：\n(1, 2)，距离²=1", C_GRAY, fs=10.5)

check_overlaps(fig, "w7d3_projection_2d")
save(fig, "w7d3_projection_2d.png")
