"""Week 5 · 点积、长度与投影。"""

import math


def dot(u: list, v: list) -> float:
    """点积：对应位置相乘再相加。u·v = Σ u[i]*v[i]。

    几何意义：|u|·|v|·cosθ —— 两个向量的长度之积，再乘上夹角的余弦。
    夹角越小点积越大；垂直时点积为 0；反向时点积为负。
    """
    return sum(a * b for a, b in zip(u, v))


def norm(u: list) -> float:
    """长度（范数）：sqrt(u·u)，勾股定理在任意维度的推广。"""
    return math.sqrt(dot(u, u))


def project_scalar(u: list, v: list) -> float:
    """u 在 v 方向上的投影长度（带符号）：(u·v) / |v|。

    相当于"把 u 的影子投到 v 这根轴上，看影子的刻度"。
    """
    return dot(u, v) / norm(v)


def project_onto(u: list, v: list) -> list:
    """u 在 v 方向上的投影向量（影子的完整箭头）。

    先算出投影长度占 |v| 的比例 s，再把 v 按比例伸缩。
    """
    s = dot(u, v) / dot(v, v)
    return [s * v[0], s * v[1]]


def is_orthogonal(u: list, v: list, eps: float = 1e-9) -> bool:
    """两个向量是否垂直：点积为 0 就是垂直。"""
    return abs(dot(u, v)) < eps


def angle_deg(u: list, v: list) -> float:
    """u 与 v 的夹角（角度制）：cosθ = u·v / (|u||v|)。"""
    cos = dot(u, v) / (norm(u) * norm(v))
    cos = max(-1.0, min(1.0, cos))  # 防浮点误差越界
    return math.degrees(math.acos(cos))
