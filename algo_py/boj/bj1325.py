import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
res = [-1, [-1]]

for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

for i in range(1, n+1):
    cnt = 0
    q = deque([i])
    check = [False for _ in range(n+1)]
    check[i] = True
    while q:
        x = q.popleft()
        cnt += 1
        for a in adj[x]:
            if not check[a]:
                check[a] = True
                q.append(a)
    if cnt > res[0]:
        res = [cnt, [i]]
    elif cnt == res[0]:
        res[1].append(i)

print(*res[1])