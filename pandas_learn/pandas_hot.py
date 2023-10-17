import pandas as pd
import os
import sqlite3

# 读取各种类型的数据
"""
pd.read_csv()
pd.read_excel()
pd.read_sql()
pd.read_json()
pd.read_html()
"""
base_path = os.path.join(os.getcwd(), "pandas_learn")
csv_path = os.path.join(base_path, "nba.csv")
dataframe1 = pd.read_csv(csv_path)
print("dataframe1:\n", dataframe1)
# conda install openpyxl
excel_path = os.path.join(base_path, "test_excel.xlsx")
print(excel_path)
dataframe2 = pd.read_excel(excel_path)
print("dataframe2:\n", dataframe2)
# conda install -c blaze sqlite3
# ....
# connection = sqlite3.connect("database.db")
# dataframe3 = pd.read_sql("select * from table_name", connection)
# 从 JSON 字符串中读取数据
json_path = os.path.join(base_path, "test.json")
dataframe4 = pd.read_json(json_path)
print("dataframe4:\n", dataframe4)
# 从 HTML 页面中读取数据
# url = "https://www.runoob.com"
# dataframes = pd.read_html(url)
# # dataframe5 = dataframes[0]  # 选择第一个数据框
# print("dataframe5:", dataframes)


# 获取数据的一些基本信息
"""
head()
tail()
info()
describe()
shape
"""
head = dataframe1.head()  # 默认5行
tail = dataframe1.tail()  # 默认5行
info = dataframe1.info()  # 显示数据的信息，包括列名、数据类型、缺失值等
descibe = dataframe1.describe()  # 显示数据的基本统计信息，包括均值、方差、最大值、最小值等
shape = dataframe1.shape  # (458, 9) 行数和列数
print(
    "infomations:\n",
    head,
    "\n",
    tail,
    "\n",
    info,
    "\n",
    head,
    "\n",
    descibe,
    "\n",
    shape,
    "\n",
)

# 基本的数据清洗操作
"""
dropna()
fillna()
replace()
duplicated()
drop_duplicates()
"""
print(
    "Data cleansing:\n",
    dataframe1[0:10].dropna(),  # 抛弃掉nan的所有行
    "\n",
    dataframe1[0:10].fillna(10),  # 用10去填充nan的地方
    "\n",
    dataframe1[0:10].replace("PG", "新智"),  # 将指定值替换为新值
    "\n",
    dataframe1[0:10].duplicated(),  # 检查是否有重复的数据
    "\n",
    dataframe1[0:10].drop_duplicates(),  # 删除重复的数据
    "\n",
)

# 数据选择与切片
"""
dataframe[column_name] 选择指定的列
dataframe.loc[row_index, column_name] 通过标签选取数据
dataframe.iloc[row_index, column_index] 通过位置选取数据
dataframe.ix[row_index, column_name] 通过标签或者位置选取数据(已废弃)
dataframe.at[row_index, column_name] 对于单个元素的快速访问
dataframe.filter(items=[column_name1, column_name2]) 选择指定的列
dataframe.filter(regex='regex') 按照正则表达式获取列
dataframe.sample(n) 随机选择n行数据
"""
print("随机选取n行数据:\n", dataframe1.sample(10), "\n")
print("选取指定的列:\n", dataframe1["Team"].sample(6), "\n")
print("根据行号和列名取数据:\n", dataframe1.loc[10, "Team"], "\n")
print("根据行号和列号取数据:\n", dataframe1.iloc[10, 1], "\n")
print("根据行号和列号取多行多列数据:\n", dataframe1.iloc[10:20, 1:6], "\n")
print("对于单个元素的快速访问:\n", dataframe1.at[10, "Team"], "\n")
print("只取指定的列:\n", dataframe1.filter(items=["Team", "Position"]).sample(10), "\n")

# 数据排序
"""
dataframe.sort_values(column_name) 按照列的值排序 
dataframe.sort_values([column_name1, column_name2], ascending=[True, False]) 按照多个列的值排序
ascending: 一个布尔值的列表,用于指定每个排序列是升序(True)还是降序(False)
dataframe.sort_index() 按照索引排序
"""
print("按照某一列的值排序:\n", dataframe1.sort_values("Age").head(10), "\n")
print(
    "按照多个列的值排序:\n",
    dataframe1.sort_values(["Age", "Weight", "Number"]).head(10),
    "\n",
)
print(
    "按照多个列的值排序:\n",
    dataframe1.sort_values(
        ["Age", "Weight", "Number"], ascending=[False, True, True]
    ).head(10),
    "\n",
)
# 排序索引
data = {"A": [3, 1, 2, 4, 5]}
index = [4, 2, 5, 1, 3]
dataframe6 = pd.DataFrame(data, index=index)
print(
    "原始数据:\n",
    dataframe6,
    "\n",
    "排序后的数据:\n",
    dataframe6.sort_index(),
    "\n",
    "排序后的数据(降序):\n",
    dataframe6.sort_index(ascending=False),
    "\n",
)

# 数据分组和聚合
"""
dataframe.groupby(column_name) 	按照指定列进行分组
dataframe.aggregate(function_name) 对分组后的数据进行聚合操作
dataframe.pivot_table(values, index, columns, aggfunc) 生成透视表
"""
group_result = dataframe1.groupby("Team")
mean_result = group_result["Salary"].mean()
print("求各team的平均薪水:\n", mean_result, "\n")
# value作为计算值,index作为聚合的标准,aggfunc是作用的函数
"""
aggfunc支持的字符串聚合函数:
'sum': 计算总和。
'mean': 计算平均值。
'median': 计算中位数。
'min': 计算最小值。
'max': 计算最大值。
'count': 计算非NA值的数量。
'std': 计算标准偏差。
'var': 计算方差。
"""
print(
    "生成透视表:\n",
    dataframe1.pivot_table(values="Salary", index="Team", aggfunc="mean"),
    "\n",
)


# 自定义一个聚合函数
def custom_agg_func(x):
    return x.sum() / x.count() + 1  # 例如，计算平均值并 +1


print(
    "根据自定义函数生成透视表:\n",
    dataframe1.pivot_table(values="Salary", index="Team", aggfunc=custom_agg_func),
    "\n",
)

# 数据合并
"""
pd.concat([df1, df2]) 将多个数据框按照行或列进行合并
pd.merge(df1, df2, on=column_name,how='left') 	按照指定列将两个数据框进行连接
"""
dataframe_concat1 = pd.concat([dataframe1, dataframe2])
print("concat两个dataframe:\n", dataframe_concat1, "\n")
data1 = {"key": ["A", "B", "C", "D"], "value1": [1, 2, 3, 4]}
df1 = pd.DataFrame(data1)
data2 = {"key": ["B", "D", "E", "F"], "value2": [5, 6, 7, 8]}
df2 = pd.DataFrame(data2)
# 所缺少的值会被NaN填充
print("merge左连接:\n", pd.merge(df1, df2, on="key", how="left"), "\n")

# 数据选择与过滤
"""
dataframe[dataframe['column_name'] > value] 保留某一列值大于某数的元素
dataframe.query('column_name > value') query提供条件查询
"""
print(
    "保留Salary>7730337.0的所有元素:\n",
    dataframe1[dataframe1["Salary"] > 7730337].sort_values("Salary").head(),
    "\n",
)
print("通过query来实现:\n", dataframe1.query("Salary>7730337").sort_index().head(), "\n")

# 数据统计和描述
"""
df.describe() 计算基本统计信息，如均值、标准差、最小值、最大值等
df.mean() 计算每列的平均值
df.median() 计算每列的中位数
df.mode() 计算每列的众数
df.count() 计算每列非缺失值的数量
"""
print("基本信息:\n", dataframe1.describe(), "\n")
