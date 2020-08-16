import sys
input = sys.stdin.readline

N = 2000 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False


def dfs(i):
    for want in cow[i]:
        if check[want]:
            continue
        check[want] = True
        if house[want] == 0 or dfs(house[want]):
            house[want] = i
            return True
    return False


n = int(input())
even = []
odd = []
candi = [[] for _ in range(n)]
for num in map(int, input().split()):
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(even) != len(odd):
    print(-1)
    exit()

for i, f in enumerate(even):
    for j, s in enumerate(odd):
        if sieve[f+s]:
            candi[i].append(j)

for i in range(n):
    check = [False for _ in range(n)]
    if dfs(i):
        res += 1

print(res)
