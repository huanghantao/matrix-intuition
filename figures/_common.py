"""生图脚本公共设施：中文字体、输出目录、画坐标轴/向量的通用函数。

每个 gen_*.py 脚本开头：

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from figures._common import OUT, save, axes, vec, ...

脚本可以独立运行，也可以被 gen_all.py 统一运行。
"""

import pathlib

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "out"

plt.rcParams["font.sans-serif"] = [
    "Arial Unicode MS",
    "PingFang SC",
    "Hiragino Sans GB",
    "STHeiti",
    "Songti SC",
]
plt.rcParams["axes.unicode_minus"] = False

# 统一的配色
C_BLUE = "#1f77b4"
C_ORANGE = "#ff7f0e"
C_GREEN = "#2ca02c"
C_RED = "#d62728"
C_GRAY = "#7f7f7f"
C_PURPLE = "#9467bd"


def save(fig, name: str, dpi: int = 150):
    """保存图片到 figures/out/，并关闭画布。"""
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  saved {path}")


def axes(ax, xlim=(-6, 6), ylim=(-6, 6), grid=True, equal=True):
    """画一幅标准直角坐标系：原点相交的两根箭头轴 + 网格。"""
    ax.axhline(0, color="#333333", lw=1.0)
    ax.axvline(0, color="#333333", lw=1.0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if equal:
        ax.set_aspect("equal", adjustable="box")
    if grid:
        ax.grid(True, color="#dddddd", lw=0.6)
    ax.set_axisbelow(True)


def vec(ax, start, v, color=C_BLUE, lw=2.5, label=None, label_offset=(0.15, 0.15),
        label_at_tip=False, dashed=False):
    """在 ax 上从 start 出发画一支箭头。

    label_at_tip=False（默认）时，标签放在箭头中点偏移处；
    设为 True 时，标签放在箭头尖端之外 —— 多支共起点的箭头用它能避免互相压住。
    标签带白色衬底（bbox），把压在下面的箭杆 / 网格垫掉，避免文字线条糊成一团。
    """
    ax.annotate(
        "",
        xy=(start[0] + v[0], start[1] + v[1]),
        xytext=(start[0], start[1]),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            linestyle="--" if dashed else "-",
            shrinkA=0,
            shrinkB=0,
            mutation_scale=18,
        ),
    )
    if label is not None:
        if label_at_tip:
            # 放在尖端往外一点；每个调用方可以传 label_offset 微调到不重叠为止
            tx = start[0] + v[0] + label_offset[0]
            ty = start[1] + v[1] + label_offset[1]
            ha = "left"
            va = "center"
        else:
            tx = start[0] + v[0] / 2 + label_offset[0]
            ty = start[1] + v[1] / 2 + label_offset[1]
            ha = "center"
            va = "center"
        ax.text(
            tx,
            ty,
            label,
            color=color,
            fontsize=12,
            ha=ha,
            va=va,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
            zorder=6,
        )


def point(ax, p, color=C_RED, label=None, label_offset=(0.2, 0.2), s=40):
    """在 ax 上画一个点，可选标注（标签带白色衬底，避免压在辅助线上）。"""
    ax.scatter([p[0]], [p[1]], color=color, s=s, zorder=5)
    if label is not None:
        ax.text(p[0] + label_offset[0], p[1] + label_offset[1], label,
                color=color, fontsize=12,
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.85),
                zorder=6)


def dashed_line(ax, p, color=C_GRAY):
    """从点 p 到两根坐标轴的虚线辅助线。"""
    ax.plot([p[0], p[0]], [0, p[1]], color=color, lw=1, ls="--", alpha=0.7)
    ax.plot([0, p[0]], [p[1], p[1]], color=color, lw=1, ls="--", alpha=0.7)
