"""Week 8 · 数值梯度：不求导公式，直接"捅一捅"函数。

神经网络参数成千上万，手动求导不现实；但"变化率"本身很好测：
把某个参数左右各挪一点点，看函数值的变化。这就是数值梯度，
也是检查反向传播是否写对的标准工具。
"""


def numerical_gradient(f, x: list, eps: float = 1e-6) -> list:
    """用中心差分近似 f 在 x 处的梯度（各个偏导数组成的向量）。

    想法：想求 f 关于 x[i] 的变化率，就把 x[i] 左右各挪 eps，
    用 (f(x+eps) - f(x-eps)) / (2*eps) 近似。挪得越小越准。
    """
    n = len(x)
    grad = [0.0] * n
    for i in range(n):
        xp = x[:]
        xm = x[:]
        xp[i] += eps
        xm[i] -= eps
        grad[i] = (f(xp) - f(xm)) / (2 * eps)
    return grad
