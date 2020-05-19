import sys
input = sys.stdin.readline


def ccw(i, j, k):
    x = i[0]*j[1]+j[0]*k[1]+k[0]*i[1]
    y = i[0]*k[1]+j[0]*i[1]+k[0]*j[1]
    return x-y


N = int(input())

point = []
for _ in range(N):
    point.append(tuple(map(int, input().split())))

p = point[0]
res = 0
for i in range(1, N-1):
    res += ccw(p, point[i], point[i+1])
if res < 0:
    res *= -1

print('{}.{}'.format(res//2, 0 if res % 2 == 0 else 5))
