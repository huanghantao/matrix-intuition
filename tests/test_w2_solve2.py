"""Week 2 · 二元一次方程组（换基器）的测试。"""

from pytest import approx, raises


def test_solve_simple(mod):
    solve2 = mod("solve2")
    # x + y = 3
    # x - y = 1  → x=2, y=1
    assert solve2.solve_2x2(1, 1, 1, -1, 3, 1) == (approx(2), approx(1))


def test_solve_scaled(mod):
    solve2 = mod("solve2")
    # 3x - 2y = 4
    # 6x + 2y = 20  → x=8/3, y=2
    x, y = solve2.solve_2x2(3, -2, 6, 2, 4, 20)
    assert x == approx(8 / 3)
    assert y == approx(2)


def test_solve_needs_swap(mod):
    solve2 = mod("solve2")
    # 0x + 2y = 4
    # 3x + 1y = 5  → y=2, x=1（第一个式子没有 x，需要交换）
    x, y = solve2.solve_2x2(0, 2, 3, 1, 4, 5)
    assert x == approx(1)
    assert y == approx(2)


def test_no_solution_parallel(mod):
    solve2 = mod("solve2")
    # x + y = 1 与 2x + 2y = 3 是两条平行线，永远不相交
    with raises(ValueError):
        solve2.solve_2x2(1, 1, 2, 2, 1, 3)


def test_no_unique_solution(mod):
    solve2 = mod("solve2")
    # 两个式子都没有 x：x 可以随便取
    with raises(ValueError):
        solve2.solve_2x2(0, 1, 0, 2, 1, 2)


def test_coordinates_in_basis_orthogonal(mod):
    solve2 = mod("solve2")
    # 基 = (2,0) 和 (0,3)：坐标轴是普通轴拉长了 2 倍、3 倍
    # 标准坐标 (4,9) 在新基下读数 = (2,3)
    s, t = solve2.coordinates_in_basis([2, 0], [0, 3], [4, 9])
    assert s == approx(2)
    assert t == approx(3)


def test_coordinates_in_basis_skew(mod):
    solve2 = mod("solve2")
    # 基 = (1,0) 和 (1,1)：一根轴斜着
    # v=(3,2)：s*(1,0) + t*(1,1) = (s+t, t) = (3,2) → t=2, s=1
    s, t = solve2.coordinates_in_basis([1, 0], [1, 1], [3, 2])
    assert s == approx(1)
    assert t == approx(2)


def test_roundtrip(mod):
    solve2 = mod("solve2")
    combo = mod("combo")
    # 换过去再换回来：用 (s,t) 线性组合基向量，应该还原出 v
    b1, b2 = [2, 1], [-1, 3]
    v = [5, -4]
    s, t = solve2.coordinates_in_basis(b1, b2, v)
    back = combo.lincomb([s, t], [b1, b2])
    assert back == [approx(v[0]), approx(v[1])]
