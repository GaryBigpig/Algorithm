import math

#Calculate probability
def calculateProbability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

def calculateClassProbabilities(summeries,inputVector):
    probabilities={}
    for classvalue,classsummeries in summeries.items():
        probabilities[classvalue]=1
        for i in range(len(classsummeries)):
            mean,stdev=classsummeries[i]
            x=inputVector[i]
            probabilities[classvalue]*=calculateProbability(x,mean,stdev)
        return probabilities
