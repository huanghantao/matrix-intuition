"""Week 7 · 最小二乘的测试。"""

from pytest import approx


def test_fit_line_exact(mod):
    lstsq = mod("lstsq")
    # 三点严格共线 y = 2x + 1：应该精确恢复
    a, b = lstsq.fit_line([0, 1, 2], [1, 3, 5])
    assert a == approx(2)
    assert b == approx(1)


def test_fit_line_noisy(mod):
    lstsq = mod("lstsq")
    xs = [0, 1, 2, 3]
    ys = [1.0, 2.2, 2.8, 4.1]
    a, b = lstsq.fit_line(xs, ys)
    # 理论值 a=0.99, b=1.04（数据有噪声，允许小误差）
    assert a == approx(0.99, rel=0.02)
    assert b == approx(1.04, rel=0.05)


def test_predict(mod):
    lstsq = mod("lstsq")
    assert lstsq.predict(10, 2, 1) == 21
    assert lstsq.predict(0, 3, -7) == -7


def test_residual_zero_on_exact_fit(mod):
    lstsq = mod("lstsq")
    assert lstsq.residual_sum([0, 1, 2], [1, 3, 5], 2, 1) == approx(0)


def test_fit_beats_bad_line(mod):
    lstsq = mod("lstsq")
    xs = [0, 1, 2, 3]
    ys = [1.0, 2.2, 2.8, 4.1]
    a, b = lstsq.fit_line(xs, ys)
    # 最小二乘的误差应该比随便一条直线（比如 y = 0x + 0）小
    assert lstsq.residual_sum(xs, ys, a, b) < lstsq.residual_sum(xs, ys, 0, 0)
