import numpy as np

# 矩阵乘法dot
X = np.array([1, 2])
print(X, X.shape)
W = np.array([[1, 3, 5],
              [2, 4, 6]])
# 2行 W.shape[0] = 2
# 3列 W.shape[1] = 3
print(W, W.shape)
Y = np.dot(X, W)
# Y = X * W
print(Y)

# test
test = np.array([[1, 3, 5],
                 [2, 4, 6],
                 [3, 6, 9],
                 [8, 5, 2]])
print(test,test.shape[0], test.shape[1],
      np.sum(test, axis=0), np.sum(test, axis=1),
      np.sum(test))
