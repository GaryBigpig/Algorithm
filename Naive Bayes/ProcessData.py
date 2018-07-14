import csv
import random

#Read data
def loadCsv(filename):
    lines=csv.reader(open(filename,"r"))
    dataset=list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]] #为何把每个数都转换为浮点数
    return dataset

#Split data into train data and test data
def splitDataset(dataset,splitRatio):
    trainSize=int(len(dataset)*splitRatio)
    trainSet=[]
    copyData=dataset
    while len(trainSet)<trainSize:
        index=random.randrange(len(copyData)) #为什么没有重复数据？
        trainSet.append(copyData[index])
    return [trainSet,copyData]


