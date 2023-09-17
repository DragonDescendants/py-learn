import torch as t
import torchvision as tv
# 在torch.transforms中有大量的数据变换类，有很大一部分可以用于
# 实现数据预处理(Data Preprocessing)和数据增广(Data Argumentation)
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from torchvision.transforms import ToPILImage

if __name__ == '__main__':
    # 主程序的代码

    show = ToPILImage()  # 可以把Tensor 转成Image ，方便可视化

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

    # Dataset 象是 个数据集，可以按下标访问，返回形如（ data, label ）的数据
    (data, label) = train_set[100]
    print(label, classes[label])

    # (data + 1)/2 可以还原归一化的数据
    image = show((data + 1) / 2).resize((100, 100))
    plt.imshow(image)
    plt.show()

    '''
    Dataloader 是一个可迭代的对象，它将 dataset 返回的每一条数据样本拼接成一个
    batch 并提供多线程加速优化和数据打乱等操作 当程序对 dataset 的所有数据遍历完
    遍之后，对 Dataloader 完成了一次迭代
    '''

    dataiter = iter(train_loader)
    # 注意版本不一样,用法有变化
    images, labels = next(dataiter)
    # 输出所取到的(batch_size = 4)4张图片的类别
    print(' '.join('%11s' % classes[labels[j]] for j in range(4)))
    images = show(tv.utils.make_grid((images + 1) / 2)).resize((400, 100))
    plt.imshow(images)
    plt.show()

