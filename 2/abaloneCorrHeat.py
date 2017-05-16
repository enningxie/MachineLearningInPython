# coding=utf-8
# 鲍鱼数据的相关性计算
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

abalone = pd.read_csv(target_url, header=None, prefix='V')
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

corMat = DataFrame(abalone.iloc[:, 1:9].corr())
print corMat

plot.pcolor(corMat)
plot.show()