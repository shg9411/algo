import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    parent[y] = x


def kruskal():
    cnt = res = 0
    for a, b, c in hq:
        if find(a) == find(b):
            continue
        cnt += 1
        res += c
        union(a, b)
        if cnt == V-1:
            return res


if __name__ == '__main__':
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    level = [0 for _ in range(V+1)]
    hq = sorted([tuple(map(int, input().split()))
                 for _ in range(E)], key=lambda x: x[2])
    print(kruskal())