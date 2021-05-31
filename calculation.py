import numpy as np
from math import log2

# 特征与分类放在同一个array归为dataset, 原dataset, classset->dataset

# 计算Shannon熵
def Info(dataset):
    # 数据集大小
    datasize = dataset.shape[0] # ndarray row's number
    # ShannonEntropy = 0.0

    # labelcnt = {}表示ei, ie, n的数目
    labelcnt = [0, 0, 0]
    # 统计
    for i in range(datasize):
        # labelcnt[classset[i] - 1] += 1
        labelcnt[dataset[i, -1] - 1] += 1

    """
    mask = np.unique(classset)
    tmp = {}
    for v in mask:
        tmp[v] = np.sum(classset == v)
    """

    prob1 = float(labelcnt[0]) / datasize
    prob2 = float(labelcnt[1]) / datasize
    prob3 = float(labelcnt[2]) / datasize

    ShannonEntropy = -(prob1 * log2(prob1) + prob2 * log2(prob2) + prob3 * log2(prob3))

    return ShannonEntropy


def splitDataSet(datasset, pois, value): # gene's poistion ACGT
    # 将pois位置上等于value(ACGT)的数据挑出,稍后作为树的分支

    # L:lsit, A:array
    dsL4return = [] # 直接用空array要处理开头的多余元素,先用list承接,再转为array
    # csL4return = []
    for i in range(datasset.shape[0]):
        if datasset[i][pois] == value:
            dsL4return.append(datasset[i])
            # csL4return.append(classset[i])

    dsA4ret = np.array(dsL4return)
    # csA4ret = np.array(csL4return)

    return dsA4ret

def bestPois2split(dataset, classset):
    # datasize = dataset.shape[0] # row
    labelsize = dataset.shape[1] # col
    info = Info(dataset, classset)
    bestInfoGain = 0.0
    bestPois = -1
    for i in range(labelsize):
        tempEnt = 0.0
        for value in [0, 1, 2, 4]:
            subDataSet, subClassSet = splitDataSet(dataset, classset, i, value)
            # 此处不需要划分数据集。。。
            prob = subClassSet.shape[1] / float(labelsize)
            tempEnt += prob * Info(subDataSet, subClassSet)
              
        tempInfoGain = info - tempEnt
        if(tempInfoGain > bestInfoGain):
            bestInfoGain = tempInfoGain
            bestPois = i
    
    return bestPois

def ID3Tree(dataset, classset, labels):
    # labels = [0, 1, .., 59]
    if (sum(classset) == classset.shape[1] * classset[0]): # 同一类
        return classset[0]
    if (dataset.shape[1] == 1): # 分到最后只有一个特征但是属于不同类
        # 多数表决（可能是错误率所在）
        # 随机可以？
        return np.argmax(np.bincount(classset)) # hahaha
    
    bestFeature = bestPois2split(dataset, classset)
    bestFeatureLabel = labels[bestFeature]
    tree = {bestFeatureLabel : {}} # mat / json 字典构树
    del[labels[bestFeature]]

    value = [0, 1, 2, 4]
    for i in range(4):
        if ((dataset[:bestFeature] == value[i]).any()):
            subLabels = labels[:]
            subdataset, subclassset = splitDataSet(dataset, classset, bestFeature, value[i]) # 合在一起好像更好。。。
            tree[bestFeatureLabel][value[i]] = ID3Tree(subdataset, subclassset, subLabels)
            # tree[bestFeatureLabel][value[i]] = ID3Tree(splitDataSet(dataset, classset, bestFeature, value[i]), subLabels) # 这样好像不对。。。

    return tree
    
    



