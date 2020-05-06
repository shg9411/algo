import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def matching(i):

    for want in people[i]:
        if check[want]:
            continue
        check[want] = True
        if notebook[want] == 0 or matching(notebook[want]):
            notebook[want] = i
            return True
    return False


people = [[] for _ in range(n+1)]
notebook = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)

res = 0

for i in range(1, n+1):
    check = [False for _ in range(n+1)]
    if matching(i):
        res += 1

print(res)
