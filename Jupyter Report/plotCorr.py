import matplotlib.pyplot as plt

def plotcorrCo(sortedAbsCC):
    print("5. Displaying Correlation Coefficient Figure...\n")
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 20
    fig_size[1] = 8
    plt.gcf().subplots_adjust(bottom=0.3)
    plt.rcParams.update({'font.size': 8})
    plt.rcParams["figure.figsize"] = fig_size
    plt.bar(range(len(sortedAbsCC)), [val[0]  for val in sortedAbsCC])
    plt.xlabel('Respones Columns', fontsize=14)
    plt.suptitle('Sorted Correlation Coefficient Values', fontsize=14)
    plt.ylabel('Absolute Value of Correlation Coefficient', fontsize=14)
    plt.xticks(range(len(sortedAbsCC)), [val[1] for val in sortedAbsCC])
    plt.xticks(rotation=90)
    plt.show()
