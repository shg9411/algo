import sys
import os


def my_find(directory, suffix):
    try:
        names = os.listdir(directory)
        for name in names:
            full_name = os.path.join(directory, name)
            if os.path.isdir(full_name):
                my_find(full_name, suffix)
            elif full_name.endswith(suffix):
                print(os.path.abspath(full_name))
    except:
        pass


if __name__ == '__main__':
    directory = sys.argv[1]
    suffix = sys.argv[2]
    my_find(directory, suffix)
