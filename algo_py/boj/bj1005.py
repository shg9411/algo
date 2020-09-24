import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve():
    def dfs(u):
        m = 0
        # 선행 작업 중 최대시간 추적
        for v in adj[u]:
            m = max(m, t[v] if vi[v] else dfs(v))
        vi[u] = 1
        # 건설 시간 + 선행시간 중 최대 시간
        t[u] += m
        return t[u]

    n, k = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    # 방문
    vi = [0 for _ in range(n+1)]
    # base 시간
    t = [0]+list(map(int, input().split()))
    for _ in range(k):
        x, y = map(int, input().split())
        adj[y].append(x)
    w = int(input())
    print(dfs(w))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
