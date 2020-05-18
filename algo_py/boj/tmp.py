import queue


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
    q = queue.SimpleQueue()
    q.put(start)
    che[start] = True

    while not q.empty():
        now = q.get()
        print(now, end=' ')

        for i in a[now]:
            if not che[i]:
                che[i] = True
                q.put(i)


che = [False]*(n+1)
bfs(v)
