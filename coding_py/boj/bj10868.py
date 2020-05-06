import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
min_tree = [0 for _ in range(2**(math.ceil(math.log2(n)+1)))]


def init(arr, node, s, e):
    if s == e:
        min_tree[node] = arr[s]
        return

    m = (s+e)//2
    init(arr, node*2, s, m)
    init(arr, node*2+1, m+1, e)
    min_tree[node] = min(min_tree[node*2], min_tree[node*2+1])
    return


def getValue(node, s, e, left, right):
    if left > e or right < s:
        return sys.maxsize
    if s <= left and right <= e:
        return min_tree[node]
    mid = (left+right)//2
    l = getValue(node*2, s, e, left, mid)
    r = getValue(node*2+1, s, e, mid+1, right)
    return min(l, r)


init(arr, 1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
    res = getValue(1, a-1, b-1, 0, n-1)
    print(res)
