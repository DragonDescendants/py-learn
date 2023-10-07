import pandas as pd
import os

data_nba = pd.read_csv(os.path.join(os.getcwd(), "pandas_learn", "nba.csv"))
print(data_nba)
# head()是获取头部数据的方法,不传参默认获取头部前5条
print(data_nba.head())
print(data_nba.head(10))
# tail()是获取尾部数据的方法,不传参默认获取尾部后5条
print(data_nba.tail())
print(data_nba.tail(8), "\n")
# info()是查看表格信息的方法
print(data_nba.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 458 entries, 0 to 457
Data columns (total 9 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Name      457 non-null    object
 1   Team      457 non-null    object
 2   Number    457 non-null    float64
 3   Position  457 non-null    object
 4   Age       457 non-null    float64
 5   Height    457 non-null    object
 6   Weight    457 non-null    float64
 7   College   373 non-null    object
 8   Salary    446 non-null    float64
dtypes: float64(4), object(5)
memory usage: 32.3+ KB
None
"""
