"""Week 3 · 矩阵 = 变换。

矩阵在代码里是"列表的列表"（行主序），比如：

    [[2, 0],
     [0, 3]]

矩阵乘向量 = 对向量施加一次变换；矩阵乘矩阵 = 连续施加两个变换。
"""

import math


def matvec(M: list, v: list) -> list:
    """矩阵乘向量：M 的每一行与 v 做点积，结果拼成新向量。

    [a b] [x]   [a*x + b*y]
    [c d] [y] = [c*x + d*y]

    几何意义：把向量 v 交给变换 M，得到它变换后的新位置。
    """
    return [M[i][0] * v[0] + M[i][1] * v[1] for i in range(len(M))]


def matmul(A: list, B: list) -> list:
    """矩阵乘矩阵：结果第 i 行第 j 列 = A 的第 i 行与 B 的第 j 列的点积。

    几何意义：先施加 B 变换、再施加 A 变换，总效果是 A@B。
    注意顺序：A@B 的意思是"B 先动，A 后动"，和读代码的顺序相反。
    """
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    result = [[0.0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s = 0.0
            for k in range(inner):
                s += A[i][k] * B[k][j]
            result[i][j] = s
    return result


def transpose(M: list) -> list:
    """转置：行变列、列变行。"""
    rows = len(M)
    cols = len(M[0])
    return [[M[i][j] for i in range(rows)] for j in range(cols)]


def identity(n: int) -> list:
    """单位矩阵：主对角线上全是 1，其余全 0。它是"什么都不做"的变换。"""
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def scale_matrix(sx: float, sy: float) -> list:
    """缩放矩阵：x 方向拉伸 sx 倍，y 方向拉伸 sy 倍。"""
    return [[sx, 0.0], [0.0, sy]]


def rotation_matrix(theta_deg: float) -> list:
    """旋转矩阵：把向量逆时针旋转 theta 度。

    第一列是 e1=(1,0) 旋转后的位置，第二列是 e2=(0,1) 旋转后的位置。
    RoPE 的位置编码，用的就是这族矩阵——Week 6 Day 5 见。
    """
    t = math.radians(theta_deg)
    c, s = math.cos(t), math.sin(t)
    return [[c, -s], [s, c]]


def shear_matrix(k: float) -> list:
    """剪切矩阵：x 方向的平移量随 y 线性变化（像一副被推歪的扑克牌）。"""
    return [[1.0, k], [0.0, 1.0]]


def apply_to_points(M: list, points: list) -> list:
    """对一个点列逐个施加变换 M（画图脚本常用）。"""
    return [matvec(M, p) for p in points]
