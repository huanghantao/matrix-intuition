"""W6D5 图：RoPE 分数热力图 —— 只依赖相对位置的"斜条纹"。"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
import numpy as np

from reference.rope import rope_score, rotate_2d
from figures._common import save

theta = 30.0
N = 8
q = [1.0, 0.0]
k = [1.0, 0.0]

score = np.zeros((N, N))
for m in range(N):
    for j in range(N):
        qm = rotate_2d(q, m * theta)
        kj = rotate_2d(k, j * theta)
        score[m, j] = rope_score(qm, kj)

fig, ax = plt.subplots(figsize=(6.5, 5.8))
im = ax.imshow(score, cmap="RdYlBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(N), [f"k{i}" for i in range(N)])
ax.set_yticks(range(N), [f"q{m}" for m in range(N)])
ax.set_title("q_m·k_n 热力图：每条“斜线”上的值相同\n= 只与 (m-n) 有关（Toeplitz 结构）", fontsize=12.5)
for m in range(N):
    for j in range(N):
        ax.text(j, m, f"{score[m, j]:.1f}", ha="center", va="center",
                fontsize=8.5, color="#222222")
fig.colorbar(im, ax=ax, label="cos((m-n)·30°)")
save(fig, "w6d5_rope_scores.png")
