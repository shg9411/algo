import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    tmp = input().split()
    if tmp[0]=='push':
        q.append(int(tmp[1]))
    elif tmp[0]=='front':
        print(q[0] if q else -1)
    elif tmp[0]=='pop':
        print(q.popleft() if q else -1)
    elif tmp[0]=='size':
        print(len(q))
    elif tmp[0]=='empty':
        print(0 if q else 1)
    elif tmp[0]=='back':
        print(q[-1] if q else -1)