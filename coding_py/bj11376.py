import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

people = [[] for _ in range(n+1)]
job = [0 for _ in range(m+1)]


def matching(i):
    for want in people[i]:
        if check[want]:
            continue
        check[want] = True
        if job[want] == 0 or matching(job[want]):
            job[want] = i
            return True
    return False


for i in range(1, n+1):
    people[i].extend(list(map(int, input().split()))[1:])

res = 0
for i in range(1, n+1):
    check = [False for _ in range(m+1)]
    if matching(i):
        res += 1
    if matching(i):
        res += 1

print(res)
