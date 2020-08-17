import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [set() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)

for a in range(N):
    for b in adj[a]:
        for c in adj[b]:
            if c == a:
                continue
            for d in adj[c]:
                if d in {a, b}:
                    continue
                for e in adj[d]:
                    if e in {a, b, c}:
                        continue
                    print(1)
                    exit()
print(0)
