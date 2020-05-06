from collections import deque

n, k = map(int, input().split())

num = deque([i for i in range(1, n+1)])
res = '<'

while num:
    num.rotate(-k+1)
    res += str(num.popleft())+', '

print(res[:-2]+'>')