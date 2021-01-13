import sys
import heapq
input = sys.stdin.readline
INF=300001
def solve():
    n, m, k, x = map(int, input().split())
    edge = [dict() for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a][b] = 1
    dist = [INF for _ in range(n+1)]
    dist[x] = 0
    pq = [(0, x)]
    while pq:
        d1, v1 = heapq.heappop(pq)
        if dist[v1] < d1:
            continue
        if d1 == k:
            break
        for v2, d2 in edge[v1].items():
            if dist[v1]+d2 < dist[v2]:
                dist[v2] = dist[v1]+d2
                heapq.heappush(pq, (dist[v2], v2))
    print('\n'.join(map(str, (i for i, v in enumerate(dist) if v == k))) or -1)

    
if __name__ == '__main__':
    solve()