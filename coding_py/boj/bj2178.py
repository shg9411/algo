from collections import deque
n, m = map(int, input().split())
d = [list(map(int, list(input()))) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
que = deque()
visited = [[False]*m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

que.append((0, 0))
visited[0][0] = True
dist[0][0] = 1

while que:
    x, y = que.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and d[nx][ny] == 1:
                que.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True

print(dist[n-1][m-1])
