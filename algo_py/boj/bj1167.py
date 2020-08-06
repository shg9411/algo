import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    tree = [dict() for _ in range(n+1)]
    for _ in range(n):
        u, *info = map(int, input().split()[:-1])
        i = 0
        while i < len(info):
            tree[u][info[i]] = info[i+1]
            tree[info[i]][u] = info[i+1]
            i += 2

    def dfs(u, w):
        global tmpu, tmpval
        dist[u] = w

        if dist[u] > tmpval:
            tmpval, tmpu = dist[u], u

        for vertex, weight in tree[u].items():
            if 0 > dist[vertex]:
                dfs(vertex, w+weight)

    dist = [-1 for _ in range(n+1)]
    tmpu, tmpval = 0, 0
    dfs(1, 0)
    dist = [-1 for _ in range(n+1)]
    dfs(tmpu, 0)
    print(tmpval)