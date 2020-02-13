import sys
T = int(sys.stdin.readline())
MAX = 1000000
check = [False, False] + [True] * (MAX-1)
primes = []
prime_count = 0
for i in range(1, MAX+1):
    if check[i]:
        primes.append(i)
        prime_count += 1
        for j in range(i*2, MAX+1, i):
            check[j] = False
for _ in range(T):    
    N = int(sys.stdin.readline())
    result = 0
    for i in range(1, prime_count):
        if primes[i] <= N - primes[i]:
            if check[N-primes[i]] == True:
                result += 1
        else:
            break

    print(result)