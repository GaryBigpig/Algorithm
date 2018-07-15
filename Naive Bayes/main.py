import ProcessData
import GetFeature
import Prediction

def main():
    # Process data
    filename="Data/pima-indians-diabetes.data.csv"
    dataset=ProcessData.loadCsv(filename)
    # print("Loaded data file {0} with {1} rows".format(filename,len(dataset)))

    splitRatio=0.67
    train,test=ProcessData.splitDataset(dataset,splitRatio)
    # print("Split {0} rows into train with {1} and test with {2}".format(len(dataset),train,test))

    #Get data feature
    separated=GetFeature.separateByClass(train)
    # print("Separated instances: {0}".format(separated))

    summaries=GetFeature.summarizeByClass(train)
    # print("Summaries[0]: {0}".format(summaries[0]) +"\n"
    #       + "Summaries[1] {0} ".format(summaries[1]))

    #Preciction
    predictions=Prediction.getPredictions(summaries,test)
    accuracy=Prediction.getAccuracy(test,predictions)
    print("Accuracy:{0}%".format(accuracy))

if __name__ == "__main__":
    main()
