import itertools 
from itertools import combinations 
  
def findsubsets(s):
    n = len(s)
    lists = [list(map(set, itertools.combinations(s, i))) for i in range(1, n+1)]
    return [{}] + [element for array in lists for element in array]
  
if __name__== "__main__":
    print(findsubsets([1, 2, 3, 4, 5]))