"""Week 7 · 最小二乘（战场版：函数体待你实现）。"""

from . import gauss


def fit_line(xs: list, ys: list):
    """用最小二乘法拟合直线 y = a*x + b，返回 (a, b)。

    思路：解 (AᵀA) [a; b] = Aᵀ y（A 的第一列是 x_i，第二列全是 1）。
    """
    raise NotImplementedError("TODO: Week 7 Day 3 —— 最小二乘拟合")


def predict(x: float, a: float, b: float) -> float:
    """用拟合出的直线做预测。"""
    raise NotImplementedError("TODO: Week 7 Day 3 —— 直线预测")


def residual_sum(xs: list, ys: list, a: float, b: float) -> float:
    """残差平方和：所有点离直线的误差平方之和。"""
    raise NotImplementedError("TODO: Week 7 Day 3 —— 残差平方和")
