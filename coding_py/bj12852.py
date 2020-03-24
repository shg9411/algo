from collections import deque

n = int(input())
if n == 1:
    print(0)
    print(1)
    exit()
dp = [0 for _ in range(n+1)]
q = deque([])
q.append(n)
while dp[1] < 1:
    i = q.popleft()
    if i % 2 == 0 and dp[i//2] < 1:
        dp[i//2] = i
        q.append(i//2)
    if i % 3 == 0 and dp[i//3] < 1:
        dp[i//3] = i
        q.append(i//3)
    if dp[i-1] < 1:
        dp[i-1] = i
        q.append(i-1)

res = [1]
while dp[res[-1]]:
    res.append(dp[res[-1]])
print(len(res)-1)
print(' '.join(map(str, res[::-1])))
