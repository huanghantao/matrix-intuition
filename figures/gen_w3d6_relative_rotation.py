"""W3D6 彩蛋图：为什么"旋转关系"只与相对位置 (m-n) 有关？

两对词：位置 (3, 5) 和位置 (100, 102) —— 绝对位置天差地别，相对位置都差 2，
所以夹角都是 2θ（θ=30°）。右边一对各自被转了 8 圈多，但"差"纹丝不动。

排版原则：所有标签避开箭头、坐标轴和圆弧 —— 夹角用楔形内部的小字 "2θ"，
"原始方向"挪到 x 轴下方，大标签统一放在箭头尖之外的空白处。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_ORANGE, C_GRAY, save

THETA = 30.0  # 每个位置转 30°
LABEL_BOX = dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.92)


def arrow(ax, deg, color, lw=2.5, dashed=False):
    t = np.radians(deg)
    ax.annotate("", xy=(np.cos(t), np.sin(t)), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                linestyle="--" if dashed else "-",
                                shrinkA=0, shrinkB=0, mutation_scale=16))


def arc(ax, deg1, deg2, r, color="#333333"):
    """画一段从 deg1 到 deg2 的圆弧，末端带小箭头，表示"转过去"。"""
    ts = np.linspace(np.radians(deg1), np.radians(deg2), 60)
    ax.plot(r * np.cos(ts), r * np.sin(ts), color=color, lw=1.8, zorder=5)
    # 用弧末端的一小段弦当箭头
    t_end, t_pre = ts[-1], ts[-3]
    ax.annotate("", xy=(r * np.cos(t_end), r * np.sin(t_end)),
                xytext=(r * np.cos(t_pre), r * np.sin(t_pre)),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                                shrinkA=0, shrinkB=0, mutation_scale=14))


def draw_panel(ax, pos_b, pos_a, b_label_xy, a_label_xy, bottom_note):
    """画一对词：词 B 在位置 pos_b，词 A 在位置 pos_a（pos_a = pos_b + 2）。

    b_label_xy / a_label_xy：两个词标签的中心坐标（调用方保证放在空白处）。
    """
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="#333333", lw=1)
    ax.axvline(0, color="#333333", lw=1)
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="#dddddd", lw=1.2))

    deg_b = (pos_b * THETA) % 360
    deg_a = (pos_a * THETA) % 360

    # 原始方向（没加位置信息时的样子）；标签放 x 轴下方，避免压线
    arrow(ax, 0, C_GRAY, lw=1.5, dashed=True)
    ax.text(1.15, -0.25, "原始方向", color=C_GRAY, fontsize=9.5,
            ha="center", va="center", zorder=6, bbox=LABEL_BOX)

    # 两个词（位置大了会转很多整圈，标注 ≡ 折回 0~360° 后的实际朝向）
    arrow(ax, deg_b, C_BLUE)
    arrow(ax, deg_a, C_ORANGE)
    fold_b = f"\n{pos_b}θ = {pos_b * THETA:.0f}°" + (f" ≡ {deg_b:.0f}°" if pos_b * THETA >= 360 else "")
    fold_a = f"\n{pos_a}θ = {pos_a * THETA:.0f}°" + (f" ≡ {deg_a:.0f}°" if pos_a * THETA >= 360 else "")
    ax.text(*b_label_xy, f"词 B · 位置 {pos_b}{fold_b}", color=C_BLUE,
            fontsize=9.5, ha="center", va="center", zorder=6, bbox=LABEL_BOX)
    ax.text(*a_label_xy, f"词 A · 位置 {pos_a}{fold_a}", color=C_ORANGE,
            fontsize=9.5, ha="center", va="center", zorder=6, bbox=LABEL_BOX)

    # 夹角弧 + 楔形内部小字（弧和箭头都不压）
    arc(ax, deg_b, deg_a, r=0.55)
    mid = np.radians((deg_b + deg_a) / 2)
    ax.text(0.85 * np.cos(mid), 0.85 * np.sin(mid), "2θ", color="#333333",
            fontsize=11, ha="center", va="center", zorder=6, bbox=LABEL_BOX)

    ax.text(0, -0.6, bottom_note, fontsize=10.5, ha="center", va="top",
            color="#333333",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f5f5f5", ec="#dddddd"))
    ax.set_xlim(-2.35, 2.1)
    ax.set_ylim(-1.35, 2.0)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.8))

draw_panel(ax1, 3, 5,
           b_label_xy=(0, 1.55),
           a_label_xy=(-1.42, 0.82),
           bottom_note="从 B 到 A：反着转 3θ（撤销 B）\n再正着转 5θ（施加 A）→ 净转 2θ")
ax1.set_title("位置 (3, 5)：夹角 = (5−3)θ = 2θ", fontsize=12.5)

draw_panel(ax2, 100, 102,
           b_label_xy=(-1.12, 1.32),
           a_label_xy=(-1.12, -0.28),
           bottom_note="从 B 到 A：反着转 100θ（撤销 B）\n再正着转 102θ（施加 A）→ 净转还是 2θ")
ax2.set_title("位置 (100, 102)：各自转了 8 圈多，\n夹角 = (102−100)θ = 2θ",
              fontsize=12.5)

fig.suptitle("绝对位置天差地别，相对位置相同 → 夹角完全相同\n"
             "两个词的「旋转关系」只认差 (m−n)，不认各自在哪",
             fontsize=14.5, y=1.0)
fig.subplots_adjust(top=0.76, wspace=0.3)
save(fig, "w3d6_relative_rotation.png")
