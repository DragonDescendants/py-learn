import numpy as np

# 矩阵乘法dot
X = np.array([1, 2])
print(X, X.shape)
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W, W.shape)
Y = np.dot(X, W)
# Y = X * W
print(Y)
