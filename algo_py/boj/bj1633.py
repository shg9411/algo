import sys


def dfs(i, w, b):
    if w == 15 and b == 15:
        return 0
    if i == len(white):
        return -1
    if dp[i][w][b]:
        return dp[i][w][b]
    dp[i][w][b] = dfs(i+1, w, b)
    if w < 15:
        dp[i][w][b] = max(dp[i][w][b], dfs(i+1, w+1, b)+white[i])
    if b < 15:
        dp[i][w][b] = max(dp[i][w][b], dfs(i+1, w, b+1)+black[i])
    return dp[i][w][b]


white = []
black = []
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(1001)]
for play in sys.stdin.read().splitlines():
    a, b = map(int, play.split())
    white.append(a)
    black.append(b)

print(dfs(0, 0, 0))