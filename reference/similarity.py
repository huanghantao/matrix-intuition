"""Week 5 · 相似度。

用 Day 1 写好的点积（proj 模块）拼出"两个向量有多像"的度量。
"""

from . import proj


def cosine_similarity(u: list, v: list) -> float:
    """余弦相似度 = 夹角的余弦 = u·v / (|u||v|)。

    取值范围 [-1, 1]：1 = 同向，0 = 垂直（无关），-1 = 反向。
    它只关心"方向像不像"，不关心长度——这正是 embedding 相似度的度量。
    """
    return proj.dot(u, v) / (proj.norm(u) * proj.norm(v))


def nearest_index(query: list, vectors: list) -> int:
    """在 vectors 里找出与 query 余弦相似度最高的那个向量的下标。

    这就是"在一堆词向量里找最相关的词"的最小实现。
    """
    best_i = -1
    best_s = -2.0  # 余弦相似度最小是 -1，初始值必须比它还小
    for i, v in enumerate(vectors):
        s = cosine_similarity(query, v)
        if s > best_s:
            best_s = s
            best_i = i
    return best_i
