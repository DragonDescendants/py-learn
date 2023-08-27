import numpy as np


# softmax
# a = np.array([0.3, 2.9, 4.0])
# exp_a = np.exp(a)
# print(exp_a)
# sum_exp_a = np.sum(exp_a)
# print(sum_exp_a)
# y = exp_a / sum_exp_a
# print(y)
def old_softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


# 指数运算,可能会导致结果过大,造成溢出
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # 利用c(输入信号中的最大值)来处理溢出
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y, np.sum(y))
