import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
info = []
for _ in range(m):
    info.append(list(map(int, input().split())))
info = sorted(sorted(info, key=lambda x: x[0]), key=lambda x: x[1])

tmp = [0 for _ in range(n+1)]

res = 0
for i in range(m):
    many = 0
    x = info[i][0]  # from
    y = info[i][1]  # to
    z = info[i][2]
    for j in range(x, y):
        many = max(many, tmp[j])
    many = min(c-many, z)
    res += many
    for j in range(x, y):
        tmp[j] += many
print(res)
