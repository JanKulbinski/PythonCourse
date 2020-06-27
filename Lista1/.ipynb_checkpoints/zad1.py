def pascal_triangle(n):
    if n < 1 :
        return
    elif n == 1 :
        print("1")
        return
    else :
        width = int((2*n - 1)/2)
        printSpaces(width)
        width -= 1
        print("1")

        line = [1,1]
        
        for _ in range(2,n+1) :
            printSpaces(width)
            width -= 1
            
            for i in line :
                print(i,end=" ")
            print('')

            for index, _ in enumerate(line) :
                if index + 1 > len(line) - 1:
                    break
                line[index]= line[index] + line[index + 1]
            line.insert(0,1)

def printSpaces(n):
    for _ in range(n) :
        print(end=" ")

pascal_triangle(7)