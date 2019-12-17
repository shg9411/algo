import sys

n, m = map(int, sys.stdin.readline().split())

pocketmon = []

for _ in range(n):
    pocketmon.append(sys.stdin.readline())

for _ in range(m):
    tmp = sys.stdin.readline()
    try:
        val = int(tmp)
        print(pocketmon[val-1])
    except ValueError:
        print(pocketmon.index(tmp)+1)
