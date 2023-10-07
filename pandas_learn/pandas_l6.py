import pandas as pd
import os, json

# json file
data_json = pd.read_json(os.path.join(os.getcwd(), "pandas_learn", "test.json"))
print(data_json, data_json.to_string())

# py文件内的json
data_test_json_str = [
    {"id": "A001", "name": "菜鸟教程", "url": "www.runoob.com", "likes": 61},
    {"id": "A002", "name": "Google", "url": "www.google.com", "likes": 124},
    {"id": "A003", "name": "淘宝", "url": "www.taobao.com", "likes": 45},
]

# 字典格式的 JSON
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "x", "row2": "y", "row3": "z"},
}
# 便捷将json数据转化为dataframe
data_json_2 = pd.DataFrame(data_test_json_str)
data_json_3 = pd.DataFrame(s)
print(data_json_2, "\n", data_json_3)

# 从 URL 中读取 JSON 数据
URL = "https://static.runoob.com/download/sites.json"
df = pd.read_json(URL)
print(df)

# df_2 = pd.read_json("nested_list.json")
df_2 = pd.read_json(os.path.join(os.getcwd(), "pandas_learn", "nested_list.json"))
print(df_2)
"""
          school_name   class                                           students
0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...
这里会注意到如果json有嵌套数据则不能完美展示
"""

