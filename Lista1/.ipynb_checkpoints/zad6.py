import random
from statistics import mean 

randoms = []
for i in range(20):
    value = random.randint(1,100)
    randoms.append(value)

print(randoms)
print(f'average = {mean(randoms)}')
randoms.sort()
print(f'min = {randoms[0]}')
print(f'max = {randoms[len(randoms) - 1]}')
print(f'number of even = {len(list(filter(lambda value: value % 2 == 0,randoms)))}')