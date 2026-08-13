"""Week 5 · 相似度的测试。"""

from pytest import approx


def test_cosine_same_direction(mod):
    sim = mod("similarity")
    assert sim.cosine_similarity([1, 0], [1, 0]) == approx(1)
    # 长度不影响：方向相同就是 1
    assert sim.cosine_similarity([2, 0], [3, 0]) == approx(1)
    assert sim.cosine_similarity([1, 1], [2, 2]) == approx(1)


def test_cosine_opposite_and_orthogonal(mod):
    sim = mod("similarity")
    assert sim.cosine_similarity([1, 0], [-1, 0]) == approx(-1)
    assert sim.cosine_similarity([1, 0], [0, 1]) == approx(0)


def test_cosine_45_degrees(mod):
    sim = mod("similarity")
    # [1,0] 与 [1,1] 夹角 45°，余弦 = 1/√2
    assert sim.cosine_similarity([1, 0], [1, 1]) == approx(1 / (2 ** 0.5))


def test_nearest_index(mod):
    sim = mod("similarity")
    vectors = [[1, 0], [0, 1], [1, 1]]
    assert sim.nearest_index([2, 0.1], vectors) == 0     # 最像"东"
    assert sim.nearest_index([0, 5], vectors) == 1       # 最像"北"
    assert sim.nearest_index([-1, -1], vectors) == 0     # 与"东""北"都约 -0.71，与"东北"是 -1；最大的是"东"


def test_nearest_index_negative_query(mod):
    sim = mod("similarity")
    # query 与"东"反向（-1），与"东北"约 -0.71，与"北"垂直（0）→ 最接近的是"北"
    vectors = [[1, 0], [0, 1], [1, 1]]
    assert sim.nearest_index([-1, 0.01], vectors) == 1
