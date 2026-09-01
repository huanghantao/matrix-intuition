"""W7D3 图（三维版·自然坐标）：成绩单空间的平面投影。

3 个点 = 3 维成绩单空间：三根坐标轴就是“点1 / 点2 / 点3 的分数”。
A 的两列（各点的 x、全 1）按 (a, b) 混合，铺出所有候选成绩单 = 一张平面（列空间）；
y = 真实成绩单悬在平面外；ŷ = 平面上离 y 最近的点；残差向量与平面垂直，
它的 3 个坐标 = 3 个点各自的残差。

数据：xs=[0,1,2]，ys=[0.2,2.8,0.6] → a=0.2, b=1.0，
ŷ=(1.0, 1.2, 1.4)，残差 y−ŷ=(−0.8, 1.6, −0.8)，RSS = 0.64+2.56+0.64 = 3.84。

视角自动挑选：遍历 (elev, azim) 网格，让“残差”在屏幕上的投影方向
与“平面两个张成方向”的投影分离角尽量大（残差才看得出的确戳出平面）。
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import proj3d

from reference.lstsq import fit_line
from figures._common import C_BLUE, C_GREEN, C_ORANGE, C_RED, save

G_DARK = "#1e7b1e"
O_DARK = "#b35a00"

xs = [0.0, 1.0, 2.0]
ys = [0.2, 2.8, 0.6]
a, b = fit_line(xs, ys)
col1 = np.array(xs, dtype=float)      # 列 1：各点的 x
col2 = np.ones(3)                     # 列 2：全 1
y = np.array(ys)                      # 真实成绩单
y_hat = a * col1 + b * col2           # 投影 ŷ
res = y - y_hat                       # 残差向量（⊥ 平面）
print(f"  a={a:.3f} b={b:.3f}  ŷ={y_hat}  残差={res}  RSS={float(res @ res):.2f}")

fig = plt.figure(figsize=(9.6, 7.6))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(0, 2.0)
ax.set_ylim(0, 3.0)
ax.set_zlim(0, 2.6)
ax.set_box_aspect((1.0, 1.3, 1.05))
ax.set_xlabel("点 1 的分数")
ax.set_ylabel("点 2 的分数")
ax.set_zlabel("点 3 的分数")
ax.set_xticks([0, 1, 2])
ax.set_yticks([0, 1, 2, 3])
ax.set_zticks([0, 1, 2])


def screen_vec(v):
    """向量 v 在当前视角下的屏幕投影方向（单位化）。"""
    M = ax.get_proj()
    x0, y0, _ = proj3d.proj_transform(0.0, 0.0, 0.0, M)
    x1, y1, _ = proj3d.proj_transform(float(v[0]), float(v[1]), float(v[2]), M)
    p0 = ax.transData.transform((x0, y0))
    p1 = ax.transData.transform((x1, y1))
    dv = np.array([p1[0] - p0[0], p1[1] - p0[1]])
    n = np.linalg.norm(dv)
    return dv / n if n > 1e-9 else dv


def ang(u, v):
    return float(np.degrees(np.arccos(np.clip(float(np.dot(u, v)), -1.0, 1.0))))


best = None
for elev in range(6, 44, 4):
    for azim in range(-95, 55, 10):
        ax.view_init(elev=elev, azim=azim)
        r = screen_vec(res)
        score = min(ang(r, screen_vec(col1)), ang(r, screen_vec(col2)))
        if r[1] > 0:
            score += 5.0          # 轻微偏好：残差在屏幕上朝上指
        if best is None or score > best[0]:
            best = (score, elev, azim)
elev, azim = best[1], best[2]
ax.view_init(elev=elev, azim=azim)
print(f"  视角 elev={elev} azim={azim}（自动挑：残差与平面两方向屏幕分离角最大）")

# 列空间平面：a·列1 + b·列2
aa = np.linspace(-0.1, 0.5, 10)
bb = np.linspace(0.5, 1.55, 10)
A, B = np.meshgrid(aa, bb)
P = A[..., None] * col1 + B[..., None] * col2
ax.plot_surface(P[..., 0], P[..., 1], P[..., 2], color=C_ORANGE, alpha=0.22,
                linewidth=0, antialiased=True)
for (s0, t0), (s1, t1) in [((aa[0], bb[0]), (aa[-1], bb[0])),
                           ((aa[-1], bb[0]), (aa[-1], bb[-1])),
                           ((aa[-1], bb[-1]), (aa[0], bb[-1])),
                           ((aa[0], bb[-1]), (aa[0], bb[0]))]:
    e0 = s0 * col1 + t0 * col2
    e1 = s1 * col1 + t1 * col2
    ax.plot([e0[0], e1[0]], [e0[1], e1[1]], [e0[2], e1[2]],
            color=C_ORANGE, alpha=0.6, lw=1.2)


def arrow3(v, color, lw=2.4, start=(0.0, 0.0, 0.0), ratio=0.08):
    ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2],
              color=color, lw=lw, arrow_length_ratio=ratio)


arrow3(col1, C_ORANGE, 2.0)                    # 两种原料列
arrow3(col2, C_ORANGE, 2.0)
arrow3(y, C_BLUE)                              # 真实成绩单
arrow3(y_hat, C_GREEN)                         # 投影 ŷ
ax.scatter(*y_hat, color=C_GREEN, s=50, depthshade=False)
ax.quiver(y_hat[0], y_hat[1], y_hat[2], res[0], res[1], res[2],
          color=C_RED, lw=3.4, arrow_length_ratio=0.09)   # 残差向量


def note3(p, s, color, fs=10):
    ax.text(p[0], p[1], p[2], s, color=color, fontsize=fs,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))


note3(col1 + np.array([0.05, -0.2, 0.3]), "列 1 = 各点的 x = (0, 1, 2)", O_DARK)
note3(col2 + np.array([0.12, -0.3, -0.25]), "列 2 = 全 1 = (1, 1, 1)", O_DARK)
note3(y + np.array([0.18, 0.05, 0.22]), "y = 真实成绩单 (0.2, 2.8, 0.6)", C_BLUE)
note3(y_hat + np.array([0.15, -0.3, 0.28]),
      "ŷ = 平面上离 y 最近的点\n(1.0, 1.2, 1.4)", G_DARK)
note3(y_hat + res * 0.55 + np.array([0.2, 0.1, 0.26]),
      "残差 y − ŷ = (−0.8, 1.6, −0.8)\n⊥ 平面（垂线段最短）", C_RED)

ax.text2D(0.02, 0.985, "三根轴 = 三个点的分数（成绩单空间）\n残差的 3 个坐标 = 3 个点各自的残差",
          transform=ax.transAxes, fontsize=11, va="top", color="#333333",
          bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88))
ax.text2D(0.02, 0.02, "ŷ = (1.0, 1.2, 1.4)　残差 y − ŷ = (−0.8, 1.6, −0.8)\n"
          "RSS = 0.64 + 2.56 + 0.64 = 3.84 = ‖y − ŷ‖²",
          transform=ax.transAxes, fontsize=11, va="bottom", color="#333333",
          bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none", alpha=0.88))

ax.set_title("三维成绩单空间：两列原料混出一张平面（列空间）\n"
             "ŷ = 平面上离 y 最近的预测成绩单，残差 ⊥ 平面", fontsize=12.5, pad=0)
save(fig, "w7d3_projection.png")
