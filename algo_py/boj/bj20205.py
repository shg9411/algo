n, k = map(int, input().split())
for _ in range(n):
    l = [s for s in input().split() for _ in range(k)]
    for _ in range(k):
        print(*l)
