from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from random import randint
import numpy as np

def runTree(train, Y, test, Yte, dep):
    model = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=dep, min_samples_leaf=5)
    model.fit(train, Y)

    yp = model.predict(test)

    print("For Max Tree Depth of "+ str(dep) + " accuracy is " + str( accuracy_score(Yte,yp)*100))
    return yp


def runTree2(train, Y, test, Yte, dep):
    model = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=dep, min_samples_leaf=5)
    model.fit(train, Y)

    yp = model.predict(test)

    return yp


def runForest(train, Y, test, Yte, dep, numTrees):
    allBags = []
    votes = []
    for i in range(len(test)):
        votes.append(0)
    for i in range(numTrees):
        bagArray = []
        newY = []
        for j in range(len(train)):
            r = randint(0, len(train)-1)
            bagArray.append(train[r])
            newY.append(Y[r])
        allBags.append(bagArray)
        pred = runTree2(bagArray, newY, test, Yte, dep)
        for h in range(len(pred)):
            if pred[h] == 1:
                votes[h]+=1
            else: 
                votes[h]-=1

    for i in range(len(votes)):
        if votes[i] >= 0:
            votes[i] = 1
        else:
            votes[i] = -1
    print("For Max Tree Depth of "+ str(dep) + " and " + str(numTrees) + " tree models, accuracy is " + str( accuracy_score(Yte,votes)*100))
