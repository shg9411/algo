import sys

isPrime = [True] * 1000001
for i in range(2,1000001):
    for j in range(i*2,1000001,i):
        if not isPrime[j]:
            continue
        isPrime[j] = False

tmp = sys.stdin.read().splitlines()[:-1]

for num in tmp:
    num = int(num)
    for i in range(2,num//2+1):
        if isPrime[i] and isPrime[num-i]:
            print(num,"=",i,"+",num-i)
            break