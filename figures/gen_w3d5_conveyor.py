"""W3D5 图：传送带规则 —— 数据从哪边进来，就先碰到哪边的矩阵。

上道（竖写）：零件 v 从右边进站，先碰 B 后碰 A —— (A@B)·v = A·(B·v)；
下道（横写）：零件 x 从左边进站，先碰 W1 后碰 W2 —— x·W1·W2 = (x·W1)·W2。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figures._common import C_BLUE, C_GRAY, C_ORANGE, C_RED, save

DARK = "#333333"


def station(ax, x, y, text, color, w=1.5, h=0.72):
    """画一个加工站（圆角盒子 + 文字），返回盒子中心。"""
    box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                         boxstyle="round,pad=0.08",
                         fc="white", ec=color, lw=2, zorder=3)
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center", fontsize=13,
            color=color, zorder=4, weight="bold")


def part(ax, x, y, text, color=C_RED):
    """画传送带上的零件（圆点 + 文字）。"""
    ax.scatter([x], [y], s=260, color=color, zorder=4)
    ax.text(x, y, text, ha="center", va="center", fontsize=12,
            color="white", zorder=5, weight="bold")


def belt(ax, x_from, x_to, y, color=C_GRAY):
    """传送带箭头（指明数据流动方向）。"""
    ax.annotate("", xy=(x_to, y), xytext=(x_from, y),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2.2,
                                shrinkA=0, shrinkB=0, mutation_scale=20))


def step_tag(ax, x, y, text, color):
    ax.text(x, y, text, ha="center", va="center", fontsize=11.5, color=color,
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.9),
            zorder=5)


fig, ax = plt.subplots(figsize=(11.5, 4.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.6)
ax.axis("off")

# ---------- 上道：竖写，数据从右进来 ----------
y1 = 3.3
ax.text(0.15, y1 + 0.75, "竖写：零件从【右】进站", fontsize=13, color=DARK, weight="bold")
belt(ax, 9.6, 0.6, y1)
part(ax, 9.0, y1, "v")
station(ax, 6.4, y1, "变换 B", C_ORANGE)
station(ax, 3.4, y1, "变换 A", C_BLUE)
step_tag(ax, 7.7, y1 + 0.62, "① 先碰到 B", C_ORANGE)
step_tag(ax, 4.9, y1 + 0.62, "② 再碰到 A", C_BLUE)
ax.text(0.75, y1, "$A\\cdot(B\\cdot v)$", ha="left", va="center",
        fontsize=13, color=DARK)
ax.text(5.0, y1 - 0.75, "$(A@B)\\cdot v$：从右往左读，B 先动、A 后动",
        ha="center", fontsize=11.5, color=C_GRAY)

# ---------- 下道：横写，数据从左进来 ----------
y2 = 1.15
ax.text(0.15, y2 + 0.75, "横写：零件从【左】进站", fontsize=13, color=DARK, weight="bold")
belt(ax, 0.6, 9.6, y2)
part(ax, 1.2, y2, "x")
station(ax, 3.6, y2, "变换 $W_1$", C_ORANGE)
station(ax, 6.6, y2, "变换 $W_2$", C_BLUE)
step_tag(ax, 2.35, y2 + 0.62, "① 先碰到 $W_1$", C_ORANGE)
step_tag(ax, 5.1, y2 + 0.62, "② 再碰到 $W_2$", C_BLUE)
ax.text(8.15, y2, "$(x\\cdot W_1)\\cdot W_2$", ha="left", va="center",
        fontsize=13, color=DARK)
ax.text(5.0, y2 - 0.75, "$x\\cdot W_1\\cdot W_2$：从左往右读，作用顺序 = 阅读顺序",
        ha="center", fontsize=11.5, color=C_GRAY)

save(fig, "w3d5_conveyor.png")
