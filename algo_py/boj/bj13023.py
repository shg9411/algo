import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    if cnt == 5:
        print(1)
        exit()
    for f in adj[idx]:
        if visited[f]:
            continue
        visited[f] = True
        dfs(f, cnt+1)
        visited[f] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False for _ in range(N+1)]
    for i in range(1, N+1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(0)
