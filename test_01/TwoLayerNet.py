from collections import OrderedDict

import numpy as np

from learn.l5_gradient_descent import numerical_gradient
from test_01.layers import Affine, Relu, SoftmaxWithLoss


class TwoLayerNet:
    """
    input_size      输入层的神经元数
    hidden_size     隐藏层的神经元数
    output_size     输出层的神经元数
    weight_init_std 初始化权重时的高斯分布(正态分布)的规模
    """

    def __init__(self,
                 input_size,
                 hidden_size,
                 output_size,
                 weight_init_std=0.01):
        # 初始化权重
        # np.random.randn() 生成指定维度的服从标准正态分布的随机数，输入参数为维度
        # np.zeros([x,y]) 返回指定形状的矩阵，但是元素的值均为0
        self.params = {'W1': weight_init_std * np.random.randn(input_size, hidden_size),
                       'b1': np.zeros(hidden_size),
                       'W2': weight_init_std * np.random.randn(hidden_size, output_size),
                       'b2': np.zeros(output_size)}

        # 生成层
        # OrderedDict()有序字典
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        self.lastLayer = SoftmaxWithLoss()

    '''
    预测
    '''

    def predict(self, x):
        for layer in self.layers.values():
            # 每层前向传播
            x = layer.forward(x)
        return x

    # x输入数据,t监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        # np,argmax()表示获取某一个维度数值最大的元素索引，axis=1表示在第一维
        y = np.argmax(y, axis=1)
        # t.ndim 输出数组的维数 t.shape 输出数组的形状
        if t.ndim != 1:
            t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    # x:输入数据, t:监督数据
    def numerical_gradient(self, x, t):
        # lambda argument_list:expersion 快速定义一个函数
        loss_W = lambda W: self.loss(x, t)

        grads = {'W1': numerical_gradient(loss_W, self.params['W1']),
                 'b1': numerical_gradient(loss_W, self.params['b1']),
                 'W2': numerical_gradient(loss_W, self.params['W2']),
                 'b2': numerical_gradient(loss_W, self.params['b2'])}

        return grads

    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        d_out = 1
        d_out = self.lastLayer.backward(d_out)

        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            d_out = layer.backward(d_out)

        # 设定
        grads = {'W1': self.layers['Affine1'].d_W,
                 'b1': self.layers['Affine1'].d_b,
                 'W2': self.layers['Affine2'].d_W,
                 'b2': self.layers['Affine2'].d_b}

        return grads
