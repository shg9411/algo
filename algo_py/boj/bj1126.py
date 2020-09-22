n = int(input())
h = sorted(map(int, input().split()))
dp = [[-1 for _ in range(500001)] for _ in range(2)]
dp[0][0] = dp[1][0] = m = 0
for i in range(n):
    for j in range(m+1):
        if dp[0][j] < 0:
            continue
        if j-h[i] >= 0:
            if dp[0][j] > dp[1][j-h[i]]:
                dp[1][j-h[i]] = dp[0][j]
        else:
            t = dp[0][j] + h[i] - j
            if t > dp[1][h[i]-j]:
                dp[1][h[i]-j] = t
        t = dp[0][j]+h[i]
        if t > dp[1][j+h[i]]:
            dp[1][j+h[i]] = t
    m += h[i]
    for j in range(m+1):
        dp[0][j] = dp[1][j]
print(dp[0][0] if dp[0][0] > 0 else -1)