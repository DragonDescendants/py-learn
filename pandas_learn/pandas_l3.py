import pandas as pd

data_1 = [["Google", 10], ["Baidu", 12], ["Bing", 13]]
print(type(data_1))  # <class 'list'>
# 这里可以直接使用dtype参数指定类型,但是仅限于所有参数都是一个类型的情况
dataframe_test_1 = pd.DataFrame(data_1, columns=["Engine", "No"])
print(dataframe_test_1, "\n")

data_2 = {"Site": ["Google", "Baidu", "Bing"], "No": [10, 12, 13]}
print(type(data_2))  # <class 'dict'>
dataframe_test_2 = pd.DataFrame(data_2)
print(dataframe_test_2, "\n")

data_3 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}, {"a": 666}]
print(type(data_3))  # <class 'list'>
dataframe_test_3 = pd.DataFrame(data_3)
print(dataframe_test_3, "\n")  # 没有对应的部分数据为 NaN
"""
     a     b     c
0    1   2.0   NaN
1    5  10.0  20.0
2  666   NaN   NaN
"""

# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推
# 返回第一(index:0)行
print(dataframe_test_3.loc[0])
"""
a    1.0
b    2.0
c    NaN
Name: 0, dtype: float64
"""
# 返回第二(index:1)行
print(dataframe_test_3.loc[1])
"""
a     5.0
b    10.0
c    20.0
Name: 1, dtype: float64
"""
# 返回多行数据
# 返回第一行和第二行
print(dataframe_test_3.loc[[0, 1]], "\n")

# 指定索引值
data_4 = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
dataframe_test_4 = pd.DataFrame(data_4, index=["day1", "day2", "day3"])
print(dataframe_test_4, "\n")
# 指定索引
print(dataframe_test_4.loc["day2"])
