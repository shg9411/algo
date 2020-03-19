N, M = map(int, input().split())
s = []
tmp = dict()
can = set()
for w in map(int, input().split()):
    try:
        tmp[w] += 1
    except:
        s.append(w)
        can.add(w)
        tmp[w] = 1

for i in range(len(s)):
    if tmp.get(s[i]) > 1 and s[i]*2 <= N:
        can.add(s[i]*2)
    for j in range(i + 1, len(s)):
        if s[i] + s[j] <= N:
            can.add(s[i] + s[j])
can = sorted(set(can))
dp = [10000 for i in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    for j in can:
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i - j] + 1)
if dp[N] >= 10000:
    print(-1)
else:
    print(dp[N])