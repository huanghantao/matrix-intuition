"""Week 2 · 解二元一次方程组（换基器的核心）。

给定基向量 b1、b2 和一个向量 v，求系数 (s, t) 使得 v = s*b1 + t*b2，
这就是"同一支箭头在新尺子下的坐标"。
"""


def solve_2x2(a: float, b: float, c: float, d: float, e: float, f: float):
    """解二元一次方程组：

        a*x + b*y = e
        c*x + d*y = f

    返回 (x, y)；没有唯一解时抛出 ValueError。

    思路 = 初中的加减消元法：让两个式子里 x 的系数相同，相减消掉 x。
    """
    eps = 1e-12
    if abs(a) < eps and abs(c) < eps:
        # 两个式子里都没有 x：x 想取多少取多少，没有唯一解
        raise ValueError("没有唯一解：x 的系数全为 0")
    if abs(a) < eps:
        # 第一个式子没有 x，把两个式子交换一下（选主元）
        a, b, c, d = c, d, a, b
        e, f = f, e
    det = a * d - b * c
    if abs(det) < eps:
        # 两直线平行（或重合）：没有唯一交点
        raise ValueError("没有唯一解：两直线平行或重合")
    # 第一式乘 c，第二式乘 a：
    #   a*c*x + b*c*y = e*c
    #   a*c*x + a*d*y = a*f
    # 相减消去 x：(b*c - a*d) * y = e*c - a*f
    y = (a * f - e * c) / det
    x = (e - b * y) / a  # 回代
    return (x, y)


def coordinates_in_basis(b1: list, b2: list, v: list):
    """在基 (b1, b2) 下表示向量 v，返回系数 (s, t)，满足 v = s*b1 + t*b2。

    几何上：新尺子的两根刻度轴是 b1、b2，v 是这支箭头在旧尺子下的坐标；
    解出来的 s、t 就是它在"新尺子"下的读数。
    """
    return solve_2x2(b1[0], b2[0], b1[1], b2[1], v[0], v[1])
