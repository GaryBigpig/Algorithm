import Nbayes_lib as NBL
import numpy as np


def main():
    dataSet,listClasses=NBL.loadDataSet()
    nb=NBL.NBayes()
    nb.tran_set(dataSet,listClasses)
    # print(nb.Pcates)
    # print(nb.doclength)
    # print(nb.vocabulary)
    # print(nb.vocablen)
    # print(nb.tf)
    # print(nb.idf)
    # print(nb.tdm)
    nb.map2vocab(dataSet[1])
    print(nb.predict(nb.testset))


if __name__ == '__main__':
    main()
