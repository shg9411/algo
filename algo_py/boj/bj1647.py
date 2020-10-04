import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(y)] = parent[find(x)]

def kruskal():
    cnt = res = 0
    for c,a,b in q:
        if find(a) == find(b):
            continue
        cnt += 1
        res += c
        union(a, b)
        if cnt == N-2:
            break
    return res


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
q = []

for _ in range(M):
    A, B, C = map(int, input().split())
    q.append((C,A,B))
q.sort()

print(kruskal())
