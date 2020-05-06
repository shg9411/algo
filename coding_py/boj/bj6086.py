import sys
from collections import deque
input = sys.stdin.readline

N = int(input())


def change(i):
    if i <= 'Z':
        return ord(i)-ord('A')
    return ord(i)-ord('a')+26


c = [[0 for _ in range(52)] for _ in range(52)]
f = [[0 for _ in range(52)] for _ in range(52)]
adj = [[] for _ in range(52)]
for _ in range(N):
    a, b, F = input().split()
    a, b = change(a), change(b)
    F = int(F)
    c[a][b] += F
    c[b][a] += F
    adj[a].append(b)
    adj[b].append(a)

res = 0
S = change('A')
T = change('Z')
while 1:
    prev = [-1 for _ in range(52)]
    q = deque()
    q.append(S)
    while q:
        tmp = q.popleft()
        if tmp == T:
            break
        for next in adj[tmp]:
            if prev[next] == -1 and c[tmp][next] - f[tmp][next] > 0:
                q.append(next)
                prev[next] = tmp
    if prev[T] == -1:
        break
    x = sys.maxsize
    i = T
    while i != S:
        x = min(x, c[prev[i]][i]-f[prev[i]][i])
        i = prev[i]
    i = T
    while i != S:
        f[prev[i]][i] += x
        f[i][prev[i]] -= x
        i = prev[i]
    res += x
print(res)
