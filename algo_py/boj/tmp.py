import sys
input = sys.stdin.readline
print(2<<20, 2<<21,2<<20<<1)
fenwik = [0 for _ in range((2 << 20) << 1)]


def update(node, value):
    node += 2 << 20
    while node:
        fenwik[node] += value
        node >>= 1


def query(node):
    i = 1
    while i < (2 << 20):
        fenwik[i] -= 1
        if fenwik[i << 1] >= node:
            i = i << 1
        else:
            node -= fenwik[i << 1]
            i = i << 1 | 1
    fenwik[i] -= 1
    return i-2 << 20


n = int(input())

for _ in range(n):
    a, *b = map(int, input().split())
    if a == 1:
        print(query(b[0]))
    else:
        update(b[0], b[1])
