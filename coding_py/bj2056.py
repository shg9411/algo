import sys
from collections import deque
input = sys.stdin.readline


def topologicalSort():
    res = [0 for _ in range(n+1)]
    q = deque([])
    for i in range(1, n+1):
        if cnt[i] == 0:
            q.append(i)
            res[i] = job[i]
    for i in range(n):
        tmp = q.popleft()
        for nxt in graph[tmp]:
            res[nxt] = max(res[nxt], res[tmp]+job[nxt])
            cnt[nxt] -= 1
            if cnt[nxt] == 0:
                q.append(nxt)
    return max(res)


n = int(input())
job = [0 for _ in range(n+1)]
cnt = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    job[i] = tmp[0]
    for x in tmp[2:]:
        graph[x].append(i)
    cnt[i] += tmp[1]

print(topologicalSort())
