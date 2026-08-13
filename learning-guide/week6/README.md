# 🚀 Week 6：手写迷你 Attention —— 把前五周全部串起来

> **适合谁：** 已经跟着课程走完 Week 1–Week 5 的你。会解二元一次方程、会写 Python 函数和类、会用 `pytest`，手里攒着五件"数学工具"的人。
>
> **本周定位：** 这是**全课程最核心的一周**。前五周每一周都憋着一股劲，就是为了这周的那一个公式——Transformer 里的 Attention。学完这周，你要能**脱稿、逐项**讲出 Attention 公式里每一个符号的含义：它为什么长这样、每一步用了前五周的哪一块积木。
>
> **承诺：** 不引入任何你没见过的新数学（唯一的"新东西" softmax 其实只是"取指数再归一化"），一行一行把你亲眼看到的公式拆开，最后亲手写一个能跑的迷你 Attention 和 RoPE。

---

## 📖 怎么用这套教程

1. **按顺序读，别跳。** 六天是一条完整的因果链：Day 1 提出问题 → Day 2 拆成三步 → Day 3 把分数变权重 → Day 4 亲手组装 → Day 5 补上位置 → Day 6 串起来看全局。
2. **边读边动手。** 看到"请这样写代码"，就真的去 `matrixlab/attention.py` 和 `matrixlab/rope.py` 里写。
3. **每写完一块就跑测试。** 绿了再往下走。
4. **卡住超过 20 分钟，去看参考答案**（`reference/attention.py`、`reference/rope.py` 里的同名函数），看懂后**自己重写一遍**。

---

## 📚 目录

| 章节 | 标题 | 内容 |
|---|---|---|
| Day 1 | [Attention 要解决的问题](./01-Day1-Attention要解决的问题.md) | 翻译"我/爱/吃/苹果"时"吃"该看谁；每个词都要学会按重要程度汇总整句话 |
| Day 2 | [Q、K、V 逐项拆解](./02-Day2-QKV逐项拆解-三个变换三种角色.md) | 三个变换三种角色；公式三步：点积 $\to$ softmax $\to$ 加权求和 |
| Day 3 | [softmax：把分数变成百分比](./03-Day3-softmax-把分数变成百分比.md) | 为什么需要归一化；指数的作用；数值技巧；实现 softmax |
| Day 4 | [代码实战：MiniAttention](./04-Day4-代码实战-MiniAttention.md) | 完整实现四个函数 + sqrt(d) 缩放；6 词热力图逐格解读 |
| Day 5 | [RoPE：用旋转矩阵给词排队](./05-Day5-RoPE-用旋转矩阵给词排队.md) | 重点章：位置信息藏进夹角，分数只依赖相对位置 |
| Day 6 | [可视化与大串讲：Attention 热力图](./06-Day6-可视化与大串讲-Attention热力图.md) | 回顾五周地图，逐行对照 Attention；多头一句话；预告 Week 8 |

---

## 🗺️ 一张图看懂本周要造什么

![QKV 流水线：三个变换、三步公式](../../figures/out/w6d2_qkv.png)

看懂这张图，本周就拿下一半了。它的读法一句话：**每个词先过三个变换（Week 3 的旋转/拉伸那种"空间运动"）变成 Q、K、V；Q 和 K 做点积（Week 5 的亲密度）得到分数；softmax 把分数变成百分比；最后把这些百分比当"配方"，把 V 们线性组合（Week 2）起来，得到每个词"吸收了上下文之后"的新向量。**

五周的工具在这里全部登场，一个不多、一个不少。

---

## ✅ 学完你会得到什么

- 一个**你自己从零写的**迷你 Attention：给一堆 2D 词向量，它就能算出"每个词该看谁、看多重"，输出融合了上下文的新向量。
- 一个**你自己从零写的** RoPE：只用"旋转矩阵"，就给一串词注入了位置信息，而且分数只和**相对位置**有关。
- 对 Attention 公式里每个符号（Q、K、V、$QK^T$、$\mathrm{softmax}$、$\sqrt{d}$、加权求和）**透彻、可脱稿讲解**的理解——这是学 LLM 底层绕不开的第一道坎，你跨过去了。
- 一张通往 Week 8 大结业（attention 机制在整张神经网络里的位置）的门票。

---

## 🧭 常用命令速查

```bash
# 看起点：参考答案全绿（见证终点长什么样）
IMPL=reference pytest tests -k w6 -q

# 看现状：你还没写，全是 TODO（红）
pytest tests -k w6 -q

# 写完 attention 相关函数后，单独跑注意力那部分
pytest tests -k w6_attention -q

# 写完 RoPE 相关函数后，单独跑 RoPE 那部分
pytest tests -k rope -q

# 跑本周全部测试
pytest tests -k w6 -q
```

> 环境变量 `IMPL` 决定测试"考谁"：`IMPL=reference` 考参考答案（应该全绿），`IMPL=matrixlab`（默认）考你自己写的代码。这是 Week 1 第 3 章就定下的规矩。
>
> 卡住时，参考答案在 `reference/` 里和你编辑的文件**同名**：`reference/attention.py`、`reference/rope.py`。

---

👋 准备好了吗？从 **[Day 1：Attention 要解决的问题](./01-Day1-Attention要解决的问题.md)** 开始吧！
