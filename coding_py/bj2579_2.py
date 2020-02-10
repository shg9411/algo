import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
dp = [0 for _ in range(n+1)]
for _ in range(n):
    stair.append(int(input()))
dp[1] = stair[1]
dp[2] = stair[1]+stair[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])

print(dp[n])