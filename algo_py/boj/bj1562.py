n = int(input())

dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(101)]
full = (1 << 10)-1
mod = 10**9
res = 0
for i in range(1, 10):
    dp[1][i][1 << i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(full+1):
            if j == 0:
                dp[i][0][k | (1 << 0)] = (
                    dp[i][0][k | (1 << 0)] + dp[i - 1][1][k]) % mod
            elif j == 9:
                dp[i][9][k | (1 << 9)] = (
                    dp[i][9][k | (1 << 9)] + dp[i - 1][8][k]) % mod
            else:
                dp[i][j][k | (1 << j)] = (
                    dp[i][j][k | (1 << j)] + dp[i - 1][j - 1][k]) % mod
                dp[i][j][k | (1 << j)] = (
                    dp[i][j][k | (1 << j)] + dp[i - 1][j + 1][k]) % mod
for i in range(10):
    res = (res+dp[n][i][full]) % mod
print(res)
