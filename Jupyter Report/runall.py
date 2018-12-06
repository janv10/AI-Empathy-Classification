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
import hingeLogSquared, mytree


rsp.printWelcome()
cols = rsp.returnColumnNames()

train, dev, test = rsp.returnTrainDevTest()
train1, dev1, test1 = rsp.returnTrainDevTest()


allVars = pd.DataFrame(np.array(train), columns=cols)

allCC, sortedCC, sortedAbsCC = cf.getCorrVals(allVars, cols)
allCCE, sortedCCE, sortedAbsCCE = cfe.getCorrVals(allVars, cols)

Y = []
Yte = []

for i in range(len(train1)):
    if train1[i][94] > 0.6:
        Y.append(1)
    else:
        Y.append(-1)
for i in range(len(test1)):
    if test1[i][94] > 0.6:
        Yte.append(1)
    else:
        Yte.append(-1)
for i in train1:
    del i[94]
for i in test1:
    del i[94]
Y = np.array(Y)
Yte = np.array(Yte)
test1 = np.array(test1)
train1 = np.array(train1)



print("                          VALID INTEGER INPUT COMMANDS")
print("        1 -> Plots and shows absolute values of the correlation coefficients for all variables")
print("        2 -> Shows the results of baseline testing using most common occurance prediction")
print("        3 -> Run KNN using all variables with K values from 1 through 17")
print("        4 -> Run KNN using all variables with K value equivalent to training group size")
print("        5 -> Run KNN using top 16 most correlated vaiables with K values from 1 through 15")
print("        6 -> Perform Gradient Descent using the Squared Loss function")
print("        7 -> Perform Gradient Descent using the Logistic Loss function")
print("        8 -> Perform Gradient Descent using the Hinge Loss function")
print("        9 -> Create Decision Tree Classifiers with Depths 1 through 10.")
print("        10 -> Perform Random Forest Classification with 100 Bagged Sets and Depth 40")
print("        11 -> Perform Random Forest Classification with Custom Input")
print("        q -> Quit the Program")

b = True

while(b):

    var = input("$>>")

    
    if var == "1":
        print("Plotting the absolute values of the correlation coefficients for all variables...")
        p.plotcorrCo(sortedAbsCC)
    elif var == "2":
        strat = base.getBaselineStrat(train)
        base.perfBaselineStrat(test, strat)
    elif var == "3":     
        for k in range(1, 19, 2):
            knn.knn(train, test, k)
    elif var == "4":
        knn.knn(train, test, 809)
        print("The test accuracy is identical to the baseline accuracy because both approaches are equivalent")
    elif var == "5":
        better15 = []
        better15Indexes = []
        for i in sortedAbsCCE:
            if i[0] > 0.15:
                better15.append(i)
                better15Indexes.append(i[2])
        corrCoefs = []
        for i in better15Indexes:
            corrCoefs.append(allCC[i][0])
        train2 = []
        test2 = []
        for i in range(len(train)):
            app = []
            for j in better15Indexes:
                app.append(train[i][j])
            train2.append(app)
            
        for i in range(len(test)):
            app = []
            for j in better15Indexes:
                app.append(test[i][j])
            test2.append(app)
          
        for k in range(1, 17, 2):
            knn16.knn(train2, test2, k)

    elif var == "6":
        print("Running gradient descent using the Squared Loss function...")

        f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.SquaredLoss(), 'lambda': 0, 'numIter': 5000, 'stepSize': 0.0001})
        hingeLogSquared.trainTest(f, train1, Y, test1, Yte)
    elif var == "7":
        print("Running gradient descent using the Logistic Loss function...")

        f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.LogisticLoss(), 'lambda': 0, 'numIter': 5000, 'stepSize': 0.01})
        hingeLogSquared.trainTest(f, train1, Y, test1, Yte)
    elif var == "8":
        print("Running gradient descent using the Hinge Loss function")
        f = hingeLogSquared.LinearClassifier({'lossFunction': hingeLogSquared.HingeLoss(), 'lambda': -0.5, 'numIter': 1000, 'stepSize': 0.05})
        hingeLogSquared.trainTest(f, train1, Y, test1, Yte)
    
    elif var == "9":
        for i in range(1,11):
            mytree.runTree(train1, Y, test1, Yte, i)
    elif var == "10":
        print("Creating Random Forest...")
        mytree.runForest(train1, Y, test1, Yte, 40, 100)
    elif var == "11":
        
        var1 = input("Enter Decision Tree Max Depth: ")
        var2 = input("Enter Number of Bagged Samples to create: ")
        int1 = int(var1)
        int2 = int(var2)
        mytree.runForest(train1, Y, test1, Yte, int1, int2)

    elif var == "q":
        b = False

    else:
        print("Invalid Command: Try Again...")

    
    print(" ")

    
print("Exiting...")
    

    



