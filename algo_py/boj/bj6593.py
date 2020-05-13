import sys
from collections import deque
input = sys.stdin.readline

while 1:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break
    building = [[] for _ in range(L)]
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    S = [-1, -1, -1]
    for i in range(L):
        for j in range(R):
            building[i].append(list(input().rstrip()))
            for k in range(C):
                if building[i][j][k] == 'S':
                    S = [i, j, k]
                    visited[i][j][k] = True
        input()

    q = deque([S])
    cnt = 0
    can = False
    while q:
        cnt += 1
        for _ in range(len(q)):
            k, i, j = q.popleft()
            tmpx = i-1
            if 0 <= tmpx:
                if building[k][tmpx][j] == 'E':
                    can = True
                    break
                if building[k][tmpx][j] == '.' and not visited[k][tmpx][j]:
                    visited[k][tmpx][j] = True
                    q.append([k, tmpx, j])
            tmpx += 2
            if tmpx < R:
                if building[k][tmpx][j] == 'E':
                    can = True
                    break
                if building[k][tmpx][j] == '.' and not visited[k][tmpx][j]:
                    visited[k][tmpx][j] = True
                    q.append([k, tmpx, j])
            tmpy = j-1
            if 0 <= tmpy:
                if building[k][i][tmpy] == 'E':
                    can = True
                    break
                if building[k][i][tmpy] == '.' and not visited[k][i][tmpy]:
                    visited[k][i][tmpy] = True
                    q.append([k, i, tmpy])
            tmpy += 2
            if tmpy < C:
                if building[k][i][tmpy] == 'E':
                    can = True
                    break
                if building[k][i][tmpy] == '.' and not visited[k][i][tmpy]:
                    visited[k][i][tmpy] = True
                    q.append([k, i, tmpy])
            tmpz = k-1
            if 0 <= tmpz:
                if building[tmpz][i][j] == 'E':
                    can = True
                    break
                if building[tmpz][i][j] == '.' and not visited[tmpz][i][j]:
                    visited[tmpz][i][j] = True
                    q.append([tmpz, i, j])
            tmpz += 2
            if tmpz < L:
                if building[tmpz][i][j] == 'E':
                    can = True
                    break
                if building[tmpz][i][j] == '.' and not visited[tmpz][i][j]:
                    visited[tmpz][i][j] = True
                    q.append([tmpz, i, j])
        if can:
            break
    print("Escaped in {} minute(s).".format(cnt) if can else "Trapped!")
