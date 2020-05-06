import sys
input = sys.stdin.readline

n = int(input())

info = []

for _ in range(n):
    s, e = map(int, input().split())
    info.append([s, e])

info = sorted(sorted(info, key=lambda x: x[0]), key=lambda x: x[1])

last = 0
res = 0
for data in info:
    if last <= data[0]:
        last = data[1]
        res += 1
print(res)
