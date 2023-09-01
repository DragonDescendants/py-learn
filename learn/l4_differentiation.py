import numpy as np
import matplotlib.pylab as plt


# 不太好的求导函数
# 因为想让h接近0,就使用了10e-50这样的极小数
# 但是极小数在计算时又会产生舍入误差,被计算机视为0.0
def non_good_numerical_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h


'''
利用微小的差分求导数的过程称为数值微分（numerical differentiation）
而基于数学式的推导求导数的过程，则用“解析性”（analytic）一词，
称为“解析性求解”或者“解析性求导”。解析性求导求出来的是精确的
'''


# 为了减小误差，计算函数f在(x + h)和(x − h)之间的差分
# 这种方法以x为中心,计算左右两边+h -h的差分,又称为中心差分
def numerical_diff(f, x):
    h = 1e-4  # 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)


# y = 0.01x2 + 0.1x
def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x


# 做出fun1的图像
# x = np.arange(0.0, 20.0, 0.1)  # 以0.1为单位，从0到20的数组x
# y = function_1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(x, y)
# plt.show()

# 求fun1在x=5和x=10处的导数
print(numerical_diff(function_1, 5), numerical_diff(function_1, 10))


# 0.1999999999990898 0.2999999999986347 和精确导数 0.2 0.3 是近似的

# f(x0,x1) = x0^2 + x1^2 偏导数
def function_2(x):
    return x[0] ** 2 + x[1] ** 2
    # 或者return np.sum(x**2)


# x0 = 3,x1 = 4,求关于x0的偏导数
def function_tmp1(x0):
    return x0 * x0 + 4.0 ** 2.0


print(numerical_diff(function_tmp1, 3.0))


# 6.00000000000378

# x0 = 3,x1 = 4,求关于x1的偏导数
def function_tmp2(x1):
    return 3.0 ** 2.0 + x1 * x1


print(numerical_diff(function_tmp2, 4.0))
# 7.999999999999119

# gradient

