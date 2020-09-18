import sys
import heapq
input = sys.stdin.readline


def solve():
    n = int(input())
    m = int(input())
    adj = [dict() for _ in range(n+1)]
    for _ in range(m):
        x, y, c = map(int, input().split())
        if (v := adj[x].get(y)):
            adj[x][y] = min(c, v)
        else:
            adj[x][y] = c
    s, e = map(int, input().split())
    dist = [sys.maxsize for _ in range(n+1)]
    tmp = []
    dist[s] = 0
    index = [0 for _ in range(n+1)]
    q = [(0, s)]
    while q:
        cost, post = heapq.heappop(q)
        if cost > dist[post]:
            continue
        for p, c in adj[post].items():
            c += cost
            if c < dist[p]:
                dist[p] = c
                index[p] = post
                heapq.heappush(q, (c, p))
    res = []
    tmp = e
    while tmp:
        res.append(tmp)
        tmp = index[tmp]
    money = dist[e]
    res = res[::-1]
    print(money)
    print(len(res))
    print(*res)


if __name__ == '__main__':
    solve()
