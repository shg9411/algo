import sys
input = sys.stdin.readline

N = 2001
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False


def dfs(i):
    for num in candi[i]:
        if not check[num]:
            check[num] = True
            if bmatch[num] == -1 or dfs(bmatch[num]):
                amatch[i] = num
                bmatch[num] = i
                return True
    return False


n = int(input())
a = []
b = []
candi = [[] for _ in range(n//2)]
ans = []
tmp = -1
for num in map(int, input().split()):
    if tmp == -1:
        tmp = num
    if num % 2 == 0:
        a.append(num)
    else:
        b.append(num)

if len(a) != len(b):
    print(-1)
    exit()

if tmp % 2 == 1:
    a, b = b, a

for i, f in enumerate(a):
    for j, s in enumerate(b):
        if sieve[f+s]:
            candi[i].append(j)


for num in candi[0]:
    amatch = [-1 for _ in range(n//2)]
    bmatch = [-1 for _ in range(n//2)]
    matching = 1
    amatch[0] = num
    bmatch[num] = 0
    for i in range(1, n//2):
        check = [False for _ in range(n//2)]
        check[num] = True
        if dfs(i):
            matching += 1
    if matching == n//2:
        ans.append(b[num])

if not ans:
    print(-1)
else:
    print(*sorted(ans))

print(sieve)
