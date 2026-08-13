# 课程大纲与写作说明书（给教程子 agent 的作业手册）

> 本文档是《理解矩阵：面向 LLM 的直觉之旅》的**总纲**。每周由一个独立的子 agent 负责撰写，
> 请严格遵守本文档的约定，保证 8 周风格一致、章节之间严丝合缝。

---

## 1. 读者画像（写作前必读）

- **数学基础：初中水平。** 会解一元一次/二元一次方程（加减消元法），知道勾股定理；函数、三角、微积分**全都没学过**。教程必须从数轴、坐标讲起，任何超出初中的概念（sin/cos 除外，课程内教）都要先用生活类比建立直觉，再给定义。
- **Python：比较熟。** 类、模块、pip 都会，但 **numpy/matplotlib 没怎么用过**（Week 1 第 3 章教）。代码可以放心用函数和类。
- **学习动机：学 LLM 底层。** 卡在 word embedding、attention、前向/反向传播、梯度下降。**每个数学概念都要接一个 AI 落地点**。
- **每周投入 7 小时以上**，每章可以写长、配练习。
- **结业目标**（第 8 周大结业围绕它们设计）：
  1. 看懂 Transformer 里的矩阵公式（attention、QKV 投影、softmax、RoPE）；
  2. 理解 embedding 空间（相似度、国王-男人+女人≈女王）；
  3. 能手推/手写一个小网络的一次前向 + 反向 + 梯度更新。
- **主线哲学**（源自孟岩《理解矩阵》，原文在 `material/理解矩阵.txt`，写作时可引用其比喻）：
  - 矩阵是线性空间里**变换（运动）的描述**；
  - 换一组基，同一个变换有不同"照片"（相似矩阵）；
  - **对象的变换等价于坐标系的变换**（运动是相对的）；
  - 矩阵乘法规则不是瞎规定，而是"连续施加两个变换"的必然结果。

## 2. 仓库布局（写章节时引用的路径）

```
matrix-intuition/
├── learning-guide/weekN/   ← 你写的东西在这里（教程正文）
├── matrixlab/              ← 读者的战场：函数体 raise NotImplementedError("TODO")，读者自己填
├── reference/              ← 参考答案：完整实现（写作时以它为准，代码已定稿、已通过测试）
├── tests/                  ← 测试（已定稿：91 个测试，reference 全绿）
├── figures/gen_*.py        ← 生图脚本（已定稿，图片已生成在 figures/out/）
├── figures/out/*.png       ← 教程里引用的图片
└── material/理解矩阵.txt    ← 孟岩原文（转存）
```

**代码与测试已经全部定稿并验证通过，子 agent 只写教程，不要改代码、测试、图片脚本。**
如果发现代码确有 bug，在交付说明里报告，不要自行修改。

## 3. 写作风格（统一要求，模仿 miniloro）

参考项目 `~/codeDir/goCode/miniloro/learning-guide/`（尤其 `week1/README.md`、`week1/01-数学扫盲.md`）。
风格要点：

1. **口语化、说人话。** 像一位耐心的朋友在讲解。允许"你可能会想…""慢着！"这类对话感。
2. **每个概念：生活类比 → 图形直觉 → 严格定义 → 代码 → 验证。** 类比先行，定义殿后。
3. **多用表格**总结对比（如"两种读法对照表"）、多用编号步骤。
4. **固定盒子**（沿用 miniloro 的约定）：
   - `> 📌 AI 联系：`——本节数学概念在 LLM 里的落点；
   - `> 💡 你可能会问：`——预判读者困惑并解答；
   - `> ⚠️ 易踩坑：`——常见错误；
   - `> 📌 划重点：`——一句话总结本节。
5. **不许要求读者证明任何东西。** 只建立直觉；出现"证明留给有兴趣的读者"即可。
6. **数学公式用 LaTeX**（mdBook 已启用 MathJax 3，`theme/head.hbs`）：行内 `$...$`、独立行 `$$...$$`；等号对齐用 `$$ \begin{aligned} ... \end{aligned} $$`；矩阵用 `\begin{bmatrix}`；中文操作数用 `\text{...}` 包裹。**代码块（```python/```bash/命令输出）与行内代码中的内容绝不放 `$`。** 常用映射：×→`\times`、·→`\cdot`、≈→`\approx`、≠→`\neq`、→→`\to`、√→`\sqrt{}`、分数→`\frac{}{}`、下标 x₁→`x_1`、上标 x²→`x^2`、转置→`^T`。**⚠️ 公式内换行必须写 `\\\\`（四个反斜杠）**：mdBook 的 Markdown 渲染会吃掉一层反斜杠，写两个反斜杠 `\\` 会在网页上变成一行。可用 `python scripts/verify_latex.py` 检查全仓库规范。
7. **每章结尾固定小节**：
   - `## 动手练习`：1-3 个练习（写 `matrixlab/xxx.py` 里的函数 + 跑测试命令）；
   - `## 参考答案`：一句话指向 `reference/` 同名文件，提示"卡住 20 分钟再看"；
   - （AI 章节）`## 📌 AI 联系`：把本章直觉接到 LLM 部件。
8. 每章开头放一行 `> 本章你将：` 的导读，列出 3-5 个收获。

## 4. 图片政策（硬性要求）

- **凡涉及精确坐标、几何位置的图，一律用仓库里已生成的 PNG**，**禁止 ASCII 图**（容易错位误导）。
- 图片引用方式：章节在 `learning-guide/weekN/` 下，所以路径写作：
  `![配图说明](../../figures/out/w3d1_transforms.png)`
- 现有图片清单（`figures/out/`）：
  - w1d1_number_axis.png、w1d4_vector_add.png、w1d4_vector_scale.png、w1d5_color_vectors.png
  - w2d1_lincomb.png、w2d2_span.png、w2d3_two_bases.png
  - w3d1_transforms.png、w3d3_compose.png
  - w4d1_two_readings.png、w4d2_relative_motion.png、w4d6_pca_intuition.png
  - w5d1_dot_intuition.png、w5d4_embedding_scatter.png
  - w6d1_attention_problem.png、w6d2_qkv.png、w6d3_softmax.png、w6d4_attention_heatmap.png、w6d5_rope_rotation.png、w6d5_rope_scores.png
  - w7d1_two_lines.png、w7d3_fit_line.png、w7d5_eigen_directions.png
  - w8d1_slope.png、w8d4_chain.png、w8d5_gd_path.png、w8d6_decision_boundary.png、w8d7_map.png
- **每张图必须至少被一章引用一次**（上表对应章节会用到；写作时确认你的周内图都被引用）。
- 允许 ASCII 的唯一场景：**与坐标无关的纯文本示意**（如 JSON 结构、目录树、代码注释）。凡出现 x/y 轴、点、箭头、几何位置，一律用 PNG。
- 若某章确实需要新图：可以**新增** `figures/gen_wXdY_*.py` 脚本（模仿现有脚本：`sys.path.insert` 那三行开头、用 `figures._common` 的 `axes/vec/point/save`、中文字体已配置），运行生成 PNG 后引用；**生图脚本必须保留在仓库里**。新脚本务必实际运行成功再交付。

## 5. 章节文件命名（必须与 SUMMARY.md 完全一致）

`SUMMARY.md` 已经定死了每章的文件名（含中文），**一个字都不能差**。每周要写的文件清单见下面第 6 节。

## 6. 每周任务分派

### Week 1：从数到向量——坐标、箭头与第一个 AI 名词（⭐ 零基础可入）

文件（都在 `learning-guide/week1/`）：`README.md` + 6 章：

| 文件 | 主题与要点 |
|---|---|
| 00-总览-LLM的底层全是矩阵.md | 用 LLM 的真实片段（embedding 表、attention 公式 QK^T、一层网络 Wx+b）让读者"看见"矩阵无处不在；课程地图（8 周表）；怎么用本教程（战场/参考答案/测试三件套）；承诺"初中数学就够了" |
| 01-数轴与坐标-位置就是地址.md | 数轴=地址；平面坐标 (x,y)=两个地址；刻度、格点；图 w1d1_number_axis.png |
| 02-从点到箭头-向量是什么.md | 位移箭头；向量的两个要素（方向、长度）；用坐标表示向量；勾股定理算长度（初中已会，衔接）；图 w1d4_vector_add.png |
| 03-环境搭建-装好工具先见证奇迹.md | python 版本检查、pip install -r requirements.txt、venv（可选）；numpy 简介（为什么用：数表=数组）、matplotlib 简介；跑 `IMPL=reference pytest tests -k w1` 先看全绿（见证终点）；跑 `pytest tests -k w1` 看红（战场现状）；讲清楚 IMPL 环境变量机制 |
| 04-Day1-用代码画向量-加法与数乘.md | 打开 matrixlab/vec2d.py：make/add/sub/scale/neg/length/from_points 逐个实现（每个都给思路+手算例子）；加法=首尾相接、数乘=伸缩；跑 `pytest tests -k w1` 到绿；图 w1d4_vector_add.png（加法）+ w1d4_vector_scale.png（数乘，单独成图） |
| 05-Day2-AI联系-把词变成向量.md | 📌 AI 联系：词怎么变成数字——颜色三维向量（红绿蓝）举例：混合=向量加法；one-hot 一句话带过；"embedding 就是给每个词找坐标"；图 w1d5_color_vectors.png；预告 Week 2 的"配方" |

README.md 要求：本周定位（不碰矩阵，把箭头直觉建牢）、目录表（链接到 6 章）、"学完你会得到什么"、常用命令速查。风格照抄 miniloro week1/README.md。

### Week 2：线性组合与基——坐标的本质（⭐）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-伸缩再相加-线性组合.md | 线性组合=伸缩再相加；实现 combo.lincomb；2e1+3e2 手算；图 w2d1_lincomb.png；测试 test_w2_combo |
| 02-Day2-张成平面-两个向量能拼出整个世界吗.md | 张成（span）直觉：两个不共线向量铺满平面；共线时只能铺一条线（点出"线性相关/无关"直觉，不展开）；span_point；图 w2d2_span.png |
| 03-Day3-基就是坐标系-选谁当尺子.md | 基=一套尺子（两根不共线的刻度轴）；标准基 e1/e2；换一套尺子照样能度量一切；"基是坐标系不是坐标值" |
| 04-Day4-换尺子-同一向量在不同基下的坐标.md | "配方"问题：v=s·b1+t·b2 求 s,t → 二元一次方程组；加减消元法复习（初中方法，一步步写）；无解/无穷解对应共线；图 w2d3_two_bases.png |
| 05-Day5-代码实战-换基器与配方求解.md | 实现 solve2.solve_2x2（含换行处理）与 coordinates_in_basis；跑 `pytest tests -k w2`；用代码验证 roundtrip |
| 06-Day6-AI联系-embedding的坐标是语义配方.md | 📌 AI 联系：embedding 的每一维=一个"语义刻度"；词=各语义刻度的配方（线性组合视角）；"国王-男人+女人≈女王"首次亮相（放在向量加减语义上）；预告矩阵=变换 |

### Week 3：矩阵 = 变换——空间的运动（⭐⭐ 全课程地基）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-三个开胃变换-拉伸旋转剪切.md | 三个变换矩阵直观体验：scale/rotation/shear；**教 sin/cos**（单位圆定义，初中可懂）；rotation_matrix 各元素含义（(1,0) 转到哪、列向量解读）；图 w3d1_transforms.png |
| 02-Day2-矩阵乘向量-为什么这么算.md | 从"对 e1、e2 施加变换后坐标怎么变"推出矩阵×向量规则；实现 mat.matvec；手算 2-3 例；线性性质：M(u+v)=Mu+Mv（用"变换不扭曲网格"的直觉） |
| 03-Day3-矩阵乘矩阵-变换的复合与顺序.md | 连续施加两个变换；matmul 的"行×列"为什么这么规定；A@B=B 先动 A 后动；顺序不能换（穿衣类比）；I=什么都不做；图 w3d3_compose.png |
| 04-Day4-代码实战-手写矩阵乘法.md | 实现 matmul/transpose/identity/apply_to_points；跑 `pytest tests -k w3`；三重循环逐行讲解 |
| 05-Day5-AI联系-一层网络就是一次变换.md | 📌 AI 联系：Wx+b 就是变换+平移；QKV 投影 X·Wq 就是把每个词变换进"查询空间"；embedding 层=查表得到坐标 |
| 06-Day6-彩蛋-RoPE预告-旋转矩阵与位置.md | 旋转矩阵的用途预告：词向量按位置旋转不同角度 → 位置信息；"转 mθ 再转 -nθ = 转 (m-n)θ"（复合=角度相加）；预告 Week 6 Day 5 动手实现；图 w6d5_rope_rotation.png 可先看一眼（或留到 W6） |

### Week 4：矩阵 = 坐标系——变换的相对性（⭐⭐ 理解矩阵的核心周）

**写作前必读 `material/理解矩阵.txt` 第（三）部分**，本周是孟岩原著的灵魂，务必把他的"照片""尺子"比喻讲透。

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-矩阵的列是基向量-一个矩阵两种读法.md | 矩阵的列=变换后的 e1、e2=一组新基；非奇异方阵的列构成坐标系；一个矩阵两种读法（变换/坐标系）；图 w4d1_two_readings.png |
| 02-Day2-Ma等于b的双重解释-运动是相对的.md | Ma=b 两解：①点动：a 被变换成 b；②尺子动：在 M 尺子里读数为 a 的向量，标准尺子里读数是 b；"把 (1,1) 变到 (2,3)"的两种做法（孟岩原文的例子）；运动是相对的；图 w4d2_relative_motion.png |
| 03-Day3-逆矩阵-把坐标换回去.md | 逆矩阵=撤销变换/把读数换回标准尺子；2x2 求逆公式（先教 determinant_2x2=有向面积）；行列式为 0=把平面压扁无法撤销；实现 inverse_2x2 |
| 04-Day4-代码实战-坐标转换器与回程票.md | 实现 to_standard/to_basis（Mv 与 M⁻¹v）；roundtrip 测试；跑 `pytest tests -k w4`；斜尺子例子 |
| 05-Day5-相似矩阵-同一个变换的不同照片.md | 猪的照片比喻（孟岩原文）；A=P⁻¹BP：同一个变换 B 在 P 尺子下的照片；is_same_transform；"换基不换本质，只是拍得更美"；相似矩阵有相同本征值（一句话预告 Week 7，不展开） |
| 06-Day6-AI联系-换基就是换视角-PCA与归一化直觉.md | 📌 AI 联系：PCA=找一根"数据最分散"的新坐标轴（换基降维）；图 w4d6_pca_intuition.png；LayerNorm=统一尺子（缩放坐标）的一句话直觉 |

### Week 5：点积、长度与相似度——向量之间的"亲密度"（⭐⭐）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-点积-一个数度量两个方向的关系.md | 点积定义（对应相乘再相加）；几何意义 |u||v|cosθ（投影视角）；图 w5d1_dot_intuition.png；实现 proj.dot；正交=点积 0 |
| 02-Day2-长度夹角与投影-余弦是方向契合度.md | norm（n 维勾股）；投影（scalar/onto）；夹角公式；is_orthogonal/angle_deg；"余弦=方向契合度" |
| 03-Day3-高维空间-公式照搬直觉还在吗.md | 3 维、n 维：公式照抄；高维直觉靠"低维投影"理解；点积/夹角在高维依然成立（不证）；维度高低不影响直觉 |
| 04-Day4-代码实战-相似度计算器与最近邻.md | 实现 similarity.cosine_similarity 与 nearest_index（复用 proj）；跑 `pytest tests -k w5`；图 w5d4_embedding_scatter.png |
| 05-Day5-AI联系-embedding相似度就是夹角.md | 📌 AI 联系：embedding 相似度=余弦；为什么不用距离（长度常被"语气强度"污染）；attention 分数 QK^T=一堆点积，预告 Week 6 |

### Week 6：手写迷你 Attention——把前五周全部串起来（⭐⭐⭐ 最核心）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-Attention要解决的问题.md | 翻译"我/爱/吃/苹果"时"吃"该看谁；每个词都要学会按重要程度汇总上下文；图 w6d1_attention_problem.png |
| 02-Day2-QKV逐项拆解-三个变换三种角色.md | XWq/XWk/XWv（Week 3 变换）；Q=我在找谁、K=我是谁、V=我装了什么；图 w6d2_qkv.png；公式逐步拆：scores=QK^T、weights=softmax(scores)、out=weights·V |
| 03-Day3-softmax-把分数变成百分比.md | 为什么需要归一化；指数的作用（放大差距、保证正数）；数值技巧（减最大值）；实现 softmax；图 w6d3_softmax.png |
| 04-Day4-代码实战-MiniAttention.md | 实现 attention_scores/attention_weights/weighted_sum/attention（含 sqrt(d) 缩放）；逐段讲解；跑 `pytest tests -k w6`（不含 rope 部分也行）；图 w6d4_attention_heatmap.png |
| 05-Day5-RoPE-用旋转矩阵给词排队.md | **重点章**：attention 天然不知道顺序 → 需要位置；RoPE 思路=位置 m 的词向量转 mθ 度（Week 3 旋转矩阵）；"旋转复合=角度相加 + 点积只与夹角有关（Week 5）"推出 q_m·k_n 只依赖 (m-n)；旋转保长度；实现 rotate_2d/apply_rope_2d/rope_score；跑 `pytest tests -k rope`；真实 RoPE 的"维度两两配对、不同频率"一句话收尾；图 w6d5_rope_rotation.png、w6d5_rope_scores.png |
| 06-Day6-可视化与大串讲-Attention热力图.md | 回顾五周地图（向量→组合→变换→坐标系→点积→attention）；读热力图；多头的两句话（同一套机制开几个副本）；与 Week 8 预告 |

### Week 7：方程组、最小二乘与特征值——矩阵的三件"正事"（⭐⭐⭐）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-Ax等于b-已知输出和变换求输入.md | 方程组=逆问题；几何=直线/平面交点；图 w7d1_two_lines.png；与 Week 2 的 solve2 呼应（n 元推广） |
| 02-Day2-代码实战-高斯消元-从2元到n元.md | 加减消元的机械化：消元+回代；选主元（除零保护）；实现 gauss.solve_linear；跑 `pytest tests -k gauss`；3x3 手算一遍 |
| 03-Day3-超定方程组与最小二乘.md | 数据点比未知数多→一般无解；"最佳妥协"=误差平方和最小；法方程 (AᵀA)x=Aᵀy（推导只给思路：投影，不深证）；实现 lstsq.fit_line/predict/residual_sum；图 w7d3_fit_line.png |
| 04-Day4-特征值与特征向量-Ax等于λx.md | 定义：A 作用后方向不变的向量；直觉：找到矩阵的"主轴"；图 w7d5_eigen_directions.png；为什么叫"特征/本征" |
| 05-Day5-代码实战-幂迭代法与特征方向.md | 反复用 A 拽向量→自动转向最大特征方向；瑞利商；实现 eigen.power_iteration；跑 `pytest tests -k eigen`；与特征方程验收 |
| 06-Day6-AI联系-最小二乘就是拟合-线性回归与损失函数.md | 📌 AI 联系：线性回归=最小二乘；Σ(预测-实际)² 就是损失函数原型；从"拟合一条线"到"训练一个网络"只差一步（Week 8）；特征值在现代 AI 中的影子（谱、主成分）一句话 |

### Week 8：神经网络 = 一连串变换——大结业：从零训练一个小网络（⭐⭐⭐）

| 文件 | 主题与要点 |
|---|---|
| 01-Day1-导数扫盲-斜率变化率与下山的方向.md | 导数=变化率=切线斜率（初中直线斜率推广）；图 w8d1_slope.png；**数值梯度**（左右捅一捅）：实现 grad.numerical_gradient；跑 `pytest tests -k grad`；"梯度指向上升最快方向，反着走就下山" |
| 02-Day2-损失函数-用数衡量错得多离谱.md | 预测 vs 目标；MSE=Σ(预测-实际)²/N（接 Week 7 Day 6）；损失是参数的函数（参数一变损失就变）；实现 mse_loss；损失曲线长什么样 |
| 03-Day3-前向传播-复合变换的流水线.md | 网络=连环变换：x→W1x+b1→ReLU→W2·+b2；ReLU 是什么（开关）；形状追踪表（N×2 → N×4 → N×1 逐层写清楚）；numpy 版实现 forward（X@W1+b1 对应 Week 3 矩阵乘法）；图 w8d4_chain.png（前向部分） |
| 04-Day4-反向传播直觉-变化如何传回去.md | 链式法则=变化的传导（多米诺骨牌/接力棒类比）；给一个 2 神经元玩具**完整手算一遍**梯度；实现 backward 公式逐行讲解；用 Week 8 Day 1 的数值梯度抽查 backward（跑 `pytest tests -k nn` 里的梯度检验测试）；ReLU 导数=开关 |
| 05-Day5-梯度下降-一步一步滑下山.md | 参数 -= lr*梯度；学习率的意义（步子大小）；图 w8d5_gd_path.png；实现 sgd_step/train；跑 `pytest tests -k "training"` |
| 06-Day6-大结业-numpy训练两层网络.md | XOR 为什么单层搞不定（需要折线）；训练 3000 步看损失下降、四类全分对；决策边界与损失曲线（图 w8d6_decision_boundary.png）；验收测试 `pytest tests -k xor`；与 PyTorch 同款代码对照（可选彩蛋） |
| 07-Day7-结业总结-回望矩阵直觉地图.md | 8 周地图回顾（图 w8d7_map.png）；矩阵直觉清单（矩阵=变换=坐标系、运动相对、点积=相似度、特征向量=主轴、网络=一连串变换）；下一步怎么走（PyTorch、3Blue1Brown、源码阅读） |

### 各周 README.md 通用模板

每周 `README.md` 必须包含：`适合谁/本周定位/承诺` 引言、`目录` 表（链接本周末各章）、`一张图看懂本周`（可用一张 figures 图）、`学完你会得到什么`、`常用命令速查`（对应 `pytest tests -k wX`）。风格照抄 miniloro week1/README.md。

## 7. 交付清单（每个子 agent 必须做到）

1. 写完本周全部 `.md` 文件（`learning-guide/weekN/README.md` + 第 6 节列出的各章，**文件名与 SUMMARY.md 逐字一致**）。
2. 每个 AI 章节必须有 `📌 AI 联系` 小节；每个动手章节必须有"动手练习 + 跑测试命令 + 参考答案指引"。
3. 章节内所有代码/测试/图片引用都**真实存在**：图片路径 `../../figures/out/*.png` 必须存在；测试命令必须真能跑（子 agent 自行运行 `IMPL=reference pytest tests -k wX -q` 与 `python figures/gen_all.py` 验证，失败则报告）。
4. 若新增生图脚本：脚本必须实际运行成功，PNG 落盘到 `figures/out/`，并把脚本与图片路径写进交付报告。
5. 章节间互链用相对路径（`./03-Day3-....md`）。
6. 交付报告：列出写了哪些文件、引用了哪些图、跑了哪些验证命令及结果、有无新增图、对代码/图片脚本的 bug 报告（若有）。

## 8. 分周依赖提醒（写作时注意前后呼应）

- W1 结尾预告 W2；W2D6 预告"矩阵=变换"；W3D6 预告 RoPE（W6D5）；W4D5 预告特征值（W7D4）；W5D5 预告 attention（W6）；W6D6 预告 W8 大结业；W7D6 预告损失函数（W8D2）。
- 术语首次出现处给直觉解释，后文可直接使用。
- 每章开头检查依赖章节已定义的概念：不超前使用"内积""特征值""softmax"等未教术语（出现则一句话解释）。
