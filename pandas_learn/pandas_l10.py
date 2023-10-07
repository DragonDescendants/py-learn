import os
import pandas as pd

"""
对具体的列进行清理
"""

file_path = os.path.join(os.getcwd(), "pandas_learn", "property-data.csv")
# 指定哪些情况是空数据
missing_values = ["n/a", "na", "--"]
# filepath na_values na_filters name
df = pd.read_csv(file_path, na_values=missing_values)
print(df)
"""
           PID  ST_NUM     ST_NAME OWN_OCCUPIED NUM_BEDROOMS NUM_BATH SQ_FT
0  100001000.0   104.0      PUTNAM            Y            3        1  1000
1  100002000.0   197.0   LEXINGTON            N            3      1.5    --
2  100003000.0     NaN   LEXINGTON            N          NaN        1   850
3  100004000.0   201.0    BERKELEY           12            1      NaN   700
4          NaN   203.0    BERKELEY            Y            3        2  1600
5  100006000.0   207.0    BERKELEY            Y          NaN        1   800
6  100007000.0     NaN  WASHINGTON          NaN            2   HURLEY   950
7  100008000.0   213.0     TREMONT            Y            1        1   NaN
8  100009000.0   215.0     TREMONT            Y           na        2  1800
"""
# subset 指定具体的列名
df.dropna(subset=["ST_NUM", "NUM_BEDROOMS"], inplace=True)
print(df)
"""
          PID  ST_NUM    ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0   104.0     PUTNAM            Y           3.0        1  1000.0
1  100002000.0   197.0  LEXINGTON            N           3.0      1.5     NaN
3  100004000.0   201.0   BERKELEY           12           1.0      NaN   700.0
4          NaN   203.0   BERKELEY            Y           3.0        2  1600.0
7  100008000.0   213.0    TREMONT            Y           1.0        1     NaN
"""
# 可以用fillna() 方法来替换一些空字段
df2 = pd.read_csv(file_path, na_values=missing_values)
df2.fillna(666, inplace=True)
print(df2)
"""
          PID  ST_NUM     ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0   104.0      PUTNAM            Y           3.0        1  1000.0
1  100002000.0   197.0   LEXINGTON            N           3.0      1.5   666.0
2  100003000.0   666.0   LEXINGTON            N         666.0        1   850.0
3  100004000.0   201.0    BERKELEY           12           1.0      666   700.0
4        666.0   203.0    BERKELEY            Y           3.0        2  1600.0
5  100006000.0   207.0    BERKELEY            Y         666.0        1   800.0
6  100007000.0   666.0  WASHINGTON          666           2.0   HURLEY   950.0
7  100008000.0   213.0     TREMONT            Y           1.0        1   666.0
8  100009000.0   215.0     TREMONT            Y         666.0        2  1800.0
"""
df3 = pd.read_csv(file_path, na_values=missing_values)
# 只替换指定列
df3["NUM_BEDROOMS"].fillna(666, inplace=True)
print(df3)
"""
           PID  ST_NUM     ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0   104.0      PUTNAM            Y           3.0        1  1000.0
1  100002000.0   197.0   LEXINGTON            N           3.0      1.5     NaN
2  100003000.0     NaN   LEXINGTON            N         666.0        1   850.0
3  100004000.0   201.0    BERKELEY           12           1.0      NaN   700.0
4          NaN   203.0    BERKELEY            Y           3.0        2  1600.0
5  100006000.0   207.0    BERKELEY            Y         666.0        1   800.0
6  100007000.0     NaN  WASHINGTON          NaN           2.0   HURLEY   950.0
7  100008000.0   213.0     TREMONT            Y           1.0        1     NaN
8  100009000.0   215.0     TREMONT            Y         666.0        2  1800.0
"""

# 替换空单元格的常用方法是:
# 计算列的均值mean()、中位数值median()或众数mode()
df_mean = pd.read_csv(file_path, na_values=missing_values)
x = df_mean["ST_NUM"].mean()  # .median() .mode()
df_mean["ST_NUM"].fillna(x, inplace=True)
print(df_mean)
"""
           PID      ST_NUM     ST_NAME OWN_OCCUPIED  NUM_BEDROOMS NUM_BATH   SQ_FT
0  100001000.0  104.000000      PUTNAM            Y           3.0        1  1000.0
1  100002000.0  197.000000   LEXINGTON            N           3.0      1.5     NaN
2  100003000.0  191.428571   LEXINGTON            N           NaN        1   850.0
3  100004000.0  201.000000    BERKELEY           12           1.0      NaN   700.0
4          NaN  203.000000    BERKELEY            Y           3.0        2  1600.0
5  100006000.0  207.000000    BERKELEY            Y           NaN        1   800.0
6  100007000.0  191.428571  WASHINGTON          NaN           2.0   HURLEY   950.0
7  100008000.0  213.000000     TREMONT            Y           1.0        1     NaN
8  100009000.0  215.000000     TREMONT            Y           NaN        2  1800.0
"""
