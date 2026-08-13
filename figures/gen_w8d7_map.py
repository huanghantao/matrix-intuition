"""W8D7 图：结业 —— 矩阵直觉地图。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import save

fig, ax = plt.subplots(figsize=(12, 6.5))
ax.axis("off")


def box(x, y, w, h, text, color="#ffffff", fs=11):
    ax.add_patch(plt.Rectangle((x, y), w, h, fill=True, facecolor=color,
                               edgecolor="#333333", lw=1.5))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.6))


# 主干
box(0.40, 0.55, 0.20, 0.16, "矩阵 = 变换 = 坐标系\n（W3/W4：运动是相对的）", "#fdeadd", 12)

# 上游
box(0.02, 0.55, 0.15, 0.16, "向量\n（W1：箭头）", "#eaf2fb")
box(0.19, 0.55, 0.15, 0.16, "线性组合与基\n（W2：尺子）", "#d5e8f7")
# 下游
box(0.66, 0.55, 0.15, 0.16, "点积/投影/相似度\n（W5：亲密度）", "#d5e8f7")
box(0.83, 0.55, 0.15, 0.16, "方程组/最小二乘/特征值\n（W7：求解与主轴）", "#d5e8f7")

# AI 落地
box(0.02, 0.24, 0.20, 0.16, "embedding：\n词 = 向量", "#c6e2c6")
box(0.25, 0.24, 0.22, 0.16, "Attention：\n点积 + softmax + 加权求和\n（W6）", "#c6e2c6")
box(0.50, 0.24, 0.22, 0.16, "RoPE：\n旋转矩阵给词排队\n（W6）", "#c6e2c6")
box(0.75, 0.24, 0.23, 0.16, "神经网络：\n一连串变换 + 梯度下降\n（W8）", "#c6e2c6")

# 底部
box(0.30, 0.03, 0.40, 0.13, "学完能读懂：attention 公式、embedding 相似度、RoPE、训练流程",
    "#f7e3c5", 12)

arrow(0.17, 0.63, 0.19, 0.63)
arrow(0.34, 0.63, 0.40, 0.63)
arrow(0.60, 0.63, 0.66, 0.63)
arrow(0.81, 0.63, 0.83, 0.63)
arrow(0.10, 0.55, 0.10, 0.40)
arrow(0.36, 0.55, 0.36, 0.40)
arrow(0.61, 0.55, 0.61, 0.40)
arrow(0.86, 0.55, 0.86, 0.40)
arrow(0.50, 0.24, 0.50, 0.16)

ax.text(0.5, 0.93, "矩阵直觉地图：一条主线，八周旅程", ha="center", fontsize=16, weight="bold")
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.97)
save(fig, "w8d7_map.png")
