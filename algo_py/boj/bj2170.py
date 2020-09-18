import sys
input = sys.stdin.readline
n = int(input())
p = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    p.append((a, b))
p.sort()
s = p[0][0]
e = p[0][1]
c = e-s
for x, y in p[1:]:
    if e > x:
        c += y-e if y > e else 0
        e = max(e, y)
    elif e <= x:
        c += y-x
        e = x
print(c)