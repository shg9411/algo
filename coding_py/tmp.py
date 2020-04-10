import math
a, b = map(int, input().split())
prime = {i for i in range(2, b+1)}
xy = set()

for i in range(2, int(math.sqrt(b))+1):
    if i in prime:
        for j in range(i*2, b+2, i):
            if j in prime:
                xy.add(j)

c=list(prime.difference(xy))
c.sort()
for i in c:
    if i >= a:
        print(i)
