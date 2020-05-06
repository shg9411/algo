n = int(input())

job = []
dp = [0 for _ in range(21)]
for _ in range(n):
    job.append(list(map(int, input().split())))
for i in range(n-1, -1, -1):
    if job[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+job[i][0]]+job[i][1])

print(dp[0])

