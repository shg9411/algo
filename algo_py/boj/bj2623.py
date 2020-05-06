import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

number = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]


def check(vertex):
    if visited[vertex]:
        if visited[vertex] == -1:
            return True
        return False
    visited[vertex] = -1
    for where in graph[vertex]:
        if check(where):
            return True
    visited[vertex] = 1
    return False


def topologicalSort(graph, number):
    que = []
    for i in range(1, n+1):
        if number[i] == 0:
            heapq.heappush(que, i)
    for i in range(n):
        tmp = heapq.heappop(que)
        print(tmp)
        for p in graph[tmp]:
            number[p] -= 1
            if number[p] == 0:
                heapq.heappush(que, p)


for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        if tmp[i+1] in graph[tmp[i]]:
            continue
        graph[tmp[i]].append(tmp[i+1])
        number[tmp[i+1]] += 1

visited = [0 for _ in range(n+1)]

ok = True
for i in range(1, n+1):
    if check(i):
        ok = False
        break

if ok:
    topologicalSort(graph, number)
else:
    print(0)
