"""Week 2 · 线性组合的测试。"""

from pytest import approx


def test_lincomb_basic(mod):
    combo = mod("combo")
    e1 = [1, 0]
    e2 = [0, 1]
    assert combo.lincomb([2, 3], [e1, e2]) == [2, 3]


def test_lincomb_mixes_everything(mod):
    combo = mod("combo")
    # 2*(1,2) + 3*(3,-1) = (2+9, 4-3) = (11, 1)
    assert combo.lincomb([2, 3], [[1, 2], [3, -1]]) == [11, 1]


def test_lincomb_zero_coeffs(mod):
    combo = mod("combo")
    # 系数全是 0：任何向量的组合都归零
    assert combo.lincomb([0, 0], [[1, 2], [3, 4]]) == [0, 0]


def test_lincomb_three_vectors(mod):
    combo = mod("combo")
    # 1*(1,1) + 1*(2,0) + (-1)*(0,3) = (3, -2)
    assert combo.lincomb([1, 1, -1], [[1, 1], [2, 0], [0, 3]]) == [3, -2]


def test_span_point(mod):
    combo = mod("combo")
    b1 = [2, 0]
    b2 = [0, 3]
    assert combo.span_point(b1, b2, 1, 1) == [2, 3]
    assert combo.span_point(b1, b2, 0.5, -1) == [1, -3]
