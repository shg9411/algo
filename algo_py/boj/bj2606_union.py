import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


f = int(input())
t = int(input())
parent = [i for i in range(f+1)]
for _ in range(t):
    a, b = map(int,input().split())
    union(a, b)
cnt = 0
for i in range(1,f+1):
    if find(i)==1:
        cnt+=1
print(cnt-1)
