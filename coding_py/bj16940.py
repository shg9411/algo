import sys

input = sys.stdin.readline

n = int(input())

edge = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    f, t = map(int, input().split())
    edge[f].append(t)
    edge[t].append(f)

q = []
q.append(1)
visited[1] = True

res = [[1]]

while q:
    tmpq = []
    while q:
        tmp = q.pop(0)
        visited[tmp] = True
        for val in edge[tmp]:
            if not visited[val]:
                tmpq.append(val)
    q = tmpq[:]
    res.append(tmpq)

check = list(map(int, input().split()))
ok = True
num = 0
while res:
    tmp = res.pop(0)
    if sorted(check[num:num+len(tmp)])!=sorted(tmp):
        ok = False
        break
    num += len(tmp)

print(1 if ok else 0)
