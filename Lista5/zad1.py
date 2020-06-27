import csv
import numpy as np
from matplotlib import pyplot as plt


def readData():
    matrix = np.full((610+1,193609+1),0.0)
    matrixToyStory = np.full((215+1,193609+1),0.0)
    userToyStory = set() # user which rated ToyStory
    with open('ratings.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            userId = int(row[0])
            movieId = int(row[1])
            rating = float(row[2])
            matrix[userId,movieId] = rating
            if movieId == 1:
                userToyStory.add(userId)
    
    index = 1
    userToyStory = sorted(userToyStory)
    for user in userToyStory:
        matrixToyStory[index] = matrix[user,:]
        index += 1

    return matrix, matrixToyStory


def linearRegression(matrix, m, limit=193609+1):
    x = matrix[1:limit, 2:m+1]
    y = matrix[1:limit, 1]
    A = np.hstack((x, np.ones((x.shape[0], 1))))
    b = np.linalg.lstsq(A, y, rcond=None)[0]
    
    # inaccuracy
    Ab = np.matmul(A,b)
    inaccuracy = np.multiply((Ab - y),(Ab - y))
    return b, inaccuracy


def drawInaccuracy(results):
    x = np.linspace(1,610,610)
    
    plt.subplot(3,1,1)
    plt.plot(x, results[0],'g', label=10, linewidth=1)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(x, results[1],'r', label=10000, linewidth=1)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(x, results[2],'b', label=100000, linewidth=1)
    plt.legend()
    plt.tight_layout(pad=1.0)
    plt.show()


def calculatePrediction(matrix, b, m):
    x = matrix[201:, 2:m+1]
    matrix = np.hstack((x, np.ones((x.shape[0],1))))
    prediction = np.matmul(matrix,b)
    return prediction


if __name__ == "__main__":
    matrix, matrixToyStory = readData()
    
    #second part of exercise
    tested_m = [10,100,200,500,1000,100000]
    print(f'\nReal values = {matrixToyStory[201:,1]}\n\nPredictions:\n')
    for m in tested_m:
        b, _ = linearRegression(matrixToyStory,m,201)
        print('#'*10)
        print(f'\nm={m}\n{calculatePrediction(matrixToyStory,b,m)}\n')

    # first part of excercise
    results = []
    for i in range(1,5):
        if i == 2:
            continue
        m = 10 ** i
        results.append(linearRegression(matrix,m)[1])
    drawInaccuracy(results)
    