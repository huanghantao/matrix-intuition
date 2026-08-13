# Day 4：代码实战——MiniAttention：随机词向量上的注意力

> 本章你将：
> 1. 亲手实现完整的迷你 Attention：`attention_scores` / `attention_weights` / `weighted_sum` / `attention`；
> 2. 看懂并理解 `attention` 里的 **sqrt(d) 缩放**，以及"为什么除以 √d"；
> 3. 跑 `pytest tests -k w6_attention` 到全绿；
> 4. 读懂那张 6 个玩具词的热力图：行和 = 1、对角最大。

---

## 4.0 今天的任务清单

昨天公式三步，今天把每一笔都写成 Python。你的战场 `matrixlab/attention.py` 里有四个待实现的函数：

| 函数 | 对应公式 | 对应周数 |
|---|---|---|
| `attention_scores(Q, K)` | scores = Q·K^T | Week 5 点积 |
| `attention_weights(scores)` | weights = softmax(逐行) | Day 3 |
| `weighted_sum(weights, values)` | out = Σ w·V | Week 2 线性组合 |
| `attention(Q, K, V, scale)` | 三步串联 + 缩放 | 综合 |

`softmax` 昨天已经写好了，今天用到它。我们按"从下到上"的顺序实现：先把三个零件函数写出来，再拼成 `attention`。

> 所有函数都操作**纯 Python 的 list 嵌套 list**（不是 numpy）。这里的 Q、K、V 是"词向量列表的列表"，例如一个 2 维词向量就是 `[0.5, -0.3]`。

---

## 4.1 attention_scores：一堆点积铺成一张表

回忆公式第一步 `scores[i][j] = dot(Q[i], K[j])`。做法就是两层循环，把每对 (i, j) 的点积填进表格：

```python
def attention_scores(Q: list, K: list) -> list:
    n = len(Q)        # Q 里有几个"查询"（n 个词）
    m = len(K)        # K 里有几个"键"（m 个词，本例 n == m）
    scores = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            scores[i][j] = proj.dot(Q[i], K[j])   # Week 5 的点积
    return scores
```

注意它 import 的是 Week 5 你写好的 `proj.dot`（文件顶部已有 `from . import proj`）。这一行 `proj.dot(Q[i], K[j])` 就是整个"亲密度"的全部数学。

> 💡 你可能会问：为什么 scores 是方阵、而且第 i 行第 j 列是"i 看 j"而不是"j 看 i"？
>
> 约定上，**行是"查询者"、列是"被关注者"**。第 i 行 = "第 i 个词在看谁"；第 j 列 = "第 j 个词被谁看"。后面读热力图时这个"行看列"的约定会反复用到。

---

## 4.2 attention_weights：逐行 softmax

公式第二步 `weights = softmax(scores)`，是对**每一行**独立做 softmax（一个词的注意力总和只能自己凑成 1，不能跟别的行混）：

```python
def attention_weights(scores: list) -> list:
    return [softmax(row) for row in scores]
```

一行就是"一个词看整句话的注意力分配方案"。对每一行调用昨天写的 `softmax` 即可。

---

## 4.3 weighted_sum：线性组合

公式第三步 `out = Σ_j w[j]·V[j]`。参数 `values` 是若干词向量（每个是 list），`weights` 是一行权重：

```python
def weighted_sum(weights: list, values: list) -> list:
    n = len(values[0])          # 每个词向量的维度（本例是 2）
    result = [0.0] * n
    for w, v in zip(weights, values):
        for i in range(n):
            result[i] += w * v[i]
    return result
```

外层循环把每个词向量 `v` 按权重 `w` 伸缩后累加进 `result`——每一维都是所有词的"该维分量 × 权重"的和。这正是 Week 2 的"伸缩再相加"：**权重是配方，V 是原料，结果是一杯调好的新向量。**

---

## 4.4 attention：三步串联 + sqrt(d) 缩放

最后拼起来。但这里多了一个昨天没细讲的细节——**缩放**：

```python
def attention(Q: list, K: list, V: list, scale: float = None) -> list:
    d = len(Q[0])                            # 词向量的维度 d
    s = scale if scale is not None else math.sqrt(d)   # 默认 sqrt(d)
    scores = attention_scores(Q, K)          # ① 点积
    scaled = [[x / s for x in row] for row in scores]  # ② 缩放（除以 sqrt(d)）
    weights = attention_weights(scaled)      # ③ softmax
    return [weighted_sum(w, V) for w in weights]        # ④ 加权求和
```

### 为什么除以 sqrt(d)？

这是论文里著名的"缩放点积注意力"里的那个"缩放"。直觉是这样的：

- 点积 = 各维分量乘积之和。维度 d 越大，这一长串加出来的数**天然就越大**（每多一维，都可能再贡献一截）；
- 分数一大，过了 softmax 的指数层，差距会被**过度放大**，权重几乎全压到最高分的那个词上、其余趋近 0——注意力就"太尖"了；
- 除以 `sqrt(d)`（d 的平方根）能把分数大致"压回正常量级"，让权重分布温和、不至于退化。

> 💡 你可能会问：为什么是 √d 而不是 d？
>
> 这是统计学里的方差归一化结果（点积的波动随 d 的平方根增长，除 √d 正好抵消）。你不需要追究推导，只要记住两个要点：①这是**缩放**，让分数别随维度膨胀；②默认值是 `sqrt(d)`，公式里写作"除以 √d"。测试里 `test_attention_full` 用的就是默认 `sqrt(2)`。

> 📌 划重点：`attention` = 点积 → **除以 sqrt(d)** → softmax → 加权求和。缩放系数默认 `sqrt(d)`，是防止维度大了分数爆炸、权重过尖。

---

## 4.5 跑测试到绿

四个函数都写完后，跑：

```bash
pytest tests -k w6_attention -q
```

（`-k w6_attention` 只测注意力那部分，把 RoPE 的测试排除在外——那些是明天的。）全部通过会看到像这样的输出：

```
...............                                              [100%]
9 passed, 6 deselected in 0.15s
```

> 当然，也可以用 `IMPL=reference pytest tests -k w6_attention -q` 先看一遍参考答案的正确输出，再回自己代码跑到同样全绿。这正是 Week 1 第 3 章说的"先见证终点"的老办法。

这几条测试在替你验证什么，逐条对一遍：

| 测试 | 它在盯什么 |
|---|---|
| `test_attention_scores_are_dot_products` | scores 的每个格子是不是真的等于点积 |
| `test_attention_weights_rows_sum_to_one` | 每行权重和是否 = 1 |
| `test_weighted_sum_is_linear_combination` | 加权求和是不是线性组合（权重 [0.25,0.75] → [0.5,1.5]） |
| `test_attention_full` | 完整 attention 的数值（默认 sqrt(2) 缩放） |
| `test_attention_ignores_scale_flag` | V 全相同时，不管权重如何，输出恒等于那个 V |

---

## 4.6 读热力图：6 个玩具词

现在看看你做出来的机器，在 6 个随机词向量上会画出什么。下图是用"我 / 爱 / 吃 / 苹果 / ，/ 很甜"六个词、各自随机的 2 维向量算出来的（数据源见 `figures/gen_w6d4_attention_heatmap.py`）：

![6 个玩具词的注意力热力图：左分数、右权重](../../figures/out/w6d4_attention_heatmap.png)

**左图**是原始分数 `scores`（未归一化、未缩放前的点积；为讲清楚，脚本直接用了 `attention_scores`）；**右图**是 `weights`（对每行 softmax 之后）。读图抓三个要点：

1. **对角线最亮**：一个词和自己做点积（自己点自己 = 长度的平方）天然最大，所以 "我"看"我"、"爱"看"爱"…都是该行最亮的那格。这就是 Day 1 说的"随机词向量下，每个词最关注自己"。
2. **每行和 = 1**：右图把第 1 行加一下（用右图每格的数字），恰好等于 1.00；每一行都如此。这是 softmax 的功劳。
3. **行 ≠ 列**：第 i 行是该词"看别人"的方案，第 j 列是该词"被别人看"的关注度。由于分数是点积、而 Q·K 在这个玩具里就是 X·X（没做 QKV 变换），分数矩阵是对称的（scores[i][j] == scores[j][i]），所以左右两图沿对角线对称。

> 💡 你可能会问：既然是随机向量，为什么还能"对角大"？
>
> 因为"自己点自己"是两个相同方向的向量求点积，等于长度的平方，永远非负且通常不小；而"两个随机向量点积"可能是正、可能负、也可能接近 0。所以对角线天然突出。这正是"自相似度最高"的体现。

> ⚠️ 易踩坑：这张玩具热力图**没有位置信息、也没做 QKV 变换**，所以它并不能体现"吃→苹果"这种语义关联——它只演示机制运转正常（行和=1、对角大）。要看到"吃关注苹果"那种漂亮模式，得等词向量先学会语义、再配上明天（Day 5）的位置编码。

---

## 4.7 一个完整跑法：在 Python 里亲手调一把

不用 pytest 也能体验。新建一个临时 `python -c` 或交互式脚本，喂几组数据：

```python
from matrixlab.attention import attention  # 或 reference.attention
Q = [[1, 0]]
K = [[1, 0], [0, 1]]
V = [[2, 0], [0, 2]]
print(attention(Q, K, V))   # 默认 scale=sqrt(2)
```

这个例子正是 `test_attention_full` 用的：Q 只有一个查询 [1,0]，它和 K[0]=[1,0] 的点积是 1、和 K[1]=[0,1] 的点积是 0，所以分数 [1,0] 缩放后大头给了 V[0]=[2,0]，输出接近 [2,0]（略偏向 [2,0]，因为 softmax 后第二个也有点权重）。跑一下，看输出是不是靠近 `[[2, 0]]`。

---

## 4.8 本章小结

- ✅ 三个零件函数一一对应公式三步：scores=点积、weights=softmax 逐行、weighted_sum=线性组合。
- ✅ `attention` 把它们串起来，并在 softmax 前**除以 sqrt(d)** 缩放，默认 scale=sqrt(d)。
- ✅ 跑 `pytest tests -k w6_attention` 到 9 个全绿。
- ✅ 热力图三要点：对角最亮（自相似最高）、每行和 = 1（softmax）、分数矩阵对称（本例没做 QKV 变换）。

---

## 动手练习

1. **代码**：实现 `matrixlab/attention.py` 的四个函数，跑 `pytest tests -k w6_attention -q` 全绿。
2. **纸面验证缩放**：d=4 时 scale 默认是多少？如果把 `attention(Q,K,V, scale=1)` 传入 scale=1，和不传有何区别？（答案见提示。）
3. **读图**：回到 4.6 的热力图右半，挑"吃"那一行，指出它给"苹果"的权重，并验证这一行全加起来 ≈ 1。

## 参考答案

1. 见 `reference/attention.py`（四个函数都在，与 4.1~4.4 基本一致）。
2. scale 默认 `sqrt(4) = 2`；传 `scale=1` 就是"不缩放"，分数原样进 softmax，权重会更尖（区分更极端）。
3. "吃"那行的权重读右图每格数字即可，求和应 = 1.00（允许浮点尾巴误差）。

卡住 20 分钟再看 `reference/attention.py`。

---

## 📌 AI 联系

你现在拥有的是一个**功能完整、可逐行讲解**的单头注意力。真实的 Transformer 里，这一步（点积→缩放→softmax→加权求和）被重复成千上万次：每一层、每一个头、每一个位置都做一遍。你手里这 30 行，就是那庞然大物最小的、可运行的"细胞"。

---

👉 迷你 Attention 跑通了。但它有个致命缺陷——**根本不知道词的先后顺序**。下一步，去 **[Day 5：RoPE——用旋转矩阵给词排队](./05-Day5-RoPE-用旋转矩阵给词排队.md)**，用 Week 3 的旋转矩阵补上"位置"这块拼图。
