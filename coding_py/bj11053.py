a = int(input())
arr = list(map(int, input().split()))
dp = [0] * a
for i in range(a):
    for j in range(a):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
