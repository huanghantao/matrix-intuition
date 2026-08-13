"""Week 4 · 矩阵 = 坐标系（战场版：函数体待你实现）。"""


def determinant_2x2(M: list) -> float:
    """2x2 行列式 = 两列向量围成的平行四边形"有向面积"。"""
    raise NotImplementedError("TODO: Week 4 Day 3 —— 行列式")


def inverse_2x2(M: list) -> list:
    """2x2 逆矩阵：把 M 的变换原样撤销。"""
    raise NotImplementedError("TODO: Week 4 Day 3 —— 逆矩阵")


def to_standard(M: list, v: list) -> list:
    """在 M 坐标系里读数为 v 的向量，标准坐标系里的读数 = Mv。"""
    raise NotImplementedError("TODO: Week 4 Day 4 —— 换到标准尺子")


def to_basis(M: list, w: list) -> list:
    """标准坐标系里的向量 w，在 M 坐标系里的读数 = M⁻¹w。"""
    raise NotImplementedError("TODO: Week 4 Day 4 —— 换到 M 尺子")


def similar_photo(P: list, B: list) -> list:
    """变换 B 在 P 坐标系下的"照片" = P⁻¹ B P。"""
    raise NotImplementedError("TODO: Week 4 Day 5 —— 相似矩阵")


def is_same_transform(A: list, B: list, P: list, eps: float = 1e-9) -> bool:
    """判断 A 是不是变换 B 在 P 坐标系下的照片（A = P⁻¹BP）。"""
    raise NotImplementedError("TODO: Week 4 Day 5 —— 相似矩阵判定")
