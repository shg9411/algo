import sys
input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if 0 == n == a == b:
        break
    ballon = []
    for _ in range(n):
        ballon.append(list(map(int, input().split())))
    ballon.sort(key=lambda a: -abs(a[1]-a[2]))
    res = 0
    for x in ballon:
        if x[1] >= x[2]:
            if x[0] <= b:
                b -= x[0]
                res += x[2]*x[0]
            else:
                x[0] -= b
                res += x[2]*b+x[0]*x[1]
                b = 0
                a -= x[0]
        else:
            if x[0] <= a:
                a -= x[0]
                res += x[1]*x[0]
            else:
                x[0] -= a
                res += x[1]*a+x[0]*x[2]
                a = 0
                b -= x[0]
    print(res)
