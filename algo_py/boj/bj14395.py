from collections import deque
s, t = map(int, input().split())
if s == t:
    print(0)
    exit()
q = deque()
visited = dict()
visited[s] = 1
q.append([s, ''])
while q:
    tmp, res = q.popleft()
    if tmp == t:
        print(''.join(res))
        exit()
    x = tmp*tmp
    if x <= t*t:
        if x not in visited:
            visited[x] = 1
            q.append([x, res+'*'])
    x = tmp << 1
    if x <= t*t:
        if x not in visited:
            visited[x] = 1
            q.append([x, res+'+'])
    x = 0
    if x not in visited:
        visited[x] = 1
        q.append([x, res+'-'])
    if tmp == 0:
        continue
    x = 1
    if x not in visited:
        visited[x] = 1
        q.append([x, res+'/'])
print(-1)
