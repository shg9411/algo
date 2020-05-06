import sys
input = sys.stdin.readline

n, m = map(int, input().split())

wak = list(map(int, input().split()))

tmpSet = set(wak)
for i in range(m-1):
    for j in range(i+1, m):
        tmp = wak[i]+wak[j]
        if n >= tmp:
            tmpSet.add(tmp)
wakSet = sorted(list(tmpSet))

dp = [sys.maxsize for _ in range(n+1)]
dp[0] = 0
for i in range(1, n+1):
    for j in wakSet:
        if i-j < 0:
            break
        dp[i] = min(dp[i], dp[i-j]+1)

print(dp[n] if dp[n] < sys.maxsize else -1)