n = int(input())
if n == 1:
    print(1)
    exit()
mod = 1000000
p = 1500000
x, y = 0, 1
for _ in range(n % p-1):
    z = (x+y) % mod
    x, y = y, z

print(z)
