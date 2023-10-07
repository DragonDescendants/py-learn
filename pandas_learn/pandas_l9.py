import pandas as pd
import os

"""
在前面的使用中会发现许多地方存在数据缺失这种NAN的状况
很多数据集存在数据缺失、数据格式错误、错误数据或重复数据的情况
如果想要让分析的结果准确,就需要手动清除这些问题
"""
file_path = os.path.join(os.getcwd(), "pandas_learn", "property-data.csv")
df = pd.read_csv(file_path)
print(df)
print(df["NUM_BEDROOMS"])
# 使用isnull()函数来判断每一行是否为空值
print(df["NUM_BEDROOMS"].isnull())
"""
0      3
1      3
2    NaN
3      1
4      3
5    NaN
6      2
7      1
8     na
Name: NUM_BEDROOMS, dtype: object
0    False
1    False
2     True
3    False
4    False
5     True
6    False
7    False
8    False
Name: NUM_BEDROOMS, dtype: bool
Pandas 把 n/a 和 NA 当作空数据,
但认为na 不是空数据，结果不符合我们要求
"""
# 默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数
# df.dropna(inplace = True)
new_df = df.dropna()
print(new_df)
"""
           PID  ST_NUM    ST_NAME OWN_OCCUPIED NUM_BEDROOMS NUM_BATH SQ_FT
0  100001000.0   104.0     PUTNAM            Y            3        1  1000
1  100002000.0   197.0  LEXINGTON            N            3      1.5    --
8  100009000.0   215.0    TREMONT            Y           na        2  1800
na 并没有被清洗掉
"""

# 指定哪些情况是空数据
missing_values = ["n/a", "na", "--"]
df2 = pd.read_csv(file_path, na_values=missing_values)

print(df2)
print(df2["NUM_BEDROOMS"].isnull())
"""
           PID  ST_NUM     ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0   104.0      PUTNAM            Y           3.0        1  1000.0
1  100002000.0   197.0   LEXINGTON            N           3.0      1.5     NaN
2  100003000.0     NaN   LEXINGTON            N           NaN        1   850.0
3  100004000.0   201.0    BERKELEY           12           1.0      NaN   700.0
4          NaN   203.0    BERKELEY            Y           3.0        2  1600.0
5  100006000.0   207.0    BERKELEY            Y           NaN        1   800.0
6  100007000.0     NaN  WASHINGTON          NaN           2.0   HURLEY   950.0
7  100008000.0   213.0     TREMONT            Y           1.0        1     NaN
8  100009000.0   215.0     TREMONT            Y           NaN        2  1800.0
Name: NUM_BEDROOMS, dtype: float64
0    False
1    False
2     True
3    False
4    False
5     True
6    False
7    False
8     True
Name: NUM_BEDROOMS, dtype: bool
"""
df2.dropna(inplace=True)
print(df2)
"""
           PID  ST_NUM ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0   104.0  PUTNAM            Y           3.0        1  1000.0
"""
