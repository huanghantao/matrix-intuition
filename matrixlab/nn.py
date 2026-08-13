"""Week 8 · 两层神经网络（战场版：函数体待你实现）。"""

import numpy as np


def relu(z: np.ndarray) -> np.ndarray:
    """ReLU 激活函数：负数归零，正数放行。"""
    raise NotImplementedError("TODO: Week 8 Day 3 —— ReLU")


def mse_loss(y_pred: np.ndarray, y: np.ndarray) -> float:
    """均方误差：(1/N) Σ (预测 - 目标)²。"""
    raise NotImplementedError("TODO: Week 8 Day 2 —— 均方误差")


def xor_dataset():
    """XOR 玩具数据：四个点，异或结果作为标签。"""
    raise NotImplementedError("TODO: Week 8 Day 6 —— XOR 数据集")


class TwoLayerNet:
    """输入 → 隐藏层(ReLU) → 输出（1 个神经元，回归 0/1）。"""

    def __init__(self, n_in: int, n_hidden: int, seed: int = 0):
        raise NotImplementedError("TODO: Week 8 Day 3 —— 参数初始化")

    def forward(self, X: np.ndarray) -> np.ndarray:
        """前向传播：X → ReLU(X@W1+b1) → @W2+b2。"""
        raise NotImplementedError("TODO: Week 8 Day 3 —— 前向传播")

    def loss(self, X: np.ndarray, y: np.ndarray) -> float:
        """先跑前向，再算均方误差。"""
        raise NotImplementedError("TODO: Week 8 Day 2 —— 损失")

    def backward(self, X: np.ndarray, y: np.ndarray):
        """反向传播：按链式法则返回各参数的梯度。"""
        raise NotImplementedError("TODO: Week 8 Day 4 —— 反向传播")

    def sgd_step(self, X: np.ndarray, y: np.ndarray, lr: float) -> None:
        """一次梯度下降：参数 -= lr * 梯度。"""
        raise NotImplementedError("TODO: Week 8 Day 5 —— 梯度下降一步")

    def train(self, X: np.ndarray, y: np.ndarray, epochs: int, lr: float,
              verbose: bool = False) -> list:
        """训练循环：返回每轮的损失历史。"""
        raise NotImplementedError("TODO: Week 8 Day 5 —— 训练循环")
