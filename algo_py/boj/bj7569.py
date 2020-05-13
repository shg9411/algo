import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
well_tomato = deque([])
not_well = 0
for i in range(H):
    for j in range(N):
        tomato[i].append(list(map(int, input().split())))
        for k in range(M):
            if tomato[i][j][k] == 1:
                well_tomato.append([i, j, k])
            elif tomato[i][j][k] == 0:
                not_well += 1

if not not_well:
    print(0)
    exit()

if not_well and not well_tomato:
    print(-1)
    exit()

cnt = 0
while well_tomato:
    for _ in range(len(well_tomato)):
        k, i, j = well_tomato.popleft()
        tmpx = i-1
        if 0 <= tmpx:
            if tomato[k][tmpx][j] == 0:
                tomato[k][tmpx][j] = 1
                not_well -= 1
                well_tomato.append([k, tmpx, j])
        tmpx = i+1
        if tmpx < N:
            if tomato[k][tmpx][j] == 0:
                tomato[k][tmpx][j] = 1
                not_well -= 1
                well_tomato.append([k, tmpx, j])
        tmpy = j-1
        if 0 <= tmpy:
            if tomato[k][i][tmpy] == 0:
                tomato[k][i][tmpy] = 1
                not_well -= 1
                well_tomato.append([k, i, tmpy])
        tmpy = j+1
        if tmpy < M:
            if tomato[k][i][tmpy] == 0:
                tomato[k][i][tmpy] = 1
                not_well -= 1
                well_tomato.append([k, i, tmpy])
        tmpz = k-1
        if 0 <= tmpz:
            if tomato[tmpz][i][j] == 0:
                tomato[tmpz][i][j] = 1
                not_well -= 1
                well_tomato.append([tmpz, i, j])
        tmpz = k+1
        if tmpz < H:
            if tomato[tmpz][i][j] == 0:
                tomato[tmpz][i][j] = 1
                not_well -= 1
                well_tomato.append([tmpz, i, j])
    cnt += 1
    if not not_well:
        break


print(-1 if not_well else cnt)
