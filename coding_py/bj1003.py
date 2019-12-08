import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())
    dp = [[0 for col in range(2)] for row in range(41)]
    dp[0][0]=dp[1][1] = 1

    for i in range(2,num+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    print("%d %d" % (dp[num][0],dp[num][1]))