import json
import os
import pandas as pd

"""
          school_name   class                                           students
0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...
这里会注意到如果json有嵌套数据则不能完美展示
"""
# 这时我们就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来


with open(os.path.join(os.getcwd(), "pandas_learn", "nested_list.json"), "r") as file:
    data_file = json.loads(file.read())

# 展平数据
df_nested_list = pd.json_normalize(data_file, record_path=["students"])
print(df_nested_list)
"""
     id   name  math  physics  chemistry
0  A001    Tom    60       66         61
1  A002  James    89       76         51
2  A003  Jenny    79       90         78
"""
# 显示结果还没有包含 school_name 和 class 元素，
# 如果需要展示出来可以使用 meta 参数来显示这些元数据
df_nested_list_and_meta = pd.json_normalize(
    data_file, record_path=["students"], meta=["class", "school_name"]
)
print(df_nested_list_and_meta)
"""
     id   name  math  physics  chemistry   class         school_name
0  A001    Tom    60       66         61  Year 1  ABC primary school
1  A002  James    89       76         51  Year 1  ABC primary school
2  A003  Jenny    79       90         78  Year 1  ABC primary school
"""
