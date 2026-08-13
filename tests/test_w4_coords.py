"""Week 4 · 矩阵 = 坐标系的测试。"""

from pytest import approx, raises


def test_determinant_is_area(mod):
    coords = mod("coords")
    assert coords.determinant_2x2([[2, 0], [0, 3]]) == approx(6)     # 2×3 矩形
    assert coords.determinant_2x2([[1, 0], [0, 1]]) == approx(1)     # 单位正方形
    assert coords.determinant_2x2([[0, 1], [1, 0]]) == approx(-1)    # 负号 = 翻转了


def test_inverse_undoes(mod):
    coords = mod("coords")
    M = [[2, 0], [0, 3]]
    M_inv = coords.inverse_2x2(M)
    assert M_inv[0][0] == approx(0.5)
    assert M_inv[1][1] == approx(1 / 3)


def test_inverse_roundtrip(mod):
    coords = mod("coords")
    mat = mod("mat")
    M = [[2, 1], [1, 3]]
    M_inv = coords.inverse_2x2(M)
    I = mat.matmul(M, M_inv)
    assert I[0][0] == approx(1)
    assert I[0][1] == approx(0)
    assert I[1][0] == approx(0)
    assert I[1][1] == approx(1)


def test_inverse_singular(mod):
    coords = mod("coords")
    # 两列共线：行列式为 0，把平面压成了一条线，没法撤销
    with raises(ValueError):
        coords.inverse_2x2([[1, 2], [2, 4]])


def test_two_readings_of_Mv(mod):
    coords = mod("coords")
    M = [[2, 0], [0, 3]]
    # 读法 2：M 尺子里读数 (1,1) → 标准尺子读数 (2,3)
    assert coords.to_standard(M, [1, 1]) == [2, 3]
    # 反过来：标准 (2,3) → M 尺子 (1,1)
    assert coords.to_basis(M, [2, 3]) == [approx(1), approx(1)]


def test_basis_roundtrip_skew(mod):
    coords = mod("coords")
    M = [[1, 1], [0, 1]]  # 斜尺子：y 轴向右歪
    w = coords.to_standard(M, [1, 2])
    assert w == [3, 2]
    back = coords.to_basis(M, w)
    assert back == [approx(1), approx(2)]


def test_similarity_photo(mod):
    coords = mod("coords")
    mat = mod("mat")
    # 变换 B = 旋转 90°；P = 把 x 轴拉长 2 倍的新尺子
    B = mat.rotation_matrix(90)
    P = [[2, 0], [0, 1]]
    A = coords.similar_photo(P, B)          # B 在新尺子下的"照片"
    assert coords.is_same_transform(A, B, P)
    # 换一套尺子（P 不同），照片也不同
    assert not coords.is_same_transform(A, B, [[1, 0], [0, 1]])


def test_similarity_means_same_effect(mod):
    coords = mod("coords")
    mat = mod("mat")
    # "照片"A 的含义：在 P 尺子里读数为 u 的点，变换后在 P 尺子里的读数。
    # 老路：换到标准尺子 → 施加 B → 换回 P 尺子读数；
    # 新路：直接用"照片"A 在 P 尺子里变换。两条路结果相同。
    B = mat.rotation_matrix(90)
    P = [[2, 0], [0, 1]]
    A = coords.similar_photo(P, B)
    u = [1, 1]                        # P 尺子里的一个点
    via_B = coords.to_basis(P, mat.matvec(B, coords.to_standard(P, u)))
    via_A = mat.matvec(A, u)
    assert via_A == [approx(via_B[0]), approx(via_B[1])]
