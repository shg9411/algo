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
    for a, b, c in q:
        if find(a) == find(b):
            continue
        union(a, b)
        res += c
        cnt += 1
        if cnt == n-1:
            return res


if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(0)
        exit()
    parent = [i for i in range(n)]
    q = sorted([(i, j, w) for i in range(n) for j, w in enumerate(
        map(int, input().split()[i+1:]), start=i+1)], key=lambda x: x[2])
    print(kruskal())
