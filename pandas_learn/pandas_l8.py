"""
读取更复杂的json数据
"""
import json
import os
import pandas as pd
import glom


# 过于复杂的数据直接读取会报错
# dataframe = pd.read_json(os.path.join(os.getcwd(), "pandas_learn", "nested_mix.json"))
# print(dataframe)

with open(os.path.join(os.getcwd(), "pandas_learn", "nested_mix.json"), "r") as file:
    data = json.loads(file.read())

dataframe = pd.json_normalize(data, record_path=["students"])
print(dataframe)
"""
     id   name  math  physics  chemistry
0  A001    Tom    60       66         61
1  A002  James    89       76         51
2  A003  Jenny    79       90         78
"""
dataframe_2 = pd.json_normalize(
    data,
    record_path=["students"],
    meta=["class", ["info", "president"], ["info", "contacts", "tel"]],
    # 以集合中多个元素的格式获取下层数据
)
print(dataframe_2)
"""
     id   name  math  physics  chemistry   class info.president info.contacts.tel
0  A001    Tom    60       66         61  Year 1    John Kasich         123456789
1  A002  James    89       76         51  Year 1    John Kasich         123456789
2  A003  Jenny    79       90         78  Year 1    John Kasich         123456789
"""

# 如果想用和js一样方便的使用.直接取json数据,那么就可以利用到glom
df_deep = pd.read_json(os.path.join(os.getcwd(), "pandas_learn", "nested_deep.json"))
print(
    "-------------------------------\n",
    df_deep["students"].apply(lambda row: glom.glom(row, "grade.math")),
    "\n",
    "-------------------------------\n",
)


# 行列之间的运算
def manage(dataframe):
    return (dataframe + 4) ** 2


def manage_test(dataframe):
    return (dataframe["A"] + dataframe["B"]) ** 2


df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})
print(df)
df["C"] = df["A"] + df["B"]
# 列轴（axis=0）行 axis=1 (默认的axis是0)
df_print = df.apply(manage, axis=0)
df_print_axis_1 = df.apply(manage_test, axis=1)
print(df, "\n", df_print, "\n", df_print_axis_1)

# 使用lambda函数为DataFrame添加一个新列，该列是A和B的和
df["D"] = df.apply(lambda row: row["A"] + row["B"], axis=1)
print(df)
