import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    n = int(input())
    check = [False for _ in range(n+1)]
    adj = [0]+list(map(int, input().split()))
    check[0] = True

    def dfs(i):
        check[i] = True
        cycle.append(i)
        idx = adj[i]

        if check[idx]:
            if idx in cycle:
                res += cycle[cycle.index(idx):]
            return
        else:
            dfs(idx)

    res = []
    for i in range(1, n+1):
        if not check[i]:
            cycle = []
            dfs(i)
    print(n-len(res))
