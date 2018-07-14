import math

#Split data by class
def separateByClass(dataset):
    separated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]]=[]
        separated[vector[-1]].append(vector)
    return separated

#Calculate mean and standard deviation
def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

#Get mean and std from data feature
def summarize(dataset):
    summarizes=[(mean(atrribute),stdev(atrribute)) for atrribute in zip(*dataset)]
    del summarizes[-1]
    return summarizes

def summarizeByClass(dataset):
    separated=separateByClass(dataset)
    summaries={}
    for classValue,instances in separated.items():
        summaries[classValue]=summarize(instances)
    return summaries