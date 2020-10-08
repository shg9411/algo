import sys
from collections import deque
input = sys.stdin.readline
nm = [(-1, 0), (0, -1), (1, 0), (0, 1)]


n, m = map(int, input().split())
ice = [[] for _ in range(n)]
visit = [[0]*m for _ in range(n)]
v = []
q = deque()
r = 0
for i in range(n):
    ice[i] = list(map(int, input().split()))
    for j in range(m):
        if ice[i][j]:
            v.append((i, j))
icecnt = len(v)
while 1:
    for i, j in v:
        if ice[i][j] > 0:
            q.append((i, j))
            visit[i][j] = 1
            break
    cnt = 0
    melt = 0
    while q:
        i, j = q.popleft()
        w = 0
        cnt += 1
        for _i, _j in nm:
            ni, nj = i+_i, j+_j
            if not visit[ni][nj]:
                if ice[ni][nj] <= 0:
                    w += 1
                else:
                    q.append((ni, nj))
                    visit[ni][nj] = 1
        ice[i][j] -= w
        if ice[i][j] <= 0:
            melt += 1
    visit = [[0]*m for _ in range(n)]
    r += 1
    if cnt != icecnt:
        print(r-1)
        exit()
    icecnt -= melt
    if icecnt == 0:
        print(0)
        exit()
