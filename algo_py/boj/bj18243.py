import sys
input = sys.stdin.readline

n, k = map(int, input().split())

adj = [[987654321 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

for i in range(1, n+1):
    adj[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k]+adj[k][j]
for line in adj[1:]:
    for tmp in line[1:]:
        if tmp > 6:
            print("Big World!")
            exit()
print("Small World!")