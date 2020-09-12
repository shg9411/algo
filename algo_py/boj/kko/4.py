import heapq
import sys


def solution(n, s, a, b, fares):
    adj = [dict() for _ in range(n+1)]
    for u, v, w in fares:
        adj[u][v] = w
        adj[v][u] = w

    def dijkstra(s):
        dist = [sys.maxsize for _ in range(n+1)]
        dist[s] = 0
        q = [(0, s)]
        while q:
            c, p = heapq.heappop(q)
            if c > dist[p]:
                continue
            for v, w in adj[p].items():
                if dist[v] <= c+w:
                    continue
                dist[v] = c+w
                heapq.heappush(q, (c+w, v))
        return dist
    dist = dijkstra(s)
    answer = dist[a]+dist[b]
    for i, v in enumerate(dist):
        if i == s:
            continue
        if v < answer:
            tmpdist = dijkstra(i)
            tmpRes = v+tmpdist[a]+tmpdist[b]
            answer = min(answer, tmpRes)
    return answer


print(solution(6, 4, 3, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# ok
