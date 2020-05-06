import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(zip(map(int, input().split()), [i for i in range(n)]))
    count = 0
    while 1:
        tmp = max(q)
        doc = q.popleft()
        if doc[0] >= tmp[0]:
            count += 1
            if m==doc[1]:
                break
            continue
        q.append(doc)
    print(count)