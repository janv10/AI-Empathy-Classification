import pandas as pd
import statsmodels.api as sm

import matplotlib.pyplot as plt 
from scipy.stats.stats import pearsonr


def getCorrVals(trainingset, cols):
    allCC = []
    sortedCC = []
    sortedAbsCC = []
    for i in range(len(cols)):
        if cols[i] != "Empathy":
            
            s = str(cols[i])
            X = trainingset[s]
            y = trainingset["Empathy"]
            a,b = pearsonr(X, y)
            allCC.append((a,cols[i]))
            sortedCC.append((a,cols[i]))
            sortedAbsCC.append((abs(a),cols[i]))
            
    sortedCC = sorted(sortedCC)
    sortedAbsCC = sorted(sortedAbsCC)
    return allCC, sortedCC, sortedAbsCC