import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
maxNum = max(num)
isPrime = [-1, -1]+[i for i in range(2, maxNum+1)]
for i in range(2, int(maxNum**0.5)+1):
    if i != isPrime[i]:
        continue
    for j in range(i*2, maxNum+1, i):
        isPrime[j] = i


for x in num:
    res = []
    while x > 1:
        if x % isPrime[x] == 0:
            res.append(isPrime[x])
        x //= isPrime[x]
    sys.stdout.write(' '.join(map(str, sorted(res)))+'\n')
