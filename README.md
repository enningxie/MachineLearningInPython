# Python 机器学习
## 预测分析核心算法
### 简介
本文主要介绍了机器学习算法的两大类：惩罚线性回归（岭回归、Lasso算法）；集成方法（随机森林、梯度提升算法）。  

惩罚线性回归代表了对最小二乘法回归方法的相对较新的改善和提高。惩罚线性回归具有的几个特征使其成为预测分析的首选，惩罚线性回归引入了一个可调参数，使最终的模型在过拟合与欠拟合之间达到了平衡。  

集成方法是目前最有力的预测分析工具之一。它可以对特别复杂的行为进行建模，特别是过定的问题，由于集成方法的性能，许多经验丰富的数据科学家在做第一次尝试时都使用该方法。集成方法使用相对简单，而且可以依据对预测的贡献程度对特征排序。  

目前集成方法与惩罚线性回归齐头并进，惩罚线性回归是从克服一般回归方法的局限性进化而来的，集成方法是从克服二元决策树的局限性进化而来的。

### 第一章 关于预测的两类核心算法
本书集中于机器学习领域，只关注那些最有效和获得广泛使用的算法。

函数逼近问题是有监督学习问题的一个子集。

解决函数逼近问题的两类算法：惩罚线性回归和集成方法。

面对实践中遇到的绝大多数预测分析（函数逼近）问题，这两类算法都具有最优或接近最优的性能。

当数据含有大量的特征时，但没有足够多的数据或时间来训练更复杂的集成方法模型时，惩罚回归方法将优于其他算法。

惩罚线性回归模型一个重要优势就是它训练所需时间（训练时间快），部署已训练好的模型后进行预测的时间也特别快。

研究表明惩罚线性回归在许多情况下可以提供最佳的答案，在即使不是最佳答案的情况下，也可以提供接近最佳的答案。

在预测模型构建过程中，最耗时的一步就是特征提取或者叫做特征工程。

惩罚线性回归方法是由普通最小二乘法衍生出来的，其设计之初的想法就是克服最小二乘法的根本缺陷，最小二乘法的一个根本问题就是有时它会过拟合。

自由度：统计学上的自由度是指当以样本的统计量来估计总体的参数时，样本中独立或能自由变化的自变量的个数称为该统计量的自由度。

惩罚线性回归可以减少自由度使之与数据规模、问题的复杂度相匹配。对于具有大量自由度的问题，惩罚线性回归方法获得了广泛的应用。

集成方法的基本思想是构建多个不同的预测模型，然后将其输出做某种组合作为最终的输出，如取平均值或采用多数人的意见（投票）。

由于某些机器学习算法输出结果不稳定，这一问题导致了集成方法的提出。

即使在某些情况下，惩罚线性回归的性能不如集成方法，它也可以是建立一个机器学习系统的有意义的第一步尝试。

如果一个问题不是很复杂，而且不能获得足够多的数据，则线性方法比更加复杂的集成方法可能会获得全面更优的性能。

线性模型倾向于训练速度快，并且经常能够提供与非线性集成方法相当的性能，特别是当能获取的数据受限时。因为它们训练时间短，在早期特征选取阶段训练线性模型是很方便的，然后可以据此大致估计针对特定问题可以达到的性能。线性模型可以提供关于特征对预测的相关信息，可以辅助特征选取阶段的工作。在有充足数据的情况下，集成方法通常能提供更好的性能，也可以提供相对间接的关于结果的贡献的评估。

构建预测模型的流程：
- 提取或组合预测所需的特征
- 设定训练目标
- 训练模型
- 评估模型在测试数据上的性能表现

特征提取就是一个把自由形式的各种数据转换成行、列形式的数字的过程。

特征工程就是对特征进行整理组合，以达到更富有信息量的过程。

### 第二章 通过理解数据来了解问题

熟悉数据集。

机器学习数据集通常列对应一个属性，行对应一个观察（实例）。

属性就是在具体实例中用来预测的数据，标签就是需要预测的数据。

预测通常不用用户ID信息，因为它太特殊了。

构建预测模型的过程叫做训练。

惩罚回归算法只能处理数值变量，SVM、核方法、K近邻也是同样。

标签是数值的，就叫做回归问题；当标签是类别的，就叫做分类问题。

检查新数据集的步骤：
- 行数、列数
- 类别变量的数目、类别的取值范围
- 缺失的值
- 属性和标签的统计特性

第一个要确定的就是数据的规模。将数据读入二维数组，则外围数组的维度就是行数，内部数组的维度就是列数。

处理缺失数据的方法：
- 直接丢弃缺失值
- 填补缺失值

遗失值插补的最简单的方法就是用每行所有此项的值的平均值来代替遗失的值。

#### 分类问题：用声纳发现未爆炸的水雷

如果数据集的列数远远大于行数，那么采用惩罚线性回归的方法则有很大的可能获得最佳的预测。

更加具体地研究异常点（异常值）的一个方法就是画出数据的分布图，然后与可能的分布进行比较，判断相关的数据是否匹配。

异常点在建模或预测期间都会带来麻烦。

一个可行办法是在对数据集进行探究阶段，先产生四分位数边界，然后看看潜在的异常点的规模对后续建模及预测可能的影响。这样在分析错误时，可以通过分位数图，确定哪些数据可以称为异常点。

分层抽样。

Python Pandas工具包可以帮助自动化数据统计分析的过程，已经被证实在数据预处理阶段特别有用。

可以比较不同分位数之间的差异。对于同一属性列，如果存在某一个差异严重异于其它差异，则说明存在异常点。

可视化可以提供对数据的直观感受，这个有时是很难通过表格的形式把握到的。

对具有多个属性问题的一种可视化方法叫做平行坐标图。

另一个需要了解的问题就是属性之间的关系。获得这种成对关系的快速方法就是绘制属性与标签的交会图。

基本上，如果散点图上的点沿着一条“瘦”直线排列，则说明这两个变量强相关；如果这些点形成一个球型，则说明这些点不相关。

两个属性（或一个属性、一个标签）的相关程度可以由皮尔逊相关系数来量化。

对于计算少量的相关性，将相关性结果打印输出或者画成散点图都是可以的。但对于大量的数据，就很难用这种方法整体把握相关性。（热图）

属性之间如果完全相关（相关系数=1）意味着数据可能有错误，如同样的数据录入两次。多个属性之间的相关性很高（相关系数>0.7），即多重共线性，往往会导致预测结果不稳定。属性与标签的相关性则不同 ，如果属性和标签相关，则通常意味着两者之间具有可预测的关系。
