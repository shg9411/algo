import sys
import math
import bisect
input = sys.stdin.readline


def dist(a, b):
    return (a.x-b.x)**2 + (a.y-b.y)**2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        else:
            return self.x > other.x


n = int(input())

point = []

for _ in range(n):
    x, y = map(int, input().split())
    point.append(Point(x, y))

point.sort()

candidate = set([point[0], point[1]])
res = dist(point[0], point[1])

s = 0

for i in range(2, n):
    now = point[i]
    while s < i:
        tmp = point[s]
        x = now.x-tmp.x
        if x**2 > res:
            candidate.remove(tmp)
            s += 1
        else:
            break
    d = int(math.sqrt(res))+1
    lp = Point(-100000, now.y-d)
    up = Point(100000, now.y+d)
    lower = bisect.bisect_left(candidate, lp)
    upper = bisect.bisect_right(candidate, up)


print(res)
