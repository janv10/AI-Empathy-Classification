import matplotlib.pyplot as plt


def getBaselineStrat(data):
    totalcount = 0
    empcount = 0
    for i in range(len(data)):
        if data[i][94] > 0.6:
            empcount += 1
        totalcount += 1
    print("Baseline: " + str(empcount) + " of the " + str(totalcount) + " people in the test set are considered 'Very Empathetic'")
    if empcount / totalcount > 0.5:
        return 1
    else:
        return 0


def perfBaselineStrat(testdata, guess):
    totalcount = 0
    rightcount = 0
    if guess == 1:
        for i in range(len(testdata)):
            if testdata[i][94] > 0.6:
                rightcount += 1
            totalcount += 1
    else:
        for i in range(len(testdata)):
            if testdata[i][94] < 0.6:
                rightcount += 1
            totalcount += 1
    print("Baseline stategy of guessing most common empathetic state accuracy is: " + str((rightcount / totalcount)) + "\n")
