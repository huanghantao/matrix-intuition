"""Week 3 · 矩阵与变换的测试。"""

from pytest import approx


def test_matvec_scale(mod):
    mat = mod("mat")
    M = mat.scale_matrix(2, 3)
    assert mat.matvec(M, [1, 1]) == [2, 3]
    assert mat.matvec(M, [-1, 2]) == [-2, 6]


def test_matvec_rotation_90(mod):
    mat = mod("mat")
    R = mat.rotation_matrix(90)
    assert mat.matvec(R, [1, 0]) == [approx(0), approx(1)]   # 东 → 北
    assert mat.matvec(R, [0, 1]) == [approx(-1), approx(0)]  # 北 → 西


def test_matvec_shear(mod):
    mat = mod("mat")
    S = mat.shear_matrix(1)
    assert mat.matvec(S, [0, 1]) == [1, 1]   # y 越高，x 被推得越远
    assert mat.matvec(S, [3, 0]) == [3, 0]   # y=0 的向量纹丝不动


def test_matmul_is_composition(mod):
    mat = mod("mat")
    # 先旋转 90° 再旋转 90° = 旋转 180°
    R90 = mat.rotation_matrix(90)
    R180 = mat.rotation_matrix(180)
    C = mat.matmul(R90, R90)
    for i in range(2):
        for j in range(2):
            assert C[i][j] == approx(R180[i][j])


def test_matmul_order_matters(mod):
    mat = mod("mat")
    # 先转 90° 再横向拉伸 2 倍 ≠ 先拉伸再旋转：穿衣服顺序不能换
    R = mat.rotation_matrix(90)
    S = mat.scale_matrix(2, 1)
    A = mat.matmul(S, R)
    B = mat.matmul(R, S)
    assert A != B
    # 检验具体效果：对 [1,0] 先转后拉 = (0,1)；先拉后转 = (0,2)
    assert mat.matvec(A, [1, 0]) == [approx(0), approx(1)]
    assert mat.matvec(B, [1, 0]) == [approx(0), approx(2)]


def test_identity_does_nothing(mod):
    mat = mod("mat")
    I = mat.identity(2)
    assert mat.matvec(I, [3, -7]) == [3, -7]
    A = mat.matmul(I, [[1, 2], [3, 4]])
    assert A == [[1, 2], [3, 4]]
    B = mat.matmul([[1, 2], [3, 4]], I)
    assert B == [[1, 2], [3, 4]]


def test_transpose(mod):
    mat = mod("mat")
    assert mat.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    # 转置两次回到原样
    M = [[1, 2], [3, 4]]
    assert mat.transpose(mat.transpose(M)) == M


def test_apply_to_points(mod):
    mat = mod("mat")
    square = [[0, 0], [1, 0], [1, 1], [0, 1]]  # 单位正方形
    M = mat.scale_matrix(2, 3)
    out = mat.apply_to_points(M, square)
    assert out == [[0, 0], [2, 0], [2, 3], [0, 3]]
