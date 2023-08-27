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
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)  # 获取概率最高的元素的索引
    if p == t[i]:
        accuracy_count += 1

accuracy = accuracy_count / len(x)
print("Accuracy:" + str(accuracy))
# Accuracy:0.9352
