"""Week 2 · 解二元一次方程组（战场版：函数体待你实现）。"""


def solve_2x2(a: float, b: float, c: float, d: float, e: float, f: float):
    """解方程组 a*x + b*y = e；c*x + d*y = f，返回 (x, y)。

    没有唯一解时抛出 ValueError。思路 = 初中的加减消元法。
    """
    raise NotImplementedError("TODO: Week 2 Day 5 —— 二元一次方程组求解")


def coordinates_in_basis(b1: list, b2: list, v: list):
    """在基 (b1, b2) 下表示向量 v，返回系数 (s, t)，满足 v = s*b1 + t*b2。"""
    raise NotImplementedError("TODO: Week 2 Day 5 —— 换基器")
