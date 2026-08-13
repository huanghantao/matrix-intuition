"""W2D3 图：同一支箭头，两把尺子的读数不同。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from fractions import Fraction

from reference.solve2 import coordinates_in_basis
from figures._common import C_BLUE, C_GREEN, C_RED, axes, save, vec

v = [4.0, 3.0]
b1 = [2.0, 1.0]
b2 = [-1.0, 1.0]
s, t = coordinates_in_basis(b1, b2, v)
s_frac = Fraction(s).limit_denominator(10)
t_frac = Fraction(t).limit_denominator(10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
for ax in (ax1, ax2):
    axes(ax, xlim=(-3, 6), ylim=(-3, 5))

# 左：标准基读数
axes(ax1, xlim=(-3, 6), ylim=(-3, 5))
vec(ax1, (0, 0), v, color=C_RED, label=f"v = {tuple(v)}",
    label_at_tip=True, label_offset=(0.15, 0.1))
ax1.plot([4, 4], [0, 3], color="#888888", lw=1, ls="--")
ax1.plot([0, 4], [3, 3], color="#888888", lw=1, ls="--")
vec(ax1, (0, 0), (1, 0), color="#999999", label="e1",
    label_at_tip=True, label_offset=(0.05, -0.35))
vec(ax1, (0, 0), (0, 1), color="#999999", label="e2",
    label_at_tip=True, label_offset=(-0.3, 0.05))
ax1.set_title("标准尺子：读数 (4, 3)\n向右 4 格、向上 3 格", fontsize=12)

# 右：新基读数
axes(ax2, xlim=(-3, 6), ylim=(-3, 5))
vec(ax2, (0, 0), v, color=C_RED, label="同一支箭头",
    label_at_tip=True, label_offset=(0.1, -0.35))
vec(ax2, (0, 0), b1, color=C_BLUE, label="b1 = (2,1)",
    label_at_tip=True, label_offset=(0.15, -0.4))
vec(ax2, (0, 0), b2, color=C_GREEN, label="b2 = (-1,1)",
    label_at_tip=True, label_offset=(-0.5, 0.1))
# 沿新基的分解虚线
sb1 = [s * b1[0], s * b1[1]]
tb2 = [t * b2[0], t * b2[1]]
ax2.plot([sb1[0], v[0]], [sb1[1], v[1]], color="#888888", lw=1, ls="--")
ax2.plot([tb2[0], v[0]], [tb2[1], v[1]], color="#888888", lw=1, ls="--")
ax2.set_title(f"新尺子（b1, b2）：读数 ({s_frac}, {t_frac})\n沿 b1 走 {s_frac} 格、沿 b2 走 {t_frac} 格", fontsize=12)

fig.suptitle("Week 2 · 向量不变，尺子变了，读数就变了", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.80, wspace=0.25)
save(fig, "w2d3_two_bases.png")
