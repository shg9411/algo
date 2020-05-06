import itertools
import sys
n, m = map(int, input().split())
num = sorted(list(set(map(int, input().split()))))
x = itertools.product(num, repeat=m)
for r in x:
    sys.stdout.write(' '.join(map(str, r))+'\n')
