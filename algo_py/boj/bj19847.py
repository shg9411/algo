n = int(input())
f = list(map(int, input().split()))
cur = f[0]
p = [1]*cur
for n in f[1:]:
    if n < cur:
        for i in range(n, cur):
            p[i % n] += p[i]
        cur = n
r = 0
for i, v in enumerate(p[:cur]):
    r += i*v/f[0]
print(r)
