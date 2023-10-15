import pandas as pd

# 清洗重复数据
person = {"name": ["Google", "Runoob", "Runoob", "Taobao"], "age": [50, 40, 40, 23]}

dataframe = pd.DataFrame(person)
print(dataframe)

# 删除重复数据，可以直接使用drop_duplicates() 方法
dataframe.drop_duplicates(inplace=True)  # 注意设置inplace=True
print(dataframe)
'''
     name  age
0  Google   50
1  Runoob   40
2  Runoob   40
3  Taobao   23
     name  age
0  Google   50
1  Runoob   40
3  Taobao   23
'''