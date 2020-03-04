import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

number = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]


def topologicalSort(graph, number):
    que = []
    for i in range(1, n+1):
        if number[i] == 0:
            heapq.heappush(que, i)
    for i in range(n):
        tmp = heapq.heappop(que)
        print(tmp, end=' ')
        for p in graph[tmp]:
            number[p] -= 1
            if number[p] == 0:
                heapq.heappush(que, p)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    number[b] += 1


topologicalSort(graph, number)
