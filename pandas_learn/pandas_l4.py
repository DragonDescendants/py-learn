import pandas as pd
import os

# os 与 csv 文件

# os.getcwd()获取当前的工作路径
current_directory = os.getcwd()
print(current_directory)

# os.path.join拼接文件路径,注意不要带\否则会覆盖前面的路径
print(os.path.join(os.getcwd(), "pandas_learn", "nba.csv"))

# 获取当前文件的路径
script_directory = os.path.dirname(os.path.abspath(__file__))
print(script_directory)

# 读取csv文件
data_1 = pd.read_csv(os.path.join(os.getcwd(), "pandas_learn", "nba.csv"))
print(data_1)

# to_csv()保存dataframe
# 三个字段 name, site, age
name = ["Google", "Runoob", "Taobao", "Wiki"]
path = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
age = [90, 40, 80, 98]
data_dict = {"name": name, "site": path, "age": age}
test_dataframe = pd.DataFrame(data_dict)
# 指定路径保存为csv
test_dataframe.to_csv(os.path.join(os.getcwd(), "save_file", "save.csv"))
