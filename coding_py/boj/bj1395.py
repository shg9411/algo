import sys
import math
input = sys.stdin.readline


def sum(node, s, e, l, r):
    update_lazy(node, s, e)
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]

    m = (s+e)//2
    return sum(node*2, s, m, l, r)+sum(node*2+1, m+1, e, l, r)


def update_lazy(node, s, e):
    if lazy[node]:
        tree[node] = (e-s+1)-tree[node]
        if s != e:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2+1] = not lazy[node*2+1]
        lazy[node] = False


def update_range(node, s, e, i, j):
    update_lazy(node, s, e)

    if j < s or i > e:
        return

    if i <= s and e <= j:
        tree[node] = (e-s+1)-tree[node]
        if s != e:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2+1] = not lazy[node*2+1]
        return

    m = (s+e)//2
    update_range(node*2, s, m, i, j)
    update_range(node*2+1, m+1, e, i, j)
    tree[node] = tree[node*2] + tree[node*2+1]


N, M = map(int, input().split())
tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
lazy = [False for _ in range(2**(math.ceil(math.log2(N)+1)))]

for _ in range(M):
    o, s, t = map(int, input().split())
    if o:
        print(sum(1, 0, N-1, s-1, t-1))
    else:
        update_range(1, 0, N-1, s-1, t-1)
