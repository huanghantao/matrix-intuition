"""Week 4 · 矩阵 = 坐标系。

一个可逆方阵的列向量构成一组基（一套新尺子）。
于是矩阵有两种读法：

  1) 变换：Mv 把向量 v 搬到新位置；
  2) 坐标系：在 M 这套尺子下读数为 v 的向量，在标准尺子下的读数是 Mv。

本模块只处理 2x2，内部自带两个小工具，不依赖其他模块。
"""


def determinant_2x2(M: list) -> float:
    """2x2 行列式 = 两列向量围成的平行四边形"有向面积"。"""
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def inverse_2x2(M: list) -> list:
    """2x2 逆矩阵：把 M 的变换原样撤销。

    公式（对 [[a,b],[c,d]]）：
        1/det * [[d, -b], [-c, a]]
    """
    det = determinant_2x2(M)
    if abs(det) < 1e-12:
        raise ValueError("行列式为 0：这个变换把空间压扁了，无法撤销")
    a, b = M[0]
    c, d = M[1]
    return [[d / det, -b / det], [-c / det, a / det]]


def _matvec2(M: list, v: list) -> list:
    return [M[0][0] * v[0] + M[0][1] * v[1],
            M[1][0] * v[0] + M[1][1] * v[1]]


def _matmul2(A: list, B: list) -> list:
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def to_standard(M: list, v: list) -> list:
    """读法 2：在 M 坐标系里读数为 v 的向量，标准坐标系里的读数 = Mv。

    例：M=[[2,0],[0,3]] 表示新尺子的 x 轴单位刻度是旧尺子的 2 倍长。
    在新尺子里读数为 (1,1) 的点，在旧尺子里读数是 (2,3)。
    """
    return _matvec2(M, v)


def to_basis(M: list, w: list) -> list:
    """反过来：标准坐标系里的向量 w，在 M 坐标系里的读数 = M⁻¹w。"""
    M_inv = inverse_2x2(M)
    return _matvec2(M_inv, w)


def similar_photo(P: list, B: list) -> list:
    """变换 B 在 P 坐标系下的"照片" = P⁻¹ B P。

    同一头"猪"（同一个变换 B），换个镜头位置（换组基 P），
    得到的新照片（新矩阵）就是 P⁻¹BP。
    """
    P_inv = inverse_2x2(P)
    return _matmul2(P_inv, _matmul2(B, P))


def is_same_transform(A: list, B: list, P: list, eps: float = 1e-9) -> bool:
    """判断 A 是不是变换 B 在 P 坐标系下的照片（即 A = P⁻¹BP）。"""
    A2 = similar_photo(P, B)
    for i in range(2):
        for j in range(2):
            if abs(A[i][j] - A2[i][j]) > eps:
                return False
    return True
