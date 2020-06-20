import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < r and 0 <= y < c and arr[x][y] == '.':
                queue.append([x, y])
                arr[x][y] = arr[a][b]+1


def bfs_S(i, j):
    queue = deque()
    queue.append([i, j])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while queue:
        a, b = queue.popleft()
        #del queue[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < r and 0 <= y < c and arr[x][y] > arr[a][b]:
                queue.append([x, y])
                arr[x][y] = arr[a][b]+1


r, c = map(int, input().split())
q, p = 0, 0
arr = []
for i in range(r):
    arr.append(list(input().rstrip()))
print(arr)

for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            arr[i][j] = 0
            bfs(i, j)
for i in range(r):
    for j in range(c):
        if arr[i][j] == '.':
            arr[i][j] = 100

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'D':
            arr[i][j] = 51
            q = i
            p = j
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':
            arr[i][j] = -1

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            arr[i][j] = 1
            bfs_S(i, j)

check = True
for i in range(r):
    for j in range(c):
        if arr[i][j] == 51:
            check = False
if check:
    print(arr[q][p]-1)
else:
    print('KAKTUS')
