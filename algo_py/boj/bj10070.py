''' TLE with python3 and pypy3
    AC with c++'''

import sys
import math
input = sys.stdin.readline
INF = 1e6+1


def u_range(node, op, h):
    if op == 1:
        tree[node] = [max(tree[node][0], h), max(tree[node][1], h)]
    else:
        tree[node] = [min(tree[node][0], h), min(tree[node][1], h)]


def update(node, s, e, l, r, op, h):
    if e < l or s > r:
        return
    if l <= s and e <= r:
        u_range(node, op, h)
        base[l] = tree[node][0]
        return
    m = (s+e)//2
    u_range(node*2, 1, tree[node][0])
    u_range(node*2, 2, tree[node][1])
    u_range(node*2+1, 1, tree[node][0])
    u_range(node*2+1, 2, tree[node][1])
    tree[node] = [0, INF]
    update(node*2, s, m, l, r, op, h)
    update(node*2+1, m+1, e, l, r, op, h)


n, k = map(int, input().split())
base = [0 for _ in range(n)]
tree = [[0, 0] for _ in range(2**(math.ceil(math.log2(n)+1)))]

for _ in range(k):
    op, l, r, h = map(int, input().split())
    update(1, 0, n-1, l, r, op, h)

for i in range(n):
    update(1, 0, n-1, i, i, 1, 0)

print('\n'.join(map(str, base)))
