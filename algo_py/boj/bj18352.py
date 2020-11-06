import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m, k, x = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)

    dist[x] = 0
    q = deque([x])
    while q:
        l = len(q)
        for _ in range(l):
            tmp = q.popleft()
            now = dist[tmp]
            if now == k:
                res = []
                for i in range(1, n+1):
                    if dist[i] == k:
                        res.append(i)
                print('\n'.join(map(str, res)))
                exit()
            for nxt in edge[tmp]:
                if dist[nxt]:
                    continue
                dist[nxt] = now+1
                q.append(nxt)
    print(-1)
if __name__=='__main__':
    main()