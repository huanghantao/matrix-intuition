"""Week 7 · 高斯消元的测试。"""

from pytest import approx, raises


def _matvec(A, v):
    n = len(A)
    return [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]


def test_solve_2x2(mod):
    gauss = mod("gauss")
    # x + y = 3；x - y = 1
    x = gauss.solve_linear([[1, 1], [1, -1]], [3, 1])
    assert x == [approx(2), approx(1)]


def test_solve_3x3(mod):
    gauss = mod("gauss")
    A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b = [8, -11, -3]
    x = gauss.solve_linear(A, b)
    assert x == [approx(2), approx(3), approx(-1)]
    # 回代验证：A x 应该等于 b
    Ax = _matvec(A, x)
    assert Ax == [approx(b[0]), approx(b[1]), approx(b[2])]


def test_solve_needs_pivot(mod):
    gauss = mod("gauss")
    # 第一行第一个系数是 0：必须换行
    x = gauss.solve_linear([[0, 1], [1, 0]], [2, 3])
    assert x == [approx(3), approx(2)]


def test_solve_3x3_pivot(mod):
    gauss = mod("gauss")
    A = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    b = [5, 4, 3]
    x = gauss.solve_linear(A, b)
    assert x == [approx(1), approx(2), approx(3)]


def test_singular_raises(mod):
    gauss = mod("gauss")
    with raises(ValueError):
        gauss.solve_linear([[1, 1], [2, 2]], [1, 3])


def test_solve_identity(mod):
    gauss = mod("gauss")
    x = gauss.solve_linear([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [7, -2, 9])
    assert x == [7, -2, 9]
