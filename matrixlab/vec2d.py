"""Week 1 · 向量的基本运算（战场版：函数体待你实现）。

按 learning-guide/week1 第 4 章（Day 1）的指示实现每个函数。
"""

import math


def make(x: float, y: float) -> list:
    """用坐标造一个向量。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 用坐标造向量")


def add(u: list, v: list) -> list:
    """向量加法：箭头首尾相接。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 向量加法")


def sub(u: list, v: list) -> list:
    """向量减法：u - v。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 向量减法")


def scale(a: float, u: list) -> list:
    """数乘：把向量伸长或缩短。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 数乘")


def neg(u: list) -> list:
    """反向量：长度相同、方向相反。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 反向量")


def length(u: list) -> float:
    """向量的长度（勾股定理）。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 长度")


def from_points(a: list, b: list) -> list:
    """从点 A 到点 B 的位移向量。"""
    raise NotImplementedError("TODO: Week 1 Day 1 —— 位移向量")
