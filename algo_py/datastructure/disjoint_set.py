import sys
import heapq
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if level[x] < level[y]:
        parent[x] = y
    elif level[x] < level[y]:
        parent[y] = x
    else:
        parent[x] = y
        level[y] += 1


def kruskal():
    cnt = res = 0
    while hq:
        c, a, b = heapq.heappop(hq)
        if find(a) == find(b):
            continue
        cnt += 1
        res += c
        union(a, b)
        if cnt == N-1:
            return res


N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
level = [0 for _ in range(N+1)]
hq = []

for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(hq, (c, a, b))

print(kruskal())
