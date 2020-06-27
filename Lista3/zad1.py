def transposition(matrix):
    n = len(matrix)
    return [" ".join([x.split(" ")[i] for x in matrix]) for i in range(n)]

if __name__== "__main__":
    matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
    print(transposition(matrix))