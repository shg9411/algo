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


n = int(input())
parent = [i for i in range(n)]
m = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if i != j and tmp[j] == 1:
            union(i, j)

trap = list(map(int, input().split()))
ans = set()
for num in trap:
    ans.add(find(num-1))
    if len(ans)>1:
        print("NO")
        exit()
print("YES")
