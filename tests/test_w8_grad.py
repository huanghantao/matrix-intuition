"""Week 8 · 数值梯度的测试。"""

from pytest import approx


def test_gradient_of_quadratic(mod):
    grad = mod("grad")
    # f = x0² + 3x1²，在 (2,1) 处梯度 = (2*2, 6*1) = (4, 6)
    f = lambda x: x[0] ** 2 + 3 * x[1] ** 2
    g = grad.numerical_gradient(f, [2.0, 1.0])
    assert g[0] == approx(4, abs=1e-6)
    assert g[1] == approx(6, abs=1e-6)


def test_gradient_of_product(mod):
    grad = mod("grad")
    # f = x0*x1，在 (2,3) 处梯度 = (3, 2)
    f = lambda x: x[0] * x[1]
    g = grad.numerical_gradient(f, [2.0, 3.0])
    assert g[0] == approx(3, abs=1e-6)
    assert g[1] == approx(2, abs=1e-6)


def test_gradient_zero_at_bottom(mod):
    grad = mod("grad")
    # f = x0² + x1²：谷底在 (0,0)，梯度为零
    f = lambda x: x[0] ** 2 + x[1] ** 2
    g = grad.numerical_gradient(f, [0.0, 0.0])
    assert g[0] == approx(0, abs=1e-9)
    assert g[1] == approx(0, abs=1e-9)


def test_gradient_sign_points_downhill(mod):
    grad = mod("grad")
    # f = (x-5)²：谷底在 x=5。x=3（在山谷左边）时梯度为负，
    # 告诉我们"往正方向走会下降"。
    f = lambda x: (x[0] - 5) ** 2
    g = grad.numerical_gradient(f, [3.0])
    assert g[0] == approx(-4, abs=1e-6)
