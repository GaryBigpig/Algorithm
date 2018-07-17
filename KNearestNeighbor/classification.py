import numpy as np
import operator as op


def cosdist(vector1, vector2):
    return np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )


def classify(testdata, trainSet, listClassses, k):
    dataSetSize = trainSet.shape[0]
    distances = np.array(np.zeros(dataSetSize))
    for i in range(dataSetSize):
        distances[i] = cosdist(testdata, trainSet[i])
    sortedDistIndicies = np.argsort(-distances)
    classCount = {}
    for i in range(k):
        voteIlabel = listClassses[
            sortedDistIndicies[i]
        ]  # Get class label from testdata
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(
        classCount.iteritems(), key=op.itemgetter(1), reverse=True
    )
    return sortedClassCount[0][0]
