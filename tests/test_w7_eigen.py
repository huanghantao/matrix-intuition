"""Week 7 · 幂迭代法（特征值）的测试。"""

from pytest import approx


def test_normalize(mod):
    eigen = mod("eigen")
    v = eigen.normalize([3, 4])
    assert (v[0] ** 2 + v[1] ** 2) ** 0.5 == approx(1)
    assert v[0] == approx(0.6)
    assert v[1] == approx(0.8)


def test_rayleigh_on_eigenvector(mod):
    eigen = mod("eigen")
    A = [[2, 0], [0, 3]]
    assert eigen.rayleigh_quotient(A, [0, 1]) == approx(3)
    assert eigen.rayleigh_quotient(A, [1, 0]) == approx(2)


def test_power_iteration_diagonal(mod):
    eigen = mod("eigen")
    A = [[2, 0], [0, 3]]
    lam, v = eigen.power_iteration(A)
    assert lam == approx(3, abs=1e-9)          # 最大特征值是 3
    assert abs(v[0]) == approx(0, abs=1e-9)    # 特征向量指向 y 轴
    assert abs(v[1]) == approx(1)


def test_power_iteration_symmetric(mod):
    eigen = mod("eigen")
    # A = [[3,1],[1,2]]，最大特征值 = (5+√5)/2 ≈ 3.6180339887
    A = [[3, 1], [1, 2]]
    lam, v = eigen.power_iteration(A)
    assert lam == approx(3.618033988749895, abs=1e-8)


def test_eigenvector_definition(mod):
    eigen = mod("eigen")
    # 验收标准：Ax 与 λx 相等（特征方程的定义本身）
    A = [[3, 1], [1, 2]]
    lam, v = eigen.power_iteration(A)
    Av = [A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1]]
    assert Av[0] == approx(lam * v[0], abs=1e-8)
    assert Av[1] == approx(lam * v[1], abs=1e-8)


def test_power_iteration_negative_eigenvalue(mod):
    eigen = mod("eigen")
    # 绝对值最大的特征值是 -4（负的）：幂迭代仍应收敛到它
    A = [[-4, 0], [0, 2]]
    lam, v = eigen.power_iteration(A)
    assert abs(lam) == approx(4, abs=1e-9)
    assert abs(v[0]) == approx(1)
