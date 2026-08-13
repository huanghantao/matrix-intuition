"""W8D5 图：梯度下降 —— 每一步都朝最陡的下坡方向走。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_RED, save

fig, ax = plt.subplots(figsize=(7.5, 6.5))

x = np.linspace(-3.5, 3.5, 300)
y = np.linspace(-3.5, 3.5, 300)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + 2 * Y ** 2
levels = [0.2, 0.8, 1.8, 3.2, 5.0, 7.2, 9.8, 12.8, 16.2, 20.0]
cs = ax.contour(X, Y, Z, levels=levels, colors="#9ecae1", lw=1)

# 梯度下降路径：x -= 0.4x, y -= 0.8y（lr=0.2）
px, py = 3.0, 2.0
path = [(px, py)]
for _ in range(8):
    px, py = 0.6 * px, 0.2 * py
    path.append((px, py))
path = np.array(path)
ax.plot(path[:, 0], path[:, 1], "o-", color=C_RED, lw=2.5, markersize=7)
for i, (px, py) in enumerate(path):
    ax.annotate(str(i), (px, py), textcoords="offset points",
                xytext=(10, 8), color=C_RED, fontsize=11)

ax.scatter([0], [0], color=C_BLUE, s=120, marker="*", zorder=6)
ax.text(0.15, 0.15, "谷底（最小值）", color=C_BLUE, fontsize=12)
ax.set_xlabel("参数 1")
ax.set_ylabel("参数 2")
ax.set_aspect("equal", adjustable="box")
ax.set_title("梯度下降：每次朝最陡的下坡走一小步（学习率）\n损失函数 L = x² + 2y²，从 (3,2) 一路滑向谷底", fontsize=13)
save(fig, "w8d5_gd_path.png")
