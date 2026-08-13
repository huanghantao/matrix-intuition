"""W4D6 图：换基就是换视角 —— PCA 直觉。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from figures._common import C_BLUE, C_GREEN, C_GRAY, axes, save, vec

rng = np.random.default_rng(7)
u = np.array([0.9, 0.45])
u = u / np.linalg.norm(u)
u_perp = np.array([-u[1], u[0]])

# 沿 u 方向拉长的点云
s = rng.normal(0, 1.4, size=120)
t = rng.normal(0, 0.25, size=120)
points = s[:, None] * u + t[:, None] * u_perp

fig, ax = plt.subplots(figsize=(7, 6))
axes(ax, xlim=(-4.5, 4.5), ylim=(-3.5, 3.5))
ax.scatter(points[:, 0], points[:, 1], s=18, color="#9ecae1", label="数据点")

vec(ax, (0, 0), (1, 0), color=C_GRAY, label="原基 e1",
    label_at_tip=True, label_offset=(0.1, -0.35))
vec(ax, (0, 0), (0, 1), color=C_GRAY, label="原基 e2",
    label_at_tip=True, label_offset=(-0.3, 0.1))
vec(ax, (0, 0), u * 4, color=C_BLUE, label="新基：数据最分散的方向（主轴）",
    label_at_tip=True, label_offset=(0.15, 0.15))
vec(ax, (0, 0), u_perp * 2, color=C_GREEN, label="新基：与主轴垂直",
    label_at_tip=True, label_offset=(-0.15, -0.4))

ax.set_title("PCA 的直觉：换一组基，让数据“躺”到主轴上\n换基后每个词的主要信息集中在少数几根轴上", fontsize=12.5)
save(fig, "w4d6_pca_intuition.png")
