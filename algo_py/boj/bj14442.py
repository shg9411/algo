# pypy3
import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
load = [input().rstrip() for _ in range(n)]
visited = [[[k+1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited[0][0][0] = 0
q = deque([[0, 0, 0, 0]])
res = 1
while q:
    qlen = len(q)
    for _ in range(qlen):
        x, y, s, c = q.popleft()
        if x == n-1 and y == m-1:
            print(res)
            exit()
        for _x, _y in nm:
            nx = x+_x
            ny = y+_y
            if 0 <= nx < n and 0 <= ny < m:
                if load[nx][ny] == '1' and visited[nx][ny] > c+1:
                    visited[nx][ny] = c+1
                    q.append([nx, ny, c+1])
                elif load[nx][ny] == '0' and visited[nx][ny] > c:
                    visited[nx][ny] = c
                    q.append([nx, ny, c])
    res += 1
print(-1)
