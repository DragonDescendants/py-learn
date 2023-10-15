import pandas as pd
import os

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
