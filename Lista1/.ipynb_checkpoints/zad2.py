def primes(n) :
    primes = [1] * (n+1)
    primes[0] = 0
    primes[1] = 0

    i = 2
    while i * i <= n+1 :
        if primes[i] == 1 :
            for j in range(2*i,n+1,i):
                primes[j] = 0
        i += 1
    
    result = []
    for index, value in enumerate(primes) :
        if value:
            result.append(index)
    return result

primes(6)  

             