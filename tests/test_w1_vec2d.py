"""Week 1 · 向量的测试。

运行方式：在仓库根目录执行 `pytest tests -k w1`
"""

from pytest import approx


def test_make_and_add(mod):
    v = mod("vec2d")
    u = v.make(1, 2)
    w = v.make(3, -4)
    assert v.add(u, w) == [4, -2]
    assert v.add(w, u) == [4, -2]  # 加法交换律：先加谁都一样


def test_add_is_head_to_tail(mod):
    v = mod("vec2d")
    # 先走 (2,0) 再走 (0,3)，总位移 (2,3)：勾三股四的网格直觉
    assert v.add(v.make(2, 0), v.make(0, 3)) == [2, 3]


def test_scale_and_neg(mod):
    v = mod("vec2d")
    u = v.make(2, 3)
    assert v.scale(2, u) == [4, 6]       # 伸长到 2 倍
    assert v.scale(0.5, u) == [1, 1.5]   # 缩短到一半
    assert v.scale(-1, u) == [-2, -3]    # 反向
    assert v.neg(u) == [-2, -3]


def test_sub(mod):
    v = mod("vec2d")
    assert v.sub([4, 5], [1, 1]) == [3, 4]


def test_length(mod):
    v = mod("vec2d")
    assert v.length([3, 4]) == approx(5.0)      # 勾股定理
    assert v.length([0, 0]) == approx(0.0)
    assert v.length([-3, -4]) == approx(5.0)    # 长度与方向无关


def test_from_points(mod):
    v = mod("vec2d")
    assert v.from_points([1, 1], [4, 5]) == [3, 4]
    assert v.from_points([4, 5], [1, 1]) == [-3, -4]  # 反向走是反向量
