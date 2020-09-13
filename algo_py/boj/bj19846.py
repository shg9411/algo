n, m, q = map(int, input().split())
alpha = 'abcdefghijklmnopqrstuvwxyz'[:n]
ans = ''
idx = 0
while m:
    if m >= 2:
        ans += alpha[idx]*2
        idx = (idx+1) % n
        m -= 2
    else:
        ans += alpha[idx]
        break
print(ans)
