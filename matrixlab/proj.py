"""Week 5 · 点积、长度与投影（战场版：函数体待你实现）。"""

import math


def dot(u: list, v: list) -> float:
    """点积：对应位置相乘再相加。"""
    raise NotImplementedError("TODO: Week 5 Day 1 —— 点积")


def norm(u: list) -> float:
    """长度（范数）：sqrt(u·u)。"""
    raise NotImplementedError("TODO: Week 5 Day 2 —— 长度")


def project_scalar(u: list, v: list) -> float:
    """u 在 v 方向上的投影长度（带符号）。"""
    raise NotImplementedError("TODO: Week 5 Day 2 —— 投影长度")


def project_onto(u: list, v: list) -> list:
    """u 在 v 方向上的投影向量。"""
    raise NotImplementedError("TODO: Week 5 Day 2 —— 投影向量")


def is_orthogonal(u: list, v: list, eps: float = 1e-9) -> bool:
    """两个向量是否垂直。"""
    raise NotImplementedError("TODO: Week 5 Day 2 —— 垂直判定")


def angle_deg(u: list, v: list) -> float:
    """u 与 v 的夹角（角度制）。"""
    raise NotImplementedError("TODO: Week 5 Day 2 —— 夹角")
