import sys
import operator
input = sys.stdin.readline
L = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    L.append((x, y))
nL = sorted(L, key=operator.itemgetter(1,0))
for i in nL:
    print(i[0], i[1])
