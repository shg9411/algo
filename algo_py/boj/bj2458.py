import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = True

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if adj[i][k] and adj[k][j]:
                adj[i][j] = True
cnt = 0
for i in range(1, N+1):
    can = True
    for j in range(1, N+1):
        if i == j:
            continue
        if adj[i][j] == adj[j][i] == False:
            can = False
            break
    if can:
        cnt += 1
print(cnt)
