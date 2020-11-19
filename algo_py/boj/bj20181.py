n, k = map(int, input().split())
satisfaction = [0]+list(map(int, input().split()))
s = [0]*(n+1)
r = 1
ans = lm = 0
for l in range(1, n+1):
    lm = max(lm, s[l-1])
    while r <= n and ans < k:
        ans += satisfaction[r]
        r += 1
    if ans >= k:
        s[r-1] = max(s[r-1], lm+ans-k)
    else:
        break
    ans -= satisfaction[l]

print(max(s[1:]))
