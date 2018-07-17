
import Nbayes_lib as NB
import classification as CL

k=3

def main():
    dataSet,listClassses=NB.loadDataSet()
    nb=NB.NBayes()
    nb.tran_set(dataSet,listClassses)
    print(CL.classify(nb.tf[3],nb.tf,listClassses,k))



if __name__ == '__main__':
    main()