import sys
input = sys.stdin.readline


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    p[find(y)] = find(x)


def k():
    cnt = r = 0
    for a, b, c in q:
        if find(a) == find(b):
            continue
        cnt += 1
        r += c
        union(a, b)
        if cnt == n-1:
            break
    return r if cnt == n-1 else -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]
    s = [0]+list(input().split())
    q = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        if s[u] != s[v]:
            q.append((u, v, d))
    q.sort(key=lambda x: x[2])
    print(k())
