"""W6D2 图：weights · V 按行切 —— "吃"的新向量是怎么配出来的。

左图（矩阵网格）：weights 的第 2 行（"吃"的注意力配方 [0.8, 0.1, 0.1]）
   调配 V 的三行（苹果/我/爱），配出 out 的第 2 行 (1.5, 1.6)。
右图（几何）：三个 V 向量与它们围成的三角形；凸组合 out 落在三角形内部 ——
   "调配"的输出永远待在原料的包围圈里。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_ORANGE, C_RED, axes, point, save, vec

# ---- 数据 ----
W_ROW = [0.8, 0.1, 0.1]                       # "吃"的注意力配方（给 苹果/我/爱）
V = {"苹果": (2.0, 2.0), "我": (-1.0, 1.0), "爱": (0.0, -1.0)}
OUT = (0.8 * 2.0 + 0.1 * (-1.0) + 0.1 * 0.0,
       0.8 * 2.0 + 0.1 * 1.0 + 0.1 * (-1.0))   # = (1.5, 1.6)

CELL = 0.62
DARK = "#333333"
ROW_COLORS = {"苹果": C_BLUE, "我": C_GREEN, "爱": C_ORANGE}
LIGHT = {C_BLUE: "#dbeaf7", C_GREEN: "#dff0d8", C_ORANGE: "#fdebd7"}

fig = plt.figure(figsize=(12.5, 5.2))
axL = fig.add_subplot(1, 2, 1)
axR = fig.add_subplot(1, 2, 2)

# ================= 左图：矩阵网格 =================
axL.set_xlim(-1.7, 7.7)
axL.set_ylim(-3.9, 1.3)
axL.set_aspect("equal")
axL.axis("off")
axL.set_title("矩阵视角：按行切，一次配出一整行", fontsize=13, color=DARK, pad=12)

WEIGHTS = [[0.2, 0.6, 0.2], W_ROW, [0.5, 0.2, 0.3]]   # 行：我/吃/苹果；列：苹果/我/爱
ROW_NAMES = ["我", "吃", "苹果"]
COL_NAMES = ["苹果", "我", "爱"]
VMAT = [V["苹果"], V["我"], V["爱"]]


def draw_matrix(ax, Mat, x0, y0, highlights=None, fmt=None):
    highlights = highlights or {}
    n, m = len(Mat), len(Mat[0])
    for i in range(n):
        for j in range(m):
            x, y = x0 + j * CELL, y0 - i * CELL
            fc = highlights.get((i, j), "white")
            ax.add_patch(plt.Rectangle((x, y - CELL), CELL, CELL,
                                       fc=fc, ec=DARK, lw=1.1, zorder=2))
            v = Mat[i][j]
            if isinstance(v, str):
                txt = v
            elif fmt:
                txt = fmt(v)
            else:
                txt = str(v) if v >= 0 else f"$-${abs(v)}"
            ax.text(x + CELL / 2, y - CELL / 2, txt,
                    ha="center", va="center", fontsize=11, color=DARK, zorder=3)


# weights 矩阵（行 1 = "吃" 高亮）
hi = {(1, j): "#fff3d6" for j in range(3)}
draw_matrix(axL, WEIGHTS, 0.0, 0.0, highlights=hi)
for i, name in enumerate(ROW_NAMES):
    axL.text(-0.15, -i * CELL - CELL / 2, name, ha="right", va="center",
             fontsize=12, color=C_RED if i == 1 else C_GRAY)
for j, name in enumerate(COL_NAMES):
    axL.text(j * CELL + CELL / 2, 0.22, name, ha="center", va="bottom",
             fontsize=12, color=ROW_COLORS[name])
axL.text(0.93, -2.3, "每行一份配方", ha="center", fontsize=10.5, color=C_GRAY)

axL.text(2.35, -0.93, "·", ha="center", va="center", fontsize=16, color=DARK)

# V 矩阵（三行分别涂三色，左侧标权重倍率）
hi = {}
for i, name in enumerate(["苹果", "我", "爱"]):
    hi[(i, 0)] = LIGHT[ROW_COLORS[name]]
    hi[(i, 1)] = LIGHT[ROW_COLORS[name]]
draw_matrix(axL, VMAT, 2.85, 0.0, highlights=hi)
for i, name in enumerate(["苹果", "我", "爱"]):
    axL.text(4.22, -i * CELL - CELL / 2, f"V（{name}）", ha="left", va="center",
             fontsize=12, color=ROW_COLORS[name])
for i, w in enumerate(W_ROW):
    axL.text(2.72, -i * CELL - CELL / 2, f"×{w}", ha="right", va="center",
             fontsize=11, color=ROW_COLORS[["苹果", "我", "爱"][i]])
axL.text(3.47, -2.3, "每行一份干货", ha="center", fontsize=10.5, color=C_GRAY)

axL.text(5.85, -0.93, "=", ha="center", va="center", fontsize=16, color=DARK)

# out 矩阵：只填"吃"那一行
OUTMAT = [["?", "?"], [round(OUT[0], 1), round(OUT[1], 1)], ["?", "?"]]
draw_matrix(axL, OUTMAT, 6.25, 0.0, highlights={(1, 0): "#fff3d6", (1, 1): "#fff3d6"})
axL.text(6.87, -2.3, "吃的新向量", ha="center", fontsize=10.5, color=C_GRAY)

axL.text(3.0, -3.2,
         "out[吃] = 0.8·V（苹果）+ 0.1·V（我）+ 0.1·V（爱）= (1.5, 1.6)",
         ha="center", fontsize=12, color=DARK,
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))

# ================= 右图：几何视角（凸组合落在包围圈内） =================
axes(axR, xlim=(-1.8, 2.8), ylim=(-1.8, 2.8))
axR.set_title("几何视角：输出落在原料围成的「包围圈」里", fontsize=13, color=DARK, pad=12)

# 三角形包围圈
tri = plt.Polygon([V["苹果"], V["我"], V["爱"]], closed=True,
                  fc="#f0f0f0", ec="#bbbbbb", lw=1.2, ls="--", zorder=1)
axR.add_patch(tri)

for name, vpos in V.items():
    vec(axR, (0, 0), vpos, color=ROW_COLORS[name],
        label=f"V（{name}）{vpos}", label_at_tip=True,
        label_offset=(0.12, 0.12 if name != "爱" else -0.28))

# 合成结果
vec(axR, (0, 0), OUT, color=C_RED, lw=3,
    label=f"out[吃] = {OUT}", label_at_tip=True, label_offset=(-2.15, 0.25))
point(axR, OUT, color=C_RED, s=55)

axR.text(0.4, -1.55, "权重和为 1（凸组合）→ 输出跑不出这个三角形",
         ha="center", fontsize=10.5, color=C_GRAY)

save(fig, "w6d2_weightsV_rows.png")
