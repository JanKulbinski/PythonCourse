import random
import re

alphabet = ['a','b','c']
def random_strings(n):
    dic = {}
    for i in range (25):
        string = ''
        for j in range (n):
            value = random.randint(0,2)
            string += alphabet[value]
        dic[string] = None
    return dic

def match_pattern(pattern):
    pattern = pattern.replace("*",".")
    patternObj = re.compile(pattern)
    for key in dic.keys():
        if patternObj.match(key):
            print(key)

dic = random_strings(5)
print(dic)
match_pattern('**a*b')