import sys
import pandas as pd
import numpy as np
import responses as rsp
import correlationFinder as cf
import correlationFinderWithEmpathy as cfe
import matplotlib.pyplot as plt
import plotCorr as p
import baseline as base
import knn
import knn16
import hingeLogSquared


rsp.printWelcome()
cols = rsp.returnColumnNames()

train, dev, test = rsp.returnTrainDevTest()

allVars = pd.DataFrame(np.array(train), columns=cols)

allCC, sortedCC, sortedAbsCC = cf.getCorrVals(allVars, cols)

##p.plotcorrCo(sortedAbsCC)
##ind = 0
##strat = base.getBaselineStrat(train)
##base.perfBaselineStrat(test, strat)
##
##
##print("7. Now running KNN with K values from 1 through 17..")
##for k in range(1, 19, 2):
##    knn.knn(train, test, k)
##print("\nNow running KNN with K value of 809 which should yield similar or identical results to the baseline test accuracy.\n")
##knn.knn(train, test, 809)
##print(sortedAbsCC)
##
##allCCE, sortedCCE, sortedAbsCCE = cfe.getCorrVals(allVars, cols)
##
##better15 = []
##better15Indexes = []
##
##for i in sortedAbsCCE:
##    if i[0] > 0.15:
##        better15.append(i)
##        better15Indexes.append(i[2])
##corrCoefs = []
##for i in better15Indexes:
##    corrCoefs.append(allCC[i][0])
##print(corrCoefs)
##train2 = []
##test2 = []
##for i in range(len(train)):
##    app = []
##    for j in better15Indexes:
##        app.append(train[i][j])
##    train2.append(app)
##    
##for i in range(len(test)):
##    app = []
##    for j in better15Indexes:
##        app.append(test[i][j])
##    test2.append(app)
##  
##for k in range(1, 17, 2):
##    knn16.knn(train2, test2, k)
##
##
##
##Y = []
##Yte = []
##
##for i in range(len(train)):
##    if train[i][94] > 0.6:
##        Y.append(1)
##    else:
##        Y.append(-1)
##for i in range(len(test)):
##    if test[i][94] > 0.6:
##        Yte.append(1)
##    else:
##        Yte.append(-1)
##for i in train:
##    del i[94]
##for i in test:
##    del i[94]
##
##Y = np.array(Y)
##Yte = np.array(Yte)
##test = np.array(test)
##train = np.array(train)
##f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.SquaredLoss(), 'lambda': 0, 'numIter': 5000, 'stepSize': 0.0001})
##hingeLogSquared.trainTest(f, train, Y, test, Yte)
##f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.LogisticLoss(), 'lambda': 0, 'numIter': 5000, 'stepSize': 0.01})
##hingeLogSquared.trainTest(f, train, Y, test, Yte)
##f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.HingeLoss(), 'lambda': -0.5, 'numIter': 1000, 'stepSize': 0.05})
##hingeLogSquared.trainTest(f, train, Y, test, Yte)


