import torch as t
'''
print('ones:',t.ones(2,3),'\n', #全1
      'zeros:',t.zeros(4,6),'\n', # 全0
      'arange:',t.arange(1,10,2),'\n'  # 一维 间隔生成
      'linspace:',t.linspace(1,10,6),'\n', # 均分切片
      'rand:',t.rand(3,4),'\n', # 均匀分布
      'randn:',t.randn(3,4),'\n', # 标准正态分布
      'randperm:',t.randperm(10),'\n' # 生成随机数
      'eye:',t.eye(12,7) # 对角线为1 可以行列数不相等
      )
'''
a = t.arange(1,13) # [1,13)
b = a.view(3,4)
c = b.view(-1,6) # 维度为-1时会自动计算大小
d = c.view(2,2,1,1,3)
e = d.squeeze() # 压缩所有维度的"1"
f = d.squeeze(2) # 压缩第(0,1)2维的"1"
# unsqueeze(1) 在第一维增加'1'
print(a,a.shape,'\n',
      b,b.shape,'\n',
      c,c.shape,'\n',
      d,d.shape,'\n',
      e,e.shape,'\n',
      f,f.shape,'\n')

'''
tensor([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]) torch.Size([12]) 
 tensor([[ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12]]) torch.Size([3, 4])
 tensor([[ 1,  2,  3,  4,  5,  6],
        [ 7,  8,  9, 10, 11, 12]]) torch.Size([2, 6])
 tensor([[[[[ 1,  2,  3]]],


         [[[ 4,  5,  6]]]],



        [[[[ 7,  8,  9]]],


         [[[10, 11, 12]]]]]) torch.Size([2, 2, 1, 1, 3])
 tensor([[[ 1,  2,  3],
         [ 4,  5,  6]],

        [[ 7,  8,  9],
         [10, 11, 12]]]) torch.Size([2, 2, 3])
 tensor([[[[ 1,  2,  3]],

         [[ 4,  5,  6]]],


        [[[ 7,  8,  9]],

         [[10, 11, 12]]]]) torch.Size([2, 2, 1, 3])
'''