import torch as t

a = t.arange(0, 16).view(4, 4)
print(a)

index = t.tensor([[0, 3]], dtype=t.int64)
print(index)
"""
gather选取对角线元素时,根据给定的下标矩阵来操作
例如给定0,3则是在第0行,第3行取元素
此时第1,2行被忽略,所以在第0行取出元素0后是在第3行取第1号位元素13
"""
print("gather选取对角线元素:", a.gather(0, index))
"""
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15]])
tensor([[0, 3]])
gather选取对角线元素: tensor([[ 0, 13]])
"""
# .t()即为转置
index_rev = t.tensor([[3, 2, 1, 0]], dtype=t.int64).t()
# 反对角线dim=1 以列为基准
print("反转对角线元素:", a.gather(1, index_rev))
"""
反转对角线元素: tensor([[ 3],
        [ 6],
        [ 9],
        [12]])
"""

print(a)

# scatter_()
b = t.zeros(4, 4)
source = a.float()
print(b, b.dtype,source.dtype)
# RuntimeError: scatter(): Expected self.dtype to be equal to src.dtype
# 要注意scatter中的src tensor的类型要与 调用方法的tensor相同
out = b.scatter_(1, index_rev, source)
print(out)
'''
tensor([[ 0.,  0.,  0.,  0.],
        [ 0.,  0.,  4.,  0.],
        [ 0.,  8.,  0.,  0.],
        [12.,  0.,  0.,  0.]])
'''