# coding=utf-8
# 鲍鱼数据的平行坐标图
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from math import exp

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

abalone = pd.read_csv(target_url, header=None, prefix='V')
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

summary = abalone.describe()
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(abalone.index)

for i in range(nrows):
    dataRow = abalone.iloc[i, 1:8]
    labelColor = (abalone.iloc[i, 8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()

meanRings = summary.iloc[1, 7]
sdRings = summary.iloc[2, 7]

for i in range(nrows):
    dataRow = abalone.iloc[i, 1:8]
    normTarget = (abalone.iloc[i, 8] - meanRings) / sdRings
    labelColor = 1.0 / (1.0 + exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.show()