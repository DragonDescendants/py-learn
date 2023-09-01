from collections import OrderedDict

import numpy as np

from test_01.layers import Affine, Relu


class TwoLayerNet:
    """
    input_size      输入层的神经元数
    hidden_size     隐藏层的神经元数
    output_size     输出层的神经元数
    weight_init_std 初始化权重时的高斯分布的规模
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
