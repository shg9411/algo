from collections import deque

isPrime = [False, False]+[True for _ in range(9998)]

for i in range(2, 101):
    if isPrime[i]:
        for j in range(i*2, 10000, i):
            isPrime[j] = False


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    prime = {v: -1 for v in range(1000, 10000) if isPrime[v]}
    prime[a] = 0
    q = deque([a])
    find = False
    while not find:
        if not q:
            break
        tmp = q.popleft()
        cnt = prime[tmp]
        for i in range(4):
            strTmp = str(tmp)
            strTmp = int(strTmp[:i]+'0'+strTmp[i+1:])
            for j in range(10):
                x = strTmp + j*10**(3-i)
                if prime.get(x) == -1:
                    if x == b:
                        print(cnt+1)
                        find = True
                        break
                    prime[x] = cnt+1
                    q.append(x)
            if find:
                break
    if not find:
        print("Impossible")
