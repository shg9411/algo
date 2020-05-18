from collections import deque

n, m, v = map(int, input().split())

a = [[]*(n+1) for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()


def dfs(node):
    ch[node] = True
    print(node, end=' ')

    for i in a[node]:
        if not ch[i]:
            dfs(i)


ch = [False]*(n+1)
dfs(v)

print()


def bfs(start):
    q = deque()
    q.append(start)
    che[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        for i in a[now]:
            if not che[i]:
                che[i] = True
                q.append(i)


che = [False]*(n+1)
bfs(v)
