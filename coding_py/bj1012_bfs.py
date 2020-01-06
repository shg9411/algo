import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        tmp = q.popleft()
        x = tmp[0]
        y = tmp[1]
        for move in nm:
            nx = x+move[0]
            ny = y+move[1]
            if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] == 1:
                farm[nx][ny] = 2
                q.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    count = 0

    for x in range(n):
        for y in range(m):
            if farm[x][y] == 1:
                farm[x][y] = 2
                count += 1
                bfs(x, y)
    print(count)
