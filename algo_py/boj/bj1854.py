import sys
import heapq
input = sys.stdin.readline


def solve():
    def dijkstra():
        q = [(0, 1)]
        dist[1] = [0]
        while q:
            c, p = heapq.heappop(q)
            for np, nc in adj[p]:
                nc += c
                if len(dist[np]) < k:
                    heapq.heappush(dist[np], -nc)
                    heapq.heappush(q, (nc, np))
                elif -dist[np][0] > nc:
                    heapq.heappop(dist[np])
                    heapq.heappush(dist[np], -nc)
                    heapq.heappush(q, (nc, np))

    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    dist = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
    dijkstra()
    for i in range(1, n+1):
        print(-1 if len(dist[i]) < k else -dist[i][0])


if __name__ == '__main__':
    solve()
