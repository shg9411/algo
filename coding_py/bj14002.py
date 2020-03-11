a = int(input())
arr = list(map(int, input().split()))
dp = [0] * a
res = [[i] for i in arr]
for i in range(a):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            res[i] = res[j]+[arr[i]]
    dp[i] += 1
ans = max(dp)
print(ans)
print(*res[dp.index(ans)])
