# coding=utf-8
# 用Python Pandas读入数据、分析数据
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

print rocksVMines.head()
print rocksVMines.tail()

summary = rocksVMines.describe()
print summary