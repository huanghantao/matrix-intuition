"""W8D6 图：大结业 —— XOR 决策边界与损失曲线（真·训练一个网络）。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from reference.nn import TwoLayerNet, xor_dataset
from figures._common import C_BLUE, C_ORANGE, save

X, y = xor_dataset()
net = TwoLayerNet(n_in=2, n_hidden=4, seed=0)
history = net.train(X, y, epochs=3000, lr=0.1)

# 决策边界
grid = np.linspace(-0.3, 1.3, 200)
GX, GY = np.meshgrid(grid, grid)
G = np.column_stack([GX.ravel(), GY.ravel()])
pred = net.forward(G).reshape(GX.shape)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.contourf(GX, GY, pred, levels=30, cmap="RdBu_r", alpha=0.8)
ax1.contour(GX, GY, pred, levels=[0.5], colors="black", lw=2)
ax1.scatter(X[:, 0], X[:, 1], c=y[:, 0], cmap="RdBu_r",
            edgecolors="black", s=180, zorder=5)
ax1.set_title("训练好的网络画出的决策边界\n（隐藏层学出了两条折线，把 XOR 拆开）", fontsize=12)
ax1.set_xlabel("x1")
ax1.set_ylabel("x2")

ax2.plot(history, color=C_ORANGE, lw=2)
ax2.set_yscale("log")
ax2.set_xlabel("epoch")
ax2.set_ylabel("损失（对数刻度）")
ax2.set_title("损失曲线：一步一步滑下山\n（梯度下降在实时起作用）", fontsize=12)
ax2.grid(True, color="#dddddd", lw=0.6)
# 只保留 3 个 10 的幂刻度，避免科学计数法标签挤成一团
import math
import matplotlib.ticker as ticker
ax2.yaxis.set_major_locator(ticker.LogLocator(base=10, numticks=3))
ax2.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"1e{int(round(math.log10(v)))}" if v > 0 else "0")
)
ax2.tick_params(axis="y", labelsize=9)

fig.suptitle("Week 8 · 大结业：用 numpy 从零训练的两层网络学会了 XOR", fontsize=15, y=0.99)
fig.subplots_adjust(top=0.80, wspace=0.3)
save(fig, "w8d6_decision_boundary.png")
