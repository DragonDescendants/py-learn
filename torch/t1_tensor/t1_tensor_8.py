import torch as t

# 数学运算
a = t.arange(0, 6).view(2, 3)
print("origin:", a, "\n")
print("cos:", t.cos(a), "\n")
print("fmod:", t.fmod(a, 3), "\n", a % 3, "\n")
print("pow:", t.pow(a, 3), "\n", a**3, "\n")
print("clamp:", t.clamp(a, min=3))
"""
origin: tensor([[0, 1, 2],
        [3, 4, 5]])

cos: tensor([[ 1.0000,  0.5403, -0.4161],
        [-0.9900, -0.6536,  0.2837]])

fmod: tensor([[0, 1, 2],
        [0, 1, 2]])
 tensor([[0, 1, 2],
        [0, 1, 2]])

pow: tensor([[  0,   1,   8],
        [ 27,  64, 125]])
 tensor([[  0,   1,   8],
        [ 27,  64, 125]])

clamp: tensor([[3, 3, 3],
        [3, 4, 5]])
"""
