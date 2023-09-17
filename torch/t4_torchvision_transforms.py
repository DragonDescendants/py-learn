from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

'''
transforms.Compose
transforms.Normalize(mean, std)
transforms.Resize(size)
transforms.Scale(size)
transforms.CenterCrop(size)
transforms.RandomCrop(size)
transforms.RandomResizedCrop(size,scale)
transforms.RandomHorizontalFlip
transforms.RandomVerticalFlip
transforms.RandomRotation
transforms.ToTensor
transforms.ToPILImage
'''

image = Image.open('../source/test100.png')
print(image.size)
plt.imshow(image)

# transforms.Compose类看作一种容器，它能够同时对多种数据变换进行组合
# 传入的参数是一个列表，列表中的元素就是对载入的数据进行的各种变换操作
transformer = transforms.Compose([
    # 多种操作的组合
    transforms.Resize(256),
    transforms.transforms.RandomResizedCrop(224, scale=(0.5, 1.0)),
    transforms.RandomHorizontalFlip(),
])
test_a = transformer(image)
plt.imshow(test_a)

# transforms.Normalize(mean, std)
# 使用的是标准正态分布变换，使用原始数据的均值(Mean)和标准差(Standard Deviation)来进行数据的标准化
# 在经过标准化变换之后，数据全部符合均值为0、标准差为1的标准正态分布

# 标准化是把图片3个通道中的数据整理到规范区间 x = (x - mean(x))/stddev(x)
# [0.485, 0.456, 0.406]这一组平均值是从imagenet训练集中抽样算出来的
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

#...

plt.show()


