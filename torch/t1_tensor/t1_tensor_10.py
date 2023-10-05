import torch as t

a = t.linspace(0, 15, 6).view(2, 3)
b = t.linspace(15, 0, 6).view(2, 3)
print(a, "\n", b)
print(a > b, (a > b).dtype)
"""
tensor([[ 0.,  3.,  6.],
        [ 9., 12., 15.]])
 tensor([[15., 12.,  9.],
        [ 6.,  3.,  0.]])
tensor([[False, False, False],
        [ True,  True,  True]]) torch.bool
"""
print(a[a > b])  # 输出a中,a>b的元素
# tensor([ 9., 12., 15.])
# max()操作设置dim后会返回两个结果,一个是值,一个是其对应的下标
print(t.max(a), "\n", t.max(b, dim=1), "\n", t.max(a, b))
"""
1.tensor(15.)
2.dim=1时max输出的元素个数=行数(0纵向1横向)
torch.return_types.max(
values=tensor([15.,  6.]),
indices=tensor([0, 0])) 
3.tensor([[15., 12.,  9.],
        [ 9., 12., 15.]])
"""
