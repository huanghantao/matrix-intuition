"""W5D2 图：余弦相似度只看方向、不看长短。

左图：三根箭头方向完全相同、长度悬殊（1 / 2 / 4），两两 cosθ 都是 1。
右图：把向量归一化（压成长度 1）到单位圆上，差别只剩方向，
      0° / 45° / 90° / 180° 对应 cos = 1 / 0.71 / 0 / −1。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GRAY, C_GREEN, C_ORANGE, C_RED, axes, save, vec

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

# ---------- 左图：方向相同，长度悬殊，cosθ 全是 1 ----------
axes(ax1, xlim=(-0.8, 5.2), ylim=(-1.6, 1.6))

# 长的先画、短的后画，避免短的箭杆被完全盖住
vec(ax1, (0, 0), (4, 0), color=C_ORANGE, label="(4,0)",
    label_at_tip=True, label_offset=(0.1, 0.3))
vec(ax1, (0, 0), (2, 0), color=C_GREEN, lw=3.0, label="(2,0)",
    label_at_tip=True, label_offset=(-0.25, 0.45))
vec(ax1, (0, 0), (1, 0), color=C_BLUE, lw=3.5, label="(1,0)",
    label_at_tip=True, label_offset=(-0.35, 0.6))

ax1.text(2.0, -0.95,
         "方向完全相同\n长度差到 4 倍\n两两 cosθ 仍都是 1",
         color="#333333", fontsize=12, ha="center", va="center",
         bbox=dict(boxstyle="round,pad=0.35", fc="#fff7e6", ec=C_ORANGE, lw=1.2),
         zorder=6)
ax1.set_title("方向相同、长度悬殊：cosθ 不变", fontsize=13)

# ---------- 右图：归一化到单位圆，差别只剩方向 ----------
axes(ax2, xlim=(-2.2, 2.2), ylim=(-2.2, 2.2))

t = np.linspace(0, 2 * np.pi, 240)
ax2.plot(np.cos(t), np.sin(t), color=C_GRAY, lw=1.2, ls="--", alpha=0.8)

vec(ax2, (0, 0), (1, 0), color=C_BLUE, label="0°：cos = 1（基准）",
    label_at_tip=True, label_offset=(0.12, -0.4))
vec(ax2, (0, 0), (np.cos(np.pi / 4), np.sin(np.pi / 4)), color=C_GREEN,
    label="45°：cos ≈ 0.71", label_at_tip=True, label_offset=(0.12, 0.12))
vec(ax2, (0, 0), (0, 1), color=C_ORANGE, label="90°：cos = 0",
    label_at_tip=True, label_offset=(0.12, 0.05))
vec(ax2, (0, 0), (-1, 0), color=C_RED, label="180°：cos = −1",
    label_at_tip=True, label_offset=(0.15, 0.35))

ax2.text(0, -1.85, "u/|u|：长度压成 1，只留方向（归一化）",
         color="#333333", fontsize=11.5, ha="center",
         bbox=dict(boxstyle="round,pad=0.3", fc="#eef4ff", ec=C_BLUE, lw=1.2),
         zorder=6)
ax2.set_title("归一化：都压成长度 1，只剩方向差别", fontsize=13)

fig.suptitle("余弦相似度：只看方向，不看长短", fontsize=14)
save(fig, "w5d2_cosine_normalize.png")
