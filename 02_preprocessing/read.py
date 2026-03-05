# -*- coding: utf-8 -*-
import pandas as pd

file_path = 'data.csv'
try:
  df = pd.read_csv(file_path,encoding = 'gbk')
  print("CSV 文件已读取成功")
  print(df.head())
except FileNotFoundError:
  print("File not found")  