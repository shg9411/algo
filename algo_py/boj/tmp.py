import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [0 for _ in range(n+1)]
fenwick = [0 for _ in range(n+1)]


def update(node, value):
    while node <= n:
        fenwick[node] += value
        node += (node & -node)


def sum(node):
    res = 0
    while node:
        res += fenwick[node]
        node -= (node & -node)
    return res


for i in range(1, n+1):
    tree[i] = int(input())
    update(i, tree[i])

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c-tree[b]
        update(b, diff)
        tree[b] = c
    else:
        print(sum(c)-sum(b-1))
