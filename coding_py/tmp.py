import math
n = int(input())
dp = [i for i in range(0, n+1)]
for i in range(1,n+1):
    tmp = int(math.sqrt(i))+1
    for j in range(1,tmp):
        dp[i] = min(dp[i],dp[i-j**2]+1)
print(dp[n])
