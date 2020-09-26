import sys
import heapq
input = sys.stdin.readline


def s():
    def g(s, e):
        d = [sys.maxsize for _ in range(n+1)]
        t = []
        d[s] = 0
        index = [0 for _ in range(n+1)]
        q = []
        heapq.heappush(q, [0, s])
        while q:
            cost, post = heapq.heappop(q)
            if cost > d[post]:
                continue
            for p, c in adj[post].items():
                c += cost
                if c < d[p]:
                    d[p] = c
                    index[p] = post
                    heapq.heappush(q, [c, p])
        r = []
        t = e
        while t:
            r.append(t)
            t = index[t]
        return d[e], r[::-1]

    n = int(input())
    m = int(input())
    adj = [dict() for _ in range(n+1)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        if adj[x].get(y):
            adj[x][y] = min(c, adj[x].get(y))
        else:
            adj[x][y] = c

    s, e = map(int, input().split())
    m, r = g(s, e)
    print(m, len(r), sep='\n')
    print(*r)


if __name__ == '__main__':
    s()
