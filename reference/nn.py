"""Week 8 · 两层神经网络：前向 = 复合变换，学习 = 梯度下降。

前向传播是 Week 3 矩阵乘法的连环套：x → W1x+b1 → ReLU → W2·+b2。
学习 = 顺着梯度的反方向，把这些变换一点点调得更"对"。
"""

import numpy as np


def relu(z: np.ndarray) -> np.ndarray:
    """ReLU 激活函数：负数归零，正数放行。"""
    return np.maximum(0.0, z)


def mse_loss(y_pred: np.ndarray, y: np.ndarray) -> float:
    """均方误差：(1/N) Σ (预测 - 目标)²。越小说明预测越准。"""
    return float(np.mean((y_pred - y) ** 2))


def xor_dataset():
    """XOR 玩具数据：四个点，异或结果作为标签。"""
    X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
    y = np.array([[0.0], [1.0], [1.0], [0.0]])
    return X, y


class TwoLayerNet:
    """输入 → 隐藏层(ReLU) → 输出（1 个神经元，回归 0/1）。"""

    def __init__(self, n_in: int, n_hidden: int, seed: int = 0):
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0.0, 1.0, size=(n_in, n_hidden))
        self.b1 = np.zeros(n_hidden)
        self.W2 = rng.normal(0.0, 1.0, size=(n_hidden, 1))
        self.b2 = np.zeros(1)

    def forward(self, X: np.ndarray) -> np.ndarray:
        """前向传播：X(N, n_in) → H(N, n_hidden) → out(N, 1)。

        每一层都是一次"线性变换 + 平移"（Week 3 的 Wx 加上平移 b）。
        """
        self.Z1 = X @ self.W1 + self.b1
        self.H = relu(self.Z1)
        self.out = self.H @ self.W2 + self.b2
        return self.out

    def loss(self, X: np.ndarray, y: np.ndarray) -> float:
        """先跑前向，再算均方误差。"""
        return mse_loss(self.forward(X), y)

    def backward(self, X: np.ndarray, y: np.ndarray):
        """反向传播：按链式法则把梯度一层层传回去。

        用到的中间量（Z1/H/out）缓存在上一次 forward 里。
        公式推导见教程 Week 8 Day 4，这里按公式实现。
        """
        N = X.shape[0]
        dout = 2.0 * (self.out - y) / N       # dL/d(out)
        dW2 = self.H.T @ dout                 # (n_hidden, 1)
        db2 = dout.sum(axis=0)
        dH = dout @ self.W2.T                 # (N, n_hidden)
        dZ1 = dH * (self.Z1 > 0)              # ReLU 的"开关"导数
        dW1 = X.T @ dZ1                       # (n_in, n_hidden)
        db1 = dZ1.sum(axis=0)
        return {"W1": dW1, "b1": db1, "W2": dW2, "b2": db2}

    def sgd_step(self, X: np.ndarray, y: np.ndarray, lr: float) -> None:
        """一次梯度下降：算梯度 → 所有参数朝反方向挪一小步 lr*grad。"""
        self.forward(X)
        grads = self.backward(X, y)
        for name, g in grads.items():
            setattr(self, name, getattr(self, name) - lr * g)

    def train(self, X: np.ndarray, y: np.ndarray, epochs: int, lr: float,
              verbose: bool = False) -> list:
        """训练循环：每个 epoch 走一步梯度下降，记录损失历史。"""
        history = []
        for epoch in range(epochs):
            self.sgd_step(X, y, lr)
            loss = self.loss(X, y)
            history.append(loss)
            if verbose and epoch % max(1, epochs // 10) == 0:
                print(f"epoch {epoch}: loss = {loss:.6f}")
        return history
