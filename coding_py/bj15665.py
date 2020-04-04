import itertools
import sys
n, m = map(int, input().split())
num = sorted(list(set(map(int, input().split()))))
for r in itertools.product(num, repeat=m):
    sys.stdout.write(' '.join(map(str, r))+'\n')
