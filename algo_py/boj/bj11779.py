import heapq
import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    def dijkstra(s, e):
        d = [sys.maxsize for _ in range(n+1)]
        t = []
        d[s] = 0
        i = [0 for _ in range(n+1)]
        q = []
        heapq.heappush(q, [0, s])
        while q:
            co, po = heapq.heappop(q)
            if co > d[po]:
                continue
            for p, c in a[po].items():
                c += co
                if c < d[p]:
                    d[p] = c
                    i[p] = po
                    heapq.heappush(q, [c, p])
        r = []
        t = e
        while t:
            r.append(t)
            t = i[t]
        return d[e], r[::-1]
    
    
    n = int(input())
    m = int(input())
    a = [dict() for _ in range(n+1)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        if a[x].get(y):
            a[x][y] = min(c, a[x].get(y))
        else:
            a[x][y] = c

    s, e = map(int, input().split())
    m, r = dijkstra(s, e)
    print(m)
    print(len(r))
    print(*r)
    
    
if __name__=='__main__':
    solve()