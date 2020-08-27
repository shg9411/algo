#pypy3
import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9
n, m = map(int, input().split())
maxv = n+m+2
S = maxv-2
E = maxv-1
c = [[0 for _ in range(maxv)] for _ in range(maxv)]
d = [[0 for _ in range(maxv)] for _ in range(maxv)]
f = [[0 for _ in range(maxv)] for _ in range(maxv)]
adj = [[] for _ in range(maxv)]
for i in range(m):
    c[i+n][E] = 1
    adj[i+n].append(E)
    adj[E].append(i+n)
for i in range(n):
    c[S][i] = 1
    adj[S].append(i)
    adj[i].append(S)
    tmp = list(map(int, input().split()))
    idx = 1
    while idx < tmp[0]*2:
        j, val = tmp[idx], tmp[idx+1]
        d[i][n+j-1], d[n+j-1][i] = -val, val
        c[i][n+j-1] = 1
        adj[i].append(n+j-1)
        adj[n+j-1].append(i)
        idx += 2
res = 0
cnt = 0
while True:
    prev = [-1 for _ in range(maxv)]
    dist = [INF for _ in range(maxv)]
    atQ = [False for _ in range(maxv)]
    q = deque()
    dist[S] = 0
    atQ[S] = True
    q.append(S)
    while q:
        cur = q.popleft()
        atQ[cur] = False
        for nxt in adj[cur]:
            if c[cur][nxt] - f[cur][nxt] > 0 and dist[nxt] > dist[cur] + d[cur][nxt]:
                dist[nxt] = dist[cur]+d[cur][nxt]
                prev[nxt] = cur
                if not atQ[nxt]:
                    q.append(nxt)
                    atQ[nxt] = True
    if prev[E] == -1:
        break
    flow = INF
    i = E
    while i != S:
        flow = min(flow, c[prev[i]][i]-f[prev[i]][i])
        i = prev[i]
    i = E
    while i != S:
        res -= flow*d[prev[i]][i]
        f[prev[i]][i] += flow
        f[i][prev[i]] -= flow
        i = prev[i]
    cnt += 1
print(cnt)
print(res)
