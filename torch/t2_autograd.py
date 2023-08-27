# 深度学习的算法本质上是通过反向传播求导数， PyTorch Autograd 模块实现了此功能
# Variable 主要包含 个属性
# • data 保存 Variable 所包含的 Tensor
# • grad 保存data 应的梯度， grad 是个 Variable 而不是 Tensor 它和data 的形状一样
# • grad_fn 指向一个 Function 对象，这个 Function 用来反向传播计算输入的梯度，
from torch.autograd import Variable
import torch as t

x = Variable(t.ones(2, 2), requires_grad=True)
print(x.data)
# tensor([[1., 1.],
#         [1., 1.]], requires_grad=True)
y = x.sum()
print(y, y.grad_fn)
# tensor(4., grad_fn=<SumBackward0>) <SumBackward0 object at 0x00000244E3E098D0>
y.backward()
print(x.grad)
# backward反向传播过程中,grad是累加的,所以操作前需要把梯度清零
y.backward()
print(x.grad)
x.grad.data.zero_()
print(x.grad)
y.backward()
print(x.grad)
# -------------------------------
a = Variable(t.ones(4, 5))
b = t.cos(a)  # 可以传入tensor也可以传入Variable
a_tensor_cos = t.cos(a.data)
print(b, a_tensor_cos)  # 两者结果一样
# tensor([[0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403]])
# tensor([[0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403],
#         [0.5403, 0.5403, 0.5403, 0.5403, 0.5403]])
