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
for i, cnt in enumerate(map(int, input().split())):
    c[m+i][E] = cnt
    adj[m+i].append(E)
    adj[E].append(m+i)
for i, cnt in enumerate(map(int, input().split())):
    c[S][i] = cnt
    adj[S].append(i)
    adj[i].append(S)
for i in range(m):
    for j, val in enumerate(map(int, input().split())):
        d[i][j+m], d[j+m][i] = val, -val
        c[i][j+m] = INF
        adj[i].append(m+j)
        adj[m+j].append(i)

res = 0
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
        res += flow*d[prev[i]][i]
        f[prev[i]][i] += flow
        f[i][prev[i]] -= flow
        i = prev[i]
print(res)