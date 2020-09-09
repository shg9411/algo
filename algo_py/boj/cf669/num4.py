import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [i for i in range(n)]
cnt = 0
tmp = num[0]
for x in num[1:]:
    if x >= tmp:
        cnt += 1
        tmp = x
if cnt == 0:
    print(dp[n-1])
else:
    print(min(cnt, dp[n-1]))
