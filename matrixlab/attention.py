"""Week 6 · 迷你注意力机制（战场版：函数体待你实现）。"""

import math

from . import proj


def softmax(scores: list) -> list:
    """把一列分数变成"百分比"：每项取指数，再除以总和。"""
    raise NotImplementedError("TODO: Week 6 Day 3 —— softmax")


def attention_scores(Q: list, K: list) -> list:
    """QK^T：第 i 行第 j 列 = 第 i 个查询与第 j 个键的点积。"""
    raise NotImplementedError("TODO: Week 6 Day 4 —— 注意力分数")


def attention_weights(scores: list) -> list:
    """对每一行做 softmax。"""
    raise NotImplementedError("TODO: Week 6 Day 4 —— 注意力权重")


def weighted_sum(weights: list, values: list) -> list:
    """加权求和 = Σ w[j] * V[j]。"""
    raise NotImplementedError("TODO: Week 6 Day 4 —— 加权求和")


def attention(Q: list, K: list, V: list, scale: float = None) -> list:
    """完整的一头注意力。"""
    raise NotImplementedError("TODO: Week 6 Day 4 —— 注意力")
