import numpy as np
from math import log2

def Info(dataset, classset):
    # 数据集大小
    datasize = dataset.shape[0] # ndarray row's number
    # ShannonEntropy = 0.0

    # labelcnt = {}
    labelcnt = [0, 0, 0]
    # 统计
    for i in range(datasize):
        labelcnt[classset[i] - 1] += 1

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


def splitDataSet(datasset, classset, pois, value): # gene's poistion ACGT
    dsL4return = []
    csL4return = []
    for i in range(datasset.shape[0]):
        if datasset[i][pois] == value:
            dsL4return.append(datasset[i])
            csL4return.append(classset[i])

    dsA4ret = np.array(dsL4return)
    csA4ret = np.array(csL4return)

    return dsA4ret, csA4ret # 这样分要确定好两个的shape

def bestDataSet2split(dataset, classset):
    datasize = dataset.shape[0] # row
    labelsize = dataset.shape[1] # col
    info = Info(dataset, classset)
    # ???
    for i in range(labelsize):
        E_condition = 0.0
        
    


    return dataset, classset


    
    



