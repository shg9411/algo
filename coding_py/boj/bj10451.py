import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


def dfs(idx):
    num[idx] = 0
    for e in edge[idx]:
        if num[e] != 0:
            dfs(e)

for _ in range(t):
    n = int(input())
    sun = list(map(int, input().split()))
    edge = [[] for _ in range(n+1)]
    num = [i for i in range(n+1)]
    for u, v in enumerate(sun):
        edge[u+1].append(v)
    count = 0
    for i in range(1, n+1):
        if num[i] != 0:
            count += 1
            dfs(i)
    print(count)