import sys
import math
input = sys.stdin.readline


def init(a, tree, node, s, e):
    if s == e:
        tree[node] = base[s]
        return tree[node]
    m = (s+e)//2
    tree[node] = init(base, tree, node*2, s, m) + \
        init(base, tree, node*2+1, m+1, e)
    return tree[node]


def sum(tree, node, s, e, l, r):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[node]
    m = (s+e)//2
    return sum(tree, node*2, s, m, l, r)+sum(tree, node*2+1, m+1, e, l, r)


def update(tree, node, s, e, idx, diff):
    if idx < s or idx > e:
        return
    tree[node] += diff
    if s != e:
        m = (s+e)//2
        update(tree, node*2, s, m, idx, diff)
        update(tree, node*2+1, m+1, e, idx, diff)


N, M, K = map(int, input().split())
base = [int(input()) for _ in range(N)]
tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
init(base, tree, 1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c-base[b-1]
        base[b-1] = c
        update(tree, 1, 0, N-1, b-1, diff)
    else:
        print(sum(tree, 1, 0, N-1, b-1, c-1))
