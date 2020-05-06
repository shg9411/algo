import sys
import copy
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

res = 1
maxH = 1
minH = 100
area = []
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]

for i in range(n):
    area.append(list(map(int, input().split())))
    maxH = max(maxH, max(area[i]))
    minH = min(minH, min(area[i]))


def dfs(i, j):
    visited[i][j] = True
    for mv in nm:
        nx = i+mv[0]
        ny = j+mv[1]
        if 0 <= nx < n and 0 <= ny < n and h < area[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


def bfs(i, j):
    q = [[i, j]]
    while q:
        tmp = q.pop(0)
        x = tmp[0]
        y = tmp[1]
        for mv in nm:
            nx = x+mv[0]
            ny = y+mv[1]
            if 0 <= nx < n and 0 <= ny < n and h < area[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])


for h in range(minH, maxH):
    tmp = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:
                #bfs
                '''
                visited[i][j] = True
                bfs(i, j)
                '''
                #dfs
                dfs(i, j)
                tmp += 1
    res = max(res, tmp)
print(res)
