import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())


def dfs(i):
    global ok
    for num in edge[i]:
        if check[num] != 0:
            if check[i] == check[num]:
                ok = False
                return
        else:
            if check[i] == 1:
                check[num] = 2
                dfs(num)
            else:
                check[num] = 1
                dfs(num)


for _ in range(k):
    v, e = map(int, input().split())
    edge = [[] for _ in range(v+1)]
    check = [0 for _ in range(v+1)]
    ok = True
    for _ in range(e):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    for i in range(1, v+1):
        if not ok:
            break
        if check[i] == 0:
            check[i] = 1
            dfs(i)
    print("YES" if ok else "NO")
