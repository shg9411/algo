import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

carInput = deque()

for i in range(n):
    carInput.append(input().rstrip())
res = 0
for _ in range(n):
    tmp = input().rstrip()
    if carInput[0] == tmp:
        carInput.popleft()
    else:
        res += 1
        carInput.remove(tmp)

print(res)
