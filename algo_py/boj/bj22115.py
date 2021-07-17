n, k = map(int, input().split())
coffees = list(map(int, input().split()))

dp = [999]*(k+1)
dp[0] = 0

for coffee in coffees:
    for i in range(k-coffee, -1, -1):
        dp[i+coffee] = min(dp[i+coffee], dp[i]+1)
print(dp[k] if dp[k] <= n else -1)
