import numpy as np


# 阶跃函数
def step_function(x):
    y = x > 0
    return y.astype(np.int_)


# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# ReLU函数
def relu(x):
    return np.maximum(0, x)

