m, n = map(int, input().split())

sieve = [True] * (n+1)
sieve[1] = False
tmp = int(n**0.5)
for i in range(2, tmp+1):
    if sieve[i] == True:
        for j in range(i+i, n, i):
            sieve[j] = False

print('\n'.join(map(str, [i for i in range(m, n+1) if sieve[i] == True])))
