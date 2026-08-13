"""W7D3 图：最小二乘拟合 —— 直线穿不过所有点，就找"最佳妥协"。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from reference.lstsq import fit_line
from figures._common import C_BLUE, C_ORANGE, C_RED, save

xs = [0, 1, 2, 3, 4, 5]
ys = [1.2, 2.0, 3.1, 3.8, 5.1, 5.9]
a, b = fit_line(xs, ys)

fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.scatter(xs, ys, color=C_BLUE, s=70, zorder=5, label="数据点")

x = [min(xs) - 0.3, max(xs) + 0.3]
ax.plot(x, [a * xi + b for xi in x], color=C_ORANGE, lw=2.5,
        label=f"拟合直线 y = {a:.2f}x + {b:.2f}")

for xi, yi in zip(xs, ys):
    y_hat = a * xi + b
    ax.plot([xi, xi], [yi, y_hat], color=C_RED, lw=1.2, ls="--")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("最小二乘：让所有红色“误差线段”的平方和最小\n（损失函数的祖宗：Σ(预测-实际)²）", fontsize=13)
ax.legend(fontsize=11)
save(fig, "w7d3_fit_line.png")
