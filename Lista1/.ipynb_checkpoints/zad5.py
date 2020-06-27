def fraczero(n) :
    res = 1
    for i in range(2,n+1) :
        res *= i

    zeros = 0
    while res % 10 == 0 :
        zeros += 1
        res /= 10
    return zeros

fraczero(15)