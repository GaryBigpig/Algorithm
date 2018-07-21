
import Nbayes_lib as NBL
import classification as CL

k = 3


def main():
    dataSet, listClassses = NBL.loadDataSet()
    nb = NBL.NBayes()
    nb.tran_set(dataSet, listClassses)
    print(CL.classify(nb.tf[3], nb.tf, listClassses, k))


if __name__ == "__main__":
    main()
