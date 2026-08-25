"""W3D3 图：矩阵乘法的两把刀 —— 按列切 vs 按行切。

用 W3D4 手算过的同一组数字：A=[[1,2],[3,4]]，B=[[5,6],[7,8]]，C=A@B=[[19,22],[43,50]]。
左图：按列切（正文那把刀）—— C 的第 1 列 = A 作用在 B 的第 1 列上。
右图：按行切（新增那把刀）—— C 的第 1 行 = A 的第 1 行配 B 的各行：1·(5,6) + 2·(7,8)。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import C_BLUE, C_GRAY, C_ORANGE, save

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[19, 22], [43, 50]]

CELL = 0.62          # 格子边长
GAP_OP = 0.85        # 矩阵与运算符之间的水平间隔
LIGHT_BLUE = "#dbeaf7"
LIGHT_ORANGE = "#fdebd7"
DARK = "#333333"


def draw_matrix(ax, M, x0, y0, highlights=None, row_labels=None):
    """在 (x0, y0) 为左上角的位置画一个数值矩阵（二维网格 + 居中数字）。

    highlights: dict {(i, j): facecolor}，要涂色的格子。
    row_labels: dict {i: text}，画在行左侧的小字（如权重 ×1、×2）。
    """
    highlights = highlights or {}
    n, m = len(M), len(M[0])
    for i in range(n):
        for j in range(m):
            x, y = x0 + j * CELL, y0 - i * CELL
            fc = highlights.get((i, j), "white")
            rect = plt.Rectangle((x, y - CELL), CELL, CELL,
                                 fc=fc, ec=DARK, lw=1.2, zorder=2)
            ax.add_patch(rect)
            ax.text(x + CELL / 2, y - CELL / 2, str(M[i][j]),
                    ha="center", va="center", fontsize=13, color=DARK, zorder=3)
    if row_labels:
        for i, text in row_labels.items():
            ax.text(x0 - 0.07, y0 - i * CELL - CELL / 2, text,
                    ha="right", va="center", fontsize=12, color=C_ORANGE)


def op_symbol(ax, s, x, y_mid, color=DARK):
    ax.text(x, y_mid, s, ha="center", va="center", fontsize=16, color=color)


fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.5, 4.6))
for ax in (axL, axR):
    ax.set_xlim(-0.6, 6.4)
    ax.set_ylim(-3.25, 0.7)
    ax.set_aspect("equal")
    ax.axis("off")

YMID = -0.62  # 矩阵竖直中线（两行矩阵：顶 0，底 -1.24）

# ---------- 左图：按列切 ----------
axL.set_title("刀法一：按列切（§3.2 那把刀）", fontsize=13, color=DARK, pad=14)
draw_matrix(axL, A, 0.0, 0.0)
op_symbol(axL, "@", 1.55, YMID)
draw_matrix(axL, B, 2.1, 0.0, highlights={(0, 0): LIGHT_BLUE, (1, 0): LIGHT_BLUE})
op_symbol(axL, "=", 3.65, YMID)
draw_matrix(axL, C, 4.2, 0.0, highlights={(0, 0): LIGHT_BLUE, (1, 0): LIGHT_BLUE})
axL.text(2.41, -1.5, "B 的第 1 列", ha="center", fontsize=11, color=C_BLUE)
axL.text(4.51, -1.5, "C 的第 1 列", ha="center", fontsize=11, color=C_BLUE)
axL.text(2.9, -2.32,
         "C 的第 1 列 = $A\\cdot$(B 的第 1 列)\n"
         "= $A\\cdot(5,7)$ = (19, 43)",
         ha="center", fontsize=11.5, color=DARK,
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))
axL.text(2.9, -3.0, "一次 matvec 搬一列，逐列搬完",
         ha="center", fontsize=10.5, color=C_GRAY)

# ---------- 右图：按行切 ----------
axR.set_title("刀法二：按行切（本节新刀）", fontsize=13, color=DARK, pad=14)
draw_matrix(axR, A, 0.0, 0.0, highlights={(0, 0): LIGHT_ORANGE, (0, 1): LIGHT_ORANGE})
op_symbol(axR, "@", 1.55, YMID)
draw_matrix(axR, B, 2.1, 0.0,
            highlights={(0, 0): LIGHT_ORANGE, (0, 1): LIGHT_ORANGE,
                        (1, 0): LIGHT_ORANGE, (1, 1): LIGHT_ORANGE},
            row_labels={0: "×1", 1: "×2"})
op_symbol(axR, "=", 3.65, YMID)
draw_matrix(axR, C, 4.2, 0.0, highlights={(0, 0): LIGHT_ORANGE, (0, 1): LIGHT_ORANGE})
axR.text(0.31, -1.5, "A 的第 1 行", ha="center", fontsize=11, color=C_ORANGE)
axR.text(2.72, -1.5, "B 的各行都被用到", ha="center", fontsize=11, color=C_ORANGE)
axR.text(4.51, -1.62, "C 的第 1 行", ha="center", fontsize=11, color=C_ORANGE)
axR.text(2.9, -2.32,
         "C 的第 1 行 = 1·(B 的第 1 行) + 2·(B 的第 2 行)\n"
         "= 1·(5,6) + 2·(7,8) = (19, 22)",
         ha="center", fontsize=11.5, color=DARK,
         bbox=dict(boxstyle="round,pad=0.35", fc="#f5f5f5", ec="#cccccc"))
axR.text(2.9, -3.0, "左行是配方，右矩阵的行是原料，一次配出一整行",
         ha="center", fontsize=10.5, color=C_GRAY)

save(fig, "w3d3_row_slice.png")
