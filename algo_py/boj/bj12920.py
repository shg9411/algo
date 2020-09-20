import sys
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    dp = [0 for _ in range(K+1)]
    for _ in range(N):
        v, c, k = map(int, input().split())
        x = 1
        while k:
            t = min(k, x)
            for i in range(K, v*t-1, -1):
                dp[i] = max(dp[i-v*t]+c*t, dp[i])
            x <<= 1
            k -= t
    print(max(dp))


if __name__ == "__main__":
    solve()
