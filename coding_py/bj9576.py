import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    people = [[]]
    book = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        people.append([i for i in range(a, b+1)])

    def dfs(i):
        for want in people[i]:
            if checked[want]:
                continue
            checked[want] = True
            if book[want] == 0 or dfs(book[want]):
                book[want] = i
                return True
        return False

    res = 0

    for i in range(1, m+1):
        checked = [False for _ in range(n+1)]
        if dfs(i):
            res += 1
    print(res)
