import numpy as np

'''
E = 1/2 ∑k (yk - tk)^2
'''


# 均方误差 y和t为numpy数组
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# 设“2”为正确解
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 例1：“2”的概率最高的情况（0.6）
y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(mean_squared_error(np.array(y1), np.array(t)))
# 0.09750000000000003

# 例2：“7”的概率最高的情况（0.6）
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(mean_squared_error(np.array(y2), np.array(t)))
# 0.5975

'''
均方误差越小(损失函数的值)越小，说明越吻合
'''

'''
E = - ∑k tk * log[e](yk)
'''


# 交叉熵误差
def cross_entropy_error(y, t):
    delta = 1e-7  # 加上一个极小数，防止负无限大产生影响后续计算
    return -np.sum(t * np.log(y + delta))  # np.log() 计算自然对数


# np.array()创建np数组
print(cross_entropy_error(np.array(y1), np.array(t)), cross_entropy_error(np.array(y2), np.array(t)))

