n = int(input())

tmp = n

i = 2
while i*i <= n:
    if n % i == 0:
        tmp = tmp/i * (i-1)
    while n % i == 0:
        n = n/i
    i += 1
if n != 1:
    tmp = tmp / n * (n-1)
print(int(tmp))
