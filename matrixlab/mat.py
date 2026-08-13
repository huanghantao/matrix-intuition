"""Week 3 · 矩阵 = 变换（战场版：函数体待你实现）。"""

import math


def matvec(M: list, v: list) -> list:
    """矩阵乘向量：M 的每一行与 v 做点积。"""
    raise NotImplementedError("TODO: Week 3 Day 2 —— 矩阵乘向量")


def matmul(A: list, B: list) -> list:
    """矩阵乘矩阵：第 i 行第 j 列 = A 第 i 行与 B 第 j 列的点积。"""
    raise NotImplementedError("TODO: Week 3 Day 3 —— 矩阵乘法")


def transpose(M: list) -> list:
    """转置：行变列、列变行。"""
    raise NotImplementedError("TODO: Week 3 Day 4 —— 转置")


def identity(n: int) -> list:
    """单位矩阵：主对角线全是 1。"""
    raise NotImplementedError("TODO: Week 3 Day 4 —— 单位矩阵")


def scale_matrix(sx: float, sy: float) -> list:
    """缩放矩阵。"""
    raise NotImplementedError("TODO: Week 3 Day 1 —— 缩放矩阵")


def rotation_matrix(theta_deg: float) -> list:
    """旋转矩阵：逆时针旋转 theta 度。"""
    raise NotImplementedError("TODO: Week 3 Day 1 —— 旋转矩阵")


def shear_matrix(k: float) -> list:
    """剪切矩阵。"""
    raise NotImplementedError("TODO: Week 3 Day 1 —— 剪切矩阵")


def apply_to_points(M: list, points: list) -> list:
    """对一个点列逐个施加变换 M。"""
    raise NotImplementedError("TODO: Week 3 Day 4 —— 点列变换")
