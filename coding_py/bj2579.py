import sys

s = int(sys.stdin.readline())
li = list()
dp = [0]*(s+1)
for _ in range(s):
    li.append(int(sys.stdin.readline()))
dp[0] = li[0]
dp[1] = li[1]
dp[2] = li[1]+li[2]
for i in range(3, s+1):
    dp[i] = max(li[i]+dp[i-2], li[i] + li[i-1] + dp[i-3])
print(dp[s])
