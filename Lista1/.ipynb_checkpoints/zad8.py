dic = { 1000 : "M",
         900 : "CM", 
         500 : "D",
         400 : "CD", 
         100 : "C", 
         90 : "XC", 
         50 : "L", 
         40 : "XL", 
         10 : "X", 
         9 : "IX", 
         5 : "V", 
         4 : "IV", 
         1 : "I" 
}

dicR = {
        "M" : 1000,
        "CM" : 900, 
        "D" : 500,
        "CD" : 400, 
        "C" : 100, 
        "XC" : 90, 
        "L" : 50, 
        "XL" : 40, 
        "X" : 10, 
        "IX" : 9, 
        "V" : 5, 
        "IV" : 4, 
        "I" : 1 
}

def floor_key(d, key):
    if key in d:
        return key
    return max(k for k in d if k < key)


def arabic_to_roman(result,number):
    if number <= 0:
        return result
    key = floor_key(dic,number)
    number -= key
    result += dic[key]
    return arabic_to_roman(result,number)

def roman_to_arabic(string):
    result = 0
    length = len(string)
    while(length > 0) :
        if(length > 2 ) :
            searched = string[length - 2:length]
        else :
            searched = string[0]   
        length -= 2
        
        if dicR.get(searched,None) == None:
            result += dicR.get(searched[0],0)
            if len(searched) == 2 :
                result += dicR.get(searched[1],0)
        else :
            result += dicR.get(searched,0)

    return result

print(arabic_to_roman('',76))
print(roman_to_arabic('MLXXXIV'),end="")
