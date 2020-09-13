import sys
input = sys.stdin.readline

tree = [0 for _ in range(2 << 21)]


def update(node, value):
    node += (2 << 20)
    while node:
        tree[node] += value
        node >>= 1


def query(node):
    i = 1
    while i < (2 << 20):
        tree[i] -= 1
        if tree[i << 1] >= node:
            i = i << 1
        else:
            node -= tree[i << 1]
            i = i << 1 | 1
    tree[i] -= 1
    return i-(2 << 20)


n = int(input())

for _ in range(n):
    a, *b = map(int, input().split())
    if a == 1:
        print(query(b[0]))
    else:
        update(b[0], b[1])
