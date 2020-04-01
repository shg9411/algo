import sys

input = sys.stdin.readline

n = int(input())

edge = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    f, t = map(int, input().split())
    edge[f].append(t)
    edge[t].append(f)


check = list(map(int, input().split()))
if check[0] != 1:
    print(0)
    exit()

q = []
q.append(1)
visited[1] = True
idx = 1
while q:
    here = q.pop(0)
    visited[here] = True
    tmp = set()
    for val in edge[here]:
        if not visited[val]:
            tmp.add(val)
            visited[val] = True
    for i in range(idx, idx+len(tmp)):
        if check[i] not in tmp:
            print(0)
            exit()
        q.append(check[i])
    idx += len(tmp)
print(1)
