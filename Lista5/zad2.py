import csv
import numpy as np
from matplotlib import pyplot as plt


def readData():
    matrix = np.full((610+1,9019+1),0.0)
    with open('ratings.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            userId = int(row[0])
            movieId = int(row[1])
            rating = float(row[2])
            if movieId < 10000:
                matrix[userId,movieId] = rating

    movies = {}
    with open('movies.csv','rt', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            movieId = int(row[0])
            title = row[1]
            if movieId > 10000:
                break
            movies[movieId] = title

    return matrix, movies

def getRecomendations(matrix, y):
    x = matrix[1:,1:]
    x = np.nan_to_num(x / np.linalg.norm(x, axis=0))
    y = np.nan_to_num(y[1:] / np.linalg.norm(y[1:]))
    movieProfile = np.dot(x,y)
    movieProfile = np.nan_to_num(movieProfile / np.linalg.norm(movieProfile))
    recomendations = np.dot(x.T,movieProfile)
    return recomendations



if __name__ == "__main__":
    np.seterr(divide='ignore', invalid='ignore')
    matrix, movies = readData()

    #example profile
    my_ratings = np.zeros((9019+1,1))
    my_ratings[2571] = 5      # 2571 - Matrix
    my_ratings[32] = 4        # 32 - Twelve Monkeys 
    my_ratings[260] = 5       # 260 - Star Wars IV
    my_ratings[1097] = 4

    recomendations = getRecomendations(matrix,my_ratings).flatten().tolist()    
    movies_with_cosinus = {}
    for moviedID, cosinus in enumerate(recomendations):
        if cosinus in movies_with_cosinus:
            movies_with_cosinus[cosinus].append(moviedID + 1)
        else:
            movies_with_cosinus[cosinus] = [moviedID + 1]

    recomendations = list(filter(lambda x: x > 0.0, recomendations))
    recomendations.sort(reverse=True)

    titles = [] # result: sorted movies titles from most recommended to least
    for cos in recomendations:
        for movieId in movies_with_cosinus[cos]:
            titles.append(movies[movieId])
    
    print("\n9 Nabardziej pasujących filmów, tak jak w przykładzie podanym w treści zadania:")
    print(*titles[:9], sep="\n")
    value = input("Podaj 'a' aby wyświetlić wszystkie filmy o cos > 0, posortowane od najbardziej rekomendowanych do najmniej. Podaj cokolwiek innego, aby zakończyć program.")
    if value == 'a':
        print(*titles,sep="\n")


   