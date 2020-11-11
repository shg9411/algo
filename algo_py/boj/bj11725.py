import sys
from collections import deque
input = sys.stdin.readline


def solve():
    n = int(input())
    p = [0]*(n+1)
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    q = deque([1])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if p[v]:
                continue
            p[v] = u
            q.append(v)
    print('\n'.join(map(str, p[2:])))


if __name__ == '__main__':
    solve()
