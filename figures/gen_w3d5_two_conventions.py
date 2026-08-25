"""W3D5 图：同一个向量、同一个变换，竖写与横写并排对照。

(2,1) 旋转 90°：
- 左图（竖写）：M·v，M 的列 = e1/e2 的新家，结果是列向量 (-1,2)；
- 右图（横写）：x·W，W = M 的转置（翻面），W 的行 = e1/e2 的新家，结果是行向量 (-1,2)。
逐分量算式完全一致 —— 乘的、加的同一批数。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_RED, save

M = [[0, -1], [1, 0]]      # 旋转 90°（竖写版）
W = [[0, 1], [-1, 0]]      # M 的转置（横写版）

CELL = 0.62
DARK = "#333333"
LIGHT_BLUE = "#dbeaf7"
LIGHT_GREEN = "#dff0d8"


def draw_matrix(ax, Mat, x0, y0, highlights=None):
    """以 (x0, y0) 为左上角画数值矩阵。highlights: {(i,j): facecolor}。"""
    highlights = highlights or {}
    n, m = len(Mat), len(Mat[0])
    for i in range(n):
        for j in range(m):
            x, y = x0 + j * CELL, y0 - i * CELL
            fc = highlights.get((i, j), "white")
            ax.add_patch(plt.Rectangle((x, y - CELL), CELL, CELL,
                                       fc=fc, ec=DARK, lw=1.2, zorder=2))
            v = Mat[i][j]
            ax.text(x + CELL / 2, y - CELL / 2,
                    str(v) if v >= 0 else f"$-${abs(v)}",
                    ha="center", va="center", fontsize=13, color=DARK, zorder=3)


def op(ax, s, x, y):
    ax.text(x, y, s, ha="center", va="center", fontsize=16, color=DARK)


fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.5, 5.2))
for ax in (axL, axR):
    ax.set_xlim(-0.7, 6.3)
    ax.set_ylim(-4.0, 1.1)
    ax.set_aspect("equal")
    ax.axis("off")

YMID = -0.62

# ---------- 左图：竖写 M·v ----------
axL.set_title("竖着写（本周约定）：$M\\cdot v$，矩阵在左", fontsize=13, color=DARK, pad=12)
draw_matrix(axL, M, 0.0, 0.0, highlights={(0, 0): LIGHT_BLUE, (1, 0): LIGHT_BLUE,
                                          (0, 1): LIGHT_GREEN, (1, 1): LIGHT_GREEN})
op(axL, "·", 1.5, YMID)
draw_matrix(axL, [[2], [1]], 1.9, 0.0)          # 列向量 v
op(axL, "=", 2.85, YMID)
draw_matrix(axL, [[-1], [2]], 3.25, 0.0)        # 结果列向量
axL.text(0.31, 0.35, "第1列", ha="center", fontsize=11, color=C_BLUE)
axL.text(0.93, 0.35, "第2列", ha="center", fontsize=11, color=C_GREEN)
axL.text(2.21, 0.35, "$v$", ha="center", fontsize=12, color=DARK)
axL.text(3.56, 0.35, "结果", ha="center", fontsize=11, color=C_RED)
axL.text(1.9, -1.6, "蓝列 = $e_1$ 的新家，绿列 = $e_2$ 的新家",
         ha="center", fontsize=10.5, color=C_GRAY)
axL.text(2.1, -2.6,
         "第一分量：$0\\cdot2+(-1)\\cdot1=-1$\n第二分量：$1\\cdot2+0\\cdot1=2$",
         ha="center", fontsize=11.5, color=DARK,
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))
axL.text(2.1, -3.55, "结果 $(-1,\\ 2)$，竖着", ha="center", fontsize=11, color=C_RED)

# ---------- 右图：横写 x·W ----------
axR.set_title("横着写（AI 约定）：$x\\cdot W$，矩阵翻面到右边", fontsize=13, color=DARK, pad=12)
draw_matrix(axR, [[2, 1]], 0.0, 0.0)            # 行向量 x
op(axR, "·", 1.5, YMID)
draw_matrix(axR, W, 1.9, 0.0, highlights={(0, 0): LIGHT_BLUE, (0, 1): LIGHT_BLUE,
                                          (1, 0): LIGHT_GREEN, (1, 1): LIGHT_GREEN})
op(axR, "=", 3.5, YMID)
draw_matrix(axR, [[-1, 2]], 3.9, 0.0)           # 结果行向量
axR.text(0.62, 0.35, "$x$", ha="center", fontsize=12, color=DARK)
axR.text(4.52, 0.35, "结果", ha="center", fontsize=11, color=C_RED)
axR.text(2.6, -1.6, "蓝行 = $e_1$ 的新家，绿行 = $e_2$ 的新家（同一组尺子）",
         ha="center", fontsize=10.5, color=C_GRAY)
axR.text(2.6, -2.6,
         "第一分量：$2\\cdot0+1\\cdot(-1)=-1$\n第二分量：$2\\cdot1+1\\cdot0=2$",
         ha="center", fontsize=11.5, color=DARK,
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))
axR.text(2.6, -3.55, "结果 $(-1,\\ 2)$，横着", ha="center", fontsize=11, color=C_RED)

save(fig, "w3d5_two_conventions.png")
