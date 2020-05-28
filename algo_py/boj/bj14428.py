import sys
import math
input = sys.stdin.readline

input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = base[s]
        return
    m = (s+e)//2
    init(node*2, s, m)
    init(node*2+1, m+1, e)
    tree[node] = min(tree[node*2], tree[node*2+1])
    return


def getMin(node, s, e, l, r):
    if l > e or r < s:
        return -1
    if l <= s and e <= r:
        return tree[node]
    m = (s+e)//2
    one = getMin(node*2, s, m, l, r)
    two = getMin(node*2+1, m+1, e, l, r)
    if one == -1:
        return two
    if two == -1:
        return one
    if base[one] <= base[two]:
        return one
    return two


def update(idx, node, s, e):
    if idx < s or e < idx:
        return tree[node]
    if s == e:
        tree[node] = s
        return tree[node]
    m = (s+e)//2
    one = update(idx, node*2, s, m)
    two = update(idx, node*2+1, m+1, e)
    if one == -1 and two == -1:
        return -1
    elif one == -1:
        tree[node] = two
    elif two == -1:
        tree[node] = one
    elif base[one] <= base[two]:
        tree[node] = one
    else:
        tree[node] = two
    return tree[node]


N = int(input())
base = [0]+list(map(int, input().split()))
tree = [0 for _ in range(2**(math.ceil(math.log2(N)+1)))]
for i in range(1, N+1):
    update(i, 1, 1, N)
M = int(input())
for _ in range(M):
    q, a, b = map(int, input().split())
    if q == 1:
        base[a] = b
        update(a, 1, 1, N)
    else:
        print(getMin(1, 1, N, a, b))
