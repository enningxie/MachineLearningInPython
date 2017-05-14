# coding=utf-8
# 实数值属性的可视化：平行坐标图
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

for i in range(208):
    if rocksVMines.iat[i, 60] == 'M':
        pcolor = 'red'
    else:
        pcolor = 'blue'

    dataRow = rocksVMines.iloc[i, 0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()