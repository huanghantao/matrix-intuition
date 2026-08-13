"""Week 1 · 向量的基本运算。

向量在代码里就是一个列表，比如 [3.0, 4.0] 表示从原点 (0, 0) 出发、
到达 (3, 4) 的那支箭头。所有函数都返回新向量，不修改传入的向量。
"""

import math


def make(x: float, y: float) -> list:
    """用坐标造一个向量。"""
    return [x, y]


def add(u: list, v: list) -> list:
    """向量加法：箭头首尾相接（三角形/平行四边形法则）。

    (u1, u2) + (v1, v2) = (u1 + v1, u2 + v2)
    几何意义：先走 u 再走 v，总位移就是 u + v。
    """
    return [u[0] + v[0], u[1] + v[1]]


def sub(u: list, v: list) -> list:
    """向量减法：从 v 的终点走回 u 的终点的位移 = u - v。"""
    return [u[0] - v[0], u[1] - v[1]]


def scale(a: float, u: list) -> list:
    """数乘：把向量伸长（|a|>1）或缩短（|a|<1）；a<0 时方向反转。"""
    return [a * u[0], a * u[1]]


def neg(u: list) -> list:
    """反向量：与原向量长度相同、方向相反。"""
    return [-u[0], -u[1]]


def length(u: list) -> float:
    """向量的长度（勾股定理）：sqrt(x² + y²)。"""
    return math.sqrt(u[0] ** 2 + u[1] ** 2)


def from_points(a: list, b: list) -> list:
    """从点 A 到点 B 的位移向量 = B - A。"""
    return [b[0] - a[0], b[1] - a[1]]
