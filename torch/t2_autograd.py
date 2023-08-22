# 深度学习的算法本质上是通过反向传播求导数， PyTorch Autograd 模块实现了此功能
# Variable 主要包含 个属性
# • data 保存 Variable 所包含的 Tensor
# • grad ：保存data 应的梯度， grad 是个 Variable 而不是 Tensor 它和data 的形
# 状一样
# • grad_fn 指向一个 Function 对象，这个 Function 用来反向传播计算输入的梯度，
from torch.autograd import Variable
