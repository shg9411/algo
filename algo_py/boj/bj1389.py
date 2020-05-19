import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
resNum = (987654321, N+1)
for i in range(1, N+1):
    friends = [-1 for _ in range(N+1)]
    q = deque()
    friends[i] = 0
    q.append(i)
    while q:
        tmp = q.popleft()
        cur = friends[tmp]
        for friend in adj[tmp]:
            if 0 > friends[friend]:
                friends[friend] = cur+1
                q.append(friend)
    val = sum(friends)+1
    if val < resNum[0]:
        resNum = (val, i)
print(resNum[1])