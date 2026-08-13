"""Week 7 · 幂迭代法：求最大的特征值和它的特征向量。"""


def normalize(v: list) -> list:
    """把向量缩成长度 1（方向不变）。"""
    n = (sum(x * x for x in v)) ** 0.5
    return [x / n for x in v]


def rayleigh_quotient(A: list, v: list) -> float:
    """瑞利商 (v·Av)/(v·v)：v 越接近特征向量，它越接近特征值。

    v 恰是特征向量时，Av = λv，于是 (v·λv)/(v·v) = λ，恰好等于特征值。
    """
    n = len(A)
    Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    num = sum(v[i] * Av[i] for i in range(n))
    den = sum(v[i] * v[i] for i in range(n))
    return num / den


def power_iteration(A: list, iters: int = 200, tol: float = 1e-13) -> tuple:
    """求 A 的（绝对值）最大特征值 λ 与对应特征向量 v，返回 (λ, v)。

    思路：随便取一个向量，反复用 A 去"拽"它。每次拽完，
    它在最大特征方向上的分量增长最快，拽着拽着整个向量
    几乎完全指向那个方向——那正是特征向量的含义（Ax = λx：
    A 作用于它，只是把它拉长/缩短，不改变方向）。
    当向量几乎不再变化时收工；特征值用瑞利商读出。
    """
    n = len(A)
    v = [1.0 / n] * n  # 随便一个初始向量
    lam = 0.0
    for _ in range(iters):
        Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        new_v = normalize(Av)
        lam = rayleigh_quotient(A, new_v)
        # 向量不再变化 = 已经指向特征方向了
        if max(abs(new_v[i] - v[i]) for i in range(n)) < tol:
            v = new_v
            break
        v = new_v
    return (lam, v)
