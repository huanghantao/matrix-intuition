"""Week 6 · 迷你注意力机制（把前五周全部串起来）。

softmax 把分数变成权重；分数是点积（Week 5）；加权求和是线性组合（Week 2）。
"""

import math

from . import proj


def softmax(scores: list) -> list:
    """把一列分数变成"百分比"：每项取指数，再除以总和。

    - 越大的分数分到的权重越大；
    - 全部加起来恰好等于 1（所以叫"权重"）；
    - 先减去最大值再取指数，防止数字过大溢出（结果不变，纯数值技巧）。
    """
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def attention_scores(Q: list, K: list) -> list:
    """QK^T：第 i 行第 j 列 = 第 i 个查询与第 j 个键的点积。

    矩阵乘法（Week 3）+ 点积（Week 5）：每个数都是一次"亲密度"测量。
    """
    n = len(Q)
    m = len(K)
    scores = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            scores[i][j] = proj.dot(Q[i], K[j])
    return scores


def attention_weights(scores: list) -> list:
    """对每一行做 softmax：每个查询对各个键的关注程度，行和为 1。"""
    return [softmax(row) for row in scores]


def weighted_sum(weights: list, values: list) -> list:
    """加权求和 = 线性组合（Week 2 的老朋友）：Σ w[j] * V[j]。"""
    n = len(values[0])
    result = [0.0] * n
    for w, v in zip(weights, values):
        for i in range(n):
            result[i] += w * v[i]
    return result


def attention(Q: list, K: list, V: list, scale: float = None) -> list:
    """完整的一头注意力：每个查询按"亲密度"软加权地汇总所有 value。

    scale 是论文里的缩放因子（默认 sqrt(d)，防止维度过大时分数爆炸）。
    """
    d = len(Q[0])
    s = scale if scale is not None else math.sqrt(d)
    scores = attention_scores(Q, K)
    scaled = [[x / s for x in row] for row in scores]
    weights = attention_weights(scaled)
    return [weighted_sum(w, V) for w in weights]
