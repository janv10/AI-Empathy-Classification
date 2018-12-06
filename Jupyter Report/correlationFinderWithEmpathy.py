import pandas as pd
import statsmodels.api as sm

import matplotlib.pyplot as plt 
from scipy.stats.stats import pearsonr


def getCorrVals(trainingset, cols):
    allCC = []
    sortedCC = []
    sortedAbsCC = []
    for i in range(len(cols)):
        
            
        s = str(cols[i])
        X = trainingset[s]
        y = trainingset["Empathy"]
        a,b = pearsonr(X, y)
        allCC.append((a,cols[i], i))
        sortedCC.append((a,cols[i], i))
        sortedAbsCC.append((abs(a),cols[i], i))
            
    sortedCC = sorted(sortedCC)
    sortedAbsCC = sorted(sortedAbsCC)
    return allCC, sortedCC, sortedAbsCC
