import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get(i, j, c):
    if c == n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = min(get(c, j, c+1)+cost[i][c], get(i, c, c+1)+cost[j][c])
    return dp[i][j]


n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
print(get(0, 0, 0))