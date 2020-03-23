import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
num = [0]+list(map(int, input().split()))
dp = [[-1000, -1000] for _ in range(n)]
dp[0] = [0, 0]
dp[1] = [num[1], num[1]]
res = max(dp[1][0], dp[1][1])

for i in range(2, n):
    dp[i][0] = max(dp[i-1][0]+num[i], num[i])
    dp[i][1] = max(dp[i-2][0]+num[i], dp[i-1][1]+num[i])
    res = max(res, dp[i][0], dp[i][1])
print(res)
