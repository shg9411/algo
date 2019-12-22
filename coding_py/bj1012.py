import sys
t = int(sys.stdin.readline())

nt = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def bfs(arr, visit, i, j):
    q = []
    q.append([i, j])
    while q:
        tmp = q.pop(0)
        for k in range(4):
            x, y = tmp[0]+nt[k][0], tmp[1] + nt[k][1]
            if x < 0 or y < 0 or x >= len(arr) or y >= len(arr[0]):
                continue
            if arr[x][y] == 0:
                continue
            if visit[x][y]:
                continue
            q.append([x, y])
            visit[x][y] = True


while t:
    t -= 1
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0]*m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    warm = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(farm, visited, i, j)
                warm += 1
    print(warm)
