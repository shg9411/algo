import sys
from collections import deque
F, S, G, U, D = map(int, input().split())
if S==G:
    print(0)
    exit()
if S < G and U == 0 or S > G and D == 0:
    print("use the stairs")
    exit()
gogo = [0 for _ in range(F+1)]
visited = [False for _ in range(F+1)]
gogo[S] = 0
visited[S] = True
deq = deque()
deq.append(S)
while deq:
    tmp = deq.popleft()
    count = gogo[tmp]
    if tmp == G:
        break
    tmp1 = tmp+U
    tmp2 = tmp-D
    if tmp1 < F+1 and not visited[tmp1]:
        visited[tmp1] = True
        gogo[tmp1] = count+1
        deq.append(tmp1)
    if 1 <= tmp2 and not visited[tmp2]:
        visited[tmp2] = True
        gogo[tmp2] = count+1
        deq.append(tmp2)

print(gogo[G] if gogo[G] != 0 else "use the stairs")