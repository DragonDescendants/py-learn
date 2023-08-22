import torch as t
import numpy as np

# 构建5*3矩阵,只是分配了空间,没有初始化
# x = t.Tensor(5, 3)
# print(x)
# tensor([[9.2755e-39, 1.0561e-38, 5.1429e-39],
#         [4.6837e-39, 5.2347e-39, 5.9694e-39],
#         [1.0286e-38, 8.9081e-39, 8.9082e-39],
#         [6.9796e-39, 9.0919e-39, 9.9184e-39],
#         [7.3470e-39, 1.0194e-38, 1.0469e-38]])

# 使用[0,1]均匀分布初始化
x = t.rand(5, 3)
print("x:", x)

# 查看形状
# print(x.size(), x.size()[0], x.size(1))  # torch.Size([5, 3]) 5 3
# torch.size()是tuple元组的子类,支持所有tuple的操作
# 在Python中，元组与列表相似，不同之处在于元组的元素不能修改，而列表的元素可以修改
y = t.rand(5, 3)
print("y:", y)

# 在这里,使用y.add(x)不会修改y的值,而是返回了一个新的tensor对象
# y.add(x)
# print(y, y.add(x))
# 但是使用add_()就是修改原来的对象y
# y.add_(x)
# print(y)

# x矩阵 + y矩阵
# print(x + y, t.add(x, y))
# result = t.Tensor(5, 3)
# print(t.add(x, y, out=result))

# tenser和numpy对象共享内存，可以很快相互转化
print(x[:, 1])  # 取出x中的第二(0,1,2)列元素
a = t.ones(5)
print(a, type(a))  # tensor([1., 1., 1., 1., 1.]) <class 'torch.Tensor'>
b = a.numpy()  # tensor -> ndarray
print(b, type(b))  # [1. 1. 1. 1. 1.] <class 'numpy.ndarray'>
# ndarray -> tensor
c = np.ones(5)
d = t.from_numpy(c)
print(c, d)
# 因为共享内存，所以修改其中一个对象，两个对象都会被修改
# 使用CUDA加速来计算x+y
if t.cuda.is_available():
    x = x.cuda()
    y = y.cuda()
    print(x + y)
