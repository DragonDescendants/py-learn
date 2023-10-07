import torch as t

a = t.ones(3, 4, 5)
# print(a, a.shape)
res_1 = a.sum(dim=0)
res_2 = a.sum(dim=1)
res_3 = a.sum(dim=2) #keepdim=True 可以保留维度"1"
# print(res_1, res_1.shape, "\n", res_2, res_2.shape, "\n", res_3, res_3.shape)
"""
tensor([[[1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.]],

        [[1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.]],

        [[1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.],
         [1., 1., 1., 1., 1.]]]) 
         torch.Size([3, 4, 5])
tensor([[3., 3., 3., 3., 3.],
        [3., 3., 3., 3., 3.],
        [3., 3., 3., 3., 3.],
        [3., 3., 3., 3., 3.]]) 
        torch.Size([4, 5])
 tensor([[4., 4., 4., 4., 4.],
        [4., 4., 4., 4., 4.],
        [4., 4., 4., 4., 4.]]) 
        torch.Size([3, 5])
 tensor([[5., 5., 5., 5.],
        [5., 5., 5., 5.],
        [5., 5., 5., 5.]]) 
        torch.Size([3, 4])
"""

# 累加运算,按照对应维度累加,结果储存在对应维度的最后一个数据上
b = t.arange(0,12).view(2,3,2)
print('origin:',b,'\n',
      'dim=0:',b.cumsum(dim=0),'\n',
      'dim=1:',b.cumsum(dim=1),'\n',
      'dim=2:',b.cumsum(dim=2))
'''
origin: tensor([[[ 0,  1],
         [ 2,  3],
         [ 4,  5]],

        [[ 6,  7],
         [ 8,  9],
         [10, 11]]])
 dim=0: tensor([[[ 0,  1],
         [ 2,  3],
         [ 4,  5]],

        [[ 6,  8],
         [10, 12],
         [14, 16]]])
 dim=1: tensor([[[ 0,  1],
         [ 2,  4],
         [ 6,  9]],

        [[ 6,  7],
         [14, 16],
         [24, 27]]])
 dim=2: tensor([[[ 0,  1],
         [ 2,  5],
         [ 4,  9]],

        [[ 6, 13],
         [ 8, 17],
         [10, 21]]])
'''
c = t.arange(0,12).view(3,4)
print('origin:',c,'\n',
      'dim=0:',c.cumsum(dim=0),'\n',
      'dim=1:',c.cumsum(dim=1))
'''
origin: tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
 dim=0: tensor([[ 0,  1,  2,  3],
        [ 4,  6,  8, 10],
        [12, 15, 18, 21]])
 dim=1: tensor([[ 0,  1,  3,  6],
        [ 4,  9, 15, 22],
        [ 8, 17, 27, 38]])
'''