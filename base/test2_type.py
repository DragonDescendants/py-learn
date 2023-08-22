a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
# 可以通过type()来查看类型
del a, b, c, d
# 通过del删除对象的引用
#     print(a,b,c,d)
#           ^
# NameError: name 'a' is not defined

# Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失
num_a = 1
num_b = 2.6
num_c = num_a + num_b
print(num_c, type(num_c))
# 3.6 <class 'float'>

# 显式转换类型
x = int(1)  # x 输出结果为 1
y = int(2.8)  # y 输出结果为 2
z = int("3")  # z 输出结果为 3
x_f = float(1)  # x 输出结果为 1.0
y_f = float(2.8)  # y 输出结果为 2.8
z_f = float("3")  # z 输出结果为 3.0
w_f = float("4.2")  # w 输出结果为 4.2
x_str = str("s1")  # x 输出结果为 's1'
y_str = str(2)  # y 输出结果为 '2'
z_str = str(3.0)  # z 输出结果为 '3.0'
# chr(x)
# 将一个整数转换为一个字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''
"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""