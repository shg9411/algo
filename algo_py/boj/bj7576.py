import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = []
ripen = deque()
for i in range(n):
    tomato.append(list(input().split()))
    for j in range(m):
        if tomato[i][j] == '1':
            ripen.append((i, j))
day = -1
while ripen:
    length = len(ripen)
    for _ in range(length):
        x, y = ripen.popleft()
        if x > 0:
            if tomato[x-1][y] == '0':
                tomato[x-1][y] = '1'
                ripen.append((x-1, y))
        if y > 0:
            if tomato[x][y-1] == '0':
                tomato[x][y-1] = '1'
                ripen.append((x, y-1))
        if x < n-1:
            if tomato[x+1][y] == '0':
                tomato[x+1][y] = '1'
                ripen.append((x+1, y))
        if y < m-1:
            if tomato[x][y+1] == '0':
                tomato[x][y+1] = '1'
                ripen.append((x, y+1))
    day += 1

for line in tomato:
    if '0' in line:
        print(-1)
        exit()
print(day)