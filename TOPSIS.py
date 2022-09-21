#importing necessary packages
import pandas as pd
import logging as lg
import sys


def TOPSIS_Manik(inputFilename, weight, impact, resultFilename):
    try:
        df = pd.read_csv(inputFilename)
    except:
        lg.warning("The file name you entered could not be found..")
        return
    try:
        weights = list(map(int, weight.split(',')))
    except ValueError:
        lg.warning("You have to separate the weights using commas(,).")
        return
    try:
        impacts = list(impact.split(','))
    except ValueError:
        lg.warning("You have to separate the impacts using commas(,).")
        return

    for i in impacts:
        if i != '+' and i != '-':
            lg.warning("Impacts can be either '+' or '-'.")
            return
    if len(weights) != len(impacts):
        lg.warning("The count of weights and impacts need to be same.")
        return

    if len(df.columns) < 3:
        lg.warning("The input model should have atleast 3 attributes.")
        return
    if (len(df.columns) - 1) != len(weights):
        lg.warning("Number of weights and attributes are different.")
        return
    for i in df.dtypes[1:]:
        if i != "float64":
            lg.warning("Input file contains non-numeric values!! Please try again.")
            return

    root_sum_square = []
    for i in df.columns[1:]:  # retrieves the name of columns in df
        total = 0
        for j in list(df[i]):  # makes list for contents of different columns
            total += (j ** 2)  
        root_sum_square.append(total ** (0.5))  # Taking sq root of summed squared elements

    for index, i in enumerate(df.columns[1:]):
        for j in df[i]:
            df[i] = df[i].replace(j, j * weights[index] / root_sum_square[index]) 

    ideal_values = []
    for index, i in enumerate(df.columns[ 1:]):  
        if impacts[index] == '-':
            ideal_best = min(df[i])
            ideal_worst = max(df[i])
        else:
            ideal_best = max(df[i])
            ideal_worst = min(df[i])

        ideal_values.append((ideal_best, ideal_worst))

    n = len(df[df.columns[1]])  

    topsis_score = []
    for i in range(n):
        totalplus = 0
        totalminus = 0
        for index, j in enumerate(list(df.iloc[i])[1:]):
            totalplus += ((j - ideal_values[index][0]) ** 2)
            totalminus += ((j - ideal_values[index][1]) ** 2)

        topsis_score.append(totalminus / totalplus + totalminus)  # appending topsis score for respective rows or attributes

    solution = pd.read_csv(inputFilename)
    solution['Topsis Score'] = topsis_score  # Adding topsis_score column to the df
    solution["Rank"] = solution["Topsis Score"].rank(ascending=False)

    for i in solution["Rank"]:
        i = int(i)

    solution.to_csv(f"{resultFilename}.csv", index=False)
    print(solution)
    print(".csv file(Result) successfully saved at the working directory....")


if __name__ == '__main__':
    filename = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result = sys.argv[4]
    TOPSIS_Manik(filename, weights, impacts, result)