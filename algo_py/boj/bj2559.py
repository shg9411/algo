n, k = map(int, input().split())
cal = list(map(int, input().split()))
total = sum(cal[:k])
res = total
for i in range(k, n):
    total = total+cal[i]-cal[i-k]
    if cal[i]-cal[i-k] > 0:
        res = max(res, total)
print(res)
