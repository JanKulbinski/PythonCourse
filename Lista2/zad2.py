import sys

base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def string_to_bin(string, source_file):
    binary_all = ""
    for c in string:
        ascii_code = ord(c)
        binary_code = str(bin(ascii_code))[2:]
        binary_code = "00000000"[0:(8 - len(binary_code))] + binary_code
        binary_all += binary_code
    with open(source_file, "w") as out:
        out.write(binary_all)

def encode(source_file, target_file):
    binary_all = ""
    result = []
    with open(source_file, "rb") as f:
        binary_all = f.read()
        while binary_all:
            index = int(binary_all[:6], 2)
            result.append(base64[index])
            binary_all = binary_all[6:]
    
    with open(target_file, "w") as out:
        out.write("".join(result))

def decode(source_file, target_file):
    with open(source_file, "r") as f:
        letter = f.read(1)
        result = ""
        while letter:
            index = base64.find(letter)
            binary_code = str(bin(index))[2:]
            result += "000000"[0:(6 - len(binary_code))] + binary_code
            letter = f.read(1)

    with open(target_file,"w") as out:
        out.write(result)        

    
if __name__== "__main__":
    string_to_bin("Python","zad2.bin")
   # Testing :
   # encode("zad2.bin","zad2.txt")
   # decode("zad2.txt","zad2.bin")
    action = sys.argv[1][2:]
    source_file = sys.argv[2]
    target_file = sys.argv[3]
    if action == "encode":
        encode(source_file, target_file)
    elif action == "decode":
        decode(source_file, target_file)
    else:
        print("Wrong first paramter. Type --encode in out or --decode in out")
