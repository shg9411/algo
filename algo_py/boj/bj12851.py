from collections import deque
n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]
here = deque()
here.append(n)
visited[n] = 1
while here:
    tmp = here.popleft()
    nxt = tmp-1
    if nxt >= 0:
        if not visited[nxt]:
            visited[nxt] = visited[tmp]
            dist[nxt] = dist[tmp]+1
            here.append(nxt)
        elif dist[nxt] == dist[tmp]+1:
            visited[nxt] += visited[tmp]
    nxt = tmp+1
    if tmp+1 <= 100000:
        if not visited[nxt]:
            visited[nxt] = visited[tmp]
            dist[nxt] = dist[tmp]+1
            here.append(nxt)
        elif dist[nxt] == dist[tmp]+1:
            visited[nxt] += visited[tmp]
    nxt = tmp*2
    if tmp*2 <= 100000:
        if not visited[nxt]:
            visited[nxt] = visited[tmp]
            dist[nxt] = dist[tmp]+1
            here.append(nxt)
        elif dist[nxt] == dist[tmp]+1:
            visited[nxt] += visited[tmp]

print(dist[k])
print(visited[k])
