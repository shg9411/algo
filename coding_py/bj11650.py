import sys
input = sys.stdin.readline
n = int(input())
point = []
for _ in range(n):
    point.append(list(map(int, input().split())))

point = sorted(point, key=lambda x: [x[0], x[1]])

for p in point:
    print(p[0],p[1])