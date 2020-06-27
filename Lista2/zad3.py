import glob
import ntpath
import os
import sys


def rename_files(root_dir):
    for file_name in glob.iglob(root_dir + '**/*', recursive=True):
        # split - return tuple (head, tail) where tail is everything after the final slash. Either part may be empty.
        _, name = ntpath.split(file_name)
        os.rename(file_name, file_name.replace(name,name.lower()))


if __name__== "__main__":
    root_dir = sys.argv[1]
    if (root_dir[len(root_dir) - 1] != "\\" and 
        root_dir[len(root_dir) - 1] != "/"):
        print("Make sure folder name ends with slash!")
    else:
        rename_files(root_dir)
