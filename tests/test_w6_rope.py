"""Week 6 · RoPE 的测试。"""

import math

from pytest import approx


def test_rotate_preserves_length(mod):
    rope = mod("rope")
    v = [3, 4]
    r = rope.rotate_2d(v, 37)
    assert (r[0] ** 2 + r[1] ** 2) ** 0.5 == approx(5)
    assert r != v  # 方向确实变了


def test_rotate_landmarks(mod):
    rope = mod("rope")
    assert rope.rotate_2d([1, 0], 0) == [approx(1), approx(0)]     # 0° 不动
    assert rope.rotate_2d([1, 0], 90) == [approx(0), approx(1)]    # 东 → 北
    assert rope.rotate_2d([1, 0], 180) == [approx(-1), approx(0)]  # 180° 反向


def test_rotation_is_linear(mod):
    rope = mod("rope")
    vec2d = mod("vec2d")
    u = [1, 2]
    v = [-3, 1]
    # 旋转(u+v) = 旋转u + 旋转v：旋转是线性变换（Week 3 的核心性质）
    left = rope.rotate_2d(vec2d.add(u, v), 40)
    right = vec2d.add(rope.rotate_2d(u, 40), rope.rotate_2d(v, 40))
    assert left == [approx(right[0]), approx(right[1])]


def test_apply_rope_2d(mod):
    rope = mod("rope")
    seq = [[1, 0], [1, 0], [1, 0]]
    out = rope.apply_rope_2d(seq, 90)
    assert out[0] == [approx(1), approx(0)]     # 位置 0：不转
    assert out[1] == [approx(0), approx(1)]     # 位置 1：转 90°
    assert out[2] == [approx(-1), approx(0)]    # 位置 2：转 180°


def test_rope_score_depends_only_on_relative_position(mod):
    rope = mod("rope")
    q = [1, 0]
    k = [1, 0]
    theta = 30.0

    def score(m, n):
        qm = rope.rotate_2d(q, m * theta)
        kn = rope.rotate_2d(k, n * theta)
        return rope.rope_score(qm, kn)

    # 位置一起平移，分数不变：score(m,n) 只由 (m-n) 决定
    assert score(1, 1) == approx(score(2, 2))
    assert score(0, 3) == approx(score(5, 8))
    assert score(1, 0) == approx(score(3, 2))
    # 相对位置不同，分数不同
    assert score(0, 0) != approx(score(0, 1))
    # 具体值：score(m,n) = cos((m-n)*30°)
    assert score(1, 2) == approx(0.8660254037844387)   # cos(-30°)
    assert score(2, 1) == approx(0.8660254037844387)   # cos(30°)


def test_rope_keeps_length_of_every_token(mod):
    rope = mod("rope")
    seq = [[3, 4], [1, 1], [-2, 5]]
    out = rope.apply_rope_2d(seq, 15)
    for v, r in zip(seq, out):
        assert (r[0] ** 2 + r[1] ** 2) ** 0.5 == approx((v[0] ** 2 + v[1] ** 2) ** 0.5)


def test_rope_real_frequencies(mod):
    rope = mod("rope")
    freqs = rope.real_frequencies(8)
    assert len(freqs) == 4                        # d/2 对，每对一个频率
    assert freqs[0] == approx(1)                  # 最快的针：1 弧度/位
    # 十倍速梯子 [1, 0.1, 0.01, 0.001]：theta_i = 10000^(-2i/8)
    assert freqs == [approx(10000 ** (-2 * i / 8)) for i in range(4)]


def test_rope_real_hand_example(mod):
    # 5.8.4 的手算例子：d=8、m=2，x=[1,0,1,0,1,0,1,0]
    rope = mod("rope")
    freqs = rope.real_frequencies(8)
    out = rope.apply_rope_d([1, 0, 1, 0, 1, 0, 1, 0], 2, freqs)
    expected = [-0.4161, 0.9093, 0.9801, 0.1987, 0.9998, 0.0200, 1.0000, 0.0020]
    assert out == [approx(e, abs=1e-3) for e in expected]


def test_rope_real_preserves_length(mod):
    rope = mod("rope")
    freqs = rope.real_frequencies(8)
    x = [3, 1, -2, 5, 0.5, -1, 2, 2]
    out = rope.apply_rope_d(x, 7, freqs)
    # 5.4 保长度在 d 维依然成立：只改方向、不改长度
    assert sum(v * v for v in out) ** 0.5 == approx(sum(v * v for v in x) ** 0.5)


def test_rope_real_reduces_to_2d(mod):
    # d=2 时真实版退化为玩具版：同一个旋转，只是弧度制换角度制
    rope = mod("rope")
    v = [3, 4]
    m, theta = 5, 0.3
    real = rope.apply_rope_d(v, m, [theta])
    toy = rope.rotate_2d(v, math.degrees(m * theta))
    assert real == [approx(toy[0]), approx(toy[1])]


def test_rope_real_score_depends_only_on_relative_position(mod):
    rope = mod("rope")
    x = [1, 0, 1, 0, 1, 0, 1, 0]
    freqs = rope.real_frequencies(8)

    def score(m, n):
        return rope.rope_score_d(x, x, m, n, freqs)

    # 两组绝对位置不同、相对距离都是 -3：分数一字不差（5.8.5 的验证）
    assert score(2, 5) == approx(score(10, 13))
    # 具体值：同词时分数 = Σcos((m-n)·θ_i) = 1.9649...
    assert score(2, 5) == approx(1.9649, abs=1e-3)
    # 相对距离不同，分数不同
    assert score(0, 0) != approx(score(0, 1))
