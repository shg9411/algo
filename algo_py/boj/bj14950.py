import sys
input = sys.stdin.readline


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
        union(a, b)
        res += c+t*(cnt)
        cnt += 1
        if cnt == n-1:
            return res


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    parent = [i for i in range(n+1)]
    hq = sorted([tuple(map(int, input().split()))
                 for _ in range(m)], key=lambda x: x[2])
    print(kruskal())
