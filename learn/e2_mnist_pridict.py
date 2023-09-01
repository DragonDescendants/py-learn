"""
进行神经网络的推理
这里输入神经元为768个(28*28=768)，输出神经元为10个
此外，这个神经网络有2个隐藏层，第1个隐藏层有50个神经元，第2个隐藏层有100个神经元
(这个50和100可以设置为任何值)
"""
import pickle

from dataset.mnist import load_mnist
import numpy as np

from learn.l1_activation_function import sigmoid
from learn.l2_softmax import softmax

'''
另外，在这个例子中，我们把load_mnist函数的参数normalize设置成了True。
将normalize设置成True后，函数内部会进行转换，
将图像的各个像素值除以255，使得数据的值在0.0～1.0的范围内。
像这样把数据限定到某个范围内的处理称为正规化（normalization）。
此外，对神经网络的输入数据进行某种既定的转换称为预处理（pre-processing）。
这里，作为对输入图像的一种预处理，我们进行了正规化
'''


def get_data():
    # (训练图像 ,训练标签)，(测试图像，测试标签)
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
                                                      normalize=True,
                                                      one_hot_label=False)
    return x_test, t_test


def init_network():
    # "python with" 是一个用于上下文管理的关键字，
    # 可以在Python中用于处理资源的打开和关闭。
    # 通过使用 "with" 关键字，可以确保资源在使用完毕后正常关闭，无论是否发生异常。
    with open("sample_weight.pkl", 'rb') as f:
        # init_network()会读入保存在pickle文件sample_weight.pkl中的学习到的权重参数
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y


'''
现在，我们用这3个函数来实现神经网络的推理处理。
然后，评价它的识别精度（accuracy），即能在多大程度上正确分类
'''

x, t = get_data()
network = init_network()

accuracy_count = 0
# for i in range(len(x)):
#     y = predict(network, x[i])
#     p = np.argmax(y)  # 获取概率最高的元素的索引
#     if p == t[i]:
#         accuracy_count += 1
#
# accuracy = accuracy_count / len(x)
# print("Accuracy:" + str(accuracy))
# Accuracy:0.9352

# 批处理
batch_size = 100
# range(start,stop[,step])根据范围生成列表
for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = predict(network, x_batch)
    # 指定了在100 × 10的数组中，沿着第1维方向（以第1维为轴）找到值最大的元素的索引（第0维对应第1个维度）
    p = np.argmax(y_batch, axis=1)
    accuracy_count += np.sum(p == t[i:i + batch_size])

accuracy = accuracy_count / len(x)
print("Accuracy:" + str(accuracy))