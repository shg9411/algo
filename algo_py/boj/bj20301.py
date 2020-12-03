from collections import deque

n, k, m = map(int, input().split())

num = deque([i for i in range(1, n+1)])
res = []

rt = [-k+1, k]
cnt = 0
i = 0
for _ in range(n):
    num.rotate(rt[i])
    res.append(num.popleft())
    cnt += 1
    if cnt % m == 0:
        i ^= 1
print('\n'.join(map(str, res)))
