import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for a in range(N):
    for b in adj[a]:
        for c in adj[b]:
            if c == a:
                continue
            for d in adj[c]:
                if d==a or d==b:
                    continue
                for e in adj[d]:
                    if e==a or e==b or e==c:
                        continue
                    print(1)
                    exit()
print(0)
