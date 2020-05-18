import sys
from collections import deque
input = sys.stdin.readline


def outside(i, j):
    if i > 0:
        if land[i-1][j] == 0:
            return True
    if j > 0:
        if land[i][j-1] == 0:
            return True
    if i < n-1:
        if land[i+1][j] == 0:
            return True

    if j < n-1:
        if land[i][j+1] == 0:
            return True
    return False


def bfs(i, j):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[i][j] = True
    cur = land[i][j]
    cnt = 0
    q = deque()
    q.append([i, j])
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if x > 0 and land[x-1][y] != cur and not visited[x-1][y]:
                if land[x-1][y]:
                    return cnt
                visited[x-1][y] = True
                q.append([x-1, y])
            if y > 0 and land[x][y-1] != cur and not visited[x][y-1]:
                if land[x][y-1]:
                    return cnt
                visited[x][y-1] = True
                q.append([x, y-1])
            if x < n-1 and land[x+1][y] != cur and not visited[x+1][y]:
                if land[x+1][y]:
                    return cnt
                visited[x+1][y] = True
                q.append([x+1, y])
            if y < n-1 and land[x][y+1] != cur and not visited[x][y+1]:
                if land[x][y+1]:
                    return cnt
                visited[x][y+1] = True
                q.append([x, y+1])
        cnt += 1


def setLand(i, j, num):
    q = deque()
    q.append([i, j])
    land[i][j] = num
    while q:
        x, y = q.popleft()
        if x > 0 and land[x-1][y] == 1:
            land[x-1][y] = num
            q.append([x-1, y])
        if y > 0 and land[x][y-1] == 1:
            land[x][y-1] = num
            q.append([x, y-1])
        if x < n-1 and land[x+1][y] == 1:
            land[x+1][y] = num
            q.append([x+1, y])
        if y < n-1 and land[x][y+1] == 1:
            land[x][y+1] = num
            q.append([x, y+1])


n = int(input())
res = n**2
land = [list(map(int, input().split())) for _ in range(n)]
num = 2
for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            setLand(i, j, num)
            num += 1

for i in range(n):
    for j in range(n):
        if land[i][j] != 0 and outside(i, j):
            res = min(res, bfs(i, j))
            if res == 1:
                break
print(res)
