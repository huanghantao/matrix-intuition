"""Week 6 · RoPE（战场版：函数体待你实现）。"""

import math


def rotate_2d(v: list, theta_deg: float) -> list:
    """把 2D 向量 v 逆时针旋转 theta 度。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— 旋转一个 2D 向量")


def apply_rope_2d(seq: list, theta_per_step: float) -> list:
    """给一个 2D 向量序列打上位置：第 i 个向量旋转 i*θ 度。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— 按位置旋转")


def rope_score(q: list, k: list) -> float:
    """旋转后 q 与 k 的点积。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— RoPE 分数")
