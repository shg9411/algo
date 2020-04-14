from collections import deque
a, b = map(int, input().split())
q = deque([a])
cnt = 0
while 1:
    cnt += 1
    for i in range(len(q)):
        tmp = q.popleft()
        if tmp == b:
            print(cnt)
            exit()
        if tmp*2 <= b:
            q.append(tmp*2)
        if tmp*10+1 <= b:
            q.append(tmp*10+1)
    if not q:
        break
print(-1)
