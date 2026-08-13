"""Week 8 · 两层神经网络的测试。"""

import numpy as np
from pytest import approx


def test_relu(mod):
    nn = mod("nn")
    out = nn.relu(np.array([-3.0, -0.1, 0.0, 2.5]))
    assert out.tolist() == [0.0, 0.0, 0.0, 2.5]


def test_mse_loss(mod):
    nn = mod("nn")
    y_pred = np.array([[1.0], [0.0]])
    y = np.array([[0.0], [0.0]])
    assert nn.mse_loss(y_pred, y) == approx(0.5)


def test_forward_shapes(mod):
    nn = mod("nn")
    net = nn.TwoLayerNet(n_in=2, n_hidden=3, seed=0)
    X = np.array([[0.0, 0.0], [1.0, 1.0], [0.0, 1.0], [1.0, 0.0]])
    out = net.forward(X)
    assert out.shape == (4, 1)
    assert net.H.shape == (4, 3)


def test_gradient_check_output_layer(mod):
    nn = mod("nn")
    net = nn.TwoLayerNet(n_in=2, n_hidden=3, seed=1)
    X = np.array([[0.5, -0.3], [0.1, 0.9]])
    y = np.array([[0.7], [0.2]])
    net.forward(X)
    grads = net.backward(X, y)

    # 数值梯度：单独扰动 W2[0,0]，用中心差分算 dL/dW2[0,0]
    eps = 1e-6
    old = net.W2[0, 0]

    def loss_with(value):
        net.W2[0, 0] = value
        L = net.loss(X, y)
        net.W2[0, 0] = old
        return L

    numeric = (loss_with(old + eps) - loss_with(old - eps)) / (2 * eps)
    assert grads["W2"][0, 0] == approx(numeric, abs=1e-6)


def test_gradient_check_hidden_layer(mod):
    nn = mod("nn")
    net = nn.TwoLayerNet(n_in=2, n_hidden=2, seed=2)
    X = np.array([[0.4, -0.2], [-0.6, 0.8]])
    y = np.array([[0.1], [0.9]])
    net.forward(X)
    grads = net.backward(X, y)

    eps = 1e-6
    old = net.W1[1, 0]

    def loss_with(value):
        net.W1[1, 0] = value
        L = net.loss(X, y)
        net.W1[1, 0] = old
        return L

    numeric = (loss_with(old + eps) - loss_with(old - eps)) / (2 * eps)
    assert grads["W1"][1, 0] == approx(numeric, abs=1e-6)


def test_training_reduces_loss(mod):
    nn = mod("nn")
    X, y = nn.xor_dataset()
    net = nn.TwoLayerNet(n_in=2, n_hidden=4, seed=0)
    loss0 = net.loss(X, y)
    history = net.train(X, y, epochs=2000, lr=0.1)
    assert history[-1] < loss0
    assert history[-1] < 0.05


def test_xor_learned(mod):
    nn = mod("nn")
    X, y = nn.xor_dataset()
    net = nn.TwoLayerNet(n_in=2, n_hidden=4, seed=0)
    net.train(X, y, epochs=3000, lr=0.1)
    pred = net.forward(X)
    # 预测值四舍五入后与标签完全一致（四个点全分对）
    assert np.all(np.abs(pred - y) < 0.5)
