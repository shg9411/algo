import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
t = [[[] for _ in range(N)] for _ in range(H)]
ripen = deque()
for i in range(H):
    for j in range(N):
        tmp = list(input().split())
        t[i][j] = tmp
        for k in range(M):
            if tmp[k] == '1':
                ripen.append((i, j, k))

cnt = -1
while ripen:
    length = len(ripen)
    for _ in range(length):
        k, i, j = ripen.popleft()
        if 0 < i and t[k][i-1][j] == '0':
            t[k][i-1][j] = '1'
            ripen.append((k, i-1, j))
        if i+1 < N and t[k][i+1][j] == '0':
            t[k][i+1][j] = '1'
            ripen.append((k, i+1, j))
        if 0 < j and t[k][i][j-1] == '0':
            t[k][i][j-1] = '1'
            ripen.append((k, i, j-1))
        if j+1 < M and t[k][i][j+1] == '0':
            t[k][i][j+1] = '1'
            ripen.append((k, i, j+1))
        if 0 < k and t[k-1][i][j] == '0':
            t[k-1][i][j] = '1'
            ripen.append((k-1, i, j))
        if k+1 < H and t[k+1][i][j] == '0':
            t[k+1][i][j] = '1'
            ripen.append((k+1, i, j))
    cnt += 1

for tt in t:
    for ttt in tt:
        if '0' in ttt:
            print(-1)
            exit()
print(cnt)