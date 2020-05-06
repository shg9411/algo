import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    importance = deque(zip(map(int, input().split()), [i for i in range(n)]))
    count = 0
    while importance:
        mv = max(importance)
        tmp = importance.popleft()
        if mv[0] > tmp[0]:
            importance.append(tmp)
        else:
            count += 1
            if tmp[1] == m:
                print(count)
                break
            else:
                continue
