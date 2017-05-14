# coding=utf-8
# 分类问题标签和实数值属性之间的相关性
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

target = []
for i in range(208):
    if rocksVMines.iat[i, 60] == 'M':
        target.append(1.0)
    else:
        target.append(0.0)

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

target = []
for i in range(208):
    if rocksVMines.iat[i, 60] == 'M':
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=160)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()