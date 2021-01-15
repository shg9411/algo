import sys
import os


def my_find(directory, suffix):
    for (path, dirr ,files) in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                print(path,file,sep='')
    


if __name__ == '__main__':
    directory = sys.argv[1]
    suffix = sys.argv[2]
    my_find(directory, suffix)
