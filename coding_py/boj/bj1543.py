doc = input().rstrip()
find = input().rstrip()
dl = len(doc)
fl = len(find)
dp = [0 for _ in range(dl+1)]
for i in range(fl, dl+1):
    if doc[i-fl:i] == find:
        dp[i] = max(dp[i], dp[i-fl]+1)
    else:
        dp[i] = dp[i-1]

print(max(dp))
