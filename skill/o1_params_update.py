"""
对参数的优化
"""
import numpy as np


# SGD随机梯度下降法
class StochasticGradientDescent:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def update(self, params, grads):
        # params 参数 grads 梯度 都是字典型变量 params['W1']
        for key in params.keys():
            params[key] = params[key] - self.learning_rate * grads[key]


'''
network = TwoLayerNet(...)
optimizer = SGD()
for i in range(10000):
    ...
    x_batch, t_batch = get_mini_batch(...) # mini-batch
    grads = network.gradient(x_batch, t_batch)
    params = network.params
    # 将功能模块化
    optimizer.update(params, grads)
    ...
'''


# Momentum 动量法
class Momentum:
    # learning_rate学习率，momentum动量
    def __init__(self, learning_rate=0.01, momentum=0.9):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        # 对字典中所有元素对应的速度矩阵初始化，置0
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.learning_rate * grads[key]
            params[key] = params[key] + self.v[key]


class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] = self.h[key] + grads[key] * grads[key]
            # 1e-7是一个极小值,避免除数为0的问题
            params[key] = params[key] - self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
