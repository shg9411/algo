import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

q = set()
res = 0
order = deque(map(int, input().split()))
for i in range(k):
    tmp = order.popleft()
    if tmp in q:
        continue
    if len(q) < n:
        q.add(tmp)
        continue
    latest = -101
    latestItem = -101
    for items in q:
        try:
            get = order.index(items)
            if get > latest:
                latest = get
                latestItem = items
        except:
            latestItem = items
            break
    q.remove(latestItem)
    q.add(tmp)
    res += 1
print(res)
