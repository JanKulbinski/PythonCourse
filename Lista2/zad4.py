import glob
import hashlib
import os
import sys

files = {}

def hash_file(file):
    BLOCK_SIZE = 65536 # The size of block read from the file
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        block = f.read(BLOCK_SIZE)
        while block:
            file_hash.update(block)
            block = f.read(BLOCK_SIZE)
        size = os.path.getsize(file)
    return file_hash.hexdigest(), size


def scan_folder(folder):
    for file_name in glob.iglob(folder + '**/*', recursive=True):
        if os.path.isdir(file_name):
            continue
        hash, size = hash_file(file_name) 
        if hash in files:
            if size in files[hash]:
                files[hash][size].append(file_name)
            else:
                files[hash][size] = [file_name]
        else:
            files[hash] = {size:[file_name]}
        

def print_duplicates():
    for hash in files:
        for size in files[hash]:
            if len(files[hash][size]) > 1:
                print("------")
                for file_name in files[hash][size]:
                    print(file_name)
                print("------")

if __name__== "__main__":
    root_dir = sys.argv[1]
    if (root_dir[len(root_dir) - 1] != "\\" and 
        root_dir[len(root_dir) - 1] != "/"):
        print("Make sure folder name ends with slash!")
    else:
        scan_folder(root_dir)
        print_duplicates()