n, m = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n+1)]
ans = [[0 for _ in range(m)] for _ in range(n+1)]
get = [[0 for _ in range(m)]]
for _ in range(n):
    get.append(list(map(int, input().split()))[1:])

for i in range(m):
    for j in range(1, n+1):
        for k in range(j+1):
            if dp[j][i] < dp[j-k][i-1]+get[k][i]:
                dp[j][i] = dp[j-k][i-1]+get[k][i]
                ans[j][i] = k

print(dp[n][m-1])
res = []
cost = n
cur = m-1
while cur >= 0:
    c = ans[cost][cur]
    res.append(c)
    cost -= c
    cur -= 1
print(*res[::-1])
