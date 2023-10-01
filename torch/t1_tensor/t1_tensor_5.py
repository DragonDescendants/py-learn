import torch as t

a = t.arange(0,16).view(4,4)
print(a)

index = t.tensor([[0,3]],
                 dtype=t.int64)
print(index)
'''
gather选取对角线元素时,根据给定的下标矩阵来操作
例如给定0,3则是在第0行,第3行取元素
此时第1,2行被忽略,所以在第0行取出元素0后是在第3行取第1号位元素13
'''
print('gather选取对角线元素:',a.gather(0,index))
'''
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15]])
tensor([[0, 3]])
gather选取对角线元素: tensor([[ 0, 13]])
'''
# .t()即为转置 
index_rev = t.tensor([[3,2,1,0]],dtype=t.int64).t()
print('反转对角线元素:',a.gather(0,index_rev))
'''
反转对角线元素: tensor([[12],
        [ 8],
        [ 4],
        [ 0]])
'''