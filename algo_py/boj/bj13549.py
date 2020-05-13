from collections import deque
N, K = map(int, input().split())
visited = [100001 for _ in range(100001)]
subin = deque([N])
visited[N] = 0
while subin:
    tmp = subin.popleft()
    cur = visited[tmp]
    if tmp == K:
        print(cur)
        exit()
    if tmp > 0:
        if visited[tmp-1] > visited[tmp]+1:
            visited[tmp-1] = cur+1
            subin.append(tmp-1)
    if tmp < 100000:
        if visited[tmp+1] > visited[tmp]+1:
            visited[tmp+1] = cur+1
            subin.append(tmp+1)
    if tmp*2 <= 100000:
        if visited[tmp*2] > visited[tmp]:
            visited[tmp*2] = cur
            subin.append(tmp*2)
