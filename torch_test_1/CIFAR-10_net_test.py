import torch as t
import torchvision as tv
# 在torch.transforms中有大量的数据变换类，有很大一部分可以用于
# 实现数据预处理(Data Preprocessing)和数据增广(Data Argumentation)
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from torch import nn
from torch import optim
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision.transforms import ToPILImage


class Net(nn.Module):
    # 初始化网络结构
    def __init__(self):
        super(Net, self).__init__()
        # nn.Conv2d() 定义二维卷积层的类
        # in_channels 输入的通道数，例如RGB图像的通道数为3,
        # out_channels 输出的通道数，即卷积核的数量,
        # kernel_size 卷积核的大小，可以是单个整数或元组
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # nn.Linear()是PyTorch中的一个函数，用于设置网络中的全连接层。
        # 全连接层接受输入数据，并将其与给定的权重和偏置项进行线性组合，以生成输出。
        '''
        nn.Linear()函数的一般用法是：[in_features,out_features]
        in_features指的是输入的二维张量的大小,即输入的[batch_size,size]中的size
        out_features指的是输出的二维张量的大小,即输出的二维张量的形状为[batch_size,output_size]
        它也代表了该全连接层的神经元个数
        '''
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        """

        :param x: 张量Tensor
        :return:
        """
        # F.max_pool2d 是 PyTorch 中的一个函数，用于执行二维最大池化操作
        # 最大池化是一种下采样技术，常用于卷积神经网络（CNN）中
        # 可以降低数据维度，提取特征，同时保留重要信息
        """
        input：输入张量，形状为 [batch_size, channels, height, width]。
        kernel_size：最大池化操作的核大小，可以是一个单独的数字，表示 height 和 width 均为该数字，
            也可以是一个元组，分别指定 height 和 width。
        stride：步长，默认为 None，表示与 kernel_size 相同。
        padding：填充大小，默认为 0，表示不填充。
        dilation：空洞大小，默认为 1，表示不进行空洞卷积。
        return_indices：是否返回每个最大值的索引，默认为 False。
        ceil_mode：是否使用 ceil 函数计算输出形状，默认为 False。
        """
        # max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
        # ReLU f(x) = max(0, x)
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        '''
        在这段代码中，x.view(x.size()[0], -1)，x.size()[0]表示张量x的第一维大小（通常是批量大小），
        -1表示让PyTorch自动计算该维度的大小，以保证总元素数量不变。
        所以，这行代码的目的是将张量x的形状变为“批量大小”乘以“-1”所计算出的新维度。
        举个例子，如果x的形状是[32, 10, 10]（批量大小为32，特征数量为10*10），
        那么执行这行代码后，x的形状将变为[32, 100]，即将原来的二维特征平展为一维。
        '''
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


if __name__ == '__main__':
    # 主程序的代码

    transform = transforms.Compose([
        transforms.ToTensor(),  # 转化为Tensor
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),  # 归一化
    ])

    # 训练集
    train_set = tv.datasets.CIFAR10(
        root='../data/',
        train=True,
        download=True,
        transform=transform
    )
    '''
    DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,
               batch_sampler=None, num_workers=0, collate_fn=None,
               pin_memory=False, drop_last=False, timeout=0,
               worker_init_fn=None, *, prefetch_factor=2,
               persistent_workers=False)
    '''
    train_loader = t.utils.data.DataLoader(
        train_set,
        batch_size=4,
        shuffle=True,
        num_workers=2
    )

    # 测试集
    test_set = tv.datasets.CIFAR10(
        root='../data/',
        train=False,
        download=True,
        transform=transform
    )

    test_loader = t.utils.data.DataLoader(
        test_set,
        batch_size=4,
        shuffle=False,
        num_workers=2
    )
    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    net = Net()
    print(net)

    # 定义损失函数的变量
    criterion = nn.CrossEntropyLoss()  # 交叉熵损失函数
    '''
    params：要优化的参数。这可以是一个包含参数的列表，也可以是一个包含参数元组的列表。
    lr：学习率（learning rate），用于调整权重更新的步长。
    momentum：动量项，用于加速梯度下降。取值范围在 0 到 1 之间，默认为 0。
    dampening：动量抑制因子，用于抑制动量项的影响。取值范围在 0 到 1 之间，默认为 0。
    weight_decay：权重衰减项，用于正则化。这是 L2 正则化的系数，默认为 0。
    nesterov：布尔值，表示是否使用 Nesterov 动量。默认为 False。
    '''
    # 定义优化函数的变量
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)  # SGD随机梯度下降法优化

    # 切换到GPU训练
    if t.cuda.is_available():
        net.cuda()
        # images = images.cuda()
        # labels = labels.cuda()
        # output = net(Variable(images))
        # loss = criterion(output, Variable(labels))

    show = ToPILImage()  # 可以把Tensor 转成Image ，方便可视化

    dataiter = iter(train_loader)
    # 注意版本不一样,用法有变化
    images, labels = next(dataiter)
    # 输出所取到的(batch_size = 4)4张图片的类别
    print(' '.join('%11s' % classes[labels[j]] for j in range(4)))
    show(tv.utils.make_grid((images + 1) / 2)).resize((400, 100))

    # 训练模型
    for epoch in range(2):
        running_loss = 0.0
        # enumerate(my_list,start=0) 用于迭代列表,同时获取index索引和data数据
        # 第一个参数是要迭代的列表,第二个参数是开始的元素序号index
        for index, data in enumerate(train_loader, 0):
            # 输入数据
            inputs, labels = data

            # GPU
            inputs = inputs.cuda()
            labels = labels.cuda()

            inputs, labels = Variable(inputs), Variable(labels)

            # 初始化,梯度清零
            optimizer.zero_grad()

            # forward 前向传播 + backward 反向传播
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()

            # 更新参数
            optimizer.step()

            # 打印log信息
            # print(loss.data)  # tensor(2.3260)
            '''
            将 loss.data[0] 替换为 loss.item()
            零维张量 loss 的值转换为一个标量，并将其添加到 running_loss 变量中
            
            tensor.item() 方法返回一个 Python 标量，而不是一个张量。
            如果张量具有多个元素，那么 tensor.item() 方法将引发错误。
            在处理单个标量值时，使用 tensor.item() 是一个安全和推荐的做法
            '''
            running_loss = running_loss + loss.item()
            if index % 2000 == 1999:
                print('[%d,%5d] loss:%.3f' % (epoch + 1, index + 1, running_loss / 2000))
                running_loss = 0.0
    print('训练ok了')

    if t.cuda.is_available():
        # net.cuda()
        images = images.cuda()
        labels = labels.cuda()
        output = net(Variable(images))
        loss = criterion(output, Variable(labels))

    # 计算图片在每个类别上的分数
    outputs = net(Variable(images))
    # 得分最高的类
    _, predicted = t.max(outputs.data, 1)

    print('预测结果:', ' '.join('%5s' % classes[predicted[j]] for j in range(4)))

    correct = 0  # 预测正确的图片
    total = 0  # 总共的图片数
    for data in test_loader:
        images, labels = data
        if t.cuda.is_available():
            # net.cuda()
            images = images.cuda()
            labels = labels.cuda()

        outputs = net(Variable(images))
        # _ 代表忽略第一个返回值
        # torch.max(input, dim)：返回输入张量 input 在指定维度 dim 上的最大值
        # t.max(outputs.data, 1) 这部分是在取outputs.data的最大值，并且返回两个值。
        # 第一个值是每一行的最大值，第二个值是最大值的索引
        _, predicted = t.max(outputs.data, 1)
        # tensor.size() 返回一个 torch.Size 对象，它是一个元组。
        # 该元组的长度表示张量的维度数，每个元素表示相应维度的大小
        total = total + labels.size(0)
        # predicted == labels 返回一个布尔值的数组或张量，其中每个元素表示相应的预测值和标签是否相等
        # .sum() 函数会计算所有 True 值的总数
        correct = correct + (predicted == labels).sum()

    print('10000张测试集中的准确率为:%d %%' % (100 * correct / total))
