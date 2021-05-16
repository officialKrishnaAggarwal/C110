import plotly.figure_factory as ff
import csv
import statistics
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
fig = ff.create_distplot([data],["Temperature"], show_hist=False)
pMean = statistics.mean(data)
pStandardDeviation = statistics.stdev(data)
print(pMean)
print(pStandardDeviation)

fig.show()

def randomSetOfMean():
    dataSet=[]
    for i in range(0,100):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(meanList)
    standardDeviation = statistics.stdev(meanList)
    fig = ff.create_distplot([df],["Random"], show_hist=False)
    print(mean)
    print(standardDeviation)
    fig.show()

def setup():
    meanList=[]
    for i in range(0,1000):
        setOfMean = randomSetOfMean()
        meanList.append(setOfMean)

    showFig(meanList)

setup()
    
    
