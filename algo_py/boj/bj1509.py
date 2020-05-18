string = ' '+input()
length = len(string)
dp = [[False for _ in range(length)] for _ in range(length)]
for i in range(length):
    dp[i][i] = True
for i in range(length-1):
    dp[i][i+1] = string[i] == string[i+1]
for i in range(3, length+1):
    for j in range(length-i+1):
        x = j+i-1
        dp[j][x] = string[j] == string[x] and dp[j+1][x-1]

ans = [0 for _ in range(length)]
for i in range(1, length):
    for j in range(1, i+1):
        if dp[j][i]:
            if ans[i] == 0 or ans[i] > ans[j-1] + 1:
                ans[i] = ans[j-1]+1
print(ans[-1])
