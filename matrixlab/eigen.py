"""Week 7 · 幂迭代法（战场版：函数体待你实现）。"""


def normalize(v: list) -> list:
    """把向量缩成长度 1（方向不变）。"""
    raise NotImplementedError("TODO: Week 7 Day 5 —— 归一化")


def rayleigh_quotient(A: list, v: list) -> float:
    """瑞利商 (v·Av)/(v·v)。"""
    raise NotImplementedError("TODO: Week 7 Day 5 —— 瑞利商")


def power_iteration(A: list, iters: int = 200, tol: float = 1e-13) -> tuple:
    """求 A 的（绝对值）最大特征值 λ 与对应特征向量 v，返回 (λ, v)。"""
    raise NotImplementedError("TODO: Week 7 Day 5 —— 幂迭代法")
