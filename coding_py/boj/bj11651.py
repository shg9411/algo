import sys
n = int(input())
ls = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ls = sorted(ls, key=lambda x: (x[1], x[0]))
for l in ls:
    print(' '.join(map(str,l)))