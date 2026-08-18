"""Day 5 配图专用：一头简笔画小猪 + 圆角卡片（matplotlib patches）。

view 三种角度对应"同一头猪的不同照片"：
  "side"  —— 侧面全身照
  "front" —— 正面大头照
  "back"  —— 背影照
"""
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

PINK = "#f7a8b8"
PINK_DARK = "#d16b86"
PINK_LIGHT = "#fcd3dc"


def draw_card(ax, cx, cy, w, h, fc="white", ec="#bbbbbb", zorder=2):
    """画一张圆角卡片（照片 / 矩阵卡片通用），返回 patch。"""
    card = FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                          boxstyle="round,pad=0.08,rounding_size=0.15",
                          fc=fc, ec=ec, lw=1.5, zorder=zorder)
    ax.add_patch(card)
    return card


def draw_pig(ax, cx, cy, s=1.0, view="side", zorder=3):
    """在 (cx, cy) 处画一头尺度为 s 的小猪。"""
    if view == "front":
        _front(ax, cx, cy, s, zorder)
    elif view == "back":
        _back(ax, cx, cy, s, zorder)
    else:
        _side(ax, cx, cy, s, zorder)


def _legs(ax, cx, cy, s, z):
    for dx in (-0.65, -0.25, 0.35, 0.75):
        ax.add_patch(Rectangle((cx + dx * s, cy - 1.05 * s), 0.22 * s, 0.5 * s,
                               fc=PINK, ec=PINK_DARK, lw=1.2, zorder=z))


def _tail(ax, cx, cy, s, z, back=True, turns=3.2, lw=1.6):
    """卷尾巴：一个小螺旋。back=True 画在身体左端，False 画在右端。"""
    t = np.linspace(0, turns * np.pi, 120)
    r = 0.06 * s + 0.028 * s * t
    sgn = -1 if back else 1
    ax.plot(cx + sgn * 1.2 * s + sgn * r * np.cos(t),
            cy + 0.35 * s + r * np.sin(t),
            color=PINK_DARK, lw=lw, zorder=z)


def _side(ax, cx, cy, s, z):
    _legs(ax, cx, cy, s, z)
    # 身体
    ax.add_patch(Ellipse((cx, cy), 2.4 * s, 1.5 * s,
                         fc=PINK, ec=PINK_DARK, lw=1.5, zorder=z))
    # 头
    ax.add_patch(Circle((cx + 1.25 * s, cy + 0.35 * s), 0.62 * s,
                        fc=PINK, ec=PINK_DARK, lw=1.5, zorder=z + 1))
    # 耳朵
    ax.add_patch(Polygon([(cx + 0.95 * s, cy + 0.85 * s),
                          (cx + 1.15 * s, cy + 1.25 * s),
                          (cx + 1.35 * s, cy + 0.9 * s)],
                         fc=PINK, ec=PINK_DARK, lw=1.2, zorder=z + 1))
    # 鼻子
    ax.add_patch(Ellipse((cx + 1.8 * s, cy + 0.25 * s), 0.5 * s, 0.36 * s,
                         fc=PINK_LIGHT, ec=PINK_DARK, lw=1.2, zorder=z + 2))
    for ddy in (-0.07, 0.07):
        ax.scatter([cx + 1.82 * s], [cy + (0.25 + ddy) * s], s=8 * s,
                   color=PINK_DARK, zorder=z + 3)
    # 眼睛
    ax.scatter([cx + 1.35 * s], [cy + 0.55 * s], s=14 * s,
               color="#333333", zorder=z + 3)
    _tail(ax, cx, cy, s, z + 1)


def _front(ax, cx, cy, s, z):
    # 耳朵
    for sgn in (-1, 1):
        ax.add_patch(Polygon([(cx + sgn * 0.35 * s, cy + 0.75 * s),
                              (cx + sgn * 0.62 * s, cy + 1.25 * s),
                              (cx + sgn * 0.85 * s, cy + 0.7 * s)],
                             fc=PINK, ec=PINK_DARK, lw=1.2, zorder=z))
    # 大脸
    ax.add_patch(Circle((cx, cy), 0.95 * s,
                        fc=PINK, ec=PINK_DARK, lw=1.5, zorder=z + 1))
    # 鼻子
    ax.add_patch(Ellipse((cx, cy - 0.15 * s), 0.8 * s, 0.55 * s,
                         fc=PINK_LIGHT, ec=PINK_DARK, lw=1.2, zorder=z + 2))
    for sgn in (-1, 1):
        ax.scatter([cx + sgn * 0.18 * s], [cy - 0.15 * s], s=10 * s,
                   color=PINK_DARK, zorder=z + 3)
        ax.scatter([cx + sgn * 0.42 * s], [cy + 0.35 * s], s=14 * s,
                   color="#333333", zorder=z + 3)


def _back(ax, cx, cy, s, z):
    _legs(ax, cx, cy, s, z)
    # 身体
    ax.add_patch(Ellipse((cx, cy), 2.4 * s, 1.5 * s,
                         fc=PINK, ec=PINK_DARK, lw=1.5, zorder=z))
    # 后脑勺（看不到五官）
    ax.add_patch(Circle((cx - 1.25 * s, cy + 0.3 * s), 0.6 * s,
                        fc=PINK, ec=PINK_DARK, lw=1.5, zorder=z + 1))
    ax.add_patch(Polygon([(cx - 1.5 * s, cy + 0.78 * s),
                          (cx - 1.3 * s, cy + 1.18 * s),
                          (cx - 1.08 * s, cy + 0.82 * s)],
                         fc=PINK, ec=PINK_DARK, lw=1.2, zorder=z + 1))
    # 背影照的主角是尾巴：画大一点
    _tail(ax, cx, cy, s, z + 2, back=False, turns=3.6, lw=2.0)
