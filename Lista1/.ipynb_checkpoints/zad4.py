def prime_factors(n):
    result = []
    x = 2
    while n > 1:
        a = 0
        while(n % x == 0):
            n = n/x
            a += 1
        if a > 0:    
            result.append((x,a))
        x += 1
    return result

prime_factors(159250)