n = input()
arr = [int(x) for x in list(n)]
arr_length = len(arr)
dp = [0] * (arr_length+1)
dp[0] = 1
for i in range(1, arr_length+1):
    if (1 <= arr[i-1]) and (arr[i-1] <= 9):
        dp[i] += dp[i-1]
    if i == 1:
        continue
    value = (arr[i-2] * 10 + arr[i-1])
    if (10 <= value) and (value <= 26):
        dp[i] += dp[i-2]

print(dp[arr_length] % 1000000)
