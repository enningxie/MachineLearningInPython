# coding=utf-8
# 数值型和类别型属性的统计信息
import urllib2
import sys
import numpy as np

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

xList = []
labels = []
for line in data:
    row = line.strip().split(",")
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

# 第4列统计分析
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))
colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = " + "\t" + str(colMean) + "\t\t" + "Std = " + "\t" + str(colsd) + "\n")

ntiles = 4

percentBdry = []

for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("Boundaries for 4 Equal Percentiles \n")
print percentBdry
sys.stdout.write("\n")

ntiles = 10
percentBdry = []

for i in range(ntiles + 1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print percentBdry
sys.stdout.write("\n")

col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print unique

catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0]*2

for elt in colData:
    catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print list(unique)
print catCount

