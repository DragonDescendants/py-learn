"""
训练集 
测试集
分类:从有限的类别中,给每个样本贴上正确的标签
回归:如果期望的输出由一个或多个连续变量组成,则该任务称为回归
有监督学习:数据带有预期的结果
无监督学习:没有给定预期结果,数据是自己聚类或密度估计等等
"""

from matplotlib import pyplot as plt
from sklearn import datasets


iris = datasets.load_iris()  # 加载iris数据集
# 1797个样本，每个样本包括8*8像素的图像和一个[0, 9]整数的标签
digits = datasets.load_digits()  # 加载digits数据集
# data即数据,target即标签
# print("data:\n", iris.data, "\ntarget:\n", iris.target)
print(digits.keys())

print(digits.images[-1])
plt.imshow(digits.images[-1])
# print(digits.data[-1:])

# test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(test, test[:-1], test[-1:])

"""
学习和预测
分类的估计器是一个Python对象,实现了fit(X,y)和predict(T)等方法
"""
from sklearn import svm

classifier = svm.SVC(gamma=0.001, C=100)  # 创建分类器对象
classifier.fit(digits.data[:-1], digits.target[:-1])
print("预测值:", classifier.predict(digits.data[-1:]), "\n", "实际值:", digits.target[-1:])
