import torch as t

a = t.Tensor(2,3)
print('a:',a) # a的数值取决于内存空间的状态

# tensor([[5.7022e-37, 8.5619e-43, 5.7022e-37],
#         [8.5619e-43, 5.7101e-37, 8.5619e-43]])

b = t.Tensor([[1,2,3],[4,5,6]]) #用二维列表来创建Tensor
print(b,'\n',b.tolist()) 

# tensor([[1., 2., 3.],
#         [4., 5., 6.]])
#  [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

# ----------------------------------------------------------------------------

# tensor.size() 返回 torch.Size 对象，它是 tuple 子类，但其使用方式与 tuple 有区别
# b.nelement() 返回 torch 里面所有的元素个数
print('b:',b.size(),b.nelement())

# torch.Size([2, 3]) 6

# 创建一个与b同形状的矩阵c
c = t.Tensor(b.size())
d = t.Tensor((2,3))
print('c:',c,'\n','d:',d)
# c: tensor([[0.0000e+00, 0.0000e+00, 2.1019e-44],
#         [0.0000e+00, 2.2704e-11, 5.1288e-43]])
#  d: tensor([2., 3.])

# tensor.shape 等同于 tensor.size()
print(c.shape,d.shape)
# torch.Size([2, 3]) torch.Size([2])