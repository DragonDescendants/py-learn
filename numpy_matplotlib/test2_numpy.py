import numpy as np

'''
矩阵创建
'''
# create创建ndarray
# 指定元素创建矩阵,2行2列
create_1 = np.array([[2, 4, 7, 9],
                     [6, 8, 5, 3],
                     [4, 3, 6, 9],
                     [8, 1, 2, 5]])
print('test1:', create_1)
# 创建元素全为0的矩阵,指定为2行4列
create_2 = np.zeros((2, 4))
print('test2:', create_2)
# 创建元素全为1的矩阵,指定为3行3列
create_3 = np.ones((3, 3))
print('test3:', create_3)
# 创建一个4阶单位矩阵,对角线元素为1,其余为0
create_4 = np.eye(4)
print('test4:', create_4)
# 生成指定范围步长的一维数组序列 (start,stop,step)
create_5 = np.arange(1, 10, 2)
print('test5:', create_5)  # test5: [1 3 5 7 9]
'''
切片
'''
# 切片操作的一般语法是array[start:end:step]
print('slices:', create_1[:, :2])
print('------------------------------')
'''
矩阵运算
'''
# 矩阵乘法dot np.dot(a,b)
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
print('---------linalg---------')
# 计算矩阵的行列式 numpy.linalg.det(a)
print(np.linalg.det(create_1))
# 计算逆矩阵 numpy.linalg.inv(a)
print(np.linalg.inv(create_1))
# 矩阵分解 返回一个Q矩阵和R矩阵，满足A = QR，其中Q是正交矩阵，R是上三角矩阵
print(np.linalg.qr(create_1))
'''
随机数生成
'''
print('---------随机数生成----------')
# 生成随机数，范围为0.0-1.0之间的浮点数,指定3行2列
print(np.random.rand(3, 2))
# 生成指定范围的随机整数,指定[1,20)的范围,指定4行3列
print(np.random.randint(1, 20, (4, 3), dtype='int64'))
# 生成具有标准正态分布的一组数据 是以0为均值、以1为标准差的正态分布，记为N(0，1)
print(np.random.randn(5, 4))
# np.random.seed() 可以指定随机数种子,让随机的结果可预测
# np.random.choice() 从给定的一维数组中生成随机数
print(np.random.choice(create_1[0]))

print('---------矩阵操作-----------')
'''
矩阵操作
'''
# test np.sum()求和
test = np.array([[1, 3, 5],
                 [2, 4, 6],
                 [3, 6, 9],
                 [8, 5, 2]])
print(test, test.shape[0], test.shape[1])
# test为 4 行 3 列
# axis = 0 以列为维度求和(求出的结果有3个元素)
# axis = 1 以行为维度求和(求出的结果有4个元素)
print(np.sum(test, axis=0),  # [14,18,22]
      np.sum(test, axis=1),  # [9,12,18,15]
      np.sum(test))  # 所有元素的和54

# np.mean()求平均值
print(np.mean(test),  # 4.5
      np.mean(test, axis=0),  # [3.5 4.5 5.5]
      np.mean(test, axis=1))  # [3. 4. 6. 5.]
# np.std() 求标准差
# 标准差即方差开根号 方差 = ∑n (xk - avg(x)) ^2 /n
print(np.std(test),  # 2.362907813126304
      np.std(test, axis=0),  # [2.6925824  1.11803399 2.5       ]
      np.std(test, axis=1))  # [1.63299316 1.63299316 2.44948974 2.44948974]
# np.medium() 计算中位数
print(np.median(test))  # 4.5
# min()找最小值 max()找最大值 argmax()最大值索引 argmin()最小值索引
print(np.min(test), np.max(test), np.argmax(test), np.argmin(test))  # 1 9 8 0

'''
np.load(file_, mmap_mode=None)：加载以NumPy二进制格式保存的文件。
np.save(file_, arr)：将数组保存为NumPy二进制格式的文件
'''
