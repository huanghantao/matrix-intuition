"""Week 7 · 高斯消元：解 n 元一次方程组。"""


def solve_linear(A: list, b: list) -> list:
    """解 A x = b（A 是 n×n 方阵），返回解向量 x。

    思路（消元 + 回代，就是加减消元法的机械化）：
      1. 用某一行把下面所有行的当前列消成 0；
      2. 从最后一行开始逐个回代，求出每个未知数。
    某列的主元为 0（或接近 0）时向下换行——"选主元"，保证不会除以 0。
    """
    n = len(A)
    # 增广矩阵：把 b 拼到 A 右边
    M = [row[:] + [b[i]] for i, row in enumerate(A)]

    for col in range(n):
        # 选主元：在 col 列找绝对值最大的行，换到当前行来
        pivot = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[pivot][col]) < 1e-12:
            raise ValueError("矩阵奇异：方程没有唯一解")
        M[col], M[pivot] = M[pivot], M[col]

        # 消元：把 pivot 行以下的每一行的 col 列消成 0
        for r in range(col + 1, n):
            factor = M[r][col] / M[col][col]
            for c in range(col, n + 1):
                M[r][c] -= factor * M[col][c]

    # 回代：从最后一行往上解
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = M[i][n]  # 等式右边
        for j in range(i + 1, n):
            s -= M[i][j] * x[j]
        x[i] = s / M[i][i]
    return x
