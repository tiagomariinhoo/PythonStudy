from statistics import median, mean
#histogram plot
from numpy.random import seed
from numpy.random import randn
import numpy
from matplotlib import pyplot
#normality test
from scipy.stats import shapiro

v1 = []
v2 = []

def genLists():
    for i in range (1,1000):
        if i < 500: 
            v1.append(0)
            
        elif i == 500:
            v1.append(5)
        else:
            v1.append(5.1)

    for i in range (1, 1000):
        if(i < 700):
            v2.append(1)
        else:
            v2.append(2)
        

def plotLists():
    bins = numpy.linspace(0, 6, 50)

    pyplot.hist(v1, bins, alpha=0.5, label='v1')
    pyplot.hist(v2, bins, alpha=0.5, label='v2')

    pyplot.legend(loc='upper right')
    pyplot.show()


def checkShapiro(lista, nome):
    stat, pvalue = shapiro(lista)
    alpha = 0.05

    if pvalue > alpha:
        print(nome + " segue uma distribuição normal!")
    else:
        print(nome + " não segue uma distribuição normal!")

# ------------ MAIN -------------

genLists()
#plotLists()
checkShapiro(v1, "V1")
checkShapiro(v2, "V2")


    