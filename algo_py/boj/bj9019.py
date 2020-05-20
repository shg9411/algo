from collections import deque
maxV = 10000
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0 for _ in range(maxV)]
    q = deque([A])
    visited[A] = '.'
    while q:
        tmp = q.popleft()
        val = visited[tmp]
        if tmp == B:
            print(val[1:])
            break
        x = tmp*2 % maxV
        if not visited[x]:
            visited[x] = val+'D'
            q.append(x)
        x = (tmp-1) % maxV
        if not visited[x]:
            visited[x] = val+'S'
            q.append(x)
        x = int((tmp % 1000) * 10 + tmp / 1000)
        if not visited[x]:
            visited[x] = val+'L'
            q.append(x)
        x = int((tmp % 10)*1000+tmp/10)
        if not visited[x]:
            visited[x] = val+'R'
            q.append(x)