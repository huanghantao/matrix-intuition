"""W8D4 图：链式法则 —— 变化一层一层传回去。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt

from figures._common import save

fig, ax = plt.subplots(figsize=(11, 4))
ax.axis("off")

nodes = [
    (0.03, 0.35, "x\n输入", "#eaf2fb"),
    (0.22, 0.35, "z₁ = W₁x + b₁\n(Week 3 变换)", "#d5e8f7"),
    (0.42, 0.35, "h = ReLU(z₁)\n(开关)", "#d5e8f7"),
    (0.62, 0.35, "z₂ = W₂h + b₂\n(变换)", "#d5e8f7"),
    (0.82, 0.35, "ŷ = z₂\n预测", "#fdeadd"),
    (0.82, 0.10, "损失 L(ŷ, y)\n(Week 7 平方误差)", "#f7c5c5"),
]
for x, y, text, color in nodes:
    w = 0.15
    ax.add_patch(plt.Rectangle((x, y), w, 0.22, fill=True, facecolor=color,
                               edgecolor="#333333", lw=1.5))
    ax.text(x + w / 2, y + 0.11, text, ha="center", va="center", fontsize=11)

# 前向箭头（上排）
for i in range(4):
    ax.annotate("", xy=(nodes[i + 1][0], 0.46), xytext=(nodes[i][0] + 0.15, 0.46),
                arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.8))
ax.annotate("", xy=(0.895, 0.32), xytext=(0.895, 0.46),
            arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.8))
ax.text(0.5, 0.52, "前向：从输入算出预测（矩阵变换流水线）", ha="center", fontsize=12)

# 反向箭头（下排）
ax.annotate("", xy=(0.895, 0.10), xytext=(0.895, 0.16),
            arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=2.2))
for i in range(4, 0, -1):
    ax.annotate("", xy=(nodes[i][0] + 0.15, 0.16), xytext=(nodes[i + 1][0], 0.16),
                arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=2.2))
ax.text(0.5, 0.02, "反向：损失对每个参数的“变化率” = 各层导数连乘（链式法则），Week 8 Day 1 的数值梯度可以抽查它",
        ha="center", fontsize=12, color="#d62728")

ax.set_xlim(0, 1)
ax.set_ylim(0, 0.6)
ax.set_title("Week 8 · 反向传播 = 把“错了多少”的变化，一层层传导回每个参数", fontsize=14)
save(fig, "w8d4_chain.png")
