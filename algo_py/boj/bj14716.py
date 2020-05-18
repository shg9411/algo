import sys
from collections import deque
input = sys.stdin.readline

nm = [[-1, 0], [-1, 1], [-1, -1], [0, 1], [0, -1], [1, 0], [1, 1], [1, -1]]


def bfs(i, j):
    q = deque([[i, j]])
    while q:
        x, y = q.popleft()
        for _x, _y in nm:
            tmpx, tmpy = x+_x, y+_y
            if 0 <= tmpx < M and 0 <= tmpy < N and can[tmpx][tmpy]:
                can[tmpx][tmpy] = 0
                q.append([tmpx, tmpy])


M, N = map(int, input().split())
can = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
for i in range(M):
    for j in range(N):
        if can[i][j]:
            can[i][j] = 0
            bfs(i, j)
            cnt += 1
print(cnt)