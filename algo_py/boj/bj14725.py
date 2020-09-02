import sys
input = sys.stdin.readline
n = int(input())
ant = dict()


def printAll(cur, cnt):
    tmp = cur
    cur = sorted(cur.items())
    for c in cur:
        print('--'*cnt, c[0], sep='')
        printAll(tmp[c[0]], cnt+1)


for _ in range(n):
    x = input().split()[1:]
    cur = ant
    for info in x:
        if info not in cur:
            cur[info] = dict()
        cur = cur[info]

printAll(ant, 0)