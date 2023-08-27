# nn构建于Autograd上,用来定义和运行神经网络
# nn.Module是nn中最重要的类,可返回前向传播的结果
# 这里以LeNet为例
import torch as t
import torch.nn as nn
import torch.nn.functional as f
from torch.autograd import Variable


class Net(nn.Module):
    """
    定义网络时，需要继承nn.Module ，并实现它的forward方法 ，
    把网络中具有可学习参数的层放在构造函数__init__中
    如果某一层（如ReLU ）不具有可学习的参数，则既可以放在构造函数中，也可以不放
    """

    def __init__(self):
        # nn.Module 函数必须在构造函数中执行父类 的构造函数
        # 下式等价nn.Module__init__(self)
        super(Net, self).__init__()

        # 卷积层'1'表示输入图片为单通道,‘6’表示输出的通道数
        # '5'表示卷积核为 5*5
        self.conv1 = nn.Conv2d(1, 6, 5)
        # 卷积层
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 仿射层／全连接层， y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 卷积 -> 激活 ->池化
        x = f.max_pool2d(f.relu(self.conv1(x)), (2, 2))
        x = f.max_pool2d(f.relu(self.conv2(x)), 2)
        # reshape, ‘-1’表示自适应
        x = x.view(x.size()[0], -1)
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()
print(net)
"""
只要在 nn.Module 的子类中定义了 forward 函数， backward 函数就会被向动实现(利用Autograd)
 forward 两数中可使用任何 Variable 支持的函数 ，
 还可以使用 if for 循环 print log Python 语法 写法和标准的 Python 写法一致
"""
# 网络的可学习参数通 net.parameters()返回， net.named_parameters 可同时返回可学习的参数及名称
params = list(net.parameters())
print(len(params))
for name, param in net.named_parameters():
    print(name, param.size())
# forward 函数的输入和输出 都是 Variable ，只有 Variable 才具有自动求导功能，
# Tensor是没有的，所以在输入时，需要把 Tensor 装成 Variable
input_test = Variable(t.randn(1, 1, 32, 32))
out = net(input_test)
print(out.size())
