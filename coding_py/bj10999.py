import sys
import math
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = base[s]
        return tree[node]
    m = (s+e)//2
    tree[node] = init(node*2, s, m)+init(node*2+1, m+1, e)
    return tree[node]


def sum(node, s, e, l, r):
    update_lazy(node, s, e)
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]

    m = (s+e)//2
    return sum(node*2, s, m, l, r)+sum(node*2+1, m+1, e, l, r)


def update_lazy(node, s, e):
    if lazy[node] != 0:
        tree[node] += (e-s+1)*lazy[node]
        if s != e:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0


def update_range(node, s, e, i, j, diff):
    update_lazy(node, s, e)

    if j < s or i > e:
        return

    if i <= s and e <= j:
        tree[node] += (e-s+1)*diff
        if s != e:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return

    m = (s+e)//2
    update_range(node*2, s, m, i, j, diff)
    update_range(node*2+1, m+1, e, i, j, diff)
    tree[node] = tree[node*2] + tree[node*2+1]


N, M, K = map(int, input().split())
base = [int(input()) for _ in range(N)]
tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
lazy = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
init(1, 0, N-1)
for _ in range(M+K):
    a, *z = map(int, input().split())
    if a == 1:
        update_range(1, 0, N-1, z[0]-1, z[1]-1, z[2])
    else:
        print(sum(1, 0, N-1, z[0]-1, z[1]-1))
