"""W4D5 图 5：常见错觉 —— "把新轴直接旋转拼成列"得到的是 BP，不是照片 A。

新尺子 P = [[2,0],[0,1]] 的两根轴 (2,0)、(0,1) 旋转 90° 后落在 (0,2)、(-1,0)。
左：落点用标准尺子读 → 拼出 BP = [[0,-1],[2,0]]（det=2，混进了拉伸，不是照片）。
右：同一对落点翻译回新尺子读（x 刻度=标准的 2 倍）→ A = [[0,-0.5],[2,0]]（det=1，真照片）。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib.pyplot as plt

from figures._common import (C_GRAY, C_GREEN, C_ORANGE, C_PURPLE, C_RED,
                             axes, save, vec)

arc1 = np.linspace(0, np.pi / 2, 60)          # (2,0) → (0,2)，半径 2
arc2 = np.linspace(np.pi / 2, np.pi, 60)      # (0,1) → (-1,0)，半径 1

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.8))

for ax in (ax1, ax2):
    axes(ax, xlim=(-3.4, 3.4), ylim=(-2.2, 3.4))
    # 新尺子的两根轴
    vec(ax, (0, 0), (2, 0), color=C_GREEN, label="新 x 轴 (2,0)",
        label_at_tip=True, label_offset=(0.15, -0.35))
    vec(ax, (0, 0), (0, 1), color=C_PURPLE, label="新 y 轴 (0,1)",
        label_at_tip=True, label_offset=(0.25, 0.05))
    # 旋转 90° 的弧线提示
    ax.plot(2 * np.cos(arc1), 2 * np.sin(arc1), color=C_GRAY, lw=1.2, ls="--")
    ax.plot(np.cos(arc2), np.sin(arc2), color=C_GRAY, lw=1.2, ls="--")
    # 落点
    vec(ax, (0, 0), (0, 2), color=C_RED, lw=2.5)
    vec(ax, (0, 0), (-1, 0), color=C_ORANGE, lw=2.5)

# 左：落点用标准尺子读
ax1.text(0.45, 2.15, "落点 (0,2)\n标准尺子读作 (0,2)", color=C_RED, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
ax1.text(-3.2, 0.3, "落点 (-1,0)\n标准尺子读作 (-1,0)", color=C_ORANGE, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
ax1.set_title("直觉的做法：旋转新轴，落点直接拼列", fontsize=12.5)
ax1.text(0, -1.55, "拼出 BP = [[0, -1], [2, 0]]\n× det = 2 ≠ 1：混进了拉伸，不是纯旋转",
         ha="center", fontsize=11.5, color=C_RED,
         bbox=dict(boxstyle="round,pad=0.3", fc="#fff0f0", ec=C_RED, lw=1.2))

# 右：落点翻译回新尺子读（紫色虚线 = 新尺子的 x 刻度，每格 = 标准的 2）
for x in (-2, 2):
    ax2.plot([x, x], [-2.2, 3.4], color="#d8c8e8", lw=1.0, ls="--", zorder=1)
ax2.text(2.0, 3.12, "新尺子 x 读数 = 1", ha="center", fontsize=9.5, color=C_PURPLE)
ax2.text(-2.0, 3.12, "新尺子 x 读数 = -1", ha="center", fontsize=9.5, color=C_PURPLE)
ax2.text(0.45, 2.15, "落点 (0,2)\n新尺子读作 (0,2)", color=C_RED, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
ax2.text(-3.25, 0.3, "落点 (-1,0)\n新尺子读作 (-0.5, 0)", color=C_ORANGE, fontsize=11,
         bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.9))
ax2.set_title("正确的做法：落点翻译回新尺子读数", fontsize=12.5)
ax2.text(0, -1.55, "拼出 A = [[0, -0.5], [2, 0]]\n✓ det = 1：如假包换的同一个旋转",
         ha="center", fontsize=11.5, color="#2a7a2a",
         bbox=dict(boxstyle="round,pad=0.3", fc="#f0faf0", ec="#2a7a2a", lw=1.2))

fig.suptitle("为什么不是 [[0,-1],[2,0]]？—— 列 = 落点，但落点必须用同一把尺子读", fontsize=14.5)
fig.subplots_adjust(top=0.8, wspace=0.2)
save(fig, "w4d5_bp_vs_a.png")
