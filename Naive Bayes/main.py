import ProcessData
import ProcessFeature

if __name__ == "__main__":
    # Process data
    filename="Data/pima-indians-diabetes.data.csv"
    dataset=ProcessData.loadCsv(filename)
    print("Loaded data file {0} with {1} rows".format(filename,len(dataset)))

    splitRatio=0.67
    train,test=ProcessData.splitDataset(dataset,splitRatio)
    print("Split {0} rows into train with {1} and test with {2}".format(len(dataset),train,test))

    #Get data feature
    separated=ProcessFeature.separateByClass(dataset)
    print("Separated instances: {0}".format(separated))
