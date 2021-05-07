n, m = map(int, input().split())
adj = [[101]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

for k in range(1, n+1):
    adj[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (tmp := adj[i][k] + adj[k][j]) < adj[i][j]:
                adj[i][j] = tmp
res = n*n
a = b = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        val = 0
        for k in range(1, n+1):
            val += adj[k][i] if adj[k][i] < adj[k][j] else adj[k][j]
        if res > val:
            a, b, res = i, j, val
print(a, b, res*2)
