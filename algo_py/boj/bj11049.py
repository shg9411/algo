import sys
input = sys.stdin.readline

N = int(input())
arr = [0]+[tuple(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N):
    for j in range(1, N-i+1):
        e = i+j
        dp[j][e] = sys.maxsize
        for k in range(j, e):
            dp[j][e] = min(dp[j][k] + dp[k+1][e] + arr[j][0]
                           * arr[k][1]*arr[e][1], dp[j][e])

print(dp[1][N])
