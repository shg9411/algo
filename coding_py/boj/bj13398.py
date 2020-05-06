import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
num = list(map(int, input().split()))
dp = [[-1001, -1001] for _ in range(n)]
dp[0] = [num[0], num[0]]
res = num[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0]+num[i], num[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+num[i])
    res = max(res, dp[i][0], dp[i][1])

print(res)
