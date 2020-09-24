from collections import deque
maxV = 10**6+1
x = int(input())
visited = [maxV for _ in range(x+1)]
visited[x] = 0
q = deque()
q.append(x)
while q:
    tmp = q.popleft()
    val = visited[tmp]
    if tmp == 1:
        print(val)
        break
    if tmp % 3 == 0:
        if visited[tmp//3] > val+1:
            visited[tmp//3] = val+1
            q.append(tmp//3)
    if tmp % 2 == 0:
        if visited[tmp//2] > val+1:
            visited[tmp//2] = val+1
            q.append(tmp//2)
    if visited[tmp-1] > val+1:
        visited[tmp-1] = val+1
        q.append(tmp-1)