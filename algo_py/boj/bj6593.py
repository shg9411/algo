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
        lenq = len(q)
        for _ in range(lenq):
            k, i, j = q.popleft()
            if 0 <= i-1:
                if building[k][i-1][j] == 'E':
                    can = True
                    break
                if building[k][i-1][j] == '.' and not visited[k][i-1][j]:
                    visited[k][i-1][j] = True
                    q.append([k, i-1, j])

            if i+1 < R:
                if building[k][i+1][j] == 'E':
                    can = True
                    break
                if building[k][i+1][j] == '.' and not visited[k][i+1][j]:
                    visited[k][i+1][j] = True
                    q.append([k, i+1, j])
            if 0 <= j-1:
                if building[k][i][j-1] == 'E':
                    can = True
                    break
                if building[k][i][j-1] == '.' and not visited[k][i][j-1]:
                    visited[k][i][j-1] = True
                    q.append([k, i, j-1])
            if j+1 < C:
                if building[k][i][j+1] == 'E':
                    can = True
                    break
                if building[k][i][j+1] == '.' and not visited[k][i][j+1]:
                    visited[k][i][j+1] = True
                    q.append([k, i, j+1])
            if 0 <= k-1:
                if building[k-1][i][j] == 'E':
                    can = True
                    break
                if building[k-1][i][j] == '.' and not visited[k-1][i][j]:
                    visited[k-1][i][j] = True
                    q.append([k-1, i, j])
            if k+1 < L:
                if building[k+1][i][j] == 'E':
                    can = True
                    break
                if building[k+1][i][j] == '.' and not visited[k+1][i][j]:
                    visited[k+1][i][j] = True
                    q.append([k+1, i, j])
        if can:
            break
    print("Escaped in {} minute(s).".format(cnt) if can else "Trapped!")
