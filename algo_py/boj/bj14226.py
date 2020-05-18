from collections import deque
s = int(input())
visited = [[0 for _ in range(s+1)] for _ in range(s+1)]
visited[1][0] = 0
q = deque([[1, 0]])
while q:
    val, tmp = q.popleft()
    cnt = visited[val][tmp]+1
    if val == s:
        print(cnt-1)
        break
    if not visited[val][val]:
        visited[val][val] = cnt
        q.append([val, val])
    if val+tmp <= s and not visited[val+tmp][tmp]:
        visited[val+tmp][tmp] = cnt
        q.append([val+tmp, tmp])
    if val > 0 and not visited[val-1][tmp]:
        visited[val-1][tmp] = cnt
        q.append([val-1, tmp])