import sys
import pandas as pd
import numpy as np
import responses as rsp
import correlationFinder as cf
import matplotlib.pyplot as plt
import plotCorr as p
import baseline as base
import knn
rsp.printWelcome()
cols = rsp.returnColumnNames()

train, dev, test = rsp.returnTrainDevTest()

allVars = pd.DataFrame(np.array(train), columns=cols)

allCC, sortedCC, sortedAbsCC = cf.getCorrVals(allVars, cols)

p.plotcorrCo(sortedAbsCC)
ind = 0
strat = base.getBaselineStrat(train)
base.perfBaselineStrat(test, strat)

print("Now running KNN with K values from 1 through 17..")
for k in range(1, 19, 2):
    knn.knn(train, test, k)
print("Now running KNN with K value of 809 which should yield similar or identical results to the baseline test accuracy.")
knn.knn(train, test, 809)
