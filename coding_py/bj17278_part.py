import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input().rstrip()
    for i in range(m):
        x, y = map(int, input().split())
        if x > k:
            continue
        y = min(y, k)
        t = int('1'*(y-x+1), 2)
        t2 = int(a[x-1:y], 2)
        tt = "{0:b}".format(t ^ t2).zfill(y-x+1)
        a = (a[:y]+tt+a[y:])
    print(a[:k])
