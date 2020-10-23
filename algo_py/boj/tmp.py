import sys
input = sys.stdin.readline


def solve():
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    check = [-1]*(V+1)

    def dfs(idx, c):
        check[idx] = c
        for j in adj[idx]:
            if check[j] == -1:
                if c == 0:
                    dfs(j, c ^ 1)

    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, V+1):
        if check[i] == -1:
            dfs(i, 1)
    for i in range(1, V+1):
        for j in adj[i]:
            if check[i] == check[j]:
                print("NO")
                return
    print("YES")
    return


if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
