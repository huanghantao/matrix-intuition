"""Week 6 · 注意力机制的测试。"""

from pytest import approx


def test_softmax_sums_to_one(mod):
    attn = mod("attention")
    w = attn.softmax([1, 2, 3])
    assert sum(w) == approx(1)
    w = attn.softmax([-5, 0, 5, 10])
    assert sum(w) == approx(1)


def test_softmax_order_preserved(mod):
    attn = mod("attention")
    w = attn.softmax([1, 2, 3])
    assert w[0] < w[1] < w[2]  # 分数越大权重越大


def test_softmax_shift_invariance(mod):
    attn = mod("attention")
    # 全体加同一个数，结果不变（所以实现里先减最大值）
    assert attn.softmax([100, 101]) == [approx(x) for x in attn.softmax([0, 1])]


def test_softmax_values(mod):
    attn = mod("attention")
    # softmax([1,2]) = [e/(e+e²), e²/(e+e²)] = [1/(1+e), e/(1+e)]
    w = attn.softmax([1, 2])
    assert w[0] == approx(1 / (1 + 2.718281828459045))
    assert w[1] == approx(2.718281828459045 / (1 + 2.718281828459045))


def test_attention_scores_are_dot_products(mod):
    attn = mod("attention")
    proj = mod("proj")
    Q = [[1, 0], [0, 1]]
    K = [[1, 0], [1, 1]]
    scores = attn.attention_scores(Q, K)
    assert scores[0][0] == approx(proj.dot(Q[0], K[0]))
    assert scores[1][1] == approx(proj.dot(Q[1], K[1]))


def test_attention_weights_rows_sum_to_one(mod):
    attn = mod("attention")
    scores = [[1, 2], [3, 4]]
    weights = attn.attention_weights(scores)
    for row in weights:
        assert sum(row) == approx(1)


def test_weighted_sum_is_linear_combination(mod):
    attn = mod("attention")
    out = attn.weighted_sum([0.25, 0.75], [[2, 0], [0, 2]])
    assert out == [approx(0.5), approx(1.5)]
    # 权重 (1, 0)：完全只看第一个 value
    out = attn.weighted_sum([1, 0], [[2, 0], [0, 2]])
    assert out == [approx(2), approx(0)]


def test_attention_full(mod):
    attn = mod("attention")
    Q = [[1, 0]]
    K = [[1, 0], [0, 1]]
    V = [[2, 0], [0, 2]]
    out = attn.attention(Q, K, V)  # 默认缩放 sqrt(2)
    # 分数 [1, 0] / √2 = [0.7071, 0]，softmax 后大头在第一个 value
    e = 2.718281828459045
    s = 0.7071067811865476
    w0 = (e ** s) / (e ** s + 1)
    w1 = 1 - w0
    assert out[0][0] == approx(w0 * 2)
    assert out[0][1] == approx(w1 * 2)


def test_attention_ignores_scale_flag(mod):
    attn = mod("attention")
    Q = [[1, 0]]
    K = [[1, 0], [0, 1]]
    V = [[1, 1], [1, 1]]
    # 不管权重怎么分配，V 都一样时，输出就是 [1,1]（权重和为 1）
    out = attn.attention(Q, K, V)
    assert out[0] == [approx(1), approx(1)]
