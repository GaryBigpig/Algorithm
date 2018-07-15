import math

#Calculate probability
def calculateProbability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

def calculateClassProbabilities(summaries,inputVector):
    probabilities={}
    for classvalue,classsummaries in summaries.items():
        probabilities[classvalue]=1
        for i in range(len(classsummaries)):
            mean,stdev=classsummaries[i]
            x=inputVector[i]
            probabilities[classvalue]*=calculateProbability(x,mean,stdev)
    return probabilities

#Prediction
def predict(summaries,inputVector):
    probabilities=calculateClassProbabilities(summaries,inputVector)
    bestLabel,bestProb=None,-1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability>bestProb:
            bestProb=probability
            bestLabel=classValue
    return bestLabel

def getPredictions(summaries,dataset):
    predictions=[]
    for i in range(len(dataset)):
        result=predict(summaries,dataset[i])
        predictions.append(result)
    return predictions

def getAccuracy(dataset,predictions):
    correct=0
    for i in range(len(dataset)):
        if dataset[i][-1]==predictions[i]:
            correct+=1
    return (correct/float(len(dataset)))*100.0