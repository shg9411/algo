m = int(input())
n = int(input())

sosu = [True] * (n+1)
sosu[1] = False

for i in range(2, int(n**0.5)+1):
    if sosu[i]:
        for j in range(i+i, n+1, i):
            sosu[j] = False

total = 0

for x in range(m,n+1):
    if sosu[x]:
        total += x

if total == 0:
    print(-1)
else:
    print(total)
    print(sosu[m:n+1].index(True)+m)
