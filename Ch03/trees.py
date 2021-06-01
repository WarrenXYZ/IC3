'''
Created on Oct 12, 2010
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: Peter Harrington
'''
from math import log
import operator

import numpy as np

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    # print(labelCounts)
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt
    
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    # if axis == 33:
        # print(retDataSet)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels, N):
    
    N = N + 1
    # if N == 3:
        # return 5
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])

    print(bestFeat)
    # print(labels)
    print("*****")
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        #print(value)
        #print("*****")
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels,N)
    return myTree                            
    
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel

def storeTree(inputTree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
    
def preprocess4matrix():
    fin = open('./dna.data', 'r')
    DNA_pois_class_array = np.empty([], dtype = int)
    # DNA_clas_array = np.empty([], dtype = int)

    # 第一行单独处理先得一个array再append / 去掉第一个元素

    for line in  fin.readlines():
        for i in range(0, len(line) - 3, 6): # "\n"占1
            if line[i] == "1":
                #fout_str += 'A'
                DNA_pois_class_array = np.append(DNA_pois_class_array, [4])
            elif line[i + 2] == "1":
                #fout_str += 'C'
                DNA_pois_class_array = np.append(DNA_pois_class_array, [2])
            elif line[i + 4] == "1":
                #fout_str += 'G'
                DNA_pois_class_array = np.append(DNA_pois_class_array, [1])
            else:
                #fout_str += 'T'
                DNA_pois_class_array = np.append(DNA_pois_class_array, [0])
                # fout_str.append("T")
    
        if line[-3] == "1":
            #fout_str += " ei\n"
            DNA_pois_class_array = np.append(DNA_pois_class_array, [1])
        elif line[-3] == "2":
            #fout_str += " ie\n"
            DNA_pois_class_array = np.append(DNA_pois_class_array, [2])
        else:
            #fout_str += " n\n"
            DNA_pois_class_array = np.append(DNA_pois_class_array, [3])

    # 用空数组接第一个元素不为空要删除
    DNA_pois_class_array = np.delete(DNA_pois_class_array, 0)
    # DNA_clas_array = np.delete(DNA_clas_array, 0)
    DNA_pois_class_array = np.reshape(DNA_pois_class_array, (2000, 61))
    # DNA的位置信息与分类信息放在同一个array表示, array的最后一列表示类别
    # print(DNA_pois_class_array)
    # print(DNA_clas_array)

    fin.close()

    # return DNA_pois_class_array
    dna_list = DNA_pois_class_array.tolist()
    # print(dna_list)
    # print(type(DNA_pois_class_array))
    # print(type(dna_list))
    dna_labels = list(range(1, 61))
    return dna_list, dna_labels

dataset, labels = preprocess4matrix()

id3 = createTree(dataset, labels,0)

print("success!")
