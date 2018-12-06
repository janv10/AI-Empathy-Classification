from numpy import *
from pylab import *


def trainTest(classifier, X, Y, Xtest, Ytest):

    classifier.reset()

    classifier.train(X, Y);                   
    Ypred = classifier.predictAll(X);         

    trAcc = mean((Y >= 0) == (Ypred >= 0));    
    Ypred = classifier.predictAll(Xtest);          

    teAcc = mean((Ytest >= 0) == (Ypred >= 0));     
    print("Training accuracy is {0}".format(trAcc, teAcc))
    print("Testing accuracy is {1}".format(trAcc, teAcc))
    return (trAcc, teAcc, Ypred)



def gd(func, grad, x0, numIter, stepSize):
    x = x0
    trajectory = zeros(numIter + 1)
    trajectory[0] = func(x)
    for iter in range(numIter):
        g = grad(x)
        i = iter + 1
        eta = stepSize / sqrt(i)
        x = x - (eta * g) 
        trajectory[iter+1] = func(x)
    return (x, trajectory)
class LossFunction:
    def loss(self, Y, Yhat):
        l = 0

    def lossGradient(self, X, Y, Yhat):
        l = 0
        
class SquaredLoss(LossFunction):
    def loss(self, Y, Yhat):
        return 0.5 * dot(Y - Yhat, Y - Yhat)

    def lossGradient(self, X, Y, Yhat):
        return - sum((Y - Yhat) * X.T, axis=1)


class LogisticLoss(LossFunction):
    def loss(self, Y, Yhat):
        return sum(log(1 + exp(-Y * Yhat)))

    def lossGradient(self, X, Y, Yhat):
        return sum(-Y * X.T * exp(-Y * Yhat)/(1 + exp(-Y * Yhat)), axis=1)


class HingeLoss(LossFunction):
    def loss(self, Y, Yhat):
        hingeLoss = 1 - multiply(Y, Yhat)
        for i in range(len(hingeLoss)):
            if hingeLoss[i] < 0:
                hingeLoss[i] = 0
        sum_n = sum(hingeLoss)
        return sum_n
    
    def lossGradient(self, X, Y, Yhat):
        sum = 0
        i = 0
        for trueValue in Y:
            if trueValue * Yhat[i] < 1:
                sum = sum - trueValue * X[i]
            i = i + 1        
        return sum
        
class BinaryClassifier:
    def __init__(self, opts):
        self.opts = opts

    def setOption(self, optName, optVal):
        self.opts[optName] = optVal

    def isOnline(self):
        i = 0
    def reset(self):
        i = 0
        
    def predict(self, X):
        i = 0

    def predictAll(self, X):
        N,D = X.shape
        Y   = zeros(N)
        for n in range(N):
            Y[n] = self.predict(X[n,:])
        return Y

    def nextExample(self, X):
        i = 0

    def nextIteration(self):
        i = 0

    def train(self, X, Y):
        if self.online():
            for epoch in range(self.opts['numEpoch']):
                # loop over every data point
                for n in range(X.shape[0]):
                    # supply the example to the online learner
                    self.nextExample(X[n], Y[n])

                # tell the online learner that we're
                # done with this iteration
                self.nextIteration()
        else:
            i = 0

    def getRepresentation(self):
        util.raiseNotDefined()

class LinearClassifier(BinaryClassifier):
    def __init__(self, opts):
        self.opts = opts
        self.reset()

    def reset(self):
        self.weights =  zeros(149)

    def online(self):
        return False

    def __repr__(self):
        return    "w=" + repr(self.weights)

    def predict(self, X):
        if type(self.weights) == int:
            return 0
        else:
            return dot(self.weights, X)

    def getRepresentation(self):
        return self.weights

    def train(self, X, Y):
        lossFn   = self.opts['lossFunction']         # loss function to optimize
        lambd    = self.opts['lambda']               # regularizer is (lambd / 2) * ||w||^2
        numIter  = self.opts['numIter']              # how many iterations of gd to run
        stepSize = self.opts['stepSize']             # what should be our GD step size?

        def func(w):
            Yhat = sum(w * X, axis=1)
            obj  = lossFn.loss(Y, Yhat) + (lambd/2.0) * norm(w)**2
            return obj

        def grad(w):
            Yhat = sum(w * X, axis=1)     
            gr = lossFn.lossGradient(X, Y, Yhat) + lambd * w
            return gr
        
        w, trajectory = gd(func, grad, self.weights, numIter, stepSize)
        self.weights = w
        self.trajectory = trajectory













