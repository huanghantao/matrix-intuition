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


def real_frequencies(d: int, base: float = 10000) -> list:
    """频率梯子：第 i 对的频率 theta_i = base^(-2i/d)，共 d/2 个（弧度/每挪一位）。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— 算出 d/2 个频率（十倍速梯子）")


def apply_rope_d(x: list, m: int, freqs: list) -> list:
    """给 d 维向量 x 打上位置 m：第 i 对 (x[2i], x[2i+1]) 转 m*freqs[i] 弧度。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— 逐对做 rotate_2d（注意：弧度制！）")


def rope_score_d(q: list, k: list, m: int, n: int, freqs: list) -> float:
    """真实 RoPE 分数：q 站位置 m、k 站位置 n，各自旋转后做 d 维点积。"""
    raise NotImplementedError("TODO: Week 6 Day 5 —— 旋转 q、旋转 k、再 d 维点积")
