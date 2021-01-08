import sys
import os


def my_sed(from_word, to_word, in_file):
    f = open(in_file, "r")
    for line in f.readlines():
        print(line.replace(from_word,to_word))
    f.close()


if __name__ == '__main__':
    from_word = sys.argv[1]
    to_word = sys.argv[2]
    in_file = sys.argv[3]
    my_sed(from_word, to_word, in_file)
