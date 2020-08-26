import sys
sys = sys.stdin.readline

while 1:
    n, a, b = map(int, input().split())
    if not n and not a and not b:
        break
    ballon = []
    for _ in range(n):
        ballon.append(list(map(int, input().split())))
    ballon.sort(key=lambda a: (-abs(a[1]-a[2]), -a[0]))
    res = 0
    for x in ballon:
        if x[1] >= x[2]:
            tmp = min(x[0], b)
            b -= tmp
            res += x[2]*tmp
        elif x[2] > x[1]:
            tmp = min(x[0], a)
            a -= tmp
            res += x[1]*tmp
        extra = x[0]-tmp
        if extra:
            if a:
                res += extra*x[1]
            else:
                res += extra*x[2]
    print(res)