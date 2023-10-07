import pandas as pd

# 清洗格式错误数据
# 第三个日期格式错误
data = {"Date": ["2020/12/01", "2020/12/02", "20201226"], "duration": [50, 40, 45]}

df1 = pd.DataFrame(data, index=["day1", "day2", "day3"])

# format 要指定日期的格式
# df1["Date"] = pd.to_datetime(df1["Date"], format="mixed")
df1["Date"] = pd.to_datetime(df1["Date"], format="ISO8601")

print(df1)


# 清洗错误的数据
person = {
    "name": ["Google", "Runoob", "Taobao"],
    "age": [50, 40, 12345],  # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)
df2 = pd.DataFrame(person)
df3 = pd.DataFrame(person)
# 单独对某一个数据进行修改
df.loc[2, "age"] = 30  # 修改数据
print(df)

# 设置条件语句修改
for x in df2.index:
    if df2.loc[x, "age"] > 120:
        df2.loc[x, "age"] = 120
print(df2)
"""
     name  age
0  Google   50
1  Runoob   40
2  Taobao  120
"""
# 将错误数据的行删除
for x in df3.index:
    if df3.loc[x, "age"] > 120:
        df3.drop(x, inplace=True)
print(df3)
"""
     name  age
0  Google   50
1  Runoob   40
"""

# ...
