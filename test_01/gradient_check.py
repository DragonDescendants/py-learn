# 读入数据
import numpy as np

from dataset.mnist import load_mnist
from test_01.TwoLayerNet import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

# 切片,取0,1,2前3行
x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)

print('------------各个权重的绝对误差的平均值-----------------')
# 求各个权重的绝对误差的平均值
# 通过.keys()取出字典的所有key遍历
for key in grad_numerical.keys():
    # 求各个误差的绝对值,然后取平均值
    diff = np.average(np.abs(grad_backprop[key] - grad_numerical[key]))
    print(key + ":" + str(diff))
