import sys
input = sys.stdin.readline

n, k = map(int, input().split())

val = []
dp = [[0 for _ in range(k+1)] for _ in range(n)]

for _ in range(n):
    w, v = map(int, input().split())
    val.append([w, v])

for i in range(n):
    for j in range(k+1):
        dp[i][j] = dp[i-1][j]
        if j-val[i][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-val[i][0]]+val[i][1])

print(dp[n-1][k])
