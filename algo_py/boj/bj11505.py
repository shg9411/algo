import math
import sys
input = sys.stdin.readline


def init(idx, s, e):
    if s == e:
        tree[idx] = node[s]
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = init(idx*2, s, mid) * init(idx*2+1, mid+1, e) % 1000000007
    return tree[idx]


def update(idx, val, node, s, e):
    if idx < s or e < idx:
        return tree[node]

    if s == e:
        tree[node] = val
        return tree[node]

    mid = (s+e)//2

    tree[node] = update(idx, val, node*2, s, mid) * \
        update(idx, val, node*2+1, mid+1, e) % 1000000007
    return tree[node]


def getValue(left, right, node, s, e):
    if left > e or right < s:
        return 1
    if left <= s and e <= right:
        return tree[node]
    mid = (s+e)//2
    return getValue(left, right, node*2, s, mid)*getValue(left, right, node*2+1, mid+1, e) % 1000000007


n, m, k = map(int, input().split())
tree = [0 for _ in range(2**(math.ceil(math.log2(n)+1)))]
node = [1]+[int(input()) for _ in range(n)]

init(1, 1, n)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c, 1, 1, n)
    else:
        print(getValue(b, c, 1, 1, n))
