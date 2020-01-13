import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())
circle = [deque(list(map(int, input().split()))) for _ in range(n)]
circle.insert(0, deque([0 for _ in range(m)]))
circle.insert(n+1, deque([0 for _ in range(m)]))

total = n*m

for _ in range(t):
    x, d, k = map(int, input().split())
    tmp = set()
    for idx in range(x, n+2, x):
        circle[idx].rotate(k) if d == 0 else circle[idx].rotate(-k)
    for i in range(1, n+2):
        for j in range(0, m):
            if circle[i][j] != 0:
                j1 = (j+1) % m
                j2 = (j-1) % m
                if circle[i][j] == circle[i+1][j]:
                    tmp.add((i, j))
                    tmp.add((i+1, j))
                if circle[i][j] == circle[i][j1]:
                    tmp.add((i, j))
                    tmp.add((i, j1))
                if circle[i][j] == circle[i][j2]:
                    tmp.add((i, j))
                    tmp.add((i, j2))
    total -= len(tmp)
    if tmp:
        for (x, y) in tmp:
            circle[x][y] = 0
    else:
        res = 0
        for x in range(1, n+2):
            res += sum(circle[x])
        for x in range(1, n+2):
            for y in range(m):
                if circle[x][y] != 0:
                    if circle[x][y] < res/total:
                        circle[x][y] += 1
                    elif circle[x][y] > res/total:
                        circle[x][y] -= 1
res = 0
for x in range(1, n+2):
    res += sum(circle[x])
print(res)
