import pandas as pd

"""
Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型
Series 由索引（index）和列组成，函数如下：
pandas.Series( data, index, dtype, name, copy)

参数说明：
data：一组数据(ndarray 类型)。
index：数据索引标签，如果不指定，默认从 0 开始。
dtype：数据类型，默认会自己判断。
name：设置名称。
copy：拷贝数据，默认为 False。
"""
# 创建 series
a = [1, 2, 3]
test = pd.Series(a)
print(test)
"""
索引 数据
0    1
1    2
2    3
dtype: int64
"""
# 读取 series
print(test[1])  # 2

# 指定索引值创建
b = ["Mike", "Bob", "Nick"]
index = ["x", "y", "z"]
test_series = pd.Series(b, index=index)
print(test_series, test_series["z"])  # Nick 通过索引'z'访问
"""
x    Mike
y     Bob
z    Nick
dtype: object
"""

# 也可以用key-value对象创建 series
source_map = {1: "haha", 2: "xixi", 3: "heihei", 4: "huohuo"}
# 通过指定index可以只取部分数据 通过指定name可以定义series的名字
test_series_2 = pd.Series(source_map, index=[2, 4], name="Series-TEST")
print(test_series_2, test_series_2[2])  # xixi
"""
2      xixi
4    huohuo
Name: Series-TEST, dtype: object
"""
