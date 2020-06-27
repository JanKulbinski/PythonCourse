from functools import reduce

def sum_bytes(file_name):
    with open(file_name, "r") as f:
        yield [int(line.split()[-1]) for line in f]
        
if __name__== "__main__":
    print(f'Calkowita liczba bajtow: {sum(next(sum_bytes("zad3_test.txt")))}')   



