n = int(input())
lope = [int(input()) for _ in range(n)]
lope.sort()
v = 0
for i in range(n):
    if v < lope[i] * (n-i):
        v = lope[i] * (n-i)
print(v)
