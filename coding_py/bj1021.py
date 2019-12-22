from collections import deque
n, m = map(int, input().split())
get = list(map(int, input().split()))
q = deque([i+1 for i in range(n)])

count = 0
while get:
    tmp = get.pop(0)
    idx = q.index(tmp)
    if idx == 0:
        q.popleft()
        continue
    size = len(q)
    if idx > size/2:
        q.rotate(size-idx)
        count += (size-idx)
        q.popleft()
    else:
        q.rotate(-idx)
        count += (idx)
        q.popleft()

print(count)