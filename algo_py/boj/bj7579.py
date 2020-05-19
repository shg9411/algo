import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    total = sum(c)
    dp = [0 for _ in range(total+1)]
    for idx, cost in enumerate(c):
        for i in range(total, cost-1, -1):
            if dp[i-cost] + m[idx] > dp[i]:
                dp[i] = dp[i-cost] + m[idx]
        if dp[cost] < m[idx]:
            dp[cost] = m[idx]
    for i in range(total+1):
        if dp[i] >= M:
            print(i)
            break
