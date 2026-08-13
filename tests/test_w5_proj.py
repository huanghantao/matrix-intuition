"""Week 5 · 点积、投影、夹角的测试。"""

from pytest import approx


def test_dot_basic(mod):
    proj = mod("proj")
    assert proj.dot([1, 2], [3, 4]) == 1 * 3 + 2 * 4
    assert proj.dot([1, 2], [3, 4]) == proj.dot([3, 4], [1, 2])  # 交换律


def test_dot_orthogonal_is_zero(mod):
    proj = mod("proj")
    assert proj.dot([1, 0], [0, 1]) == 0
    assert proj.dot([1, 1], [1, -1]) == 0


def test_dot_negative(mod):
    proj = mod("proj")
    # 反向的两个向量：点积 = 长度之积的相反数
    assert proj.dot([1, 0], [-1, 0]) == approx(-1)


def test_norm(mod):
    proj = mod("proj")
    assert proj.norm([3, 4]) == approx(5)
    assert proj.norm([0, 0]) == approx(0)


def test_project_scalar(mod):
    proj = mod("proj")
    assert proj.project_scalar([1, 1], [1, 0]) == approx(1)   # 影子落在 x 轴，长度 1
    assert proj.project_scalar([1, 1], [-1, 0]) == approx(-1)  # 投到反方向，带负号
    assert proj.project_scalar([0, 5], [1, 0]) == approx(0)   # 垂直：影子缩成一个点


def test_project_onto(mod):
    proj = mod("proj")
    out = proj.project_onto([1, 1], [1, 0])
    assert out == [approx(1), approx(0)]
    out = proj.project_onto([3, 4], [1, 0])
    assert out == [approx(3), approx(0)]
    # 投到自己身上 = 自己
    out = proj.project_onto([2, 2], [2, 2])
    assert out == [approx(2), approx(2)]


def test_is_orthogonal(mod):
    proj = mod("proj")
    assert proj.is_orthogonal([1, 0], [0, 1])
    assert proj.is_orthogonal([1, 1], [1, -1])
    assert not proj.is_orthogonal([1, 0], [1, 1])


def test_angle_deg(mod):
    proj = mod("proj")
    assert proj.angle_deg([1, 0], [1, 0]) == approx(0)
    assert proj.angle_deg([1, 0], [0, 1]) == approx(90)
    assert proj.angle_deg([1, 0], [-1, 0]) == approx(180)
    assert proj.angle_deg([1, 0], [1, 1]) == approx(45)
