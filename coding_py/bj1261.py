import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
wall = [list(input().rstrip()) for _ in range(n)]
dist = [[9999 for _ in range(m)] for _ in range(n)]
#visited = [[False for _ in range(m)] for _ in range(n)]
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def bfs(x, y):
    dist[x][y] = 0
    q = deque([[x, y]])

    while q:
        tmp = q.popleft()
        tx = tmp[0]
        ty = tmp[1]
        for move in nm:
            nx = tx+move[0]
            ny = ty+move[1]

            if 0 <= nx < n and 0 <= ny < m:
                if wall[nx][ny] == '1':
                    if dist[nx][ny] > dist[tx][ty] + 1:
                        dist[nx][ny] = dist[tx][ty] + 1
                        q.append([nx, ny])
                elif wall[nx][ny] == '0':
                    if dist[nx][ny] > dist[tx][ty]:
                        dist[nx][ny] = dist[tx][ty]
                        q.append([nx, ny])


bfs(0, 0)
print(dist[n-1][m-1])

