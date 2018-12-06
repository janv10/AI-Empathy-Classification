import numpy as np
def knn(train, test, k):
    closest = []
    guesses = []
    if k > 0 and k <= len(train):
        
        for te in range(len(test)):
            singleres = []
            for tr in range(len(train)):
                sums = 0
                for c in range(len(train[0])):
                    sums += abs(test[te][c]-train[tr][c])
                singleres.append((sums,tr,train[tr][94]))
            singleres = sorted(singleres)
            closest.append(singleres)
            
            #print(singleres[:3])
            sum2 = 0
            for kn in range(k):
                sum2 += singleres[kn][2]
            sum2 /= k
            if  sum2> 0.6:
                guesses.append(1)
            else:
                guesses.append(0)  
    tru = []
    for i in range(len(test)):
        if test[i][94] > 0.6:        
            tru.append(1)
        else:
            tru.append(0)
    inter = []
    inter = np.array(guesses) == np.array(tru)
    count=0
    rcount=0
    for i in range(len(inter)):
        if inter[i] == True:
            rcount+=1
        count+=1
        
        
    print("KNN run with k = " + str(k) + " yielded a testing accuracy of: " + str(rcount/count))
  