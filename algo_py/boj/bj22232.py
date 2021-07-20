import sys


def cmp(x):
    fName, fExt = x.split('.')
    return fName, fExt not in ext, fExt


n, _ = map(int, input().split())
inputs = sys.stdin.read().split()
ext = set(inputs[n:])
print('\n'.join(sorted(inputs[:n], key=cmp)))