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
    # 将pois位置上等于value(ACGT)的数据挑出,稍后作为树的分支(删去当前特征)

    # L:lsit, A:array
    dsL4return = [] # 直接用空array要处理开头的多余元素,先用list承接,再转为array
    # csL4return = []
    for i in range(datasset.shape[0]):
        if datasset[i][pois] == value:
            # 把当前pois去掉 ***
            tempArray = np.delete(datasset[i], pois)
            dsL4return.append(tempArray)
            # csL4return.append(classset[i])

    dsA4ret = np.array(dsL4return)
    # csA4ret = np.array(csL4return)

    return dsA4ret

def bestPois2split(dataset):
    # 比较Shannon熵决定最优的位置划分数据集,返回位置即特征
    datasize = dataset.shape[0] # row
    featuresize = dataset.shape[1] - 1 # col
    info = Info(dataset)
    bestInfoGain = 0.0
    bestPois = -1
    for i in range(featuresize):
        # 遍历特征 比较
        tempEnt = 0.0
        for value in [0, 1, 2, 4]:
            # subDataSet, subClassSet = splitDataSet(dataset, classset, i, value)
            subDataSet = splitDataSet(dataset, i, value)
            # 此处不需要划分数据集。。。
            prob = subDataSet.shape[0] / float(datasize) # opt point*
            tempEnt += prob * Info(subDataSet)
              
        tempInfoGain = info - tempEnt
        if(tempInfoGain > bestInfoGain):
            # 最大信息增益对应的位置特征
            bestInfoGain = tempInfoGain
            bestPois = i
    
    return bestPois

def ID3(dataset, labels):
    # classset = dataset[ : , -1]
    # labels = [0, 1, .., 59]
    # labels为list
    classset = dataset[ : , -1] # 1-D array's shape[0] = size
    cs4present = ['ei', 'ie', 'n']
    if (sum(classset) == classset.shape[0] * classset[0]): # 同一类
        return cs4present[classset[0] - 1] # ie, ei, n***
    if (dataset.shape[1] == 1): # 分到最后只有一个特征但是属于不同类(没有特征)
        # 多数表决（影响正确率）
        # 随机可以?*
        return np.argmax(np.bincount(classset)) # hahaha
    
    bestFeature = bestPois2split(dataset) # 不划分
    bestFeatureLabel = labels[bestFeature]
    
    tree = {bestFeatureLabel : {}} # mat / json 字典构树 --> graphviz画树(finally)
    del[labels[bestFeature]] # 0~59跟着删 或者 在之前不删pois改为-2

    """
    value = [0, 1, 2, 4]
    for i in range(4):
        if ((dataset[:,bestFeature] == value[i]).any()):
            subLabels = labels[:]
            subdataset, subclassset = splitDataSet(dataset, classset, bestFeature, value[i]) # 合在一起好像更好。。。
            tree[bestFeatureLabel][value[i]] = ID3(subdataset, subclassset, subLabels)
            # tree[bestFeatureLabel][value[i]] = ID3Tree(splitDataSet(dataset, classset, bestFeature, value[i]), subLabels) # 这样好像不对。。。
    """
    value = [0, 1, 2, 4]
    value4present = ['T', 'G', 'C', 'A']
    for i in range(4):
        if((dataset[ : , bestFeature] == value[i]).any()):
            # 有ATGC则创建一个分支
            subLabels = labels[:]
            subdataset = splitDataSet(dataset, bestFeature, value[i]) # 划分

            tree[bestFeature][value4present[i]] = ID3(subdataset, subLabels) # value ATGC 

    """
    for value in [0, 1, 2, 4]:
        if((dataset[ : , bestFeature] == value).any()):
            # 有ATGC则创建一个分支
            subLabels = labels[:]
            subdataset = splitDataSet(dataset, bestFeature, value) # 划分

            tree[bestFeature][value] = ID3(subdataset, subLabels) # value ATGC***
    """
    
    return tree
    
    



