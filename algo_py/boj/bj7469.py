# merge sort tree

import sys
import math
import bisect
import heapq
input = sys.stdin.readline


def init(node, s, e):
    if s == e:
        tree[node] = [base[s]]
        return tree[node]
    m = (s+e)//2
    a = init(node*2, s, m)
    b = init(node*2+1, m+1, e)
    tree[node] = list(heapq.merge(a, b))
    return tree[node]


def get(node, s, e, l, r, v):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        val = bisect.bisect_right(tree[node], v)
        return val
    m = (s+e)//2
    return get(node*2, s, m, l, r, v) + get(node*2+1, m+1, e, l, r, v)


n, m = map(int, input().split())
base = list(map(int, input().split()))
tree = [[0] for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(1, 0, n-1)
for _ in range(m):
    a, b, c = map(int, input().split())
    left = -10**9-1
    right = 10**9+1
    while(left <= right):
        mid = (left+right)//2
        if get(1, 0, n-1, a-1, b-1, mid) < c:
            left = mid+1
        else:
            right = mid-1
    print(left)
