n, m = map(int, input().split())
i = 1
for _ in range(n):
    print(' '.join(map(str,range(i, i+m))))
    i+=m
