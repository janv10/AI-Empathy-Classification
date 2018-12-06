import csv


def printWelcome():
    print ("-----------------------------------------------")
    print ("        Welcome to HW5: Mini-Project")
    print (" Authors: Patrick O'Connell & Jahnvi Patel ")
    print ("-----------------------------------------------")


def returnColumnNames():
    cols = []
    print("1. Opening young-people-survey/columns.csv for column name retrieval...")
    with open('young-people-survey/columns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count > 0:
                cols.append(row[1])
            count += 1
    print("**Successfully done retrieving column names.\n")
    return cols


def returnTrainDevTest():
    print("2. Opening young-people-survey/responses.csv for data retrieval and processing...")
    with open('young-people-survey/responses.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count, nilcount, e = 0, 0, 0
        totalArr = []
        print("Building responses data structure...")
        for row in csv_reader:

            rowArr = []
            count = 0

            if line_count == 0:
                c = 0
                for ci in row:
                    if (ci == "Empathy"):
                        e = c
                    c += 1
            if line_count > 0:
                for col in row:
                    app = col
                    if count == 73:
                        if col == "never smoked":
                            app = "0"
                        elif col == "tried smoking":
                            app = "1"
                        elif col == "former smoker":
                            app = "2"
                        elif col == "current smoker":
                            app = "3"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error smoke" + col)
                    if count == 74:
                        if col == "never":
                            app = "0"
                        elif col == "social drinker":
                            app = "1"
                        elif col == "drink a lot":
                            app = "2"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error drink" + col)
                    if count == 107:
                        if col == "i am often early":
                            app = "0"
                        elif col == "i am always on time":
                            app = "1"
                        elif col == "i am often running late":
                            app = "2"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 108:
                        if col == "never":
                            app = "0"
                        elif col == "only to avoid hurting someone":
                            app = "1"
                        elif col == "sometimes":
                            app = "2"
                        elif col == "everytime it suits me":
                            app = "3"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 132:
                        if col == "no time at all":
                            app = "0"
                        elif col == "less than an hour a day":
                            app = "1"
                        elif col == "few hours a day":
                            app = "2"
                        elif col == "most of the day":
                            app = "3"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 144:
                        if col == "female":
                            app = "0"
                        elif col == "male":
                            app = "1"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 145:
                        if col == "left handed":
                            app = "0"
                        elif col == "right handed":
                            app = "1"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 146:
                        if col == "currently a primary school pupil":
                            app = "0"
                        elif col == "primary school":
                            app = "1"
                        elif col == "secondary school":
                            app = "2"
                        elif col == "college/bachelor degree":
                            app = "3"
                        elif col == "masters degree":
                            app = "4"
                        elif col == "doctorate degree":
                            app = "5"

                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 147:
                        if col == "no":
                            app = "0"
                        elif col == "yes":
                            app = "1"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 148:
                        if col == "village":
                            app = "0"
                        elif col == "city":
                            app = "1"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)
                    if count == 149:
                        if col == "house/bungalow":
                            app = "0"
                        elif col == "block of flats":
                            app = "1"
                        elif col == "":
                            nilcount += 1
                        else:
                            print("Error " + col)

                    count += 1
                    if app == "":
                        app = "999"
                    rowArr.append(int(app))
                totalArr.append(rowArr)
            line_count += 1
        sumArr = []
        countArr = []
        maxArr = []
        for col in totalArr[1]:
            sumArr.append(0)
            countArr.append(0)
            maxArr.append(0)

        print("Calculating column sums and blank responses...")
        for row in range(len(totalArr)):
            for col in range(len(totalArr[row])):
                if (totalArr[row][col] != 999):
                    countArr[col] += 1
                    sumArr[col] += totalArr[row][col]
                    if(totalArr[row][col] > maxArr[col]):
                        maxArr[col] = totalArr[row][col]
        print("**Successfully done calculating column sums and blank responses.\n")

        print("3. Calculating column averages...")
        avgArr = [(x / y) for x, y in zip(sumArr, countArr)]
        print("**Successfully done calculating column averages.\n")

        print("4. Replacing blank responses with column averages...")
        for row in range(len(totalArr)):
            for col in range(len(totalArr[row])):
                if (totalArr[row][col] == 999 or totalArr[row][col] == 0):
                    totalArr[row][col] = avgArr[col]

                totalArr[row][col] = totalArr[row][col] / maxArr[col]
        print("**Successfully done replacing blank responses.\n")

        Train = totalArr[0:810] # Train = totalArr[0:810]
        Dev = totalArr[811:911] # Dev = totalArr[811:911]
        Test = totalArr[911:]   # Test = totalArr[911:]

        return Train, Dev, Test
