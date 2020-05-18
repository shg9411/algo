import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
nm = [[-1, 0], [0, -1], [1, 0], [0, 1]]
size = [0 for _ in range(N*M+1)]
group = [False for _ in range(N*M+1)]
shape = []
ans = 0
for i in range(N):
    shape.append(list(map(int, input().split())))


def setNum(n, m, num):
    c = 1
    q = deque()
    shape[n][m] = num
    q.append([n, m])
    while q:
        x, y = q.popleft()
        for _x, _y in nm:
            tmpx, tmpy = x+_x, y+_y
            if 0 <= tmpx < N and 0 <= tmpy < M and shape[tmpx][tmpy] == 1:
                shape[tmpx][tmpy] = num
                c += 1
                q.append([tmpx, tmpy])
    return c


def dfs(n, m, idx, res):
    global ans
    if idx == 4:
        if ans < res:
            ans = res
        return
    tx = n+nm[idx][0]
    ty = m+nm[idx][1]
    if 0 <= tx < N and 0 <= ty < M and group[shape[tx][ty]] == False and shape[tx][ty] != 0:
        group[shape[tx][ty]] = True
        dfs(n, m, idx+1, res+size[shape[tx][ty]])
        group[shape[tx][ty]] = False
    else:
        dfs(n, m, idx+1, res)
        return


where = []
num = 2
for i in range(N):
    for j in range(M):
        if shape[i][j] == 1:
            size[num] = setNum(i, j, num)
            num += 1
        elif shape[i][j] == 0:
            where.append([i, j])
for x, y in where:
    dfs(x, y, 0, 1)


print(ans)