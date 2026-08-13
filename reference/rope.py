"""Week 6 · RoPE：用旋转矩阵给词排队。

位置 m 的词向量被旋转 m*θ 度。因为"旋转的复合 = 角度相加"、
而点积只与夹角有关（Week 5），所以第 m 个查询与第 n 个键的点积
只取决于相对位置 (m - n)——这正是 RoPE 的全部魔法。
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
