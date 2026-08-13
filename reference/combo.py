"""Week 2 · 线性组合。

线性组合 = 先把每个向量伸缩，再把结果全部加起来。
它回答的问题是：给几支箭头，通过"伸缩 + 相加"能拼出哪些向量？
"""


def lincomb(coeffs: list, vecs: list) -> list:
    """计算系数 coeffs 与向量 vecs 的线性组合：Σ coeffs[i] * vecs[i]。

    例：lincomb([2, 3], [[1, 0], [0, 1]]) = [2, 3]，即 2*e1 + 3*e2。
    """
    n = len(vecs[0])
    result = [0.0] * n
    for c, v in zip(coeffs, vecs):
        for i in range(n):
            result[i] += c * v[i]
    return result


def span_point(b1: list, b2: list, s: float, t: float) -> list:
    """两个向量 b1、b2 张成的平面里，系数为 (s, t) 的那个点 = s*b1 + t*b2。"""
    return [s * b1[0] + t * b2[0], s * b1[1] + t * b2[1]]
