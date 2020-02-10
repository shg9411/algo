n, m = map(int, input().split())
l = list(range(1, n + 1))
r = []
index = 0

while l:
    index = (index + m - 1) % len(l)
    r.append(str(l.pop(index)))

print('<', ', '.join(r), '>', sep='')