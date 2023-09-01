"""
激活函数层的实现
"""
import numpy as np

from learn.l2_softmax import softmax
from learn.l3_loss_function import cross_entropy_error


class Relu:
    def __init__(self):
        # 保存由True或者False构成的Numpy数组
        # 它会把正向传播时的输入x的元素中小于等于0的地方保存为True，
        # 其他地方（大于0的元素）保存为False
        self.mask = None

    # 前向传播
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    '''
    如果正向传播时的输入值小于等于0，则反向传播的值为0。
    因此，反向传播中会使用正向传播时保存的mask，
    将从上游传来的d_out的mask中的元素为True的地方设为0
    '''

    def backward(self, d_out):
        d_out[self.mask] = 0
        d_x = d_out
        return d_x


# test
x = np.array([[1.0, -0.5], [-2.0, 3.0]])
print(x)
mask = (x <= 0)
print(mask)


class Sigmoid:
    def __init__(self):
        # 保存正向传播的结果
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, d_out):
        d_x = d_out * (1.0 - self.out) * self.out
        return d_x


class Affine:
    # W权重,b偏置
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.d_W = None
        self.d_b = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backward(self, d_out):
        d_x = np.dot(d_out, self.W.T)
        self.d_W = np.dot(self.x.T, d_out)
        self.d_b = np.sum(d_out, axis=0)
        return d_x


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None  # 损失
        self.y = None  # softmax的输出
        self.t = None  # 监督数据

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self, d_out=1):
        batch_size = self.t.shape[0]  # 获取批的大小
        d_x = (self.y - self.t) / batch_size  # 传递的是单个数据的误差,要除以批的大小
        return d_x
