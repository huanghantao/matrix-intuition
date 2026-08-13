"""Week 7 · 最小二乘：找不到完美解时的"最佳妥协"。

数据点比未知数多时，直线不可能穿过所有点；最小二乘找的是
"所有点到直线的竖直误差的平方和最小"的那条直线——这正是
AI 里损失函数的祖宗。
"""

from . import gauss


def fit_line(xs: list, ys: list):
    """用最小二乘法拟合直线 y = a*x + b，返回 (a, b)。

    思路：对每个数据点写方程 a*x_i + b = y_i。未知数只有 a、b 两个，
    数据点却有一堆 → "超定方程组"，一般无解。退而求其次：
    解 (AᵀA) [a; b] = Aᵀ y，得到让误差平方和最小的 (a, b)。
    """
    n = len(xs)
    # A 的第一列是 x_i，第二列全是 1；未知数 c = [a, b]，Ac = y
    AtA = [[sum(xs[i] * xs[i] for i in range(n)), sum(xs)],
           [sum(xs), float(n)]]
    Aty = [sum(xs[i] * ys[i] for i in range(n)), sum(ys)]
    a, b = gauss.solve_linear(AtA, Aty)
    return (a, b)


def predict(x: float, a: float, b: float) -> float:
    """用拟合出的直线做预测：y = a*x + b。"""
    return a * x + b


def residual_sum(xs: list, ys: list, a: float, b: float) -> float:
    """残差平方和：所有点离直线的竖直误差的平方加起来（越小越好）。"""
    return sum((a * x + b - y) ** 2 for x, y in zip(xs, ys))
