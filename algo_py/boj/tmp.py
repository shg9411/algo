import sys
import bisect
input = sys.stdin.readline


def getdist(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2


n = int(input())
p = sorted([list(map(int, input().split())) for _ in range(n)])
dist = getdist(p[0], p[1])
candi = [p[0], p[1]]
start = 0
for i in range(2, n):
    tmp = p[i]
    while start < i:
        xx = p[start]
        x = tmp[0]-xx[0]
        if x*x > dist:
            candi.remove(xx)
            start += 1
        else:
            break
    d = int(dist**0.5)+1
    lp = [-100000, tmp[1]-d]
    mp = [100000, tmp[1]+d]
    lower = bisect.bisect_left(candi, lp)
    upper = bisect.bisect_right(candi, mp)
    for qqq in range(lower, upper):
        xxx = getdist(tmp, candi[qqq])
        if xxx < dist:
            dist = xxx
    bisect.insort(candi, tmp)
print(dist)
