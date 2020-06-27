import random
import sys
import math

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ "

def miller_rabin_test(p, accuracy=10):
    if p == 2 or p == 3:
        return True
    if not p % 2:
        return False

    d = p - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = round(d/2)

    for _ in range(accuracy):
        if not miller_rabin_helper(s,d,p):
            return False
    return True


def miller_rabin_helper(s,d,p):
    a = random.randrange(2, p - 1)
    x = pow(a, d, p)
    if x == 1 or x == p - 1:
        return True
    for _ in range(s - 1):
        x = pow(x, 2, p)
        if x == p - 1:
            return True
    return False


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def generateKeys(bits):
    length = int(math.log(2)/math.log(10)*bits)

    p = random.randint(10**length,10**(length + 1))
    while not miller_rabin_test(p):
        p = random.randint(10**length,10**(length + 1))
    
    q = 4 # any not prime
    while p != q and not miller_rabin_test(q):
        q = random.randint(10**length,10**(length + 1))
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 0
    for i in range(3, phi):
        if math.gcd(i, phi) == 1:
            e = i
            break

    _, d, _ = egcd(e, phi)
    while d < 0:
        d += phi

    with open('key.pub',"w") as out:
        out.write(f'{n} {e}')
    with open('key.priv',"w") as out:
        out.write(f'{n} {d}')



def encrypt(secret):
    with open('key.pub', 'rb') as f:
        data = f.read()
        numbers = data.split()
        n = int(numbers[0])
        e = int(numbers[1])
    
    encrypted = "" 
    for char in secret:
        index = alphabet.find(char) + 10
        if int(encrypted + str(index)) < n:
            encrypted += str(index)
        else:
            print((int(encrypted) ** e) % n)
            encrypted = "" 
    
    print((int(encrypted) ** e) % n)


def decrypt(code):
    with open('key.priv', 'rb') as f:
        data = f.read()
        numbers = data.split()
        n = int(numbers[0])
        d = int(numbers[1])
        
        to_decrypt = code.split(" ")
        for block in to_decrypt:
            decrypted = str(pow(int(block),d,n))
            length = len(decrypted)
            for i in range(0,length-1,2):
                print(alphabet[int(decrypted[i:i+2]) - 10], end='')




if __name__== "__main__":
    
    action = sys.argv[1]
    if action == "--gen-keys":
        bits = sys.argv[2]
        generateKeys(int(bits))

    elif action == "--encrypt":
        secret = sys.argv[2]
        encrypt(secret)
    
    elif action == "--decrypt":
        secret = sys.argv[2]
        decrypt(secret)