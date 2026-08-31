"""Week 6 · RoPE：用旋转矩阵给词排队。

位置 m 的词向量被旋转 m*θ 度。因为"旋转的复合 = 角度相加"、
而点积只与夹角有关（Week 5），所以第 m 个查询与第 n 个键的
点积只取决于相对位置 (m - n)——这正是 RoPE 的全部魔法。

真实 RoPE（5.8）：把 d 维切成 d/2 对，每对配一个频率
theta_i = base^(-2i/d)，快针管近处、慢针管远处。机制不变，
只是把一条链扩成 d/2 条不同转速的链。
"""

import math


def rotate_2d(v: list, theta_deg: float) -> list:
    """把 2D 向量 v 逆时针旋转 theta 度（Week 3 旋转矩阵的实战）。"""
    t = math.radians(theta_deg)
    c, s = math.cos(t), math.sin(t)
    return [c * v[0] - s * v[1], s * v[0] + c * v[1]]


def apply_rope_2d(seq: list, theta_per_step: float) -> list:
    """给一个 2D 向量序列打上位置：第 i 个向量旋转 i*θ 度。"""
    return [rotate_2d(v, i * theta_per_step) for i, v in enumerate(seq)]


def rope_score(q: list, k: list) -> float:
    """旋转后 q 与 k 的点积（RoPE 之后的注意力分数，未缩放）。"""
    return q[0] * k[0] + q[1] * k[1]


def real_frequencies(d: int, base: float = 10000) -> list:
    """频率梯子：第 i 对的频率 theta_i = base^(-2i/d)，共 d/2 个（弧度/每挪一位）。

    d=8、base=10000 时正好是十倍速梯子 [1, 0.1, 0.01, 0.001]。
    """
    return [base ** (-2 * i / d) for i in range(d // 2)]


def apply_rope_d(x: list, m: int, freqs: list) -> list:
    """给 d 维向量 x 打上位置 m：第 i 对 (x[2i], x[2i+1]) 转 m*freqs[i] 弧度。

    和 rotate_2d 是同一个公式，只是：角度用弧度制、
    每一对的转速来自 freqs、所有对各自独立地转。
    """
    out = []
    for i, f in enumerate(freqs):
        c, s = math.cos(m * f), math.sin(m * f)
        a, b = x[2 * i], x[2 * i + 1]
        out += [c * a - s * b, s * a + c * b]
    return out


def rope_score_d(q: list, k: list, m: int, n: int, freqs: list) -> float:
    """真实 RoPE 分数：q 站位置 m、k 站位置 n，各自旋转后做 d 维点积。

    只依赖 (m-n)：等于 sum(cos((m-n)*freqs[i]) * (第 i 对的 q·k))，
    同一对词时内容项固定，分数就是各频率余弦的加权和。
    """
    qm = apply_rope_d(q, m, freqs)
    kn = apply_rope_d(k, n, freqs)
    return sum(a * b for a, b in zip(qm, kn))
