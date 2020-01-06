import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
miro = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
q = deque()
visited[0][0] = True
dist[0][0] = 1
q.append((0, 0))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if miro[nx][ny] == 0 or visited[nx][ny]:
            continue
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y]+1
        visited[nx][ny] = True

print(dist[n-1][m-1])
